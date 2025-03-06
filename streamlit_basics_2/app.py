import streamlit as st
import pandas as pd

#importing matplotlib and seaborn

import matplotlib.pyplot as plt
import seaborn as sns

st.header("Dataframes and Tables")
df = pd.read_csv("dataframes/auto.csv")
st.dataframe(df.head(5))

# View as table
st.table(df.head(10))

# Plottings

st.area_chart(df[['mpg', 'cylinders']])
st.bar_chart(df[['mpg', 'cylinders']].head(20))
st.line_chart(df[['mpg', 'cylinders']].head(20))


# Matplotlib and Seaborn
fig,ax= plt.subplots()
corr_plot = sns.heatmap(df[['mpg', 'cylinders', 'displacement']].corr(), annot=True)
st.pyplot(fig)

# Date and Time

st.header("Date and Time")
import datetime

today = st.date_input("Today is:", datetime.datetime.now())

import time

time = st.time_input("The time is:", datetime.time(12,30))

# Display JSON code

data = {"name": "Krishna", "place": "Vrindavan"}
st.json(data)


#Display text as code
st.code("import pandas as pd")

# Progress bar

import time
my_bar = st.progress(0)
for value in range(100):
    time.sleep(0.1)
    my_bar.progress(value+1)


#Spinner

import time
with st.spinner("Please wait..."):
    time.sleep(10)
st.success("Done!")
