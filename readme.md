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

***
## Findings:

Data Wrangle:
* Web scraped random respository README files. 
* Filtered out….
* Remove….
* Normalized, tokenized, stemmed and lemmatized the content for NLP
* Split data into train, validate and test set
***
Explore:
* Question 1: What are the most common languages from the repos we explored?
* Question 2: What are the most common words across all READme's?
* Question 3: Does length of READme differ between languages
* Question 4: Are there any words that are found in all repos?
* Question 5: 
***
Modeling:
* Baseline Model:
    * 
* Models created on cleaned, stemmed and lemmatized data:
    * 
* Best Model:

* Model testing:
    * Train Dataset

    * Validate Dataset (unseen)
    * 
* Performance:
    * Test Dataset (unseen)
***
Data Dictionary: 


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