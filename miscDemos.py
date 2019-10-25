# Throwing together lots of crap from streamlit demos

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define read_and_cache_csv, which kinda is like a function
read_and_cache_csv = st.cache(pd.read_csv)

st.title('My second app')


# Just messing around here, writing a dataframe
st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [9, 21, 29, 41]
})

st.write(df)


# Read in a (hard-coded) data file.
st.write("Now for my own data.")
myData = read_and_cache_csv("data/test.csv")

cpData = myData.copy()
cpData['Col2noisy'] = cpData['Col2'] + np.random.normal(size=5)
st.write(cpData)

# Make a chart
st.write("Here's a plot")
# myPlot = myData.plot.scatter(x='Col1', y='Col2')
plt.scatter(cpData.Col1, cpData.Col2)
plt.scatter(cpData.Col1, cpData.Col2noisy)
st.pyplot()
# st.line_chart(myData)

# Button to create new noisy data
st.button("Re-randomize", key="rerunButton")
