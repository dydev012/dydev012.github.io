import re

def clean_mathjax(content):
    # Regular expression to remove MathJax delimiters and content
    mathjax_pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)
    cleaned_content = re.sub(mathjax_pattern, '', content)
    return cleaned_content

def extract_first_p_tag_content(content):
    # Regex pattern to match everything between the first pair of <p> tags
    pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)
    # Finding the first match
    match = re.search(pattern, content)
    if match:
        return match.group(1)  # Return the content inside the first <p> tags
    else:
        return ""  # Return empty string if no match is found

def capitalize(content):
    # print(content)
    print(type(content))
    return content.upper()