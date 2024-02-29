import re

file = "analysis.txt"

with open(file, 'r') as f:
    file_cont = f.read()


def analyze_file(file_cont):
    
    def count_lines(lines):
    # Count the number of lines in a text file
        return sum(1 for line in lines)

    
    def count_words(words):
    # Use regular expression to find all words
        return len(re.findall(r'\w+', words))  #returns total word count by reading through entire file

    
    def count_characters(characters):
    # Return the total number of characters (including spaces and punctuation)
        return len(characters)

    def average_word_length(file):
    # Calculate the average length of words in the file  
        num_words = count_words(file)
        if num_words == 0:
            return 0 
        num_letters = sum(len(word) for word in re.findall(r'\w+', file ))
    # Calculate the average word length else return 0
        return num_letters / num_words
   

    def most_common_word(file):
    # Calculate the number of times a particular word occurs
        word_counts = {}
        for word in re.findall(r'\w+', file.lower()):
            if word not in word_counts:
                 word_counts[word] = 0
            word_counts[word] += 1
        max_count = max(word_counts.values())
    # returns occurrences of each word in file then finds word with highest occurrence
        return [word for word, count in word_counts.items() if count == max_count][0] 



    # Call the functions to analyze the file        
    lines = count_lines(file_cont.splitlines())
    words = count_words(file_cont)
    characters = count_characters(file_cont)
    avg_word_length_ = average_word_length(file_cont)
    most_common_word_ = most_common_word(file_cont)

    print("Number of lines: ", lines)
    print("Number of words: ", words)
    print("Number of characters: ", characters)
    print("Average word length: ", avg_word_length_)
    print("Most common word: ", most_common_word_)
    
analyze_file(file_cont)
    

             