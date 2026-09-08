def calculate_total(price, quantity, delivery_fee):
    """
    Calculates the total cost of an order: (price * quantity) + delivery_fee.
    """
    subtotal = price * quantity  # already done for you

    # TODO: create a variable called `total` that adds delivery_fee to subtotal
    total = delivery_fee + subtotal # TODO: replace 0 with the correct calculation

    return total