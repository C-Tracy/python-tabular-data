#! /usr/bin/env python3

import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt
import scipy
from scipy import stats

def regression_plots(dataframe, *argv):

    for arg in argv:
        species_dataframe = dataframe[dataframe.species == "Iris_{}".format(arg)]


#Plotting with matplotlib
#dataframe = pd.read_csv("iris.csv")
plt.scatter(dataframe.petal_length_cm, dataframe.sepal_length_cm)
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.savefig("petal_v_sepal_length.png")


#Basic Stats with scipy
x = dataframe.petal_length_cm
y = dataframe.sepal_length_cm
regression = stats.linregress(x, y)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x, y, label = 'Data')
plt.plot(x, slope * x + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("petal_v_sepal_length_regress.png")





dataframe = pd.read_csv("iris.csv")


if name
