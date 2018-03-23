from aylienapiclient import textapi
import csv, io

#initialize a new client of AYLIEN text api
client = textapi.Client('e67be2b0', '816057ee391c17e610cb4206b2167087')

with io.open('tweetybird.csv', 'w', encoding='utf8', newline= '') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Tweet", "Sentiment"])
    with io.open("tweetybird3.txt", 'r', encoding='utf8') as f:
        for tweet in f.readlines():
            #remove extra spaces or newlines around text
            tweet = tweet.strip()

            if len(tweet) == 0:
                print ('skipped')
                continue

            print (tweet)

            #make call to Aylien Text api
            sentiment = client.Sentiment({'text': tweet})

            #write the sentiment result into csv file
            csv_writer.writerow([sentiment['text'], sentiment['polarity']])
