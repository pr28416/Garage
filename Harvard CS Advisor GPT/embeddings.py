from webscraper import crawl
import pandas as pd
import os
import tiktoken

full_url = "https://csadvising.seas.harvard.edu/"
domain = "csadvising.seas.harvard.edu"

# crawl(full_url)

# Create a list to store the text files
texts = []
for file in os.listdir(f'text/{domain}/'):
    # Open file and read text
    with open(f'text/{domain}/{file}', 'r', encoding='UTF-8') as f:
        text = f.read()
        # print(text)
        # Omit the first 11 lines and the last 4 lines, then replace -, _, and #update with spaces
        texts.append((file[11:-4].replace('-', ' ').replace('_', ' ').replace('#update', ' '), text))

# print(texts)

# Create a dataframe from the list of texts
pd.options.display.max_colwidth = 10000000000000000
df = pd.DataFrame(texts, columns=['fname', 'text'])
# print(texts)
print(df.head(1000000))

# Set the text column to be the raw text with the newlines removed
def remove_newlines(serie):
    serie = serie.str.replace('\n', ' ')
    serie = serie.str.replace('\\n', ' ', regex=True)
    serie = serie.str.replace('  ', ' ')
    serie = serie.str.replace('  ', ' ')
    return serie

df['text'] = f'{df.fname}. {remove_newlines(df.text)}'
df.to_csv('processed/scraped.csv')
# df.head()

# Load the cl100k_base tokenizer, which is designed to work with the ada-002 model
tokenizer = tiktoken.get_encoding('cl100k_base')

df = pd.read_csv('processed/scraped.csv', index_col=0)
df.columns = ['title', 'text']

# Tokenize the text and save the number of tokens to a new column
df['n_tokens'] = df.text.apply(lambda x: len(tokenizer.encode(x)))

# print(df.n_tokens.hist())