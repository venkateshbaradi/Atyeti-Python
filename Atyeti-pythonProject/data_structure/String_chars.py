# calculate the character that is repeated the most

sentence = "this is very common interview question"

count = {}

# chars = [char for char in sentence]
for char in sentence:
    if char not in count:
        count[char] = 1
    elif char in count:
        count[char] += 1

sorted_chars = sorted(count.items(), key=lambda item:item[1], reverse=True)
print(sorted_chars)
