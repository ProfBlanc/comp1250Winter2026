"""
This is the official documentation for the module

"""

def order_tshirt(shirt_size:int, shirt_type:str, shirt_color:list[str])->str:
    """
    This method controls how someone can order a t-shirt

    :param shirt_size: Represents the size of the t-shirt
    :param shirt_type: Represents the type of t-shirt
    :param shirt_color: Represents the color of the t-shirt
    :type shirt_size: int
    :type shirt_type: str
    :type shirt_color: list[str]
    :rtype: str
    :return: Represents whether the function params were used correctly
    """

    is_valid = True
    if isinstance(shirt_size, int) and shirt_size in [1,2,3]:
        pass
    else:
        is_valid = False

    if isinstance(shirt_type, str) and shirt_type in "short,long,sweater".split(","):
        pass
    else:
        is_valid = False

    if isinstance(shirt_color, list) and len(shirt_color) > 0:
        for v in shirt_color:
            if not isinstance(v, str):
                is_valid = False

    return "Good job!" if is_valid else "Bad job!"


def main():
    print("Welcome to our f5 module")
    print(__doc__)
    print("Order t-shirt documentation")
    print(order_tshirt.__doc__)

if __name__ == "__main__":
    main()