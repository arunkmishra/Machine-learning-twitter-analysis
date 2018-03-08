
# coding: utf-8

# In[53]:

# import shutil
import nbimporter
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import langid # identify languages based on tweets

get_ipython().magic('matplotlib inline')
plt.style.use('ggplot')


class NetworkAnalysis:
    
    def __init__(self):
        pass
        
    def Make_Graph(self,name):
        print "ashish"
        
    def Extract_Username_And_Edges(self,data):  # for making the nodes of the graph  
        nodes=set()
        edges=[]
        tweets=np.array(data['tweets'])
        username=np.array(data['username'])
       
        for i in range(0,tweets.size):
            nodes.add(username[i]) #adding the username into the set of nodes for the graph

            # extracting tagged username from the tweets using Regular Expression
            m = np.array(re.findall("(?:^|[ ])@([a-zA-Z]+)",tweets[i]))
            if len(m) :  # if the current tweet has any tagged any username
                edges.append([username[i],m]) #adding the username into the set of nodes for the graph 
            for i in m:
                nodes.add(i)
        return nodes,edges
    
    def Make_Graph(self,nodes,edges):
        UsernameMapping={}
        # mapping the username to the vertex using dictonary
        for i,data in enumerate(nodes):
            UsernameMapping[data]=i
#         return UsernameMapping
        
        
        graph = np.zeros(shape=(len(nodes),len(nodes)))   # initializing the graph
        
        # making the adjacency matrix according to the edges
        
        for each_edge in edges:
            source = each_edge[0] 
            for destination in each_edge[1]:
                graph[ UsernameMapping[source] ][ UsernameMapping[destination] ]+=1
                
        return graph,UsernameMapping
    
    def Languages_Used(self,tweets):
        
        predicted_languages = [langid.classify(tweet) for tweet in tweets]

        lang_df = pd.DataFrame(predicted_languages, columns=['language','value'])
           
        # show the top ten languages & their counts
#         print(lang_df['language'].value_counts().head(10))
       
        # plot the counts for the top ten most commonly used languages
        colors=sns.color_palette('hls', 10) 
        pd.Series(lang_df['language']).value_counts().head(10).plot(kind = "bar",
                                                                figsize=(12,9),
                                                                color=colors,
                                                                fontsize=14,
                                                                rot=45,
                                                                title = "Top 10 most common languages Used")
               
        
    def Most_Active_Users(self,data):
        
        tweeterites = data.groupby(['username']).count().reset_index()
        tweeterites = tweeterites.sort_values(by='tweets').tail(10)
        x = tweeterites['username']
        y = tweeterites['tweets']
        plt.xlabel('Twitter handle')
        plt.ylabel('Number of tweets')
        plt.title('Most number of tweets by user')
        plt.xticks(range(10), x, rotation=45)
        plt.bar(range(10), y, label='Most tweets+retweets by user')
        plt.show()
        
    
    def Actual_And_Retweets(self,data):
        retweets = []
        actual_tweets = []
        for user, tweet in zip(data['username'], data['tweets']):
            match = re.search(r'^\bRT\b', tweet)
            if match == None:
                actual_tweets.append([user,tweet])
            else:
                retweets.append([user,tweet])   

        actual_tweets = np.array(actual_tweets)
        retweets = np.array(retweets)

        plt.bar([1,2], [len(actual_tweets[:,1]), len(retweets[:,1])], align='center')
        ax = plt.gca()
        ax.set_xticks([1,2])
        ax.set_xticklabels(['Actual Tweets', 'Retweets'])
        plt.show()
        
    def Most_Mentioned_Users(self,Graph,InverseUsernameMapping):
        
        
        Total_For_Each_User = Graph.sum(axis=0)  # Total number of times a particular user is mentioned in a comment
        
        Top_10_Users = sorted(range(len(Total_For_Each_User)), key=lambda i: Total_For_Each_User[i])[-10:]
        
        username_x = [ InverseUsernameMapping[i] for i in Top_10_Users]
        total_times_mentioned_y = [ Total_For_Each_User[i] for i in Top_10_Users ]
        
        plt.xlabel('Twitter handle')
        plt.ylabel('Number of Times Mentioned')
        plt.title('Users that are Mentioned Most of the times')
        plt.xticks(range(10), username_x, rotation=45)
        plt.bar(range(10), total_times_mentioned_y, label='Most tweets+retweets by user')
        plt.show()
        
        
            
        
        
        
        

        
                
            
            
        
        

        
    
        


    
 
        

    


# In[47]:


mat = [["ashish",np.array([2,3])],["ram",np.array([5,6,5,88])],["raman",np.array([8])]]

mat.append(["daddu",np.array([5,6,5,88])])



# np.append(mat,[2,5,8],axis=0)
# x = nmat.sum(axis=0)

