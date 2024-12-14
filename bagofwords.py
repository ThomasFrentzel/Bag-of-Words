import re
import pandas
import requests
from bs4 import BeautifulSoup

words = []  
unique_words = []  
vector = []  

# URLs to scrape
urls = ['https://www.ibm.com/cloud/learn/natural-language-processing', 
        'https://en.wikipedia.org/wiki/Natural_language_processing', 
        'https://monkeylearn.com/natural-language-processing/',
        'https://www.cio.com/article/228501/natural-language-processing-nlp-explained.html',
        'https://magnimindacademy.com/blog/how-do-natural-language-processing-systems-work/']

for site in urls:
    url = requests.get(site).content  
    soup = BeautifulSoup(url, "html.parser")
    for data in soup(['style', 'script']):  
        data.decompose()  
    text = ' '.join(soup.stripped_strings)
    text = re.sub(r"[\n\t]", "", text)  
    separators = re.split("[!?.;:,]", text)  
    words.append(" ".join(separators))

def unique(p):  
    no_duplicates = set()
    for array in p:
        for word in array.split():
            no_duplicates.add(word)
    return no_duplicates

unique_words = unique(words)  
unique_words = list(unique_words)  
print(len(unique_words))  

def BOW(wordArray, text):  
    array = [0] * len(wordArray)
    for string in text.split():
        array[wordArray.index(string)] += 1
    return array

for array in words:
    vector.append(BOW(unique_words, array))  

df = pandas.DataFrame(vector, columns=unique_words)  
display(df)
