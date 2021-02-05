"""
updated modules for getting data for predicting next months rankings
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

banzuke_text_url = 'http://sumodb.sumogames.de/Banzuke.aspx?b={}{}&heya=-1&shusshin=-1&snr=on&hl=on&c=on&simple=on'


# currently predicting on win, loss, absent, previous absolute rank, tier rank (yokozuna, ozeki (normalized)), ease west flag
x_cols = ['win', 'loss', 'absent', 'abs_rank', 'tier_rank', 'is_east']
y_cols = ['next_abs_rank']

def get_results(year, month):
    """
    get results for a given year and month
    """
    
    url = banzuke_text_url.format(year, month)
    print(url)
    
    res = requests.get(url)
    soup = BeautifulSoup(res.content, features="html5lib")
    
    df = pd.read_html(str(soup.find_all('table', class_ = 'banzuke')),  flavor = 'html5lib' )[0]
    df['year'] = year
    df['month'] = month
    
    return df

def get_year(year):
    """
    grab results for entire ear
    """
    
    months = [str(x).zfill(2) for x in list(range(1,13,2))] # banzukes only occur every 3 months (starting in january)
    
    banzuke = []
    
    for month in months:
        tf = get_results(year, month)
        if tf.columns.str.contains('Rank').any() == True:
            banzuke.append(tf)
        
    df = pd.concat(banzuke)
    
    return banzuke