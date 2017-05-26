# -*- coding: utf-8 -*-
"""
Created on Sun May 21 04:15:40 2017

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt 


def f(x):
    return x**2 


def draw_bars(a, b, number_of_bars):
    '''need to define your own function'''
    intervals = (b-a)/number_of_bars
    x = intervals
    bar_height = []
    left = [a]
    new_interval = a
    while x <= b:
        bar_height.append(f(x))
        x = x + intervals 
    while True:
        new_interval += intervals
        if new_interval == b:
            break
        left.append(new_interval)
    return bar_height, left, intervals


fig = plt.figure()


#plot the function, f(x)
p = np.poly1d([1,0,0])
x = np.arange(5)
y = p(x)
plt.plot(x,y)


#left is the starting value of x, intervals are the width. 
#note this script runs out of memory real quick (can't get more than 4 bars)
left = draw_bars(0,2,4)[1]
bar_height = draw_bars(0,2,4)[0]
interval = draw_bars(0,2,4)[2]


#plot the bar graph
plt.bar(left,bar_height,interval, color = 'yellow', align = 'edge', edgecolor = 'black')
plt.title('Approximating area under curves')
plt.ylabel('y')
plt.xlabel('x')

plt.show()
















    
    
                
               
    