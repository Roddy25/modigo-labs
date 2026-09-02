def find_longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    # TODO: loop through `words` and update `longest` whenever
    # a strictly longer word is found
    return longest