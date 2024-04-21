def formatter(response):
    markdown_string = ""
    for data in response:
        markdown_string += data.text
    
    return markdown_string