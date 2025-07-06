from typing_extensions import Annotated, TypedDict

class Add(TypedDict):
    """ Add two integers.

    Args:
        a: The first integer to add.
        b: The second integer to add.
    """
    a: Annotated[int, "The first integer to add."]
    b: Annotated[int, "The second integer to add."]

class Multiply(TypedDict):
    """ Multiply two integers.

    Args:
        a: The first integer to multiply.
        b: The second integer to multiply.
    """
    a: Annotated[int, "The first integer to multiply."]
    b: Annotated[int, "The second integer to multiply."]

tools = [Add, Multiply]