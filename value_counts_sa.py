import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file_path", type=str, help="path to CSV/Excel file")
parser.add_argument("--output_folder", type=str, help="path to output folder")
args = parser.parse_args()

file_path = args.file_path
output_folder = args.output_folder

def fetch_file(df):
    
    if df.endswith('csv'):
        df = pd.read_csv(df)
        
    elif df.endswith('xlsx'):
        df = pd.read_excel(df)
         
    return df

def value_counts():

    dataframe = fetch_file(file_path)
    
    for col in dataframe.columns:
        
        index = dataframe[col].value_counts().index.to_list()
        values = dataframe[col].value_counts().to_list()
        null_values =  dataframe[f'{col}'].isnull().sum()
        final_df = pd.DataFrame()
        final_df[f'{col}'] = index
        final_df['Values'] = values
        
        null_dict = {f'{col}': 'Null values', 'Values': null_values}
        final_df = final_df.append(null_dict, ignore_index = True)
        
        output_file_name = f'{col}.csv'
        
        final_df.to_csv(os.path.join(output_folder, output_file_name), index=False)

if os.path.exists(output_folder) == False:
    os.makedirs(output_folder)
else:
    pass

value_counts()