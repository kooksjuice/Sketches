#
# Anna Novikova
#
#
# Visualizations using pandas. Part of Yelp Data Challenge



import pandas as pd
df = pd.read_csv('biz10.csv')


def dataviz1():
    """function plots a histogram of Number of Reviews for each Stars Score"""
    ax = df.hist('stars', grid = False)
    ax[0][0].set_ylabel('Number of Reviews')
    ax[0][0].set_xlabel('Stars Score')
    ax[0][0].set_title('Yelp Star Rating Distribution',fontsize=14, fontweight='bold')
    
    
def dataviz2():
    """Function plots a histogram of number of businesses in each city in the Yelp Data Set"""
    g = df.groupby(['city']).count()['business_id'].nlargest(13)
    ax = g.plot(kind='bar')
    ax.set_ylabel('Number of Businesses')
    ax.set_xlabel('City')
    ax.set_title('Top 13 Cities by Number of Businesses',fontsize=14, fontweight='bold')

