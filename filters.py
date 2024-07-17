import re
import pelican
import pelican.urlwrappers

def clean_mathjax(content):
    # Regular expression to remove MathJax delimiters and content
    mathjax_pattern = re.compile(r'(\$\$.*?\$\$|\$.*?\$)', re.DOTALL)
    cleaned_content = re.sub(mathjax_pattern, '', content)
    return cleaned_content

def clean_mathjax_markup(content):
    # Regex pattern to match everything between the first pair of <p> tags
    pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)
    # Finding the first match
    match = re.search(pattern, content)
    if match:
        return match.group(1)  # Return the content inside the first <p> tags
    else:
        return ""  # Return empty string if no match is found

def capitalize(content):
    return content.upper()

def name2slug(content: pelican.urlwrappers.Category | pelican.urlwrappers.Tag):
    print(content)
    content = content.name
    content = content.lower()
    content = content.replace(" ", "-")
    print(content)
    print()
    return content

def title2url(content):
    content = content.lower()
    content = content.replace(" ", "-")
    return content

def rm_html_suffix(content):
    if content[-5:] == ".html":
        return content[:-5]
    