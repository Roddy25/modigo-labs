def sum_even_numbers(numbers):
    # TODO: return the sum of all even numbers in `numbers`
    total = 0
    for num in numbers:
     if num % 2 == 0:
        total += num
    return total
print(sum_even_numbers([1, 2, 3, 4, 5]))