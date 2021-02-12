
# coding: utf-8

# ## Author - Rimsha Virmani
# ## The Sparks Foundation GRIPFEB'21
# ## Task 4: Exploratory Data Analysis - Sports
# ## Perform ‘Exploratory Data Analysis’ on dataset ‘Indian Premier League’
# ## Dataset: https://bit.ly/34SRn3b

# In[1]:


#importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#reading the dataset
matches = pd.read_csv('matches.csv')
matches.head()


# In[4]:


deliveries= pd.read_csv('deliveries.csv')
deliveries.head()


# In[5]:


#overall info of 1st dataset
matches.info()


# In[6]:


matches.describe()


# In[7]:


#overall info of 2nd dataset
deliveries.info()


# In[8]:


deliveries.describe()


# In[9]:


matches.isnull().sum()


# In[10]:


deliveries.isnull().sum()


# ##  No. of matches 
# 

# In[11]:


matches['id'].max()


# ## Seasons

# In[12]:


matches['season'].unique()


# In[13]:


len(df['season'].unique())


# ## Team won by maximum runs

# In[15]:


matches.iloc[matches['win_by_runs'].max()]


# In[16]:


matches.iloc[matches[matches['win_by_wickets'].ge(1)].win_by_wickets.idxmin()]


# In[18]:


# seasons having most number of matches
sns.countplot(x='season', data= matches)
plt.show()


# In[19]:


data = matches.winner.value_counts()
sns.barplot(y = data.index, x= data, orient='h')


# ## Top player of match winners

# In[20]:


top_players = df.player_of_match.value_counts()[:10]
top_players


# In[21]:


matches['team1'].unique()


# In[22]:


matches['team2'].unique()


# In[23]:


deliveries['batting_team'].unique()


# In[24]:


deliveries['bowling_team'].unique()


# In[27]:


matches.loc[matches['city'].isnull()]


# ## Matches per season

# In[28]:


plt.subplots( figsize=(20,10))
sns.countplot(x = 'season', data= matches, palette='rocket_r')
plt.title('Matches per season', fontsize=35)
plt.xlabel('Seasons', fontsize=15)
plt.ylabel('Matches', fontsize=15)
plt.show()


# ## MATCHES PER TEAM

# In[31]:


num_matches = pd.concat([matches['team1'], matches['team2']])
num_matches= num_matches.value_counts()
plt.figure(figsize=(20,10))
plt.bar(x= num_matches.index, height= num_matches.values, color='blue')
plt.title('Matches per team', fontsize=35)
plt.xlabel('Team', fontsize=15)
plt.ylabel('Matches', fontsize=15)
plt.xticks(rotation=270, fontsize=15)
plt.show()


# ## How many matches were played in which venue

# In[32]:


plt.subplots(figsize=(20,10))
sns.countplot(x = 'venue', data=matches, palette='mako', order=matches['venue'].value_counts().index)
plt.title('IPL Venue', fontsize=35)
plt.xlabel('Stadium', fontsize=15)
plt.ylabel('Matches', fontsize=15)
plt.xticks(rotation=270, fontsize=15)
plt.show()


# In[33]:


top_players = matches.player_of_match.value_counts()[:10]


# ## Top player of the match winners

# In[34]:


plt.subplots(figsize=(20,10))
sns.barplot(x =top_players.index,y=top_players,  data=matches, palette='mako')
plt.title('Top player of the match Winners', fontsize=35)
plt.xlabel('Player', fontsize=15)
plt.ylabel('Match', fontsize=15)
plt.xticks(rotation=270, fontsize=15)
plt.show()


# ## Conclusion
# # 2013 has the most matches played.
# # 2009 is the season with less no. of matches
# # Mumbai Indians play the highest amount of matches
# # CSK is the second highest in winning matches.
