import streamlit as st
import pandas as pd


## title
st.title("Streamlit Text Input")
name = st.text_input("Enter your Name")

## if name is given to input box then print message
if name:
    st.write(f"Hello {name}!") 

## age
st.write("What is your age")
age = st.slider("select your age :", 0, 100, 25)  ##(0: minimum age, 100:maximum age, 25:set default age)
st.write("your age is : ",age)


## create a choice box
options=['python', 'Java', 'C++', 'JavaScript']
choice=st.selectbox("Choose your favorite language:",options)
st.write(f"you selected : {choice}")


## create a dataframe
data = ({
    'Name': ['ram', 'shyam', 'geeta', 'sita'],
    'age':[22,33,21,24]
})
df = pd.DataFrame(data)
## save it to csv file
df.to_csv("nameAgeData.csv")
st.write("a simple Name age table is :")
st.write(df)


## upload a new csv file from user
uploaded_file = st.file_uploader("choose a CSV file", type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("you have uploaded this data")
    st.write(df)