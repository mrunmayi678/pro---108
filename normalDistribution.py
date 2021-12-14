import random
import plotly.figure_factory as ff
import csv
import pandas as pd


df = pd.read_csv("108/data.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand avg rating"])
fig.show()