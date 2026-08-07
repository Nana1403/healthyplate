"""Local recipes and educational content for HealthyPlate."""

import re

RECIPES = [
    {
        "slug": "berry-oat-breakfast-bowl",
        "name": "Berry oat breakfast bowl",
        "emoji": "🥣",
        "category": "Breakfast",
        "description": "Creamy oats with berries, yogurt, and seeds for an easy start.",
        "prep_time": "5 minutes",
        "cook_time": "5 minutes",
        "servings": 1,
        "ingredients": ["1/2 cup rolled oats", "1 cup milk or fortified alternative", "1/2 cup berries", "1/3 cup plain yogurt", "1 tablespoon seeds"],
        "instructions": ["Cook oats with milk according to the package.", "Spoon into a bowl and add berries and yogurt.", "Finish with seeds and a splash of milk if desired."],
        "nutrition_note": "Oats and berries add fiber; yogurt adds protein. Choose a fortified dairy alternative when needed.",
        "tags": ["quick", "vegetarian", "budget-friendly"],
    },
    {
        "slug": "chicken-broccoli-rice-bowl",
        "name": "Chicken, broccoli & rice bowl",
        "emoji": "🍚",
        "category": "Dinner",
        "description": "A flexible balanced bowl with a simple lemon-herb finish.",
        "prep_time": "10 minutes",
        "cook_time": "20 minutes",
        "servings": 2,
        "ingredients": ["2 cups cooked brown rice", "2 cooked chicken breasts, sliced", "3 cups broccoli florets", "1 tablespoon olive oil", "1 lemon", "Garlic powder and black pepper"],
        "instructions": ["Roast or sauté broccoli with olive oil until tender.", "Divide warm rice, chicken, and broccoli between bowls.", "Season with lemon juice, garlic powder, and black pepper."],
        "nutrition_note": "Chicken provides protein, rice provides carbohydrates, and broccoli contributes fiber and micronutrients.",
        "tags": ["high-protein", "meal-prep", "beginner"],
    },
    {
        "slug": "black-bean-taco-bowls",
        "name": "Black bean taco bowls",
        "emoji": "🫘",
        "category": "Dinner",
        "description": "An affordable plant-forward dinner built from pantry staples.",
        "prep_time": "10 minutes",
        "cook_time": "10 minutes",
        "servings": 4,
        "ingredients": ["2 cups cooked rice", "1 can black beans, rinsed", "1 cup frozen corn", "2 chopped tomatoes", "1 avocado", "Lime and mild taco seasoning"],
        "instructions": ["Warm beans and corn with taco seasoning.", "Layer rice, beans, corn, and tomatoes in bowls.", "Top with avocado and a squeeze of lime."],
        "nutrition_note": "Beans provide plant protein and fiber; rice supplies energy; vegetables add color and variety.",
        "tags": ["vegan", "budget-friendly", "quick"],
    },
    {
        "slug": "hummus-crunch-wrap",
        "name": "Hummus crunch wrap",
        "emoji": "🌯",
        "category": "Lunch",
        "description": "A no-cook wrap packed with crisp vegetables and creamy hummus.",
        "prep_time": "10 minutes",
        "cook_time": "No cooking",
        "servings": 1,
        "ingredients": ["1 whole-grain wrap", "1/3 cup hummus", "1 handful spinach", "1/2 sliced bell pepper", "1/2 grated carrot", "Cucumber slices"],
        "instructions": ["Spread hummus over the wrap.", "Layer vegetables down the center.", "Fold in the sides, roll tightly, and slice."],
        "nutrition_note": "Hummus adds plant protein and fat, while the wrap and vegetables supply carbohydrates and fiber.",
        "tags": ["vegetarian", "no-cook", "quick"],
    },
    {
        "slug": "apple-yogurt-snack-cup",
        "name": "Apple yogurt snack cup",
        "emoji": "🍎",
        "category": "Snacks",
        "description": "A satisfying sweet-and-crunchy snack in five minutes.",
        "prep_time": "5 minutes",
        "cook_time": "No cooking",
        "servings": 1,
        "ingredients": ["3/4 cup plain Greek yogurt", "1 small chopped apple", "1 tablespoon chopped nuts", "Cinnamon"],
        "instructions": ["Add yogurt to a bowl or container.", "Top with apple, nuts, and cinnamon."],
        "nutrition_note": "Yogurt offers protein, while apple and nuts add fiber and texture.",
        "tags": ["high-protein", "quick", "vegetarian"],
    },
    {
        "slug": "sheet-pan-salmon-potatoes",
        "name": "Sheet-pan salmon & potatoes",
        "emoji": "🐟",
        "category": "Dinner",
        "description": "A colorful one-pan dinner with very little cleanup.",
        "prep_time": "10 minutes",
        "cook_time": "30 minutes",
        "servings": 2,
        "ingredients": ["2 salmon fillets", "2 cups baby potatoes, halved", "2 cups asparagus", "1 tablespoon olive oil", "Lemon, dill, and black pepper"],
        "instructions": ["Heat oven to 425°F (220°C).", "Roast oiled potatoes for 15 minutes.", "Add salmon and asparagus; season and roast 12–15 minutes until cooked through."],
        "nutrition_note": "Salmon provides protein and unsaturated fats; potatoes and asparagus round out the plate.",
        "tags": ["high-protein", "one-pan", "dinner"],
    },
]


def _slugify(name):
    """Create a URL-safe, stable recipe identifier."""
    return re.sub(r"[^a-z0-9]+", "-", name.casefold()).strip("-")


def _recipe(name, emoji, category, description, ingredients, instructions, note, tags,
            prep="10 minutes", cook="15 minutes", servings=2):
    return {
        "slug": _slugify(name),
        "name": name,
        "emoji": emoji,
        "category": category,
        "description": description,
        "prep_time": prep,
        "cook_time": cook,
        "servings": servings,
        "ingredients": ingredients,
        "instructions": instructions,
        "nutrition_note": note,
        "tags": tags,
    }


# These structured collections keep a large recipe library consistent and easy
# to expand while still giving every recipe a complete, useful detail page.
OATMEAL_VARIATIONS = [
    ("Banana cinnamon", "🍌", "1 sliced banana", "1/2 teaspoon cinnamon", "1 tablespoon peanut butter"),
    ("Blueberry lemon", "🫐", "1/2 cup blueberries", "1 teaspoon lemon zest", "1 tablespoon pumpkin seeds"),
    ("Apple walnut", "🍎", "1 chopped apple", "1/2 teaspoon cinnamon", "1 tablespoon chopped walnuts"),
    ("Peach pecan", "🍑", "1 chopped peach", "1/4 teaspoon vanilla", "1 tablespoon chopped pecans"),
    ("Strawberry almond", "🍓", "1/2 cup sliced strawberries", "1 tablespoon almond butter", "1 teaspoon chia seeds"),
    ("Pumpkin spice", "🎃", "1/3 cup pumpkin purée", "1/2 teaspoon pumpkin spice", "1 tablespoon sunflower seeds"),
]
for title, emoji, fruit, flavor, topping in OATMEAL_VARIATIONS:
    RECIPES.append(_recipe(
        f"{title} oatmeal", emoji, "Breakfast", f"Warm, creamy oats with {title.casefold()} flavor.",
        ["1/2 cup rolled oats", "1 cup milk or fortified alternative", fruit, flavor, topping],
        ["Combine the oats and milk in a small saucepan.", "Cook over medium-low heat until creamy, stirring often.", f"Add {fruit.lower()} and finish with {topping.lower()}."],
        "Oats provide fiber and carbohydrates; the fruit and topping add flavor, texture, and additional nutrients.",
        ["vegetarian", "budget-friendly", "breakfast"], prep="5 minutes", cook="5 minutes", servings=1,
    ))

SMOOTHIE_VARIATIONS = [
    ("Mango spinach", "🥭", "1 cup frozen mango", "1 handful spinach", "1/2 cup plain yogurt"),
    ("Berry banana", "🫐", "1 cup frozen mixed berries", "1 banana", "1/2 cup plain yogurt"),
    ("Peach oat", "🍑", "1 cup frozen peaches", "1/4 cup rolled oats", "1/2 cup plain yogurt"),
    ("Pineapple ginger", "🍍", "1 cup frozen pineapple", "1/2 teaspoon grated ginger", "1/2 cup silken tofu"),
    ("Cherry cocoa", "🍒", "1 cup frozen cherries", "1 teaspoon cocoa powder", "1/2 cup plain yogurt"),
    ("Peanut butter banana", "🥜", "1 frozen banana", "1 tablespoon peanut butter", "1/2 cup plain yogurt"),
]
for title, emoji, produce, extra, protein in SMOOTHIE_VARIATIONS:
    RECIPES.append(_recipe(
        f"{title} smoothie", emoji, "Breakfast", f"A quick {title.casefold()} smoothie for busy mornings.",
        [produce, extra, protein, "3/4 cup milk or fortified alternative", "A handful of ice"],
        ["Add all ingredients to a blender.", "Blend until smooth, adding a splash of milk if needed.", "Pour into a glass and enjoy right away."],
        "Fruit supplies carbohydrates, while yogurt or tofu adds protein for a more satisfying smoothie.",
        ["quick", "vegetarian", "no-cook"], prep="5 minutes", cook="No cooking", servings=1,
    ))

EGG_BREAKFASTS = [
    ("Spinach tomato egg toast", "🍳", "1 handful spinach", "1 chopped tomato", "whole-grain toast"),
    ("Pepper and egg breakfast tacos", "🌮", "1/2 sliced bell pepper", "2 corn tortillas", "salsa"),
    ("Mushroom egg breakfast bowl", "🍄", "1 cup sliced mushrooms", "1 cup cooked potatoes", "chopped chives"),
    ("Broccoli cheddar egg muffins", "🧁", "1 cup chopped broccoli", "1/3 cup shredded cheddar", "whole-grain toast"),
    ("Black bean breakfast scramble", "🫘", "1/2 cup black beans", "1 chopped tomato", "1 small avocado"),
    ("Sweet potato kale breakfast hash", "🍠", "1 diced sweet potato", "1 cup chopped kale", "2 eggs"),
]
for name, emoji, produce, base, finish in EGG_BREAKFASTS:
    RECIPES.append(_recipe(
        name, emoji, "Breakfast", "A savory breakfast with protein, colorful produce, and lasting energy.",
        ["2 eggs", produce, base, finish, "1 teaspoon olive oil and black pepper"],
        ["Warm the oil in a skillet and cook the vegetables until tender.", "Add the eggs and cook until set.", "Serve with the remaining ingredients and season to taste."],
        "Eggs provide protein, while the vegetables and carbohydrate source help create a balanced breakfast.",
        ["high-protein", "beginner", "breakfast"], prep="10 minutes", cook="12 minutes", servings=1,
    ))

WRAP_VARIATIONS = [
    ("Turkey avocado veggie wrap", "🦃", "sliced turkey", "avocado", "spinach and tomato"),
    ("Chickpea salad wrap", "🫘", "mashed chickpeas", "plain yogurt", "celery and lettuce"),
    ("Chicken Caesar-style wrap", "🌯", "cooked chicken", "yogurt lemon dressing", "romaine and tomato"),
    ("Tofu rainbow wrap", "🌈", "baked tofu", "hummus", "carrot, cabbage, and pepper"),
    ("Tuna cucumber wrap", "🐟", "canned tuna", "plain yogurt", "cucumber and spinach"),
    ("White bean pesto wrap", "🌿", "white beans", "pesto", "arugula and tomato"),
    ("Egg and spinach lunch wrap", "🍳", "2 sliced hard-boiled eggs", "mustard yogurt spread", "spinach and peppers"),
    ("Lentil taco wrap", "🌮", "seasoned lentils", "salsa", "lettuce and corn"),
]
for name, emoji, protein, spread, vegetables in WRAP_VARIATIONS:
    RECIPES.append(_recipe(
        name, emoji, "Lunch", "A portable, crunchy lunch that comes together quickly.",
        ["1 large whole-grain wrap", f"1/2 cup {protein}", f"2 tablespoons {spread}", f"1 cup {vegetables}", "Lemon or lime juice"],
        ["Lay the wrap flat and spread the sauce over the center.", "Add the protein and vegetables.", "Fold in the sides, roll tightly, and cut in half."],
        "The filling provides protein and vegetables; the whole-grain wrap adds carbohydrates and fiber.",
        ["quick", "meal-prep", "lunch"], prep="10 minutes", cook="No cooking", servings=1,
    ))

SALAD_VARIATIONS = [
    ("Mediterranean chickpea salad", "🥗", "chickpeas", "cucumber, tomato, and peppers", "lemon olive oil dressing"),
    ("Chicken apple crunch salad", "🍎", "cooked chicken", "apple, celery, and greens", "mustard yogurt dressing"),
    ("Tuna white bean salad", "🐟", "canned tuna and white beans", "tomato, parsley, and greens", "lemon olive oil dressing"),
    ("Roasted vegetable quinoa salad", "🥕", "quinoa and chickpeas", "roasted zucchini, peppers, and onions", "balsamic dressing"),
    ("Southwest corn and bean salad", "🌽", "black beans", "corn, tomato, lettuce, and avocado", "lime cumin dressing"),
    ("Lentil beet salad", "🫘", "cooked lentils", "cooked beets, arugula, and orange", "orange vinaigrette"),
    ("Greek-style tofu salad", "🫒", "baked tofu", "cucumber, tomato, olives, and greens", "oregano lemon dressing"),
    ("Salmon potato green salad", "🥔", "cooked salmon", "baby potatoes, green beans, and lettuce", "dill mustard dressing"),
]
for name, emoji, protein, vegetables, dressing in SALAD_VARIATIONS:
    RECIPES.append(_recipe(
        name, emoji, "Lunch", "A colorful, make-ahead salad with a satisfying mix of textures.",
        [f"1 cup {protein}", f"2 cups {vegetables}", f"2 tablespoons {dressing}", "2 cups leafy greens", "Black pepper to taste"],
        ["Add the protein, vegetables, and greens to a large bowl.", "Drizzle with dressing and toss gently.", "Divide between bowls or pack for lunch."],
        "This salad combines protein-rich ingredients with colorful produce and a flavorful fat source.",
        ["meal-prep", "produce-packed", "lunch"], prep="15 minutes", cook="No cooking", servings=2,
    ))

SOUP_VARIATIONS = [
    ("Red lentil tomato soup", "🍅", "red lentils", "crushed tomatoes", "spinach"),
    ("Chicken vegetable noodle soup", "🍜", "cooked chicken", "whole-grain noodles", "carrots and celery"),
    ("Black bean corn soup", "🫘", "black beans", "corn and tomatoes", "bell pepper"),
    ("White bean kale soup", "🥬", "white beans", "diced potatoes", "kale"),
    ("Ginger tofu vegetable soup", "🥣", "cubed tofu", "rice noodles", "mushrooms and bok choy"),
    ("Turkey sweet potato chili", "🍠", "ground turkey", "sweet potato and beans", "tomatoes"),
    ("Chickpea vegetable curry soup", "🍛", "chickpeas", "light coconut milk", "cauliflower and peas"),
    ("Minestrone with beans", "🥕", "kidney beans", "small whole-grain pasta", "zucchini and carrots"),
]
for name, emoji, protein, base, vegetables in SOUP_VARIATIONS:
    RECIPES.append(_recipe(
        name, emoji, "Lunch", "A comforting one-pot lunch that is friendly to leftovers.",
        [f"1 1/2 cups {protein}", f"2 cups {base}", f"2 cups {vegetables}", "4 cups low-sodium broth", "1 teaspoon dried herbs or spices"],
        ["Add all ingredients except quick-cooking greens or noodles to a pot.", "Simmer until the vegetables are tender, then add any quick-cooking ingredients.", "Taste, adjust seasoning, and serve warm."],
        "Soup is a flexible way to combine protein, vegetables, and an energy-providing carbohydrate.",
        ["one-pot", "meal-prep", "budget-friendly"], prep="15 minutes", cook="25 minutes", servings=4,
    ))

BOWL_VARIATIONS = [
    ("Lemon herb chicken quinoa bowl", "🍋", "chicken", "quinoa", "zucchini and tomatoes", "lemon herb sauce"),
    ("Sesame tofu rice bowl", "🥢", "tofu", "brown rice", "broccoli and carrots", "sesame ginger sauce"),
    ("Salmon edamame grain bowl", "🐟", "salmon", "brown rice", "edamame and cucumber", "lime soy dressing"),
    ("Turkey taco rice bowl", "🌮", "ground turkey", "rice", "corn, lettuce, and tomato", "salsa"),
    ("Chickpea shawarma bowl", "🧆", "chickpeas", "couscous", "cucumber and tomato", "lemon yogurt sauce"),
    ("Lentil roasted vegetable bowl", "🥕", "lentils", "farro", "roasted carrots and cauliflower", "tahini lemon sauce"),
    ("Teriyaki chicken pineapple bowl", "🍍", "chicken", "brown rice", "pineapple and peppers", "lower-sodium teriyaki sauce"),
    ("Greek turkey meatball bowl", "🫒", "turkey meatballs", "whole-grain orzo", "cucumber and tomato", "tzatziki"),
    ("Peanut tofu noodle bowl", "🥜", "tofu", "whole-grain noodles", "cabbage and carrots", "peanut lime sauce"),
    ("Egg and vegetable breakfast-for-dinner bowl", "🍳", "eggs", "roasted potatoes", "spinach and peppers", "salsa"),
    ("White bean pesto grain bowl", "🌿", "white beans", "quinoa", "green beans and tomato", "pesto"),
    ("Shrimp corn avocado bowl", "🍤", "shrimp", "brown rice", "corn, cabbage, and avocado", "lime dressing"),
]
for name, emoji, protein, grain, vegetables, sauce in BOWL_VARIATIONS:
    RECIPES.append(_recipe(
        name, emoji, "Dinner", "A flexible bowl with protein, grains, vegetables, and a flavorful finish.",
        [f"2 cups cooked {protein}", f"2 cups cooked {grain}", f"3 cups {vegetables}", f"1/3 cup {sauce}", "Fresh herbs or seeds for serving"],
        ["Cook or warm the protein, grain, and vegetables.", "Divide the grain between bowls and arrange the protein and vegetables on top.", "Spoon over the sauce and add the finishing ingredients."],
        "This bowl includes protein, carbohydrates, vegetables, and fat from the sauce or garnish.",
        ["balanced bowl", "meal-prep", "dinner"], prep="15 minutes", cook="20 minutes", servings=4,
    ))

SHEET_PAN_VARIATIONS = [
    ("Sheet-pan lemon chicken and vegetables", "🍋", "chicken thighs", "baby potatoes", "broccoli and red onion", "lemon and oregano"),
    ("Sheet-pan tofu and sesame vegetables", "🥦", "extra-firm tofu", "sweet potato", "broccoli and peppers", "sesame ginger sauce"),
    ("Sheet-pan turkey meatballs and zucchini", "🧆", "turkey meatballs", "whole-grain pita", "zucchini and tomatoes", "Italian herbs"),
    ("Sheet-pan cod with tomatoes and beans", "🐟", "cod fillets", "white beans", "tomatoes and green beans", "lemon and parsley"),
    ("Sheet-pan sausage peppers and potatoes", "🫑", "chicken sausage", "baby potatoes", "peppers and onions", "garlic and paprika"),
    ("Sheet-pan chickpeas and cauliflower", "🫘", "chickpeas", "whole-grain couscous", "cauliflower and carrots", "cumin and lemon"),
    ("Sheet-pan chicken fajitas", "🌮", "chicken strips", "corn tortillas", "peppers and onions", "lime and mild chili spices"),
    ("Sheet-pan maple tofu and squash", "🍁", "extra-firm tofu", "butternut squash", "Brussels sprouts", "maple mustard glaze"),
    ("Sheet-pan shrimp broccoli and potatoes", "🍤", "shrimp", "baby potatoes", "broccoli", "lemon garlic seasoning"),
    ("Sheet-pan balsamic chicken and grapes", "🍇", "chicken breast", "farro", "grapes and Brussels sprouts", "balsamic glaze"),
    ("Sheet-pan tempeh sweet potato dinner", "🍠", "tempeh", "sweet potato", "green beans and onions", "smoky paprika sauce"),
    ("Sheet-pan herb pork and apples", "🍎", "pork tenderloin", "baby potatoes", "apples and cabbage", "rosemary mustard seasoning"),
]
for name, emoji, protein, carbohydrate, vegetables, seasoning in SHEET_PAN_VARIATIONS:
    RECIPES.append(_recipe(
        name, emoji, "Dinner", "A colorful oven dinner with simple preparation and minimal cleanup.",
        [f"1 pound {protein}", f"3 cups {carbohydrate}", f"4 cups {vegetables}", f"2 tablespoons {seasoning}", "1 tablespoon olive oil"],
        ["Heat the oven to 425°F (220°C) and line a large sheet pan.", "Toss the ingredients with oil and seasoning, spreading them in a single layer.", "Roast until the vegetables are tender and the protein is safely cooked, stirring halfway."],
        "Sheet-pan meals make it easy to include a protein, carbohydrate, and several vegetables in one dinner.",
        ["one-pan", "meal-prep", "dinner"], prep="15 minutes", cook="30 minutes", servings=4,
    ))

SKILLET_VARIATIONS = [
    ("Chicken spinach tomato pasta", "🍝", "chicken", "whole-grain pasta", "spinach and tomatoes", "garlic tomato sauce"),
    ("Creamy white bean broccoli pasta", "🥦", "white beans", "whole-grain pasta", "broccoli", "light lemon yogurt sauce"),
    ("Turkey zucchini rice skillet", "🥒", "ground turkey", "brown rice", "zucchini and tomatoes", "Italian herbs"),
    ("Tofu vegetable noodle stir-fry", "🥢", "tofu", "whole-grain noodles", "broccoli, peppers, and carrots", "ginger soy sauce"),
    ("Lentil sloppy joe skillet", "🫘", "lentils", "whole-grain buns", "peppers and onions", "tomato mustard sauce"),
    ("Chicken black bean enchilada skillet", "🌮", "chicken and black beans", "corn tortillas", "corn and peppers", "enchilada sauce"),
    ("Salmon pea lemon pasta", "🍋", "canned salmon", "whole-grain pasta", "peas and spinach", "lemon herb sauce"),
    ("Chickpea spinach coconut curry", "🍛", "chickpeas", "brown rice", "spinach and tomatoes", "light coconut curry sauce"),
    ("Turkey mushroom barley skillet", "🍄", "ground turkey", "quick-cooking barley", "mushrooms and kale", "thyme and broth"),
    ("Shrimp vegetable fried rice", "🍤", "shrimp and eggs", "brown rice", "peas, carrots, and cabbage", "ginger soy sauce"),
    ("Sweet potato black bean skillet", "🍠", "black beans", "sweet potato", "corn and peppers", "lime and cumin"),
    ("Chicken pesto vegetable orzo", "🌿", "chicken", "whole-grain orzo", "zucchini, peas, and spinach", "pesto"),
]
for name, emoji, protein, carbohydrate, vegetables, sauce in SKILLET_VARIATIONS:
    RECIPES.append(_recipe(
        name, emoji, "Dinner", "A weeknight-friendly skillet meal with plenty of room for substitutions.",
        [f"2 cups {protein}", f"2 cups cooked {carbohydrate}", f"3 cups {vegetables}", f"1/3 cup {sauce}", "1 tablespoon olive oil"],
        ["Warm the oil in a large skillet and cook the vegetables until nearly tender.", "Add the protein, carbohydrate, and sauce.", "Stir until everything is hot and well combined, then serve."],
        "This skillet combines a protein, energy-providing carbohydrate, and vegetables in one practical meal.",
        ["one-pan", "quick", "dinner"], prep="15 minutes", cook="20 minutes", servings=4,
    ))

SNACK_VARIATIONS = [
    ("Banana peanut butter bites", "🍌", "1 sliced banana", "1 tablespoon peanut butter", "1 teaspoon seeds"),
    ("Berry cottage cheese cup", "🫐", "3/4 cup cottage cheese", "1/2 cup berries", "1 tablespoon chopped nuts"),
    ("Cucumber hummus crackers", "🥒", "1 sliced cucumber", "1/3 cup hummus", "6 whole-grain crackers"),
    ("Pear almond yogurt bowl", "🍐", "3/4 cup plain yogurt", "1 chopped pear", "1 tablespoon almonds"),
    ("Trail mix snack cup", "🥜", "2 tablespoons nuts", "2 tablespoons seeds", "2 tablespoons raisins"),
    ("Tomato basil cottage cheese toast", "🍅", "1 slice whole-grain toast", "1/2 cup cottage cheese", "tomato and basil"),
    ("Frozen yogurt berry bark", "🍓", "1 cup plain yogurt", "1/2 cup berries", "2 tablespoons granola"),
    ("Roasted paprika chickpeas", "🫘", "1 can chickpeas", "1 teaspoon olive oil", "paprika and garlic powder"),
    ("Orange pistachio snack plate", "🍊", "1 peeled orange", "2 tablespoons pistachios", "1 cheese stick"),
    ("Avocado egg toast", "🥑", "1 slice whole-grain toast", "1/2 avocado", "1 hard-boiled egg"),
    ("Cinnamon apple oat bites", "🍎", "1 chopped apple", "1/2 cup rolled oats", "2 tablespoons peanut butter"),
    ("Edamame crunch cup", "🫛", "1 cup cooked edamame", "1/2 chopped bell pepper", "lime and chili powder"),
    ("Peach chia yogurt cup", "🍑", "3/4 cup plain yogurt", "1 chopped peach", "1 teaspoon chia seeds"),
    ("Carrot raisin peanut snack", "🥕", "1 cup carrot sticks", "2 tablespoons peanut butter", "1 tablespoon raisins"),
    ("Mini bean and cheese quesadilla", "🧀", "1 small whole-grain tortilla", "1/3 cup beans", "2 tablespoons shredded cheese"),
    ("Chocolate banana chia pudding", "🍫", "2 tablespoons chia seeds", "1/2 mashed banana", "1 teaspoon cocoa powder"),
]
for name, emoji, first, second, third in SNACK_VARIATIONS:
    no_cook = name not in {"Roasted paprika chickpeas", "Cinnamon apple oat bites", "Mini bean and cheese quesadilla"}
    RECIPES.append(_recipe(
        name, emoji, "Snacks", "A simple snack that pairs satisfying ingredients and everyday flavors.",
        [first, second, third, "Cinnamon, herbs, or spices as desired"],
        ["Gather and portion the ingredients.", "Combine or layer everything as described in the recipe name.", "Serve immediately, or chill in a covered container when appropriate."],
        "Pairing produce or whole grains with a protein or fat can make a snack more satisfying.",
        ["snack", "quick", "budget-friendly"], prep="10 minutes", cook="No cooking" if no_cook else "10 minutes", servings=1,
    ))

# The recipe page intentionally launches with 100 complete recipes.
assert len(RECIPES) == 100
assert len({recipe["slug"] for recipe in RECIPES}) == 100

ARTICLES = [
    {"icon": "🥗", "category": "Beginner basics", "title": "What does healthy eating look like?", "summary": "A flexible pattern built on variety, enough food, hydration, and meals you can realistically repeat."},
    {"icon": "🍽️", "category": "Balanced plate", "title": "Build a balanced meal", "summary": "Try vegetables or fruit, a protein, a carbohydrate, and some fat. Adjust the mix for your culture, budget, appetite, and needs."},
    {"icon": "🧠", "category": "Nutrition", "title": "Protein, carbs, fats & fiber", "summary": "Protein supports growth and repair, carbohydrates provide energy, fats support cells and vitamin absorption, and fiber supports digestion."},
    {"icon": "🏷️", "category": "Food labels", "title": "Read the whole label", "summary": "Start with serving size, then look at nutrients and ingredients in context. One number never tells the full story."},
    {"icon": "💧", "category": "Hydration", "title": "Make hydration easier", "summary": "Keep water nearby, drink with meals, and include water-rich foods. Individual fluid needs vary."},
    {"icon": "🔄", "category": "Food swaps", "title": "Add options, not rigid rules", "summary": "Try whole grains, roasted sides, or water more often when they work for you. Balance matters more than perfection."},
]

GROCERY_GROUPS = [
    {"name": "Fruits & vegetables", "icon": "🥦", "items": ["Apples", "Bananas", "Berries", "Spinach", "Broccoli", "Carrots", "Tomatoes", "Peppers"]},
    {"name": "Protein sources", "icon": "🫘", "items": ["Chicken", "Fish", "Eggs", "Beans", "Lentils", "Tofu", "Greek yogurt", "Peanut butter"]},
    {"name": "Grains & carbohydrates", "icon": "🌾", "items": ["Brown rice", "Oats", "Potatoes", "Whole-grain bread", "Whole-grain pasta", "Quinoa"]},
    {"name": "Fats & flavor", "icon": "🥑", "items": ["Avocado", "Nuts", "Seeds", "Olive oil", "Herbs", "Spices", "Lemons and limes"]},
]
