n = int(input())
word = input()
words = []
filtered_word = []


for _ in range(n):
    command = input()

    words.append(command)

    if word in command:
        filtered_word.append(command)

print(words)
print(filtered_word)
