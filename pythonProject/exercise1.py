def replace_word(word, text):
    count = 0
    words = text.split()
    new_words = []
    for w in words:
        if w.strip(".,?!'-").lower() == word:
            count += 1
            if count % 2 == 0:
                new_words.append("pathetic")
            else:
                new_words.append("marvellous")
        else:
            new_words.append(w)

    new_text = ' '.join(new_words)
    return new_text

# Read file contents
with open('file_to_read.txt', 'r') as file:
    file_content = file.read()

# Count the number of times the word "terrible" appears
word_count = file_content.lower().count("terrible")
print("Number of occurrences of 'terrible':", word_count)

# Replace the word "terrible"
new_text = replace_word("terrible", file_content)

# Writes the new text
with open('result.txt', 'w') as file:
    file.write(new_text)

print("The text has been replaced successfully, please check result.txt.")