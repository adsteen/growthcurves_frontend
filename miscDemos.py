# Throwing together lots of crap from streamlit demos

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import copy as cp  # Wild that you need a package to copy objects

# Define read_and_cache_csv, which kinda is like a function
read_and_cache_csv = st.cache(pd.read_csv)

st.title('My second app')

st.write("Here's our first attempt at using data to create a table:")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [9, 21, 29, 41]
})

newDf = cp.copy(df)
st.write(newDf)

st.write("Now for my own data. Please ignore the following big yellow box, which contains incorrect information.")
myData = read_and_cache_csv("data/test.csv")
myData['Col2noisy'] = myData['Col2'] + np.random.normal(size=5)
st.write(myData)

# Make a chart
st.write("Here's a plot")
# myPlot = myData.plot.scatter(x='Col1', y='Col2')
plt.scatter(myData.Col1, myData.Col2)
plt.scatter(myData.Col1, myData.Col2noisy)
st.pyplot()
# st.line_chart(myData)

# Button to redo the noisy data
st.button("Re-randomize", key="rerunButton")
