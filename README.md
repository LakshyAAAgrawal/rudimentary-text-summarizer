# Rudimentary Text Summarizer
A very basic text summarizer.

## Usage
   ```bash
   ./ts.py <filename>
   ```

## Algorithm
1. Split the text into sentences.
2. Calculate word frequency for every non-stop-word.
3. Calculate score for every sentence as - sum of word frequency of all non-stop-words.
4. Filter top 10% of sentences by score.
5. Sort based on order of appearance in the original text.
6. Join the sentences