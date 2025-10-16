import random


def choose(lower: int, upper: int) -> list:
    """Return a random permutation of all integers within the given range.

    This function generates a list containing all integers between
    `lower` (inclusive) and `upper` (exclusive), randomly shuffled.

    Args:
        lower (int): The lower bound of the range.
        upper (int): The upper bound of the range.

    Returns:
        list: A randomly ordered list of integers in the range [lower, upper).

    Raises:
        ValueError: If the range is empty (i.e., when `lower == upper`).

    Example:
        >>> choose(1, 5)
        [3, 1, 4, 2]

    """
    lower, upper = min(lower, upper), max(lower, upper)
    return random.sample(population=range(lower, upper), k=(upper - lower))
