import csv
import plotly.figure_factory as ff
import pandas as pd

df = pd.read_csv("project-c108.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["average rating"], show_hist=False)
fig.show()
