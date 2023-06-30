import os

def title():
    with open('prompt.md', 'r') as file:
        content = file.read()
        start = content.find('**Title**: ') + len('**Title**: ')
        end = content.find('\n', start)
        title = content[start:end]
    print(title)
    #instead of creating folder just parse the title 
    return title

title = title()
def generate_folder(title):
    os.makedirs(title, exist_ok=True)

generate_folder(title)
    
    
   
    
#title()