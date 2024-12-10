# -*- coding: utf-8 -*-
"""Youtube.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OLAMacq36U2KSIwkmhwgkTGNSYoOAA1u
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#importing the dataset
df = pd.read_csv(r'video_id_info.csv', on_bad_lines='skip', engine='python', quoting=3)

df.head()

## lets find out missing values in your data
df.isnull().sum()

## drop missing values as we have very few & lets update dataframe as well..
df.dropna(inplace=True)

df.isnull().sum()

"""***Perform Sentiment Analysis***

**Sentiment analysis is a way for computers to understand and analyze the emotions expressed in text, like whether it's positive, negative, or neutral.
example:
<br>1.This video is quite helpful-->Positive sentiment [0,1] more it will close to 1 it will positve sentiment
<br>2.Uable to understand the topic -->Negative sentiment[-1]
<br>3. I'm attending the lecture this afternoon.-->Neutral sentiment[0]
<br>The polarity range refers to the scale used in sentiment analysis to measure the degree of positivity or negativity in text, typically ranging from -1 to 1 **

TextBlob is a Python library for processing textual data. It provides a simple API for common natural language processing (NLP) tasks
"""

#!pip install textblob
import sys #It's called "sys" because it provides access to system-specific parameters and functions.
!{sys.executable} -m pip install textblob

from textblob import TextBlob

df.head(6)

df.shape

"""
***Creating a new DataFrame (sample_df) by selecting the first 1000 rows of an existing DataFrame (df).
This can be useful for working with a smaller subset of data, such as when you want to perform quick analyses or tests without using the entire dataset.***"""

sample_df = df[0:1000]

# normal text box
TextBlob("Logan Paul it's yo big day ‼️‼️‼️")

#attribute
TextBlob("Logan Paul it's yo big day ‼️‼️‼️").sentiment

### its a neutral sentence !
TextBlob("Logan Paul it's yo big day ‼️‼️‼️").sentiment.polarity

#performing sentiment for each row of comment_text'
#polarity = [] #--black list

#for comment in df['comment_text']:
    #TextBlob(comment).sentiment.polarity
    #polarity.append(TextBlob(comment).sentiment.polarity)

#if there is black txt then will get the exception error . so avoid the exception we have to use try exception block

#syntax
#try:
    # Code that might raise an exception
 #except :
    # Code to handle the exception

!pip install tqdm
!pip install textblob
from textblob import TextBlob
from tqdm import tqdm  # For progress tracking

# Initialize an empty list to store polarity scores
polarity = []

# Iterate through each comment with a progress bar
for comment in tqdm(df['comment_text'], desc="Processing comments"):
    try:
        # Calculate sentiment polarity for the comment
        polarity_score = TextBlob(comment).sentiment.polarity
        polarity.append(polarity_score)
    except Exception as e:
        # Handle exceptions by appending a default polarity of 0
        polarity.append(0)
        print(f"Error processing comment: {comment}. Exception: {e}")

# Add the polarity list as a new column to the DataFrame (optional)
df['polarity'] = polarity

polarity = []

for comment in df['comment_text']:
    try:
        polarity.append(TextBlob(comment).sentiment.polarity)
    except:
        polarity.append(0);

len(polarity)

"""***Inserting polarity values into comments dataframe while defining feature name as "polarity"***"""

df['polarity']  = polarity

df.head(5)

"""***Wordcloud Analysis of your data: #Word cloud analysis is a visual representation technique that displays the most frequently occurring words in a text dataset***"""

filter1 = df['polarity']==1
comments_positive=df[filter1]

filter2 = df['polarity']==-1
comments_negative= df[filter2]

#!pip install wordcloud
import sys
!{sys.executable} -m pip install wordcloud

"""
***Stopwords are common words like "the," "is," and "and" that are often removed from text during analysis because they don't carry significant meaning.***"""

from wordcloud import WordCloud , STOPWORDS

set(STOPWORDS)
#turns the stopwords list into a unique collection of words for faster processing.

df['comment_text']

type(df['comment_text'])

"""***For wordcloud , we need to frame our 'comment_text' feature into string.
<br>joins all the text data from the 'comment_text' column in the DataFrame 'comments_positive' into a single string, separated by spaces.***
"""

total_comments_positive = ' '.join(comments_positive['comment_text'])

"""***This line of code creates a word cloud from the text data in `total_comments_positive`, using a predefined set of stopwords to filter out common words that don't carry significant meaning.***"""

wordcloud = WordCloud(stopwords=set(STOPWORDS)).generate(total_comments_positive)

"""
***The imshow() function in matplotlib is used to display images, and in this case, it's used to display the word cloud generated by the WordCloud library.***"""

plt.imshow(wordcloud)
plt.axis('off')

"""***Conclusion: Positive Users are emphasizing more on best , awesome , perfect , amazing , look , happy  etc..***

same for negative
"""

total_comments_negative = ' '.join(comments_negative['comment_text'])

wordcloud = WordCloud(stopwords=set(STOPWORDS)).generate(total_comments_negative)

plt.imshow(wordcloud)
plt.axis('off')

"""***Word cloud analysis is a visual representation technique that displays the most frequently occurring words in a text dataset***

***Perform Emoji's Analysis***
"""

#!pip install emoji==2.10.1
import sys
!{sys.executable} -m pip install emoji==2.10.1
## 2.10.0 is a most stable version till date , hence installing this version makes sense !

import emoji

emoji.__version__

df['comment_text'].head(6)

comment = 'trending 😉'

"""***The code snippet you provided is a list comprehension that filters out characters from a string (comment) if they are present in the emoji.
<br>EMOJI_DATA dictionary. It's a way to extract emojis from a text string.***
"""

[char for char in comment if char in emoji.EMOJI_DATA]

## lets try to write above code in a more simpler & readable way :
emoji_list = []

for char in comment:
    if char in emoji.EMOJI_DATA:
        emoji_list.append(char)

emoji_list

all_emojis_list = []

for comment in df['comment_text'].dropna(): ## in case u have missing values , call dropna()
    for char in comment:
        if char in emoji.EMOJI_DATA:
            all_emojis_list.append(char)

all_emojis_list[0:10]# 1st 10 emojis

"""***Now we have to compute frequencies of each & every emoji in "all_emojis_list"..***"""

from collections import Counter # collection package

Counter(all_emojis_list).most_common(10)

Counter(all_emojis_list).most_common(10)[0]

Counter(all_emojis_list).most_common(10)[0][0]

Counter(all_emojis_list).most_common(10)[0][1]

Counter(all_emojis_list).most_common(10)[1][0]

Counter(all_emojis_list).most_common(10)[2][0]

Counter(all_emojis_list).most_common(10)[0][1]

Counter(all_emojis_list).most_common(10)[1][1]

Counter(all_emojis_list).most_common(10)[2][1]

freqs = [Counter(all_emojis_list).most_common(10)[i][1] for i in range(10)]
freqs

emojis = [Counter(all_emojis_list).most_common(10)[i][0] for i in range(10)]
emojis

#pip install plotly
!pip install plotly==5.24.1

import plotly.io as pio
pio.renderers.default = 'iframe_connected'

""" ***use this if your chart is not displaying
<br>Plotly is configured to display plots correctly.***
"""

from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go

# Initialize notebook mode for offline plotting
init_notebook_mode(connected=True)

# Example data
emojis = ['😀', '😂', '😍', '😭', '😊']
freqs = [10, 20, 15, 25, 30]

# Create bar chart
trace = go.Bar(x=emojis, y=freqs)
iplot([trace])

"""***Conclusions : Majority of the customers are happy as most of them are using emojis like: funny , love , heart , outstanding..***

***Collect Entire data of Youtube !***
"""

import os

files= os.listdir(r'C:\Users\Desktop\youtube_Project\YT_additional_data')

files

## extracting csv files only from above list ..

files_csv = [file for file in files if '.csv' in file]
files_csv

#while colllecting the data if you encounter any kind of warning its always good to consider a warning modules.
import warnings
from warnings import filterwarnings
filterwarnings('ignore')

"""#### different types of encoding-->>
    Note : encoding may change depending upon data  , country data , sometimes regional data as well.
    Fore more inforation on Encoding -- Follow below
### https://docs.python.org/3/library/codecs.html#standard-encodings¶
"""

#all the csv file i have to store in big data frame

full_df = pd.DataFrame()
path = r'C:\Users\Desktop\youtube_Project\YT_additional_data'
for file in files_csv:
    current_df = pd.read_csv(path+'/'+file, encoding='iso-8859-1')
    full_df = pd.concat([full_df, current_df], ignore_index=True)

full_df.shape

full_df.duplicated() #True will represent the duplicate rows and  False represent the uniques rows.

full_df[full_df.duplicated()].shape

full_df = full_df.drop_duplicates() ## lets drop duplicate rows ..

full_df.shape

#### a... Storing data into csv ..
full_df[0:1000].to_csv(r'C:\Users\Desktop\youtube_Project\export_data/youtube_sample.csv' , index=False)

#### b... Storing data into json
full_df[0:1000].to_json(r'C:\Users\Desktop\youtube_Project\youtube_sample.json')

"""***Q. Which Category has the maximum likes ?***"""

full_df.head(5)

full_df['category_id'].unique() #returns an array containing the unique values of the category_id

## lets read json file ..
json_df = pd.read_json(r'C:\Users\Desktop\youtube_Project\YT_additional_data/US_category_id.json')

json_df

"""
***Retrieves the first item (index 0) from the 'items' column of the DataFrame***"""

json_df['items'][0]

#now i want id and title in a dictionary
cat_dict = {} #empty dict


for item in json_df['items'].values:     #values here return the array representation
    ## cat_dict[key] = value (Syntax to insert key:value in dictionary)
    cat_dict[int(item['id'])] = item['snippet']['title'] # snippet here is the sub dict so we have to write this way  ['snippet']['title']

cat_dict

"""
***Maps category IDs in the 'category_id' column of full_df DataFrame to their corresponding category titles using the cat_dict dictionary.***"""

full_df['category_name'] = full_df['category_id'].map(cat_dict)
full_df['category_name']

"""***Now you can notice that you have a new feature which is a category name ***"""

full_df.head(4)

"""***Q. which category has the maximum likes ?***"""

plt.figure(figsize=(12,8))#Creates a new figure with a specified size of 12 inches by 8 inches for better visualization.
sns.boxplot(x='category_name' , y='likes' , data=full_df)
plt.xticks(rotation='vertical')#Rotates the x-axis labels vertically for better readability.

"""***Find out whether audience is engaged or not
like rate ,dislike , comment_count_rate ***
"""

(full_df['likes']/full_df['views'])*100

full_df['like_rate'] = (full_df['likes']/full_df['views'])*100
full_df['dislike_rate'] = (full_df['dislikes']/full_df['views'])*100
full_df['comment_count_rate'] = (full_df['comment_count']/full_df['views'])*100

full_df.columns # three things added 'like_rate','dislike_rate', 'comment_count_rate'

#creating box plot for like rate
plt.figure(figsize=(8,6))
sns.boxplot(x='category_name' , y='like_rate' , data=full_df)
plt.xticks(rotation='vertical')
plt.show()

"""***Analysing relationship between views & likes***"""

#using Regression plot
#regression plot is nothing but it is the combination of a scatter plot + a regression kine on top of that
sns.regplot(x='views' , y='likes' , data = full_df)

"""***it seems that there is straight line it means views will increase my like will also icrease in a same way.
its is cocept of correlation***
"""

full_df.columns

full_df[['views', 'likes', 'dislikes']]

full_df[['views', 'likes', 'dislikes']].corr() ### finding co-relation values between ['views', 'likes', 'dislikes']

#Now if you want to showcase this correlation table in a vsiualized way , you can use the heatmap
sns.heatmap(full_df[['views', 'likes', 'dislikes']].corr() , annot=True)
#When annot=True, numerical values are displayed on the heatmap cells

"""***Q. Which channels have the largest number of trending videos?***"""

full_df.head(6)

full_df['channel_title'].value_counts()
# returns the count of unique values in a Series, providing a frequency distribution of the values.

### lets obtain above frequency table using groupby approach :
full_df.groupby(['channel_title']).size()

""" ***Reset_index() is a pandas DataFrame method used to reset the index of a DataFrame.
<br>It converts the index labels into a new column and assigns a default numeric index to the DataFrame.***
"""

cdf = full_df.groupby(['channel_title']).size().sort_values(ascending=False).reset_index()

cdf

cdf = cdf.rename(columns={0:'total_videos'})

cdf

import plotly.express as px

"""***Q. Which channels have the largest number of trending videos?***"""

px.bar(data_frame=cdf[0:20] , x='channel_title' , y='total_videos')