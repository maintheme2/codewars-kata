def top_3_words(text):
    text = text.lower()
    for ch in ['#','/', '\\', '.', '!', '@', '%', '^', '&', '*', '$', ',']:
        if ch in text:
            text = text.replace(ch, ' ')

    words = text.split(' ')

    words_freq = {}

    for word in words:
        if word in words_freq: words_freq[word] += 1
        else: words_freq[word] = 1

    words_freq = dict(sorted(words_freq.items(), reverse = True))

    top3 = []

    for key in words_freq: 
        while len(top3) != 3: 
            top3.append(key)
            break

    return top3


print(top_3_words("qwer$,qwer%qwe'r"))