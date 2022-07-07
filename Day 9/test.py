import os
import string
​import os
​story = os.path (/Users/ruby/Desktop/story.txt)
def read_file_content(story):
    """Read the contents of a file"""
​
    with open(story, "r") as file:
        text = file.read()
​
    return text
​
​
def count_words(filename):
    """
    Properly parse punctuations out of a string and return
    the number of words in the string.
    """
​
    # Read the content of `filename`.
    text = read_file_content(filename)
​
    # Create a translation table that maps all punctuation value
    # to None. i.e {"!": None, ",": None}
    translation_table = str.maketrans("", "", string.punctuation)
    
    # Apply the translation table on text, and split the test using
    # whitespace.
    split_parsed_text = text.translate(translation_table).split()
    
    # Count the content of each words in the list.
    word_dict = {}
    for word in split_parsed_text:
        word_dict[word] = word_dict.get(word, 0) + 1
​
    return word_dict
    
​
print(count_words("misc/story.txt"))