from collections import defaultdict
words = defaultdict(int)

words["one"] = 1
words["two"] = 2
print(words["three"])

print(words)

for k, v in words.items():
    print(k, v)
