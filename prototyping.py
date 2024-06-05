from utils import common_utils as cu
from prompter import generate

response = generate(50, "minimum of seven characters long, including at least one letter and one number or special character (excluding semi-colons and question marks when used alone at the end)")

markdown = cu.response_to_markdown(response)

print(markdown)

df = cu.markdown_to_df(markdown)

print(df)
