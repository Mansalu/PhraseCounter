"""
PhraseCounter is a utility for counting sequences of words in
texts. Emphasis has been placed on extensibility and readability.

PhraseCounter can be run from the command line where it accepts file paths
as arguments OR text on stdin. PhraseCounter will print the top 100 most common
sequences of 3 words in the input text.

PhraseCounter can also be imported as a library and used for counting or collecting
arbitrarily sized sequences of words. It can also be used for collecting non-word n-grams
from generic sequences.

Supports Unicode characters and large files.

Written by Mitchell Steinman
Modified May 1, 2021
"""
import re
import sys
from collections import Counter

# Number of words in each sequence
SEQUENCE_SIZE = 3
# Number of top entries to print 
NUMBER_OF_ENTRIES = 100

def CleanInputText(text):
    """
    Removes all non-word and non-space characters from
    the input text and converts all characters to lowercase.
    Replaces instances of multiple spaces with a single space.
    Additionally merges words split accross lines. Apostrophes
    are stripped from contractions, but the contraction
    is maintained as one word.

    Parameters:
        text (str): The text to clean

    Returns: 
        (str): Text with all punctuation and newlines removed
    """
    # Merge words split across lines
    text = text.replace('-\n', '')
    # Replace all punctuation (preserve spaced contractions)
    text = re.sub('\s\'', '', text)
    text = re.sub("[^\w\s]", '' , text)
    # Shrink multiple spaces
    text = re.sub('\s{2,}', ' ', text)
    text = text.replace('\n', ' ')
    return text.lower()

def GetNgrams(tokens, n):
    """
    Given a list of tokens, returns all N-Grams.
    Where an N-Gram is any sequence of tokens with
    length N. 

    Parameters:
        tokens (list): The list of tokens to get N-Grams of
        n (int): The size of the gram

    Returns:
        (list): All the N sized grams that can be from tokens
    """
    return [tokens[index:index+n] for index in range(len(tokens)-n+1)]

def GetPhrases(text, numWords):
    """
    Given a text returns a list of all the phrases
    consisting of the specified number of words.

    Parameters:
        text (str): The text to get phrases from
        numWords (int): The size of the phrases in words
    
    Returns:
        (list): All the phrases in the text consisting of numWords
    """
    tokens = text.split(' ')
    # Trim empty string off the end of the token list
    if (tokens[-1] == ''):
        tokens.pop(-1)
    return [' '.join(ngram) for ngram in GetNgrams(tokens, numWords)]

def GetTopPhrases(text, phraseSize, topN):
    """
    Counts the top 'N' most common phrases in a text, where a phrase is
    a predefined number of words long, given by phraseSize.

    Parameters:
        text (str): The text to count top phrases in
        phraseSize (int): The size of each phrase in words
        topN (int): How many lines to return

    Returns:
        (Counter): Top phrase counts from the text
    """
    return Counter(GetPhrases(text, phraseSize)).most_common((topN))

def main():
    InputText = ""
    # Loop through all the command line arguments and try to read
    # the file at that path
    for argument in sys.argv[1:]:
        try:
            InputFile = open(argument, 'r', encoding='utf-8')
            InputText += InputFile.read() + ' '
        except OSError as Error:
            print("File could not be opened:", argument)
        finally:
            InputFile.close()

    if (InputText == ""):
        InputText += sys.stdin.read()

    # Top 100 3-word sequences
    counts = GetTopPhrases(CleanInputText(InputText), SEQUENCE_SIZE, NUMBER_OF_ENTRIES)

    for phrase in counts:
        print(phrase[0], '-', phrase[1], '\n')

if __name__ == "__main__":
    main()
