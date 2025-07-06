from pydantic import BaseModel, Field

class Add(BaseModel):
    """ Add two integers.

    Args:
        a: The first integer to add.
        b: The second integer to add.
    """
    a: int = Field(..., description="The first integer to add.")
    b: int = Field(..., description="The second integer to add.")

class Multiply(BaseModel):
    """ Multiply two integers.

    Args:
        a: The first integer to multiply.
        b: The second integer to multiply.
    """
    a: int = Field(..., description="The first integer to multiply.")
    b: int = Field(..., description="The second integer to multiply.")

tools = [Add, Multiply]