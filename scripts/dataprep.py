import pandas as pd
import json

"""
Set of functions used to load and categorize dataset (train or test)
"""

def load_dataset(dset: str, fields: str, verbose=False):
    """Load one of the NSL-KDD datasets (train or test)

    Args:
    dset : a string in {KDDTrain+,KDDTest+}
    verbose : whether or not to print info about the dataset
    
    Returns:
    df: pandas dataframe
    """
    #Read files and name columns
    df = pd.read_csv(f'../../cyber-security-project/{dset}.csv', header=None)
    col_names = pd.read_csv(f'../../cyber-security-project/{fields}.csv', header=None)
    
    #Rename columns
    df.rename(columns=col_names[0], inplace=True)
    #Drop column 42 - unkown column 
    df.drop(columns=[42], axis=1, inplace=True)
    #Drop num_outbound - redundant data
    df.drop('num_outbound_cmds', axis=1, inplace=True)
    #Replace 2 to 0 
    df.su_attempted.replace(2, 0, inplace=True)

    if verbose:
        print(f"\n {f' Reading the dataset {dset} ':*^80}")
        print(f'\n It has {df.shape[0]} rows and {df.shape[1]} columns')
        print(f"\n {' It has the following columns ':*^80}")
        print(df.columns)
        print(f"\n {' First 5 Rows ':*^80}")
        print(df.head())
        
    return df

def mal_categorizer(df, filename='attack_dictionary'):
    """Malware categorizer loads dictionary file and categorizes the attack names
    
    Args:
    df = pandas dataframe
    filename = name of malware dictionary
    
    Returns:
    df = new pandas dataframe with labeled categories (labels_2cat & labels_5cat)
    """
    
    with open(f'./data/{filename}.json') as f_in:
            attack_dict = json.load(f_in)
            
    df['labels_5cat'] = df['attack_name'].map(attack_dict)
    df['labels_2cat'] = df.labels_5cat.apply(lambda label: 'normal' if label == 'normal' else 'malicious')
    
    return df