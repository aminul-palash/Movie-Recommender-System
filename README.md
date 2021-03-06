# Recommender System Notes

![Python](https://img.shields.io/badge/Python-3.6-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)

## Introduction to Recommender System

> Recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy or anything else depending on industries).

For example, if you’ve recently purchased a book on Machine Learning in Python and you’ve enjoyed reading it, it’s very likely that you’ll also enjoy reading a book on Data Visualization.People also tend to have similar tastes to those of the people they’re close to in their lives. Recommender systems try to capture these patterns and similar behaviors, to help predict what else you might like. As a proof of the importance of recommender systems, we can mention that, a few years ago, Netflix organised a challenges (the “Netflix prize”) where the goal was to produce a recommender system that performs better than its own algorithm with a prize of 1 million dollars to win.

## Types of Recommendar System

The purpose of a recommender system is to suggest relevant items to users. There are generally 2 main types of recommendation systems:

* <b> Content-based </b> and 
* <b>Collaborative filtering.</b>

Also, there are Hybrid recommender systems, which combine various mechanisms. In terms of implementing recommender systems, there are 2 types: 
* memory based 
* model based approaches.

> In memory-based approaches, we use the entire user-item dataset to generate a recommendation system. It uses statistical techniques to approximate users or items. Examples of these techniques include: Pearson Correlation, Cosine Similarity and Euclidean Distance, among others.

> In model-based approaches, a model of users is developed in an attempt to learn their preferences. Models can be created using Machine Learning techniques like regression, clustering, classification, and so on. 

## Content-based filtering

A Content-based recommendation system tries to recommend items to users based on their profile. The user's profile revolves around that user's preferences and tastes. It is shaped based on user ratings, including the number of times that user has clicked on different items or perhaps even liked those items. The recommendation process is based on the similarity between those items. Similarity or closeness of items is measured based on the similarity in the content of those items.

![](Images/content-base.png)
   
   > Image taken from [coursera.org](https://www.coursera.org/learn/machine-learning-with-python)

If the user has watched and rated three movies so far and she has given a rating of two out of 10 to the first movie, 10 out of 10 to the second movie and eight out of 10 to the third. The task of the recommender engine is to recommend one of the three candidate movies to this user, or in other, words we want to predict what the user's possible rating would be of the three candidate movies if she were to watch them. 


#### Limitaion of Content base System

Content-based filtering has a limitation on the quality of the description provided by the content provider. Technically, there is a limitation of what features can be extracted from the limited amount of content information. Extracting “content” information from the user is hard too. In reality, it is easier to judge people by what they do than what they say. Behavior information, like what they view, how they rate items, is much easier to collect, less intrusive and more accurate.




## Collaborative filtering methods

Collaborative filtering is based on the fact that relationships exist between products and people's interests. Collaborative filtering is based on a user saying, “Tell me what's popular among my neighbors because I might like it too.” Collaborative filtering techniques find similar groups of users, and provide recommendations based on similar tastes within that group. In short, it assumes that a user might be interested in what similar users are interested in. 

For example, suppose you're building a website to recommend blogs. By using the information from many users who subscribe to and read blogs, you can group those users based on their preferences. For example, you can group together users who read several of the same blogs. From this information, you identify the most popular blogs that are read by that group. Then — for a particular user in the group — you recommend the most popular blog that he or she neither reads nor subscribes to. 

Collaborative filtering has basically two approaches:

* <b>User-based</b>

* <b>Item-based</b>

### User based collaborative filtering

User-based collaborative filtering is based on the user similarity or neighborhood. In user-based collaborative filtering, we have an active user for whom the recommendation is aimed. The collaborative filtering engine first looks for users who are similar. That is users who share the active users rating patterns. Collaborative filtering basis this similarity on things like history,preference, and choices that users make when buying, watching, or enjoying something.

   ![](Images/collaborative.png)
   
   > Image taken from [coursera.org](https://www.coursera.org/learn/machine-learning-with-python)

For example, movies that similar users have rated highly. Then it uses the ratings from these similar users to predict the possible ratings by the active user for a movie that she had not previously watched. For instance, if two users are similar or are neighbors in terms of their interested movies, we can recommend a movie to the active user that her neighbor has already seen.

### Item based collaborative filtering

Item-based collaborative filtering is based on similarity among items.Item-item collaborative filtering is one kind of recommendation method which looks for similar items based on the items users have already liked or positively interacted with.Two items are considered to be similar if most of the users that have interacted with both of them did it in a similar way. It was developed by Amazon in 1998 and plays a great role in Amazon’s success.

It suggests an item based on items the user has previously consumed. It looks for the items the user has consumed then it finds other items similar to consumed items and recommends accordingly.

```diff
@@ But how to find similar items? and what if there are multiple similar items in that case which item to suggest first? @@
```

#### Limitations of collaborative System

* <b>Data sparsity:</b> Data sparsity happens when you have a large data set of users who generally rate only a limited number of items. Collaborative based recommenders can only predict scoring of an item if there are other users who have rated it.Due to sparsity, we might not have enough ratings in the user item dataset which makes it impossible to provide proper recommendations.

* <b>Cold start:</b> Another issue to keep in mind is something called cold start.Cold start refers to the difficulty the recommendation system has when there is a new user,
and as such a profile doesn't exist for them yet. Cold start can also happen when we have a new item which has not received a rating.

* <b>Scalability:</b> Scalability can become an issue as well.As the number of users or items increases and the amount of data expands,collaborative filtering algorithms will begin to suffer drops in performance, simply due to growth and the similarity computation.

<b>Solution: </b> There are some solutions for each of these challenges such as using <b> hybrid based recommender systems</b>. These methods, that combine collaborative filtering and content based approaches, achieves state-of-the-art results in many cases and are, so, used in many large scale recommender systems nowadays. The combination made in hybrid approaches can mainly take two forms: we can either train two models independently (one collaborative filtering model and one content based model) and combine their suggestions or directly build a single model (often a neural network) that unify both approaches by using as inputs prior information (about user and/or item) as well as “collaborative” interactions information.



## Challenges with recommender systems

Taking advantage of the "wisdom of crowds" (with collaborative filtering) has been made simpler with the data-collection opportunities the web affords. But the massive amounts of available data also complicate this opportunity. For example, although some users' behavior can be modeled, other users do not exhibit typical behavior. These users can skew the results of a recommender system and decrease its efficiency. Further, users can exploit a recommender system to favor one product over another — based on positive feedback on a product and negative feedback on competitive products, for example. A good recommender system must manage these issues.

One problem that's endemic to large-scale recommendation systems is scalability. Traditional algorithms work well with smaller amounts of data, but when the data sets grow, the traditional algorithms can have difficulty keeping up. Although this might not be a problem for offline processing, more-specialized approaches are needed for real-time scenarios.

Finally, privacy-protection considerations are also a challenge. Recommender algorithms can identify patterns individuals might not even know exist. A recent example is the case of a large company that could calculate a pregnancy-prediction score based on purchasing habits. Through the use of targeted ads, a father was surprised to learn that his teenage daughter was pregnant. The company's predictor was so accurate that it could predict a prospective mother's due date based on products she purchased.

### References

* https://www.coursera.org/learn/machine-learning-with-python 
* https://www.ibm.com/developerworks/library/os-recommender1/index.html
* https://towardsdatascience.com/introduction-to-recommender-systems-6c66cf15ada
* https://towardsdatascience.com/comprehensive-guide-on-item-based-recommendation-systems-d67e40e2b75d
* https://medium.com/@jonathan_hui/machine-learning-recommender-system-e3237b9df14a


