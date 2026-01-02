# Documenting code-blocks in reStructuredText

## creating recipes

You can use the `lumache.get_recepies()` function:

### lumache.get_recepies(kind=None)

This is documents string for get_recipes.

* **Parameters:**
  **kind** (*list* *[**str* *] or* *None*) – Optional ingredient kind.
* **Returns:**
  List of recipes.
* **Return type:**
  list[str]

you can use the `lumache.get_random_ingredients()` function:

### lumache.get_random_ingredients(kind=None)

Return a list of random ingredients as strings.

* **Parameters:**
  **kind** (*list* *[**str* *] or* *None*) – Optional “kind” of ingredients.
* **Raises:**
  [**lumache.InvalidKindError**](#lumache.InvalidKindError) – If the kind is invalid.
* **Returns:**
  The ingredients list.
* **Return type:**
  list[str]

<!-- or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients` -->
<!-- will raise an exception. -->

### *exception* lumache.InvalidKindError

Raised if the kind is invalid.
