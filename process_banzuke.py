"""
modules for cleaning and processing banzukes and hoshitori
"""

import pandas as pd
import itertools

def numerical_rank(df_rank):
    """
    take rank and extract numerical rank
    """
    
    df_num = df_rank.str.extract(r'(\d+)').astype('float')
    
    return df_num

def get_tier(rank_raw):
    """
    get tier rank by taking the first characters of the rank columns
    """
    
    tier = "".join(itertools.takewhile(str.isalpha, rank_raw))
    
    return tier

def tier_rank(df_rank):
    """
    return ordinal ranks for Y, O, S, K, M, J
    """
    
    df_tier = df_rank.apply(get_tier)
    mapper = {
        'Y': 1,
        'O': 2,
        'S': 3,
        'K': 4,
        'M': 5,
        'J': 6,
        'Ms': 7,
        'Sd': 8,
        'Jd': 9,
        'Jk': 10
    }
    
    df_tier = df_tier.replace(mapper)
    
    return df_tier

def east_west(df_rank):
    """
    turn east west into binary
    """
    
    df_is_east = df_rank.str.contains('e')
    
    return df_is_east

def extract_ranks(df):
    """
    expand rank into 3 categories
    is east
    numerical rank
    tier
    """
    
    df['tier_rank'] = tier_rank(df['rank'])
    df['num_rank'] = numerical_rank(df['rank'])
    df['is_east'] = east_west(df['rank'])
    
    return df

def abs_rank(df, cols = ['year', 'month', 'tier_rank', 'num_rank', 'is_east']):
    """
    order and rank results to get absoulte rank
    """
    
    cols = cols
    rf = df.sort_values(by = cols, ascending = [True, True, True, True, False],ignore_index = True)
    rf['order'] = rf.index
    rf['abs_rank'] = rf.groupby(['year','month'])['order'].rank()
    
    return rf