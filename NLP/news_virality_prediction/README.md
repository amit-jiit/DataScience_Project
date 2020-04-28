News Article Vairality Prediction
For Raw Data i have scraped news website(The Print) from there we get news link,Title of News,Summary of news,Published Date and Author name.
i have used python scrapy module to create spider.first spider has link of news and second spider gets all the infomation from news article.
First, the cleaning part:
  Using pandas unnecessary features were removed.
  converting string to datetime, dropping null values.
Next, the preprocessing part:
  Tokenization and removal of punctuations.
  Removing stopwords. I added some extra stopwords I thouht that were relevant and then removed all stopwords.
  Training a bigrams model on the clean data. I also tried the trigrams model but that didn't really help that much.
Now, the clean data was converted into a corpus (Bag of Words model). A gensim dictionary was also formed from the clean data.
Modelling:
A very important feature for predicting views is the topic of the particular article. This can help identify if the article is related to one of the trending topics which can be determined by finding the correlation between recently published articles that went viral.
Basically, if our article is highly "similar" (cosine similarity) with recently viral articles, then our article has a high probability of going viral.

So, I did topic modelling with LDA (Latent Dirichlet Allocation) and created a distribution of topics for the given articles based on the cleaned content.
It is kinda difficult to gauge how good the LDA model performed solely by looking at the topics it spits out after being trained.
Lucky for us, there is a metric known as coherence value. Computing the coherence value will tell us how correlated the words in a single topic are. Thus, it is favorable to have a high coherence value which would imply that there is low overlap between topics.

After training with varying hyperparameters, I found that for number of topics = 15, the coherence value was the highest (~0.53).

Now, after topic modelling, to find similarity between current document and recently viral ones, we need to convert the articles into vectors with doc2vec.

Finallu, an update function was created, which needs to be called every once in while with new data to update the models (LDA, bigram, doc2vec).

All these features will then be fed to a deep neural net which will then be able to predict the number of views a particular article gets.
  
