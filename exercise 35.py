# This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.

# In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.

# In this exercise, use the bokeh Python library to plot a histogram of which months the scientists 
# have birthdays in! Because it would take a long time for you to input the months of various scientists, 
# you can use my scientist birthday JSON file. Just parse out the months (if you don’t know how, I suggest 
# looking at the previous exercise or its solution) and draw your histogram.











import json

with open("/home/stefan/Desktop/exercises/scientist_birthdays.json", "r") as f:
    data = json.load(f)

from bokeh.plotting import figure, show, output_file
output_file("plot.html")

x = [key for key in data.keys()]
y = [val for val in data.values()]

p = figure(x_range=x)
p.vbar(x=x, top=[int(el.split('/')[2]) for el in y], width=0.5, bottom=0, color="firebrick")
show(p)
