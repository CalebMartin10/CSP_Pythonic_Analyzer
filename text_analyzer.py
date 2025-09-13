def analyze_text(file_name):
    """
    Anazlyzes a txt file and pulls all the words from it for later computations.
    """
    with open(file_name, "r") as file:
        text_content = file.read()
        return text_content.lower().split()

def count_words(file_name):
    """
    Anazlyzes a text file and counts the unique words wihtin it.
    """
    word_list = analyze_text(file_name)
    from collections import Counter
    return Counter(word_list)

def count_long_words(file_name):
    """
    Anazlyzes a text file and counts the words longer than 3 characters within it.
    """
    word_list = analyze_text(file_name)
    return [word for word in word_list if len(word) > 3]

def print_word_counts(file_name):
    """
    Prints the report on how many words, unique words, and words longer than 3 characters are within a txt file.
    """
    word_list = analyze_text(file_name)
    word_count = count_words(file_name)
    long_words = count_long_words(file_name)
    print(f"The total number of words is: {len(word_list)}")
    print(f"The unique words count is: {len(word_count)}")
    print("The most frequent words are:")
    print(f"{word_count.most_common(5)}")
    print(f"Long words (more than 3 characters): {len(long_words)}")

if __name__ == "__main__":
    print_word_counts("sample.txt")