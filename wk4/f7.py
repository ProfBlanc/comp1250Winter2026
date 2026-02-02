# Ask the user to input a word
first_list = list(input("Enter a word: "))
# ask the user to input another word
second_list = list(input("Enter another word: "))

# ask the user to input a positive number
pos_num = int(input("Enter a positive integer: "))
if pos_num < 0:
    print("Invalid input")

# ask the user to input a negative number
neg_num = int(input("Enter a negative integer: "))
if neg_num >= 0:
    print("Invalid input")
# ask the user to input a letter
search = input("Enter a letter")[0]

# create 1 list for first word
# create 1 list of second word
first_and_second_list = first_list + second_list
first_values_of_lists = [first_list[0], second_list[0]]
l = [1, "a"]
first_values_of_lists_v2 = first_list[:1] + second_list[:1]

# determine if index of 1st number exists in first list
    # if yes, output the value found at this index
if pos_num >= len(first_list):
    print(first_list[pos_num])
# same thing for neg index
if neg_num <= len(first_list) * -1:
    print(second_list[neg_num])
# determine if letter found in both lists
print(search in first_list and search in second_list)

# repeat for tuples