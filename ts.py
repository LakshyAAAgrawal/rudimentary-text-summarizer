#!/usr/bin/env python3

import sys
import os
import re
import math

from collections import Counter

def is_stopword(word):
    return word in [
        "a", "about", "above", "above", "across", "after", "afterwards", "again",
        "against", "all", "almost", "alone", "along", "already", "also", "although",
        "always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another",
        "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",
        "at", "back","be","became", "because","become","becomes", "becoming", "been",
        "before", "beforehand", "behind", "being", "below", "beside", "besides", "between",
        "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co",
        "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down",
        "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere",
        "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything",
        "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire",
        "first", "five", "for", "former", "formerly", "forty", "found", "four", "from",
        "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have",
        "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers",
        "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in",
        "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last",
        "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile",
        "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must",
        "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine",
        "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off",
        "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our",
        "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather",
        "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she",
        "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow",
        "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system",
        "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence",
        "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they",
        "thick", "thin", "third", "this", "those", "though", "three", "through", "throughout",
        "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty",
        "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well",
        "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas",
        "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither",
        "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without",
        "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"
    ]

def break_to_sentences(text):
    return([sentence for sentence in text.split(". ")])

def split_to_words(sentence):
    return map(str.lower, re.split(",\ |\ |;\ ", sentence))

def s_score(sentence, word_frequency):
    return sum([
        word_frequency.get(word, 0) for word in split_to_words(sentence)
    ])

def summarize(text):
    sentences = break_to_sentences(text)
    lc_text = text.lower()
    words = [
        word.lower() for sentence in sentences
        for word in split_to_words(sentence)
        if not is_stopword(word)
    ]
    word_frequency = Counter(words)
    sentence_scores = {
        sentence : score
        for score, sentence in
        sorted(zip(map(lambda x: s_score(x, word_frequency), sentences), sentences), reverse = True)
    }
    summary_sentences = list(sentence_scores.keys())[:math.ceil(len(sentences)/10)]
    summary_sentences.sort(key = lambda x: sentences.index(x))
    return(". ".join(summary_sentences))
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Usage: ts <filename>")
    if not os.path.isfile(sys.argv[1]):
        sys.exit("Sourcefile not a valid filename")
    with open(sys.argv[1], 'r') as sourcefile:
        source = sourcefile.read()
    print(summarize(source.replace("\n", " ")))
