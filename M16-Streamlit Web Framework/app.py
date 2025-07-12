import streamlit as st
import numpy as np
import pandas as pd

### Title og the application
st.title("Hello Steamlit")

## Display a simple text
st.write("This is a simple text")


st.write("create a simple data frame")
df = pd.DataFrame({
    'first column':[1,2,3,4,5],
    'second column':[10,20,30,40,50]
})
## Display the data frmae
st.write('here is the data frame')
st.write(df)

## create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), ## 20 rows and 3 columns
    columns=['a','b','c']
)
st.write('table for line chart')
st.write(chart_data)
st.write('here the line chart of above data table')
st.line_chart(chart_data)