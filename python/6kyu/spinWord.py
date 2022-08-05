def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word[::-1] if len(word) >= 5 else word for word in words]
    return " ".join(words)

print(spin_words("Hey fellow warriors"))