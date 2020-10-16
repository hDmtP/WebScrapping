# Import BeautifulSoup
from bs4 import BeautifulSoup as bs
content = []
# Read the XML file
with open('sample.xml', 'r') as file:
    # Read each lines in the XML file through readlines()
    content = file.readlines()
    # Combine the lines into the list of strings
    content = "".join(content)
    bs_content = bs(content, 'lxml')

# result = bs_content.find('data')
# result = bs_content.find_all('data')
# result = bs_content.find('child', {"name": "Jack"})
second_child = bs_content.find('child', {"name": "Rose"})
# result = second_child.parent
# result = list(second_child.children)

# Similiarly next_siblings, previous_siblings => https://linuxhint.com/parse_xml_python_beautifulsoup/

# result = second_child.get('name')
result = second_child.prettify()
print(result)