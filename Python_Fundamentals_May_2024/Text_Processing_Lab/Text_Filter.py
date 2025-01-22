banned_words = input().split(", ")
text = input()

for x in banned_words:
    if x in text:
        text = text.replace(x, "*" * len(x))
print(text)
