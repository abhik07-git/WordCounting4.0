# wc_helpers.py
# Helper functions for the Word Count program.
# Import this module in other scripts to reuse the core counting logic.


def count_word_in_text(text: str, word: str, case_sensitive: str) -> tuple:
    """
    Count how many times a word or two-word phrase appears in a block of text.

    Arguments:
        text          -- the full text to search through (a string)
        word          -- the word or two-word phrase to count (a string)
        case_sensitive -- "yes" to match case exactly, "no" to ignore case (a string)

    Returns a tuple: (count, error_message)
        count         -- integer number of matches, or -1 if there was an error
        error_message -- string describing the error, or "" if no error occurred

    Example usage:
        count, err = count_word_in_text("The cat sat on the mat", "the", "no")
        # count -> 2, err -> ""
    """
    # Check that the search term is one or two words — no longer phrases allowed
    input_words = word.split()
    if len(input_words) > 2:
        return (-1, "Search term must be one word or a two-word phrase, not longer.")

    # Strip common punctuation so "word." still matches "word"
    clean = (text
             .replace(".", "")
             .replace(",", "")
             .replace(":", "")
             .replace("\"", "")
             .replace("(", "")
             .replace(")", "")
             .replace("_", "")
             .replace("-", ""))

    # Apply case sensitivity setting
    if case_sensitive.lower() == "no":
        clean = clean.lower()
        search_term = word.lower()
    else:
        search_term = word

    word_list = clean.split()

    # Count a single word with .count(), or step through pairs for a two-word phrase
    if len(input_words) == 1:
        count = word_list.count(search_term)
    else:
        count = 0
        phrase_parts = search_term.split()
        for i in range(len(word_list) - 1):
            if word_list[i] == phrase_parts[0] and word_list[i + 1] == phrase_parts[1]:
                count = count + 1

    return (count, "")


# --- Tests for count_word_in_text (uncomment to run manually and verify) ---
# test_text = "The quick brown fox jumps over the lazy dog"
# count, err = count_word_in_text(test_text, "the", "no")
# print(count)  # expected: 2
# count, err = count_word_in_text(test_text, "the", "yes")
# print(count)  # expected: 1
# count, err = count_word_in_text(test_text, "quick brown", "no")
# print(count)  # expected: 1
# count, err = count_word_in_text(test_text, "too many words here", "no")
# print(err)    # expected: error message about phrase being too long
