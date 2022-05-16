# Team 2 NLP Project
## Project Goals:
The goal of this project was to build a classification model that can predict the programming language of a repository based on the text of the repository's README.md file. 
***
Project Goals/Description
Most of the code hosting platforms for opensource projects consider the README file as the project introduction. As it is the first document seen by the reader, such a document needs to be crafted with care.  The goal of this project is to predict the programming language for 100 repository by scraping, analyze the repository's README file contents. Using these datasets from 100 README's we were able to predict what programming language was used based on the composition of the README text.
*** 

## Project Outline:
* Acquisiton of data:
    * Search for repositories on git hub.
    * Conduct web scraping of repositories' readme contents.
* Prepare and clean data:
    * Remove repositories in languages other than english. 
    * Drop nulls.
    * Converted all characters to lowercase,
    * Remove stopwords 
    * Tokenize the data
    * Stem and Lemmatize
    * Narrow data down to repo,…. 
* Explore data:
    * Explore word clouds for top languages. 
    * How often are words used?
    * Utilize bar graphs, bigrams and trigrams for top languages
    * Analyze bigram and trigram word clouds for top  languages
    * Few other.....?
* Modeling:
    * Created baseline model.
    * Make multiple competitive models
    * Use cleaned, stemmed and lemmatized data on models
    * Pick best performing model to move forward with.
    * Test the top model on unseen test data set
    * Conclude results
* Deliverables: 
    * A clearly named final notebook with more detailed processes. 
    * A README that explains what the project is, how to reproduce the project, and notes about the project.
    * A Python module or modules that automate the data acquisition and preparation process.
    * A final presentation on google slides. 

## Data Dictionary 
   |Column | Description | Dtype|
    |--------- | --------- | ----------- |
    repo | Name of the Github repo used to extract data | object |
    language | repo language used | object | 
    readme_contents | Repo's README.md | object |
    clean | removed inconsistencies in unicode characters from readme_contents. Converted the resulting string to the ASCII character set and turne dthe resulting bytes object back into a string | object |
    stemmed | stemmed words from originial readme_contents | object
    lemmatized | root words from the clean column | object |
    character_count | counts the characters in the lemmatized column | int64 |
    word_count | counts the words in the lemmatized column | int 64
    top_five_languages | takes the five most popular languages, keeps them as their own, and bundles all other languages as 'other'. Used for modeling | object

* Language Dictionary
|Language | Description |
 |--------- | --------- |
 JavaScript | Object-oriented computer language commonly used to create interactive effects within web browsers |
 Python | An interpreted, object-oriented, high-level programming langauage with dynamic semantics | 
 Java | A general-purpose programming language that is class-based and object oriented| 
 TypeScript | A language developed and maintained by Microsoft. It is a strict syntactical superset of JavaScript and adds optional static typing to the language |
 C++ | C++ is a general-purpose programming language and widely used nowadays for competitive programming. |     
    
    
## Acquisition/Preparation:

Data Wrangle:
* Web scraping methods were used to create a list from random respository README files. 
    - The list of repositories was put into the acompanying acquire.py file which creates a list of dictionaries that includes the name of the repository, the programming language used in the repository, and the content of the readme file for each repository in the list, and saves it as a .json file. The .json file is required to reproduce this project with this notebook and can be created by saving the acquire.py file in your local repository and running 'python acquire.py' from the terminal.
* Create a function in the matt_prepare.py file that does the following:
    - Drops nulls and removes languages other than English
    - Lowercase all letters
    - Normalize text
    - Create columns for stemmed data and lemmatized data
    - Remove stopwords
    - Adds column for character and word count
* Split data into train, validate and test set
    - Split 20% (test), 24% (validate), and 56% (train)
* Test functions
***
## Exploration:
* Ask questions/form hypothesis
    * Question 1: What are the most common languages from the repos we explored?
    * Question 2: What are the most common words across all READme's?
    * Question 3: Does length of READme differ between languages
    * Question 4: Are there any words that are found in all repos?
    * Question 5: 
* Explore using visualizations:
    - Create wordclouds
    - Explore word frequencies
    - Explore ngrams
* Use statistical tests to test hypothesis
    - Pearsonr test
    - kruskal-wallis
*  Document answers to questions and takeaways
    - JavaScript and Python are the most popular programmig languages
    - There are popular words across the top language README such as aligncenter, application, build, web ...
    - There is a positive relationship between characer count vs. word count
    - By average, JavaScript has the longest character count across all languages, followed by TypeScript
***
Modeling:
* Baseline Model:
    * 
* Models created on cleaned, stemmed and lemmatized data:
    - Decision tree 
    - Logistic regression 
    - Random forest
* Best Model:

* Model testing:
    * Train Dataset

    * Validate Dataset (unseen)
    * 
* Performance:
    * Test Dataset (unseen)


Project Replication
* Download the acquire.py, prepare.py, explore.py, and model.py modules to your working directory.
* Run the final_report.ipynb Juypter Notebook.

***
Recommendations: 
* 
* 
* 


Next Steps: 
* 
* 
* 