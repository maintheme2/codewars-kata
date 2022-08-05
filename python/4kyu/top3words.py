def top_3_words(text):
    text = text.lower()
    for ch in ['#','/', '\\', '.', '!', '@', '%', '^', '&', '*', '$', ',', "'"]:
        if ch in text:
            if ch == "'":
                if (text[text.find(ch)-1] == ' ' or text[text.find(ch)-1] == "'") and (text[text.find(ch)+1] == ' ' or text[text.find(ch)+1] == "'"):
                    text = text.replace(ch, ' ')
                else: continue      
            else : text = text.replace(ch, ' ')

    words = text.split(' ')

    words_freq = {}
    for word in words:
        if word in words_freq: words_freq[word] += 1
        else: words_freq[word] = 1

    del words_freq['']
  
    words_freq = dict(sorted(words_freq.items(), key=lambda item: item[1], reverse=True))
    
    top3 = []
    for elem in words_freq:
        while len(top3) != 3:
            top3.append(elem)
            break

    return top3


print(top_3_words(" qw ''  "))