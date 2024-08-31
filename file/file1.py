# Prompt the user to enter a sentence or paragraph
user_input = input("Please enter a sentence or paragraph: ")

# Check if the user input is empty
if not user_input:
    print("Error: Please enter a valid input.")
else:
    # Proceed with word counting logic
    pass



def count_words(text):
    """
    Counts the number of words in the input text.
    """
    words = text.split()  # Split the input text into a list of words
    return len(words)  # Return the number of words


# Call the count_words function and store the result
word_count = count_words(user_input)

# Print the word count to the console
print(f"The input contains {word_count} words.")  

# Prompt the user to enter a sentence or paragraph
user_input = input("Please enter a sentence or paragraph: ")

# Check if the user input is empty
if not user_input:
    print("Error: Please enter a valid input.")
else:
    # Define a function to count the number of words
    def count_words(text):
        """
        Counts the number of words in the input text.
        """
        words = text.split()  # Split the input text into a list of words
        return len(words)  # Return the number of words

    # Call the count_words function and store the result
    word_count = count_words(user_input)

    # Print the word count to the console
    print(f"The input contains {word_count} words.")~
