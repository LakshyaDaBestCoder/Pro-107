import csv
import pandas as pd
import plotly_express as px

fileData=pd.read_csv("data.csv")
mean=fileData.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
print(mean)

fig=px.bar(mean,x="student_id", y="level", size="attempt", color="attempt")
fig.show()