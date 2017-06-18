import nltk
#from nltk.tokenize import TweetTokenizer
#from nltk.tokenize.api import TokenizerI

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        self.positiveWords = []
        self.negativeWords = []
        
        #Skip all the comments at the top and add each line to a
        #list of words.  Don't include the leading/trailing whitespace
        with open(positives, "r") as allPositiveLines:
            for line in allPositiveLines.readlines():
                if line[0] != ";":
                    self.positiveWords.append(line.strip())
        
        with open(negatives, "r") as allNegativeLines:  
            for line in allNegativeLines.readlines():
                if line[0] != ";":
                    self.negativeWords.append(line.strip())

    def analyze(self, text):
        score = 0
        
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        
        for token in tokens:
            if (token.lower() in self.positiveWords):
                score += 1
            elif (token.lower() in self.negativeWords):
                score -= 1
                
        return score
