words = ["apple", "grape", "maple"]
common = set(words[0])
for word in words[1:]:
    common &= set(word)
print(common)
