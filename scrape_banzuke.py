"""
modules to scrape banzuke 
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

banzuke_text_url = 'http://sumodb.sumogames.de/Banzuke_text.aspx?b={}{}'

def retrieve_rows(soup, start_rank = 'Makuuchi', end_rank = 'Juryo'):
    """
    takes banzuke soup object and grabs rows data from makuuchi and juryo
    returns as dataframe
    """
    
    if len(soup.find_all('pre')) == 0:
        return 'None'
    
    l = str(soup.find_all('pre')[0]).split('\n')
    
    start_idx = l.index(start_rank) + 2
    end_idx = l.index(end_rank) -1
    
    to_df = l[start_idx:end_idx]
    to_df = [y.split() for y in to_df]
    
    cols = ['rank', 'name', 'pob', 'stable', 'birthdate', 'height', 'weight']
    
    df = pd.DataFrame(to_df, columns = cols)
    
    return df

def combine_divisions(div1, div2):
    """
    join data frames from two different divisions
    """
    
    jf = pd.concat([div1, div2])
    
    return jf

def scrape_year(year):
    """
    scrape an entire years worth of data for makuuchi and juryo banzukes
    """

    months = [str(x).zfill(2) for x in list(range(1,13,1))] # banzukes only occur every 3 months (starting in january)
    
    
    urls = [banzuke_text_url.format(year, x) for x in months ]
    
    banzuke = []
    
    for r in urls:
        res = requests.get(r)
        soup = BeautifulSoup(res.content, features="html5lib")
        mak = retrieve_rows(soup, start_rank = 'Makuuchi', end_rank = 'Juryo')
        if type(mak) == type(str()):
            continue
        jur = retrieve_rows(soup, start_rank = 'Juryo', end_rank = 'Makushita')
        
        print(r)
        df = combine_divisions(mak, jur)
        df['year'] = year
        df['month'] = r[-2::1]
        banzuke.append(df)
    
    banzuke = pd.concat(banzuke, ignore_index=True)
    
    return df

def scrape_month(year, month):
    """
    get banzuke results for just one month / year
    """
    
    return df