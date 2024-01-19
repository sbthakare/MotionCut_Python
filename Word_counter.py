def count_words(input_text):
    # Split the input text into words using whitespace as a delimiter
    words = input_text.split()

    # Return the count of words
    return len(words)

def main():
    try:
        # Prompt the user to enter a sentence or paragraph
        user_input = input("Enter a sentence or paragraph: ")

        # Check if the input is not empty
        if user_input.strip():
            # Call the count_words function to get the word count
            word_count = count_words(user_input)

            # Display the word count
            print(f"Word count: {word_count}")
        else:
            print("Error: Empty input. Please enter a valid text.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
