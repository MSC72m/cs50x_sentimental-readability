from cs50 import get_string

input_string = get_string("text: ")
letters = words = sentences = 0

for c in input_string:
    if c.isalpha():
        letters += 1
    if c == ' ':
        words += 1
    if c == '.' or c == '!' or c == '?':
        sentences += 1
words += 1

L = (letters / words) * 100
s = (sentences / words) * 100
subindex = 0.0588 * L - 0.296 * s - 15.8
index = round(subindex)

if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
