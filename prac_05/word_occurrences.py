text = input("Text: ")
word_list = text.split()
word_count = {}
max_width = 0

for word in word_list:
    if len(word) > max_width:
        max_width = len(word)
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word:{max_width}} : {count}")