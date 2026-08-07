"""HealthyPlate Flask application."""

import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from openai import OpenAI

from content import ARTICLES, GROCERY_GROUPS, RECIPES

load_dotenv()


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "dev-change-me"),
        OPENAI_MODEL=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        MAX_QUESTION_LENGTH=600,
    )
    if test_config:
        app.config.update(test_config)

    @app.context_processor
    def inject_globals():
        return {"recipe_categories": sorted({recipe["category"] for recipe in RECIPES})}

    @app.get("/")
    def homepage():
        return render_template(
            "homepage.html",
            featured_recipes=RECIPES[:3],
            featured_articles=ARTICLES[:3],
        )

    @app.get("/learn")
    def learn():
        return render_template("learn.html", articles=ARTICLES)

    @app.get("/recipes")
    def recipes():
        query = request.args.get("q", "").strip()
        category = request.args.get("category", "").strip()
        results = RECIPES
        if query:
            needle = query.casefold()
            results = [
                recipe
                for recipe in results
                if needle in " ".join(
                    [recipe["name"], recipe["description"], *recipe["ingredients"], *recipe["tags"]]
                ).casefold()
            ]
        if category:
            results = [recipe for recipe in results if recipe["category"] == category]
        return render_template(
            "recipes.html", recipes=results, query=query, selected_category=category
        )

    @app.get("/recipes/<slug>")
    def recipe_detail(slug):
        recipe = next((item for item in RECIPES if item["slug"] == slug), None)
        if recipe is None:
            return render_template("404.html"), 404
        return render_template("recipe_detail.html", recipe=recipe)

    @app.get("/grocery-guide")
    def grocery_guide():
        return render_template("grocery.html", grocery_groups=GROCERY_GROUPS)

    @app.get("/diets")
    def diets():
        return render_template("diets.html")

    @app.route("/assistant", methods=["GET", "POST"])
    def assistant():
        answer = ""
        user_question = ""
        if request.method == "POST":
            user_question = request.form.get("user", "").strip()
            if not user_question:
                flash("Please enter a question so the assistant can help.", "error")
            elif len(user_question) > app.config["MAX_QUESTION_LENGTH"]:
                flash("Please keep your question under 600 characters.", "error")
            elif not os.getenv("OPENAI_API_KEY"):
                answer = (
                    "The assistant is not configured yet. Try the Recipes or Grocery Guide pages "
                    "for practical ideas, or add OPENAI_API_KEY to your local .env file."
                )
            else:
                try:
                    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
                    response = client.responses.create(
                        model=app.config["OPENAI_MODEL"],
                        instructions=(
                            "You are HealthyPlate's beginner-friendly food education assistant. "
                            "Give concise, practical meal ideas using familiar foods. Encourage balance, "
                            "variety, affordability, cultural flexibility, and substitutions. Never diagnose, "
                            "prescribe a diet, give calorie targets, or claim to replace a clinician. For "
                            "allergies, pregnancy, eating disorders, medical conditions, or personalized "
                            "nutrition advice, recommend a qualified healthcare professional. Clearly state "
                            "that suggestions are general educational information."
                        ),
                        input=user_question,
                    )
                    answer = response.output_text
                except Exception:
                    app.logger.exception("HealthyPlate assistant request failed")
                    answer = (
                        "I couldn't reach the assistant just now. Please try again later, or browse "
                        "the recipe collection for meal ideas."
                    )
        return render_template(
            "aiassistant.html", assistant=answer, user_question=user_question
        )

    @app.get("/resources")
    def resources():
        return render_template("otherresources.html")

    @app.get("/search")
    def search():
        query = request.args.get("q", "").strip()
        if not query:
            return redirect(url_for("recipes"))
        return redirect(url_for("recipes", q=query))

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html"), 404

    return app


main = create_app()


if __name__ == "__main__":
    main.run(debug=os.getenv("FLASK_DEBUG") == "1")
