# Create a function to find the length of the longest word in a sentence.

def longest_word_length(sentence):
    words = sentence.split()
    max_length = len(words[0])
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

print(longest_word_length("The quick brown fox jumps over the lazy dog"))
