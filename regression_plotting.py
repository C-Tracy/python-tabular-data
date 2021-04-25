#! /usr/bin/env python3

import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt
import sys
import scipy
from scipy import stats

print('Outside the first function')


def plot_all(data, *argv):
    '''
    Read in a specific dataframe and make both general and regression plots for the designated species.

    Parameters
    ----------
    data: str 
        A string with the name of the dataframe to be used for regression/plotting.

    species: str
        Any number of species names to create plots for individually, formatted as Iris_setosa.
    '''

    plot_data(data, *argv)
    
    regression_plots(data, *argv)




def plot_data(data, *argv):
    '''
    Read in a specific dataframe and make general plots for the designated species.

    Parameters
    ----------
    data: str 
        A string with the name of the dataframe to be used for regression/plotting.

    species: str
        Any number of species names to create plots for individually, formatted as Iris_setosa.
    '''
    dataframe = pd.read_csv(data)

    test =  "{} is the data frame"


    print('Inside the function...')

    #print (test.format(data))

    for arg in argv:

        print('inside the loop')
        species_dataframe = dataframe[dataframe.species == (arg)]
        

        #Plotting with matplotlib
        #dataframe = pd.read_csv("iris.csv")
        plt.scatter(species_dataframe.petal_length_cm, species_dataframe.sepal_length_cm)
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.savefig("{}_petal_v_sepal_length.png".format(arg))
        plt.clf()
        

def regression_plots(data, *argv):
    '''
    Read in a specific dataframe and make individual regression plots for the designated species.

    Parameters
    ----------
    data: str 
        A string with the name of the dataframe to be used for regression/plotting.

    species: str
        Any number of species names to create plots for individually, formatted as Iris_setosa.

    '''
    dataframe = pd.read_csv(data)

    test =  "{} is the data frame"


    print('Inside the function...')

    #print (test.format(data))

    for arg in argv:

        print('inside the loop')
        species_dataframe = dataframe[dataframe.species == (arg)]
        #Basic Stats with scipy
        x = species_dataframe.petal_length_cm
        y = species_dataframe.sepal_length_cm
        regression = stats.linregress(x, y)
        slope = regression.slope
        intercept = regression.intercept
        plt.scatter(x, y, label = 'Data')
        plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
        plt.xlabel("Petal length (cm)")
        plt.ylabel("Sepal length (cm)")
        plt.legend()
        plt.savefig("{}_petal_v_sepal_length_regress.png".format(arg))

        plt.clf()

if __name__ == '__main__':
    plot_all(*sys.argv)

