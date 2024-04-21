import re
import pandas as pd

def response_to_markdown(response):
    markdown_string = ""
    for data in response:
        markdown_string += data.text
    
    return markdown_string

def markdown_to_df(markdown):
    pattern = r"\| ([\w\s]+) \| ([\w\s]+) \| ([\w\s]+) \|"
    matched_data = re.findall(pattern, markdown)
    header = matched_data[0]
    data = matched_data[1:]
    df = pd.DataFrame(data, columns=header)
    return df