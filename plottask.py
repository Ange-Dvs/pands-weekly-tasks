# plottask.py
# This program plots with: 
#   1. A histogram of a normal distribution with a mean of 5 and standard deviation of 2
#   2. A plot of the function h(x)=x^3 in the range 0 to 10
#   3. Both the historgram and line plot should be shown in the same set of axes
# Author: Angela Davis

import numpy as np
import matplotlib.pyplot as plt

# setting the values to be used in the histogram as varaibles which will be called later 
mean_of_dist = 5
stand_deviation = 2
size = 1000

'''np.random.seed(1)''' # seed used during testing & troubleshooting

#"np.random.normal" is used create a random array of figures using the variables set above, .normal ensures the results of random numbers generated are of normal distribution.
norm_dist = np.random.normal(mean_of_dist, stand_deviation, size)

# The array of random numbers generated above is then plotted to a histogram
# The colour is specified "xkcd:" before the colour name results in a different shade of the colour being show in the plot
# A label is defined for the legend of the plot 
plt.hist(norm_dist, color = "xkcd:lavender", label="normal distribution") 

# now the program will move onto the second requirement for a line to be plotted of the results for h(x)=x^3
x_cubed = np.array(range(0, 10)) # an array is generated with a range of 0 to 10
h_x = x_cubed * x_cubed * x_cubed # h(x) is then calculated by multiplying each entry by itself twice

plt.plot( x_cubed, h_x, color = "xkcd:indigo", label ="h(x) = x^3")

# A title is added to the plot, the font specified as bold, font size 14 and the colour changed to indigo
plt.title("plottask.py results", fontweight = "bold", fontsize = 14, color = "xkcd:indigo")

plt.legend() # legend is generated, it uses the labels defined for the .hist and .plot results

'''plt.savefig("plottask_results.png")''' # image is saved automatically used to generate png file to upload along side the code as requested 

plt.show() # the results of both the histogram and the h(x) = x^3 calculation are shown in the plot

