def smart_title_case(sentence):
    # TODO: capitalize each word except connector words (a, an, the, of, in, on, and),
    # unless that connector word is the first word in the sentence
    if not sentence:
        return ""
    small_words = {"a", "an", "the", "of", "in", "on", "and"}
    words = sentence.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word not in small_words:
            result.append(word.capitalize())
        else:
            result.append(word)
    return " ".join(result)
print(smart_title_case("the lord of the rings"))