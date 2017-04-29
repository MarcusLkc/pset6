import nltk

class Analyzer():
    """Implements sentiment analysis."""
    
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        self.positivewords = set()
        self.negativewords = set()
        with open(positives, 'r') as f:
            
	        for line in f:
		        if line.startswith(';') == False:
			        self.positivewords.add(line.rstrip("\n"))
			        
        with open(negatives, 'r') as f:
            
            for line in f:
                if line.startswith(';') == False:
                    self.negativewords.add(line.rstrip("\n"))
        
                    
            
        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        score = 0
        for word in tokens:
            if word.lower() in self.positivewords:
                score += 1
            elif word.lower() in self.negativewords:
                score -= 1
        
        return score
