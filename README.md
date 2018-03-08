# Machine-learning-twitter-analysis
Goals of this project : 

Generate Reports :
Generating report using data mining.

Keywords Analysis :
Which keywords derived from the tweet were the most commonly used.

Twitter Sentimental Analysis: 
classify the tweet as positive, negative on the basis of keywords.

TECHONOLGIES USED: 
JetBrains PyCharm Community Edition 5.0.1
Anaconda
SQLite
Flask : Web Framework

HOW ITS DONE:

Step 1 : Initial Analysis and Filtration
We notice a consistent group of usernames at the bottom of the weighted degree distribution and the centrality measures.
We exclude these usernames from this analysis as their contribution to the weighted links is not essential. This allows 
us to avoid challenges with the 20-min runtime for the scripts. Below the plots, we display the top usernames according 
to weighted degree and centrality (eigenvector centrality) to support the approach of filtering the most significant
usernames for the purposes of this initial model.

Step 2 : Ingesting The Data And Transformations
We transform most of the columns as character, and further truncate the usernames to have at most 20 characters in length
in order to eliminate certain anomalous usernames.  
      
Step 3 : Generating The Adjacency Matrix
This is the most computation-expensive apart of the model, as we do pair-wise tweet comparison for each username and all
the tweets. This is a highly parallelizable process so future solutions can handle millions of usernames with billions of 
tweet in the whole set.

Step 4 : Data Mining
Data mining is the computing process of discovering patterns in large data sets involving methods at the intersection of
artificial intelligence, machine learning, statistics, and database systems. It is an interdisciplinary sub-field of computer
science.
Two Steps Involved:
 Data Cleaning
 Data Processing
   
Step 5 : Machine Learning
Machine learning is a branch of artificial intelligence (AI) in which, computers develop the ability to learn according to different changing surroundings without being explicitly programmed to react to every change.
Algorithm Used :
 Logistic Regression 
 Multinomial Naïve Bayes
