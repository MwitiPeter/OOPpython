import json
import difflib

# Load the dictionary
with open('data.json', 'r') as file:
    dictionary_data = json.load(file)

# Function to get the definition of a word
def get_definition(word):
    word = word.lower()  # Convert word to lowercase
    if word in dictionary_data:
        return dictionary_data[word]
    else:
        # Use difflib to find close matches
        matches = difflib.get_close_matches(word, dictionary_data.keys())
        if matches:
            return f"Did you mean '{matches[0]}'?"
        else:
            return "The word doesn't exist in the dictionary. Please check your spelling."

# Main function to take input and display the definition
def main():
    word = input("Enter a word: ")
    definition = get_definition(word)
    print(definition)

if __name__ == "__main__":
    main()
