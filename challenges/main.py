def remove_duplicates(items):
    duplicates = []
    for item in items:
        if item not in duplicates:
            duplicates.append(item)
    return duplicates