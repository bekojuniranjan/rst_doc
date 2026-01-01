def get_recepies(kind=None):
    """
    This is documents string for get_recipes.
    
    :param kind: Optional ingredient kind.
    :type kind: list[str] or None
    :return: List of recipes.
    :rtype: list[str]
    """
    return ['shells', 'gorgonzola', 'parsley']


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass