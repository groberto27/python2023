#import all required packages
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.linear_model import LogisticRegression


header=st.container()
features=st.container()
st.image('li.jpg',caption="Image Source: LinkedIn",width=600)

st.markdown(
    """
    <style>
    .main{
    background-color:#DEB887;
    }
    </style>
    """,
    unsafe_allow_html=True
)

with header:
    st.markdown(
        """
        <h1 align="center">
        Do you use LinkedIn?
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h2 align="center">
        Let's predict if you're a user or not!
        </h2>
        """,
        unsafe_allow_html=True
    )
 

def get_data():
    ss=pd.read_csv("ss.csv")
    ss = ss.dropna()
    return ss
    
#from dataframe ss: y as sm_li; x as income, education, parent, marital, gender, age
ss= get_data()

y = ss["sm_li"]
X = ss[["income", "education", "parent", "marital","gender","age"]]
lr= LogisticRegression()
lr.fit(X,y)
y_pred = lr.predict(X)

# Income
income = st.selectbox("What is your current income level?", 
             options = ["Less than $10,000",
                       "$10,000 - $20,000",
                        "$20,000 - $30,000",
                        "$30,000 - $40,000",
                        "$40,000 - $50,000",
                        "$50,000 - $75,000",
                        "$75,000 - $100,000",
                        "$100,000 - $150,000",
                        "Over $150,000"])
if income == "Less than $10,000":
    income = 1
elif income == "10 to under $20,000":
    income = 2
elif income == "20 to under $30,000":
    income = 3
elif income == "30 to under $40,000":
    income = 4   
elif income == "40 to under $50,000":
    income = 5  
elif income == "50 to under $75,000":
    income = 6
elif income == "75 to under $100,000":
    income = 7
elif income == "100 to under $150,000":
    income = 8    
else:
    income  = 9 


# Education
education = st.selectbox("What is the highest level of education/ degree? ", 
             options = ["Less than high school",
                       "Some high high school",
                        "High school graduate/ GED",
                        "Some college",
                        "Two-year college/ Associates",
                        "Four-year college/ Bachelors",
                        "Some post-graduate or professional schooling",
                        "Graduate or professional degree (MA, MS, Phd, MD, JD, others"])
if education == "Less than high school":
    education = 1
elif education == "Some high high school":
    education = 2
elif education == "High school graduate/ GED":
    education = 3
elif education == "Some college":
    education = 4
elif education == "Two-year college/ Associates":
    education = 5
elif education == "Four-year college/ Bachelors":
    education = 6
elif education == "Some post-graduate or professional schooling":
    education = 7
else:
    education = 8

# Marital
marital = st.selectbox("Marital status?", 
             options = ["Married",
                       "Living with a partner",
                        "Divorced",
                        "Some college",
                        "Separated",
                        "Widowed",
                        "Never been married/ Single"])
if marital == "Married":
    marital = 1
elif marital == "Living with a partner":
   marital = 2
elif marital == "Divorced":
   marital = 3
elif marital == "Separated":
    mar_label =4
elif marital == "Widowed":
    marital = 5
else:
    marital = 6


#Parent
parent = st.radio(label="Do you have children?", 
                  options=["No", "Yes"])
if parent == "No":
    parent = 0
else:
    parent = 1
           


#Gender
gender = st.radio(label="Gender", 
                  options=["Male", "Female"])
if gender == "Male":
    parent = 0
else:
    parent = 1

         
#Age
age = st.number_input(label="What is your age?", 
           min_value=18,
           max_value=98,
           value=45,placeholder="type a number...")

input_data = st.text.input ({income}, {education},{parent}, {marital},{gender},{age})
#Making predictions 
if st.button ('Make Prediction'):
    input_array = np.array(float(input_data)).reshape(1,-1)
    prediction=lr.predict(input_array)[0]
st.write(f'Prediction:{prediction}')

