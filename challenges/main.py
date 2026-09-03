def sum_of_digits(number):
    # TODO: use a for loop to add up each digit of `number`
    total = 0
    for num in str(number):
        total += int(num)
    return total