

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

    >>> order_tshirt(1, "short", ["red", "white"])
    'Good job!'
    >>> order_tshirt('blah', 1234, True)
    'Bad job!'
    >>> order_tshirt(3, 'long', ['purple', 'green'])
    'Good job!'
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


shirt_colors_as_list = ['green', 'purple']
shirt_size_as_int = 2
short_type_as_str = "long"

result1 = order_tshirt(1, "short", ["red", "white"])
result2 = order_tshirt("blah", 1234, True)

result3 = order_tshirt(shirt_size_as_int, short_type_as_str, shirt_colors_as_list)
# print(result1, result2, result3, sep='\n')
