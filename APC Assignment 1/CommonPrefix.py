# longest prefix
# 20240802652
word1 = input("Enter a Word1:")
word2 = input("Enter a Word2:")
longest_prefix = ""
if len(word1)<len(word2):
    word = len(word1)
else:
    word = len(word2)
for i in range(word):
    if word1[i] == word2[i]:
        longest_prefix+=word1[i]
    else:
        break
print(longest_prefix)