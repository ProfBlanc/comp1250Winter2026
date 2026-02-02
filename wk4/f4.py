nums_one_to_ten = range(11)  # 0, 1, 2,....10
nums_one_to_ten = range(1, 11)  # 1, 2,....10
nums_two_to_twenty = range(2, 21)
nums_threes_by_three_to_thiry = range(3, 31, 3)  # 3, 6, 9, ...30

# ranges give a series of int values

nums_one_to_ten = list(range(1, 11))
print(nums_one_to_ten)

mystery = list("class") + list(range(3)) * 2
print(mystery)  # ['c' , 'l', 'a', 's', 's', 0, 1, 2, 0, 1, 2]