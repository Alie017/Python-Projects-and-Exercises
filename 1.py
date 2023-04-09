# **************************************  PART A ************************************************
def func_a(no):  # First function which takes an integer and transforms it to a list of digits
    if no <= 0:
        return []
    return func_a(no // 10) + [no % 10]

# **************************************  PART B ************************************************
# Second function to take list of Integers and an 1 digit y to perform the given steps in the homework


def func_b(nums_list, num):
    size = len(nums_list)
    if size % 2 == 0:
        digit_maximum = max(nums_list)
        return list(map(lambda j: num if j == digit_maximum else j, nums_list))
    elif size % 2 != 0:
        return [num] * size + nums_list


# **************************************  PART C ************************************************
# Part C (main) to Read 2 integers x and y (y should be 1-digit), call the first function with x,
# and send the resulting list, and y to the second function. Lastly, print the resulting list.

X = int(input("Enter an integer to be formed into a list: "))
Y = int(input("Enter an another integer but with only 1-digit: "))
print("\n********** Results are Shown Below **********")
print("           ", func_b(func_a(X), Y))

