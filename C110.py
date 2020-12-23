import statistics
import random
import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

population_mean = statistics.mean(data)
print("Mean Of The Whole Thing: "+str(population_mean))

standard_deviation = statistics.stdev(data)
print("Standard Deviation Of The Whole Thing: "+str(standard_deviation))

def RandomSetOfMeans(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data))
        value=data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    standard_deviation_set_100 = statistics.stdev(dataset)

    return mean
    

def showFigure(meanlist):
    df=meanlist
    fig=ff.create_distplot([df], ["Temperature"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0, 100):
        setOfMeans=RandomSetOfMeans(30)
        meanList.append(setOfMeans)
    showFigure(meanList)

setup()
