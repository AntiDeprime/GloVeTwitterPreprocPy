import re 

class GloVePreprocessor(object):
    """Tweet preporcessor for glove.twitter.27B
       :param lowercase: Transform tweets to lowercase?, defaults to True
       :type lowercase: Bool"""
    
    def __init__(self, lowercase = True):   
        self.lowercase = lowercase
    
    def __hashtags__ (self, hashtag):    
        hashtag_body = hashtag.group()[1:]
        if( hashtag_body.upper == hashtag_body):
            result = f" <hashtag> {hashtag_body} <allcaps> "
        else:
            result = " <hashtag> " + ' '.join(hashtag_body.split('/(?=[A-Z])/)'))
        return (result)       

    def preprocess (self, tweet):
        '''Preprocessor function
        
        :param tweet: Tweet string
        :type tweet: str

        :returns: Preprocessed Tweet 
        :rtype: str
        
        '''
        self.tweet = tweet

        # Different regex parts for smiley faces
        eyes = "[8:=;]"
        nose = "['`\-]?"
        
        # Mark allcaps words
        self.tweet = re.sub(r'\b[A-Z][A-Z0-9]+\b', 
                    lambda x: f"{x.group().lower()} <allcaps> ", 
                    self.tweet)
        
        # Mark urls
        self.tweet = re.sub('https?:\/\/\S+\b|www\.(\w+\.)+\S*', " <url> ", self.tweet)
        # Force splitting words appended with slashes (once we tokenized the URLs, of course)
        self.tweet = re.sub("/"," / ", self.tweet) 
        # Mark @users
        self.tweet = re.sub('@\w+', " <user> ", self.tweet)

        # Mark smileys
        self.tweet = re.sub(f'{eyes}{nose}[)dD]+|[)dD]+{nose}{eyes}', " <smile> ", self.tweet)
        self.tweet = re.sub(f'{eyes}{nose}[pP]+', "<lolface>", self.tweet)
        self.tweet = re.sub(f'{eyes}{nose}\(+|\)+{nose}{eyes}', " <sadface> ", self.tweet)
        self.tweet = re.sub(f'{eyes}{nose}[\/|l*]', " <neutralface> ", self.tweet)
        self.tweet = re.sub('<3',"<heart>", self.tweet)
        
        # Mark numbers 
        self.tweet = re.sub(r'[-+]?[.\d]*[\d]+[:,.\d]*', " <number> ", self.tweet)

        # Mark hashtags 
        self.tweet = re.sub('#\S+', self.__hashtags__, self.tweet)

        # Mark punctuation repetitions (eg. "!!!" => "! <REPEAT>")
        self.tweet = re.sub('([!?.]){2,}', 
                    lambda x: f"{x.group()[0]} <repeat> ", 
                    self.tweet)

        # Mark elongated words like heyyy -> hey <elong>
        self.tweet = re.sub(r'\b(\S*?)(.)\2{2,}\b', 
                   lambda x: f'{x.group(1)}{x.group(2)} <elong> ',
                   self.tweet)
        
        # To lowercase 
        if self.lowercase:
            self.tweet = self.tweet.lower()
        
        # Trim whitespaces 
        self.tweet = ' '.join(self.tweet.split())

        return (self.tweet)
