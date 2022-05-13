import matplotlib.pyplot as plt

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


