import re
import pandas as pd
import streamlit as st
from datetime import datetime

def response_to_markdown(response):
    markdown_string = ""
    for data in response:
        markdown_string += data.text
    
    return markdown_string

def markdown_to_df(markdown):
    try:
        pattern = r"\|([^\n\|]+)\|([^\n\|]+)\|"
        matched_data = re.findall(pattern, markdown)
        header = matched_data[0]
        data = matched_data[1:]
        df = pd.DataFrame(data, columns=header)
        df = df[~df.iloc[:, 1].str.contains('Input|---')]
    except IndexError:
        print("Markdown to dataframe failed, possible regex match issue. Please retry")
    return df

@st.cache_data
def export_to_csv(dataframe: pd.DataFrame):
    return dataframe.to_csv()
    
def export_file_name(text):
    current_time = datetime.today().strftime("%d-%m/-Y_%H%M%S")
    return text + str(current_time) + ".csv"
    