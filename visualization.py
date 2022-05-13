import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import seaborn as sns

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

def char_count(train):
    train_subset = train[(train['language'] =='Python') | 
                    (train['language'] =='Java')|
                    (train['language'] =='JavaScript')|
                    (train['language'] =='TypeScript')|
                    (train['language'] =='C++')] 
    plt.figure(figsize = (12, 8))
    sns.regplot(data = train_subset, x = 'word_count', y = 'character_count',color="black",marker="+")
    sns.scatterplot(data = train_subset, x = 'word_count', y = 'character_count',hue = 'language')
    plt.title('Relationship Between Character Count and Word Count\n',fontsize=15)


    plt.legend(title='Languages',title_fontsize=15,loc='center left', bbox_to_anchor=(1, 0.9))
    plt.grid()
    plt.ylim([0,17500])
    plt.xlim([0,1200])
    plt.show()
    
def char_count(train):
    '''
    This function takes in the train df and creates and df of the average character count and freq per language.   
    '''

    # creating df for character count and freq
    character_count = pd.DataFrame(train.groupby('top_five_languages').character_count.mean().sort_values())
    character_count['freq'] = round(character_count.character_count / character_count.character_count.sum(), 3)

    # plotting viz
    character_count.freq.plot.barh(color = ['bisque', 'wheat', 'lightsalmon', 'orange', \
                                                    'coral','red'], figsize = (12, 7))
    plt.title('By Average, JavaScript has the longest Character Count Across All Languages\n')
    plt.ylabel('Languages')
    plt.xlabel("The Frequency")
    plt.show()
    
def word_count(train):
    '''
    This function takes in the train df and creates and df of the average word count and freq per language.
    It the plots the language frequencies on a barplot and prints the results of the corresponding statistical 
    test.
    '''

    # creating dfs for word count and freq
    word_count = pd.DataFrame(train.groupby('top_five_languages').word_count.mean().sort_values())
    word_count['freq'] = round(word_count.word_count / word_count.word_count.sum(), 3)

    # plotting viz
    word_count.freq.sort_values(ascending = True).plot.barh(color = ['bisque', 'wheat', 'lightsalmon', 'orange', \
                                                    'coral','red'], figsize = (12, 7))
    plt.title('JavaScript also has the Longest Word Count Among Languages')
    plt.show()
