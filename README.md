# Word Count 4.0

A Python program that counts how many times a word (or two-word phrase) appears
in a text file or in every text file inside a directory.

---

## How to run the program

Open a terminal and navigate to the folder containing `wordcount_4.py`, then run:

```
python wordcount_4.py
```

The program will walk you through everything interactively.

### Optional: command-line arguments

You can also skip the interactive questions by passing three arguments after the
script name, in this order:

```
python wordcount_4.py <path> <word> <yes|no>
```

| Argument | What to put here |
|---|---|
| `<path>` | Path to a file or directory to search |
| `<word>` | The word or two-word phrase to count (use quotes for two words) |
| `<yes|no>` | `yes` for case-sensitive search, `no` to ignore case |

Example:

```
python wordcount_4.py ./my_folder "hello world" no
```

---

## What the program does

1. Prints your current working directory and its contents so you can easily
   find the file or folder you want to search.
2. Asks you for a path to a file or directory (or reads it from the command line).
   - If you type a path that does not exist, the program will ask again until
     you provide a valid one.
   - If a directory is provided, the program searches every file directly inside
     that directory (not sub-folders).
3. Asks for the word or two-word phrase to search for.
4. Asks whether the search should be case-sensitive.
5. Reads each file, cleans punctuation so words like `"word."` match `"word"`,
   and counts how many times the search term appears.
6. Prints each result to the terminal.
7. Appends all results to `wordcount_results.csv` in the current working
   directory. Each row looks like:

   ```
   word,directory,filename,count
   ```

---

## Features included

- Counts a single word or a two-word phrase (three or more words causes an error
  with an informative message).
- Case-sensitive or case-insensitive counting based on user choice.
- Accepts either a single file or a whole directory as the search target.
- Keeps asking for a valid path until the user provides one.
- Saves results to `wordcount_results.csv` (appends, so multiple runs
  accumulate in the same file).
- Supports optional command-line arguments to skip interactive prompts.

## Known limitations / bugs

- Only searches files directly inside a directory — sub-folders are not searched.
- Files that cannot be decoded as UTF-8 text are skipped with a warning message.
- The CSV file is appended to on every run, delete it manually if you want a
  fresh results file.

---

## Files in this project

| File | Purpose |
|---|---|
| `wordcount_4.py` | Main script — run this |
| `wc_helpers.py` | Helper module with the word-counting function |
| `wordcount_results.csv` | Created/updated automatically when the program runs |
