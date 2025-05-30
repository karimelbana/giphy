import streamlit as st
import numpy as np
import pandas as pd
import requests

st.markdown("""# This is not a fancy header
## This is a sub header for the 2012 *Barcelona* batch ❤️
This is the **BOLDDDDD** text [git](http://github.com/streamlit)
- item 1
- item 2
- item 3
- item 4""")

st.write('this is for BEN')


df = pd.DataFrame({
'first column': list(range(1, 11)),
'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 10)

# and used to select the displayed lines
head_df = df.head(line_count)
st.write(head_df)

url = "https://api.giphy.com/v1/gifs/search"
query = st.text_input("Search a GIF")
params = {"api_key": st.secrets["api_key"], "q": query, "Limit": 10}
response = requests.get(url=url, params=params).json()
#st.write(response)
gif_url = response["data"][np.random.randint(0, 5) ]["embed_url"]
st.write(gif_url)
st.markdown(f'<iframe src="{gif_url}" width="480" height="240">', unsafe_allow_html=True)
st.image(gif_url, width=480)
