#!/usr/bin/env python
# coding: utf-8

# # Ch 4 (Twitter) Practice: Python Basic Data Types

# ## Greeting
# Make a new variable called `greeting_part_1` and assign it the string: `"Welcome, "`
# 
# Note: There is an extra space after the word

# In[1]:


greeting_part_1 = "Welcome, "


# Make a new variable called `greeting_part_2` and assign it the string: `"! It is nice to meet you!"`
# 
# Note: this string starts with an exlamation mark.

# In[2]:


greeting_part_2 = "! It is nice to meet you!"


# Make a variable called name_1 and assign it with a string of someone's name.

# In[3]:


name = "Kyle"


# Now, combine them all together into a new variable called `full_greeting`. Combine the parts together by taking `greeting_part_1` then adding `name` then adding `greeting_part_2`.
# 
# Then display the variable `full_greeting`.

# In[4]:


full_greeting = greeting_part_1 + name + greeting_part_2
display(full_greeting)


# Now make a variable called `name_2` with another name in it and make a variable `called_full_greeting_2` the same way you did `full_greeting`, but with `name_2` instead.
# 
# Then display the variable `full_greeting_2`

# In[5]:


name_2 = "Susan"
full_greeting = greeting_part_1 + name_2 + greeting_part_2
display(full_greeting)


# ## Engagement report

# Make up numbers for tweet metrics and save them into variables: `number_likes`, `number_retweets`, `number_quote_tweets`

# In[6]:


number_likes = 8
number_retweets = 3
number_quote_tweets = 7


# Write three different `display()` function calls, one to report on each of those variables.
# 
# Inside the parentheses first put a string like, `"The number of likes is: "` and then add the relevant variable to it, but remember, since the variable has a number in it, you have to put a `str()` function call around that variable name

# In[7]:


display("The number of likes is: " + str(number_likes))
display("The number of retweets is: " + str(number_retweets))
display("The number of quote tweets is: " + str(number_quote_tweets))


# Make a new variable called `total_engagement` and save the total number of all the likes, retweets and quote tweets. 
# 
# Then display that information the way you did the other variables.

# In[8]:


total_engagement = number_likes + number_retweets + number_quote_tweets

display("The total engagement is: " + str(total_engagement))


# ## Is your tweet too long

# Make a variable called `tweet_1` with a string of your choosing that is fairly short

# In[9]:


tweet_1 = "This is a short tweet"


# Make a variable called `tweet_1_length`, and save the length of the string `tweet_1` into it (using the `len()` function)

# In[10]:


tweet_1_length = len(tweet_1)


# Check if the `tweet_1_length` is less than or equal to 280 characters (the max length of a tweet) using the less than or equal operator: `<=`, and save the result into a variable called `is_tweet_1_short_enough`

# In[11]:


is_tweet_1_short_enough = tweet_1_length <= 280


# Use the `display()` function to display a string (`"Is tweet 1 short enough? "`), adding the variable `is_tweet_1_short_enough` to that string.
# 
# Remember, since the variable has a boolean and not a string in it, you have to put a str() function call around that variable name

# In[12]:


display("Is tweet 1 short enough? " + str(is_tweet_1_short_enough))


# Make a variable called `tweet_2` with a string of your choosing that is very long (over 280 characters)

# In[13]:


tweet_2 = "This is a long tweet: sadasdsaddsadsadsadsadsadsadsadsadsadsadsaasdfdsafsadfsaddsadsaasddsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsdsadsadsadsadsadsadsadsadsadsaddsafdsadsasadadssadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsadsasda"


# Repeat the rest of the steps from before, but with tweet_2
# - find tweet_2_length
# - make a variable is_tweet_2_short_enough
# - display the result

# In[14]:


tweet_2_length = len(tweet_2)
is_tweet_2_short_enough = tweet_2_length <= 280
display("Is tweet 2 short enough? " + str(is_tweet_2_short_enough))

