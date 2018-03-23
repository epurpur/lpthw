import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
import csv

#open up your csv file with the sentiment results
with open('tweetybird.csv', 'r', encoding = 'utf8') as csvfile:
    #use pandas to read the "sentiment" column,
    df = pd.read_csv(csvfile)
    sent = df["Sentiment"]

#use Counter to count how many times each sentiment appears and save each as variable
    counter = Counter(sent)
    positive = counter['positive']
    negative = counter['negative']
    neutral = counter['neutral']

#declare the variables for the pie chart, using the Counter variables for "sizes"
labels = 'Positive', 'Negative', 'Neutral'
sizes = [positive, negative, neutral]
colors = ['green', 'red', 'grey']
yourtext = "Adam Ondra"

#use matplotlib to plot the chart
plt.pie(sizes, labels = labels, colors = colors, shadow = True, startangle = 90)
plt.title("Sentiment of 200 Tweets about" +yourtext)
plt.show()
