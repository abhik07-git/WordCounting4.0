# Word Count 4.0
# Counts how many times a word or two-word phrase appears in a file
# or in every file inside a directory.
# Results are printed to the terminal and saved to wordcount_results.csv.
#
# Refactored from WC 3.0: the core counting logic now lives in wc_helpers.py
# so it can be reused by other scripts.

import os
import sys
import wc_helpers

# -----------------------------------------------------------------------
# CHUNK 1 — Show the user where they are
# -----------------------------------------------------------------------
print("Current working directory: " + os.getcwd())
print("Contents of this directory:")
print(os.listdir())

# -----------------------------------------------------------------------
# CHUNK 2 — Collect inputs (from sys.argv if provided, otherwise ask)
# -----------------------------------------------------------------------

# Optional command-line usage:
#   python wordcount_4.py <path> <word> <yes|no>
# All three arguments must be supplied together to skip interactive mode.

if len(sys.argv) == 4:
    # Arguments supplied at the command line — skip the interactive questions
    user_path = sys.argv[1]
    word_to_count = sys.argv[2]
    case_choice = sys.argv[3]
    print(f"Using command-line arguments: path='{user_path}', word='{word_to_count}', case-sensitive='{case_choice}'")

    # Still validate the path even when given on the command line
    if not os.path.isfile(user_path) and not os.path.isdir(user_path):
        print("Error: the path provided as an argument does not exist.")
        sys.exit(1)

else:
    # Interactive mode — ask the user for each value

    # Keep asking for a path until the user gives one that actually exists
    valid_path = False
    while valid_path == False:
        user_path = input("Enter the path to a file or directory you want to search: ")
        if os.path.isfile(user_path):
            valid_path = True
        elif os.path.isdir(user_path):
            valid_path = True
        else:
            print("That path doesn't seem valid. Please try again.")

    # Get the search word or two-word phrase from the user
    word_to_count = input("Enter the word or two-word phrase to count: ")

    # Get case-sensitivity preference
    case_choice = input("Should the search be case-sensitive? (yes/no): ")

# Validate the search term length — raise an informative error if it is too long
input_words = word_to_count.split()
if len(input_words) > 2:
    raise ValueError("Search term must be one word or a two-word phrase, not longer.")

# -----------------------------------------------------------------------
# CHUNK 3 — Build the list of files to search
# -----------------------------------------------------------------------

files_to_search = []

if os.path.isfile(user_path):
    # Single file — just add it directly
    files_to_search.append(user_path)

elif os.path.isdir(user_path):
    # Directory — collect every file directly inside it
    for filename in os.listdir(user_path):
        full_path = os.path.join(user_path, filename)
        if os.path.isfile(full_path):
            files_to_search.append(full_path)

# -----------------------------------------------------------------------
# CHUNK 4 — Count the word in each file using the helper function
# -----------------------------------------------------------------------

# results is a list of tuples: (file_path, count)
results = []

for file_path in files_to_search:

    # Try to read the file; skip it with a message if reading fails
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            file_contents = f.read()
    except:
        print("Could not read file: " + file_path + " — skipping.")
        results.append((file_path, -1))
        continue

    # Call the helper function to do the actual counting
    count, error_msg = wc_helpers.count_word_in_text(file_contents, word_to_count, case_choice)

    if error_msg != "":
        print("Error: " + error_msg)
        results.append((file_path, -1))
    else:
        results.append((file_path, count))
        print(f"The word '{word_to_count}' was found {count} time(s) in: {file_path}")

# -----------------------------------------------------------------------
# CHUNK 5 — Save results to wordcount_results.csv
# -----------------------------------------------------------------------

# Each run appends rows so multiple searches accumulate in the same file.
# CSV format: word,directory,filename,count

with open("wordcount_results.csv", "a", encoding="utf-8") as csv_file:
    for result_tuple in results:
        file_path, count = result_tuple

        # Skip files that could not be read (count stored as -1)
        if count == -1:
            continue

        directory = os.path.dirname(file_path)
        filename = os.path.basename(file_path)

        # If the file was in the current directory, dirname comes back empty
        if directory == "":
            directory = os.getcwd()

        csv_row = word_to_count + "," + directory + "," + filename + "," + str(count)
        csv_file.write(csv_row + "\n")

print("Results also saved (appended) to wordcount_results.csv")
