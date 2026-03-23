# Python Text Processing Assignment - Starter Code

# ============================================================================
# Task 1: String Manipulation and Analysis
# ============================================================================

def count_words(text):
    """Count the number of words in the given text."""
    # TODO: Implement this function
    pass


def reverse_string(text):
    """Return the string in reverse order."""
    # TODO: Implement this function
    pass


def find_longest_word(text):
    """Find and return the longest word in the given text."""
    # TODO: Implement this function
    pass


def convert_case(text):
    """Convert text to different cases."""
    # TODO: Implement this function
    # Return a dictionary with keys: 'uppercase', 'lowercase', 'titlecase'
    pass


# Test Task 1
if __name__ == "__main__":
    sample_text = "Python is a powerful programming language"
    
    print("=== Task 1: String Manipulation ===")
    print(f"Original text: {sample_text}")
    print(f"Word count: {count_words(sample_text)}")
    print(f"Reversed: {reverse_string(sample_text)}")
    print(f"Longest word: {find_longest_word(sample_text)}")
    print(f"Case conversions: {convert_case(sample_text)}")


# ============================================================================
# Task 2: File Reading and Writing
# ============================================================================

def analyze_file(input_filename, output_filename):
    """Read a file, analyze its content, and write statistics to output file."""
    # TODO: Implement this function
    # It should:
    # - Count lines, words, and characters
    # - Handle file not found errors
    # - Write results to output_filename
    pass


# ============================================================================
# Task 3: Text Processing Application
# ============================================================================

def clean_and_deduplicate_text(input_filename, output_filename):
    """Clean text data and remove duplicates."""
    # TODO: Implement this function
    # It should:
    # - Read entries from input file
    # - Remove duplicates (preserve order)
    # - Remove special characters and extra spaces
    # - Write cleaned data to output file
    # - Return statistics (original count, final count, duplicates)
    pass
