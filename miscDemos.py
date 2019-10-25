# Throwing together lots of crap from streamlit demos

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define read_and_cache_csv, which kinda is like a function
read_and_cache_csv = st.cache(pd.read_csv)


st.title('Simple file plotting app')


# Crude file picker, from https://discuss.streamlit.io/t/upload-files-to-streamlit-app/80/2
filename = st.text_input('Enter a path to a .csv file on your machine:', value="data/test.csv")

# try:
#     with open(filename) as input:
#         df = input.read()
#         # st.text(input.read())
# except FileNotFoundError:
#     st.error('File not found.')

st.text("This is your data, hopefully")
myData = read_and_cache_csv("data/test.csv")

cpData = myData.copy()
dataLen = cpData.shape[0]
cpData['Col2noisy'] = cpData.iloc[:, 1] + np.random.normal(size=dataLen)
st.write(cpData)

# Make a chart
st.write("Here's a plot of your data, plus your data with random noise")
# myPlot = myData.plot.scatter(x='Col1', y='Col2')
plt.scatter(cpData.Col1, cpData.Col2)
plt.scatter(cpData.Col1, cpData.Col2noisy)
st.pyplot()
# st.line_chart(myData)

# Button to create new noisy data
st.button("Re-randomize", key="rerunButton")
