# -*- coding: utf-8 -*-
#importing important libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Reading in the file
df = pd.read_csv("books.csv")

#Visualizing the dataset
df.head(100)

#dropping null values
df = df.dropna()

#dropping features that I don't need
df = df.drop(columns=['Rank','book title','book price','author','year of publication','url'])

#Checking that the features were dropped successfully and reviewing the updated index for genre and rating.
df.info()

#Visualizing the dataset using a barplot, in this barplot only 36% of the data was used to make the graph less messy.
sns.barplot(data=df[0:35], x='rating',y="genre", palette=['purple'])
plt.show()

#Finding the genre with the highest rating.
def highest_rating():
  rating = []
  max1 = 0.0
  for i in df['rating'].index:
    rating.append(float(df['rating'][i]))
  max1 = max(rating)
  max_index = rating.index(max1)
  most_popular = df['genre'][max_index]
  return most_popular

print(highest_rating())