import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud

def top_languages(train):
# creating language freq barplot (horizontal)
    train.language.value_counts(ascending = True, normalize = True).tail().plot.barh(color =\
                                                    ['bisque', 'wheat', 'lightsalmon', 'orange', \
                                                    'coral'],figsize = (12, 7))
# adding title
    plt.xlabel('% of Languages',fontsize=12)# set up the x axis. 
    plt.ylabel('languages',fontsize=12)# set up the y axis
    plt.title('Javascript and Python are the Most Popular Programming Languages\n',fontsize=15)
    plt.show()


def word_cloud(train):

    python_words = ''.join(str(train[train.language == 'Python'].lemmatized))
    javascript_words = ''.join(str(train[train.language == 'JavaScript'].lemmatized))
    c_words = ''.join(str(train[train.language == 'C++'].lemmatized))
    java_words = ''.join(str(train[train.language == 'Java'].lemmatized))
    typescript_words = ''.join(str(train[train.language == 'TypeScript'].lemmatized))

# generating text strings for each df
    python_words = pd.Series(python_words.split()).value_counts()
    javascript_words = pd.Series(javascript_words.split()).value_counts()
    c_words = pd.Series(c_words.split()).value_counts()
    java_words = pd.Series(java_words.split()).value_counts()
    typescript_words = pd.Series(typescript_words.split()).value_counts()

    word_counts = pd.concat([python_words, javascript_words, c_words, java_words, typescript_words], axis=1).fillna(0).astype(int)
    word_counts.columns = ['python_words', 'javascript_words', 'c_words', 'java_words', 'typescript_words']
    word_counts['all_words'] = word_counts.sum(axis=1)
    plt.figure(figsize=(12,6))
    wc = WordCloud(background_color="white", width=800, height=400, 
                       contour_width=1, contour_color='black'
                )
    wc.generate_from_frequencies(word_counts['all_words'])                    

    # show
    plt.title('Most Common Words Across all README')
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    return