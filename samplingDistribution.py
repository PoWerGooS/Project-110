import pandas as pd
import csv
import statistics
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("newdata.csv")
data = df["average"].tolist()

fig = ff.create_distplot([data], ["average"], show_hist=False)
fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    df = mean_list    
    fig2 = ff.create_distplot([df], ["mean_list"], show_hist=False)
    fig2.show()
setup()    
    