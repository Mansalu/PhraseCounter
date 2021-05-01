# PhraseCounter

PhraseCounter is a utility for counting sequences of words in texts.
Emphasis has been placed on extensibility and readability. This Project
can be run on the command line or used as a library.

PhraseCounter is designed to clean punctuation, line endings, multi-spaces,
and merge words split accross line endings. Unicode characters are handled as well as 
ASCII.

PhraseCounter uses n-grams composed from lists of words parsed from text to compute frequencies
of word sequences. PhraseCounter is also capable of counting sequences of any size, and
the n-gram windowing can be applied to generic sequences.

## Running the Project

The project can be run on the Command Line using `python3` OR using the included Dockerfile.

### On the command line

PhraseCounter accepts one or more file paths as input. Text is read from all the files provided
and sequences are compared across all the files.

If no arguments are provided, PhraseCounter accepts input on stdin.

Example:

`python3 PhraseCounter.py testFiles/moby_dick.txt testFiles/les_mis.txt`

OR

`cat testFiles/wizardOfOz.txt | python3 PhraseCounter.py`

### Run with Docker

Build the image

`docker build . -t counter`

Run the container 

`docker run counter testFiles/les_mis.txt`

## Use as a library

The code for collecting n-grams, cleaning input text, and counting sequence frequencies
can also be imported as a library.

`from PhraseCounter import *`

This allows for counting sequences with a specified number of words, getting more than 
just the top 100 results, and composing n-gram sequences from generic tokens.

It would also be reasonable to impose different input cleaning requirements (e.g. consider punctuation).

## Future Work

The current n-gram windowing algorithm is linear in both time and space. For a gram size N, and a text
containing W words complexity is O(N * W).

Given more time I would investigate using suffix trees to improve efficiency. I would add further testing.

## Tests

A comprehensive test file is provided. You can run the tests with the following command:

`python3 TestPhraseCounter.py`

## Tradeoffs considered and made

Any contractions are reported as one word with their apostrophe removed (Shouldn't becomes shouldnt).

The unit tests on large files can only really be considered regression tests since it is impossible to validate those inputs by hand. The results have been checked for sensibility, however.
