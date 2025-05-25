import pandas as pd

import requests


def extract(url):
    """Extracting of the data from the url."""
    response = requests.get(url)
    res_data = response.json()
    transform(res_data)

def transform(res_data):
    """Transformation of data."""
    data_df = pd.DataFrame(res_data)
    transformed_data_df = data_df.groupby(['userId', 'completed']).size().reset_index(name='count')
    load(transformed_data_df)

def load(transformed_data_df):
    """Converts the data frame into a csv file."""
    transformed_data_df.to_csv('data/final.csv')

if __name__ == '__main__':
    URL='https://jsonplaceholder.typicode.com/todos/'
    extract(URL)


# basic python script
#     extract - Extraction of data from files/api's/scraping/any kind of servers or databases.
#     Transform - Transformation depends on the business needs.
#     Load - Loading of data after we transform the data into a meaningful form.

# 1. Download python from the official website.
# 2. Best pactises to write the code in python like wrt naming convention or about the folder structuring or any other.
# 3. We will start with the project, where we will perform ETL operations.

