word = input()
reverse_word = ''
for i in reversed(range(len(word))):
    reverse_word += word[i]
print(reverse_word)
