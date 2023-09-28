# -*- coding: utf-8 -*-
"""Movie Recomender System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19Qy-iU998QiuCVjrm0-WJGTVCB1Pffk_

#Movie Recommender System
"""

# importing dependencies
import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

path = '/content/drive/MyDrive/Datasets/movies.csv'
df = pd.read_csv(path)

df.head()

# number of rows and columns
df.shape

# Total data present in the data
df.size

# slecting relevant features for recommendation
# feature engineering
# feature selection
selected_feature = ['keywords', 'genres', 'tagline' , 'cast' , 'director']
print(selected_feature)

# replacing the null values with null strings

for feature in selected_feature:
  df[feature] = df[feature].fillna('')

# combining all the selected 5 features

combined_features = df['genres']+''+df['keywords']+''+df['tagline']+''+df['cast']+''+df['director']

print(combined_features)

# convert the text data to feature vectors

vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_features)

print(feature_vectors)

"""Cosine Similarity"""

# getting the similarity scores using cosine similarity

similarity = cosine_similarity(feature_vectors)

print(similarity)

print(similarity.shape)

# getting the movie name from the user input

movie_name = input('Enter your favorite movie name :')

# creating list with all the movie name given in the dataset

list_of_all_titles = df['title'].tolist()
print(list_of_all_titles)

# finding the close match for the movie name is by the user

find_close_match = difflib.get_close_matches(movie_name , list_of_all_titles)
print(find_close_match)

close_match = find_close_match[0]
print(close_match)

# finding the index of the movie with title

index_of_the_movie = df[df.title == close_match]['index'].values[0]
print(index_of_the_movie)

# geeting a list of similar movies similar mvoies

similarity_score = list(enumerate(similarity[index_of_the_movie]))
print(similarity_score)

# sorting movies based on their similarity

sorted_similar_movies = sorted(similarity_score , key= lambda x:x[1] , reverse=True)
print(sorted_similar_movies)

# print the name of the similar movies based on the index ofv the movie
print('Movies Suggested for you \n')

i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['title'].values[0]
  if (i<30):
    print(i , '.',title_from_index)
    i+=1

"""### Movie Recommender System"""

movie_name = input(" enter the name of your favorite movie : ")
list_of_all_titles = df['title'].tolist()
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
close_match = find_close_match[0]
index_of_the_movie = df[df.title == close_match]['index'].values[0]
similarity_score = list(enumerate(similarity[index_of_the_movie]))
sorted_similar_movies = sorted(similarity_score , key= lambda x:x[1] , reverse=True)
print('Movies Suggested for you \n')

i = 1
for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.index==index]['title'].values[0]
  if (i<30):
    print(i , '.',title_from_index)
    i+=1