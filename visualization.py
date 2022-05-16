import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
import seaborn as sns

from sklearn.model_selection import train_test_split
import sklearn.preprocessing
from sklearn.feature_selection import SelectKBest, f_regression, RFE
from sklearn.linear_model import LinearRegression, LassoLars, TweedieRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
from scipy.stats import stats, spearmanr, kruskal

def top_languages(train):
    """
    This function is to create a visual to show and get top five languages. 
    """
    # creating language freq barplot (horizontal)

    train.language.value_counts(ascending = True, normalize = True).tail().plot.barh(color =\
                                                    ['bisque', 'wheat', 'lightsalmon', 'orange', \
                                                    'coral'],figsize = (12, 7))
    # adding title
    plt.xlabel('% of Languages',fontsize=12)# set up the x axis. 
    plt.ylabel('languages',fontsize=12)# set up the y axis
    plt.title('Javascript and Python are the Most Popular Programming Languages\n',fontsize=15) # set up the title. 
    plt.show()


def word_cloud(train):
    """
    This function takes in a words_list and create a wordcloud
    """

    python_words = ''.join(str(train[train.language == 'Python'].lemmatized)) # create the list for python list. 
    javascript_words = ''.join(str(train[train.language == 'JavaScript'].lemmatized)) #create the list for javascript list. 
    c_words = ''.join(str(train[train.language == 'C++'].lemmatized)) #create the c word list. 
    java_words = ''.join(str(train[train.language == 'Java'].lemmatized)) #create the java words list. 
    typescript_words = ''.join(str(train[train.language == 'TypeScript'].lemmatized)) # create the typescript words list. 

    # generating text strings for each df
    python_words = pd.Series(python_words.split()).value_counts() #create the python words series. 
    javascript_words = pd.Series(javascript_words.split()).value_counts() #create the javascript words series. 
    c_words = pd.Series(c_words.split()).value_counts()  #create the c words series. 
    java_words = pd.Series(java_words.split()).value_counts() #create java words series.
    typescript_words = pd.Series(typescript_words.split()).value_counts() #create the typescript words

    word_counts = pd.concat([python_words, javascript_words, c_words, java_words, typescript_words], axis=1).fillna(0).astype(int)
    #Fill the NA by 0. 
    word_counts.columns = ['python_words', 'javascript_words', 'c_words', 'java_words', 'typescript_words']
    #Creating the list. 
    word_counts['all_words'] = word_counts.sum(axis=1)
    #create the word counts by sum up all the words. 
    plt.figure(figsize=(12,6))
    wc = WordCloud(background_color="white", width=800, height=400, 
                       contour_width=1, contour_color='black'
                )
    wc.generate_from_frequencies(word_counts['all_words'])                    

    # show
    plt.title('Most Common Words Across all README') #create the title.
    plt.imshow(wc, interpolation="bilinear") #set up the imshow. 
    plt.axis("off") #turn off the axis. 
    plt.show()  # create the show. 

    return



def char_word(train):
    '''
    This function takes in a dataframe
    and the column you want to create the word counts of
    returns a series of the words and their counts'''
    train_subset = train[(train['language'] =='Python') | 
                    (train['language'] =='Java')|
                    (train['language'] =='JavaScript')|
                    (train['language'] =='TypeScript')|
                    (train['language'] =='C++')] #Create the subset to to get the top languages. 
    plt.figure(figsize = (12, 8))  #Show the plt figure
    sns.regplot(data = train_subset, x = 'word_count', y = 'character_count',color="black",marker="+") #create a regplot. 
    sns.scatterplot(data = train_subset, x = 'word_count', y = 'character_count',hue = 'language') #also create a scatterplot
    plt.title('Relationship Between Character Count and Word Count\n',fontsize=15) #create a title. 


    plt.legend(title='Languages',title_fontsize=15,loc='center left', bbox_to_anchor=(1, 0.9)) #set legend. 
    plt.grid() #plt the grid 
    plt.ylim([0,17500]) #set the ylim.
    plt.xlim([0,1200])  #set the xlim. 
    plt.show() 
    
def char_count(train):
    '''
    This function takes in the train df and creates and df of the average character count and freq per language.   
    '''

    # creating df for character count and freq
    character_count = pd.DataFrame(train.groupby('top_five_languages').character_count.mean().sort_values()) 
    #groupby the top languages and get the count mean. 
    character_count['freq'] = round(character_count.character_count / character_count.character_count.sum(), 3)
    #also get the freq of the word count. 

    # plotting viz
    character_count.freq.plot.barh(color = ['bisque', 'wheat', 'lightsalmon', 'orange', \
                                                    'coral','red'], figsize = (12, 7))
    plt.title('By Average, JavaScript has the longest Character Count Across All Languages\n')#create the title 
    plt.ylabel('Languages') #set up the ylabel. 
    plt.xlabel("The Frequency")  #set up the xlabel. 
    plt.show() #show the plt. 
    
def word_count(train):
    '''
    This function takes in the train df and creates and df of the average word count and freq per language.
    It the plots the language frequencies on a barplot and prints the results of the corresponding statistical test.
    '''

    # creating dfs for word count and freq
    word_count = pd.DataFrame(train.groupby('top_five_languages').word_count.mean().sort_values())
    word_count['freq'] = round(word_count.word_count / word_count.word_count.sum(), 3)

    # plotting viz
    word_count.freq.sort_values(ascending = True).plot.barh(color = ['bisque', 'wheat', 'lightsalmon', 'orange', \
                                                    'coral','red'], figsize = (12, 7))
    plt.title('JavaScript also has the Longest Word Count Among Languages') #show the title. 
    plt.show()

def question3_spearman_stats(df):
    """This function runs a Spearman's r test in order to determine if there is a 
    correlation between character and word count for the data given.
    """
    # Set alpha
    alpha = .01
    # Set what info we want and run Pearson's R on our two train sets
    rho, p = spearmanr(df.character_count, df.word_count) 
    # Set our parameters to print our answer
    print(f'The findings of the Spearman\'s test are as follows:')
    print('----------------------------------------------------------------------')
    print(f'r-value = {round(rho,3)}')
    print(f'p-value = {round(p,3)}')
    print('=========================================================================')
    if rho >= .7:
        print(f'From the output, we can conclude that the Spearman rank correlation is\n{round(rho,3)} suggesting a strong positive correlation while the corresponding\np-value is {round(p,3)} meaning that this finding is statistically significant.')
    elif rho < .7 & rho >=.35:
        print(f'From the output, we can conclude that the Spearman rank correlation is\n{round(rho,3)} suggesting a weak positive correlation while the corresponding\np-value is {round(p,3)} meaning that this finding is statistically significant.') 
    elif rho < .35 & rho >-.35:
        print(f'From the output, we can conclude that the Spearman rank correlation is\n{round(rho,3)} suggesting little correlation while the corresponding\np-value is {round(p,3)} meaning that this finding is statistically significant.') 
    elif rho < -.35 & rho >-.7:
        print(f'From the output, we can conclude that the Spearman rank correlation is\n{round(rho,3)} suggesting a weak negative correlation while the corresponding\np-value is {round(p,3)} meaning that this finding is statistically significant.')
    else:
        print(f'From the output, we can conclude that the Spearman rank correlation is\n{round(rho,3)} suggesting a strong negative correlation while the corresponding\np-value is {round(p,3)} meaning that this finding is statistically significant.')
    return

def question4_word_stats(df):
    """
    This function defines arguments for the word count of the top 5 languages and
    then runs a Kruskal-Wallis test in order to determine if there are significant 
    differences between languages.
    """
    # Set alpha
    alpha = .01
    # Define arguments for testing
    python_length = df[df.top_five_languages == 'Python'].word_count
    javascript_length = df[df.top_five_languages == 'JavaScript'].word_count
    c_length = df[df.top_five_languages == 'C++'].word_count
    java_length = df[df.top_five_languages == 'Java'].word_count
    typescript_length = df[df.top_five_languages == 'TypeScript'].word_count
    other_length = df[df.top_five_languages == 'other'].word_count
    # Set info needed to run Kruskal-Wallis H-test using the above arguments
    H, p = stats.kruskal(python_length, javascript_length, c_length, java_length, 
                         typescript_length, other_length, nan_policy='omit')
    # Set our parameters to print our conclusion
    print(f'The findings of the Kruskal-Wallis test are as follows:')
    print('-------------------------------------------------------------------------')
    if p < alpha:
        print(f'H-statistic = {round(H,3)}')
        print(f'p-value = {round(p,3)}')
        print(f'With an p-value of {round(p,3)}, we fail to reject the null hypothesis that there is no\nlinear relationship between character count and word count.')
    else:
        print(f'H-statistic = {round(H,3)}')
        print(f'p-value = {round(p,3)}')
        print('=========================================================================')
        print(f'With an p-value of {round(p,3)}, we reject the null hypothesis that the\npopulation median for word count is equal for all languages.')
    return

def question4_char_stats(df):
    """
    This function defines arguments for the character count of the top 5 languages and
    then runs a Kruskal-Wallis test in order to determine if there are significant 
    differences between languages.
    """
    # Set alpha
    alpha = .01
    # Define arguments for testing
    python_char = df[df.top_five_languages == 'Python'].character_count
    javascript_char = df[df.top_five_languages == 'JavaScript'].character_count
    c_char = df[df.top_five_languages == 'C++'].character_count
    java_char = df[df.top_five_languages == 'Java'].character_count
    typescript_char = df[df.top_five_languages == 'TypeScript'].character_count
    other_char = df[df.top_five_languages == 'other'].character_count
    # Set info needed to run Kruskal-Wallis H-test using the above arguments
    H, p = stats.kruskal(python_char, javascript_char, c_char, java_char, 
                         typescript_char, other_char, nan_policy='omit')
    # Set our parameters to print our conclusion
    print(f'The findings of the Kruskal-Wallis test are as follows:')
    print('-------------------------------------------------------------------------')
    if p < alpha:
        print(f'H-statistic = {round(H,3)}')
        print(f'p-value = {round(p,3)}')
        print(f'With an p-value of {round(p,3)}, we fail to reject the null hypothesis that \
        the\npopulation median for character count is equal for all languages.')
    else:
        print(f'H-statistic = {round(H,3)}')
        print(f'p-value = {round(p,3)}')
        print('=========================================================================')
        print(f'With an p-value of {round(p,3)}, we reject the null hypothesis that the\npopulation median for character count is equal for all languages.')
    return