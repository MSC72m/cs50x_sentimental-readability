# Readability Score Calculator

## Project Description
This project is a solution that calculates the readability score of a given text using the Coleman-Liau index. The program prompts the user for a string of text, analyzes the text to count the number of letters, words, and sentences, and then computes the grade level of the text.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Explanation](#algorithm-explanation)
- [Code Explanation](#code-explanation)

## Installation
No special installation is required for this project. Ensure you have Python installed and the `cs50` library available.

## Usage
To run the project, use the following command:
``` python
python readability.py
``` 
You will be prompted to enter a text string, and the program will output the readability grade level of the text.

## Algorithm Explanation
The Coleman-Liau index is a readability test designed to gauge the understandability of a text. The formula for the index is:
index = 0.0588 × 𝐿 − 0.296 × 𝑆 − 15.8
index=0.0588×L−0.296×S−15.8
Where:
𝐿 is the average number of letters per 100 words.
𝑆 is the average number of sentences per 100 words.

The algorithm works as follows:

### Count Letters, Words, and Sentences:
Letters are counted as any alphabetical character.
Words are counted as sequences of characters separated by spaces.
Sentences are counted based on the punctuation marks '.', '!', and '?'.

### Calculate L and S:
𝐿 is computed as the number of letters per 100 words.
𝑆 is computed as the number of sentences per 100 words.

### Compute the Index:
The index is calculated using the Coleman-Liau formula.
The index is rounded to the nearest whole number.

### Determine the Grade Level:
If the index is greater than 16, the output is "Grade 16+".
If the index is less than 1, the output is "Before Grade 1".
Otherwise, the output is the grade level corresponding to the index.

## Code Explanation
Importing the Library
``` python
from cs50 import get_string
``` 
This imports the get_string function from the cs50 library, which is used to prompt the user for input.

Input String
``` python

input_string = get_string("text: ")
letters = words = sentences = 0
``` 
Prompts the user for a string of text and initializes counters for letters, words, and sentences to zero.

Counting Letters, Words, and Sentences
```  python
for c in input_string:
    if c.isalpha():
        letters += 1
    if c == ' ':
        words += 1
    if c == '.' or c == '!' or c == '?':
        sentences += 1
words += 1
``` 
Iterates over each character in the input string:

Increments the letters counter if the character is an alphabetic letter.
Increments the words counter for each space encountered (indicating a new word).
Increments the sentences counter for each sentence-ending punctuation mark.
Adds one to the words counter to account for the last word in the text.
Calculating L and S
```  python
L = (letters / words) * 100
s = (sentences / words) * 100
``` 
Calculates the average number of letters and sentences per 100 words.

Computing the Index
```  python
subindex = 0.0588 * L - 0.296 * s - 15.8
index = round(subindex)
``` 
Computes the Coleman-Liau index and rounds it to the nearest whole number.

Outputting the Grade Level
```  python
if index > 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {index}")
``` 
Determines the readability grade level based on the computed index and prints the result.
