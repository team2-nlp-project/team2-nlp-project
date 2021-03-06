# unicode, regex, json for text digestion
import unicodedata
import re
import json

# nltk: natural language toolkit -> tokenization, stopwords (more on this soon)
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

# pandas dataframe manipulation, acquire script, time formatting
import pandas as pd
# import acquire
from time import strftime
# import for splitting
from sklearn.model_selection import train_test_split

# shh, down in front
import warnings
warnings.filterwarnings('ignore')

import numpy as np

################### ACQUIRE DATA ###################

df = pd.read_json('data.json')

################### BASIC CLEAN ###################

def basic_clean(string):
    '''
    This function takes in a string and
    returns the string normalized.
    '''
    string = unicodedata.normalize('NFKD', string)\
            .encode('ascii', 'ignore')\
            .decode('utf-8', 'ignore')
    string = re.sub(r'[^\w\s]', '', string).lower()
    return string

################### TOKENIZE ###################

def tokenize(string):
    '''
    This function takes in a string and
    returns a tokenized string.
    '''
    # Create tokenizer.
    tokenizer = nltk.tokenize.ToktokTokenizer()
    
    # Use tokenizer
    string = tokenizer.tokenize(string, return_str = True)
    
    return string

################### FUNCTIONS ###################

def remove_stopwords(string, extra_words=[], exclude_words=[]):
    '''
    This function takes in a string, optional extra_words and exclude_words parameters
    with default empty lists and returns a string.
    '''
    # Create stopword_list.
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list.
    stopword_list = stopword_list.union(set(extra_words))

    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords

################### STEM ###################

def stem(string):
    '''
    This function takes in a string and
    returns a string with words stemmed.a
    '''
    # Create porter stemmer.
    ps = nltk.porter.PorterStemmer()
    
    # Use the stemmer to stem each word in the list of words we created by using split.
    stems = [ps.stem(word) for word in string.split()]
    
    # Join our lists of words into a string again and assign to a variable.
    string = ' '.join(stems)
    
    return string

################### LEMMATIZE ###################

def lemmatize(string):
    '''
    This function takes in string for and
    returns a string with words lemmatized.
    '''
    # Create the lemmatizer.
    wnl = nltk.stem.WordNetLemmatizer()
    
    # Use the lemmatizer on each word in the list of words we created by using split.
    lemmas = [wnl.lemmatize(word) for word in string.split()]
    
    # Join our list of words into a string again and assign to a variable.
    string = ' '.join(lemmas)
    
    return string

################### CLEAN DATAFRAME ###################

def clean_df(extra_words = [], exclude_words = ['width100px', 'altbr', 'td', 'aligncentera']):
    # pull the data
    df = pd.read_json('data.json')
    # drops nulls
    df.dropna(inplace = True)
    # add clean column that applies basic clean function
    df['clean'] = df.readme_contents.apply(basic_clean).apply(remove_stopwords)
    # tokenize df applied after running tokenize function
    tokenized_df = df.clean.apply(tokenize)
    # stemmed column created from stem function
    df['stemmed'] = tokenized_df.apply(stem)
    # lemmatized column created from lemmatize function
    df['lemmatized'] = tokenized_df.apply(lemmatize)
    # create columns with character and word counts
    df = df.assign(character_count= df.lemmatized.str.len(), 
             word_count=df.lemmatized.str.split().apply(len))
    #create a variable that stores a list of the top five languages
    top_five = ['JavaScript', 'Python', 'Java', 'TypeScript', 'C++']
    #add a column to the dataframe where any language not in the top five is represented by 'other'
    df['top_five_languages'] = np.where(df.language.isin(top_five), df.language, 'other') 
    return df

################### SPLIT THE DATA ###################

def split_data(df):
    '''
    This function takes in a data frame and splits it appropriately in order
    to return a train with 56%, validate with 24%, and test with 20% of the
    original data frame.
    '''
    # Split with train being 80% and test being 20%. Stratify on target.
    train, test = train_test_split(df, test_size = .2, random_state = 123)
    # Split the remaining train into 70% train and 30% validate.
    train, validate = train_test_split(train, test_size = .3, random_state = 123)
    # Spiltting results in a split with 56% train, 24% validate, and 20% test data from original
    # View the row and column counts of the split dataframes
    print(f'The split of this data results in the following:')
    print('------------------------------------------------')
    print(f'The train dataset contains {train.shape[0]} rows.')
    print(f'The validate dataset contains {validate.shape[0]} rows.')
    print(f'The test dataset contains {test.shape[0]} rows.')
    print(f'All split datasets contain {train.shape[1]} columns.')
    print('================================================')
    return train, validate, test