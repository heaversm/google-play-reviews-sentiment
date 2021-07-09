import nltk
#nltk.download('vader_lexicon') #TODO: needed for first run only
from google_play_scraper import Sort, reviews
from nltk.sentiment import SentimentIntensityAnalyzer

IDENTIFIER = 'org.mozilla.firefox.vpn'

sia = SentimentIntensityAnalyzer()
f = open('results-w-sentiment.txt', 'w')

def init():
    results, continuation_token = reviews(
        IDENTIFIER,
        lang='en', # defaults to 'en'
        country='us', # defaults to 'us'
        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
        count=3, # defaults to 100
        #filter_score_with=5 # defaults to None(means all score)
    )
    #print(results)
    
    
    for result in results:
      #print(sia.polarity_scores(result['content']))
      #print(result['content'])
      f.write(str(sia.polarity_scores(result['content'])) + ' ')
      f.write("%s\n" % str(result['content']))
    
    #f.close() #TODO: TEMPORARY!

    continue_results(continuation_token)

def continue_results(continuation_token):
  results, _ = reviews( 
    IDENTIFIER,
    continuation_token=continuation_token # defaults to None(load from the beginning)
  )
  #print(results)
  if results:

    for result in results:
      #print(result['content'])
      f.write(str(sia.polarity_scores(result['content'])) + ' ')
      f.write("%s\n" % str(result['content']))
    continue_results(_)
  else:
    f.close()

init()