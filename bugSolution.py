def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if sum(numbers) == 0 and len(numbers)>0:
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage:
my_numbers = [1, 2, 3, 4, 5]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

my_list_with_zero = [1,2,0,4,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average with zero is: {average_zero}")

my_list_all_zeros = [0,0,0]
average_all_zeros = calculate_average(my_list_all_zeros)
print(f"The average with all zeros is: {average_all_zeros}"