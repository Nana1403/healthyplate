import os
import sys
import unittest
from unittest.mock import patch

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from main import create_app
from content import RECIPES


class HealthyPlateTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app({"TESTING": True, "SECRET_KEY": "test"})
        self.client = self.app.test_client()

    def test_core_pages_load(self):
        for path in ["/", "/learn", "/recipes", "/grocery-guide", "/diets", "/resources", "/assistant"]:
            with self.subTest(path=path):
                response = self.client.get(path)
                self.assertEqual(response.status_code, 200)

    def test_recipe_search_matches_ingredient(self):
        response = self.client.get("/recipes?q=black+beans")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Black bean taco bowls", response.data)
        self.assertNotIn(b"Sheet-pan salmon", response.data)

    def test_recipe_collection_contains_one_hundred_unique_recipes(self):
        self.assertEqual(len(RECIPES), 100)
        self.assertEqual(len({recipe["slug"] for recipe in RECIPES}), 100)
        response = self.client.get("/recipes")
        self.assertIn(b"100 recipes found", response.data)

    def test_recipe_category_filter(self):
        response = self.client.get("/recipes?category=Breakfast")
        self.assertIn(b"Berry oat breakfast bowl", response.data)
        self.assertNotIn(b"Hummus crunch wrap", response.data)

    def test_recipe_detail_and_missing_recipe(self):
        response = self.client.get("/recipes/chicken-broccoli-rice-bowl")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Chicken, broccoli &amp; rice bowl", response.data)
        self.assertEqual(self.client.get("/recipes/not-real").status_code, 404)

    def test_empty_assistant_question_shows_validation(self):
        response = self.client.post("/assistant", data={"user": ""}, follow_redirects=True)
        self.assertIn(b"Please enter a question", response.data)

    @patch.dict(os.environ, {"OPENAI_API_KEY": ""})
    def test_assistant_has_helpful_unconfigured_state(self):
        response = self.client.post("/assistant", data={"user": "What can I make?"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"assistant is not configured yet", response.data)


if __name__ == "__main__":
    unittest.main()
