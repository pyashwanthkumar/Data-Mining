import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def plotHisto(df):
	fig = plt.figure(figsize=(20,15))  #Creating a new figure with the mentioned figure size
	cols = 4         # No of columns to display the charts
	rows = 4         # No of rows to display the charts. These numbers are chosen as we have 16 attributes
	# Alternatively, *rows = math.ceil(float(df.shape[1]) / cols)* 
	# can be used when there are indefinete number of attributes.
	for i, column in enumerate(df.columns):
	    ax = fig.add_subplot(rows, cols, i+1)      #Adds a subplot in the i+1 th position
	    ax.set_title(column)
	    if df.dtypes[column] == np.object:         #For categorical attributes.
	        df[column].value_counts().plot(kind="bar", axes=ax)
	    else:
	    	df[column].hist(axes=ax)		#For conitnous attributes
	    	plt.xticks(rotation="vertical")

# plt.subplots_adjust(hspace=0.7, wspace=0.2)    # To adjust the plots and their labels

if __name__ == '__main__':
	df = pd.read_csv("wine.csv")
	plotHisto(df)
	print(df)
