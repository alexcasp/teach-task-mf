# To complete this Kata you need to make a function multiplyAll/multiply_all which takes an array of integers as an argument. This function must return another function, which takes a single integer as an argument and returns a new array.
#
# The returned array should consist of each of the elements from the first array multiplied by the integer.
#
# Example:
#
# multiply_all([1, 2, 3])(2); // => [2, 4, 6]
# You must not mutate the original array.


def multiply_all(arr):
    def multiply_by(n):
        return [x * n for x in arr]
    return multiply_by
print(multiply_all([1, 2, 3])(2))  # Ожидаемый результат: [2, 4, 6]
print(multiply_all([0, -1, 5])(3))  # Ожидаемый результат: [0, -3, 15]
print(multiply_all([])(10))