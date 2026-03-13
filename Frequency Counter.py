# Take sentence input
sentence = input("Enter a sentence: ")

# Convert sentence into words
words = sentence.split()

# Create empty dictionary
word_count = {}

# Count word frequency
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display result
print("Word Frequency:")
for word, count in word_count.items():
    print(word, ":", count)