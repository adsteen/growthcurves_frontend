# Intro python script to use streamlit to deal with modeling
# Currently copied from streamlit plotting example

import streamlit as st
import pandas as pd
import numpy as np

# Leftover; I'm not really sure what these do
progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()

# Title the app
st.title("Frontend for growth curves modeling software")

st.text("my butt")

# Janky file selector based on
# https://discuss.streamlit.io/t/upload-files-to-streamlit-app/80/2
filename = st.text_input('Enter a file path:', value="data/test.csv")

try:
    with open(filename) as input:
        # df = input.read()
		st.text(input.read())
    st.error('File not found.')

# st.text(input.read(filename))


# Plot the data frame I've imported
# myPlot=myData.plot.scatter(x='time', y='abundance')

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.001)

#progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
# st.button("Re-run")