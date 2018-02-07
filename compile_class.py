import glob
import csv
import numpy as np
import pandas as pd
import string
import os
import shutil

def main():
    collect_csv_files()
    cat_data()
    camel_case()
    check_for_spaces()
    write_data()

def collect_csv_files():
    names_netids = glob.glob('*.csv')
    names_netids.remove('mlp6.csv')
    names_netids.remove('everyone.csv')
    return names_netids


def cat_data():
    names_netids = glob.glob('*.csv')
    names_netids.remove('mlp6.csv')
    names_netids.remove('everyone.csv')
    combined_files = pd.DataFrame(dtype='str')
    for files in names_netids:
        read_files = pd.read_csv(files, delimiter=',', index_col=False, names=[1, 2, 3, 4, 5])
        combined_files = pd.concat([combined_files, read_files])
    combined_files.to_csv('everyone.csv')
    return combined_files

def check_for_spaces():
    names_netids = glob.glob('*.csv')
    names_netids.remove('mlp6.csv')
    names_netids.remove('everyone.csv')
    combined_files = pd.DataFrame(dtype='str')
    for files in names_netids:
        read_files = pd.read_csv(files, delimiter=',', index_col=False, names=[1, 2, 3, 4, 5])
        combined_files = pd.concat([combined_files, read_files])
    combined_files.to_csv('everyone.csv')
    j = 0
    column_five = combined_files[5]
    for files5 in column_five:
        if ' ' in files5 == True:
            j=j+1
        else:
            j=j+0
    print(j, 'teams have spaces')

def camel_case():
    names_netids = glob.glob('*.csv')
    names_netids.remove('mlp6.csv')
    names_netids.remove('everyone.csv')
    combined_files = pd.DataFrame(dtype='str')
    for files in names_netids:
        read_files = pd.read_csv(files, delimiter=',', index_col=False, names=[1, 2, 3, 4, 5])
        combined_files = pd.concat([combined_files, read_files])
    combined_files.to_csv('everyone.csv')
    i = 0
    column_five = combined_files[5]
    for files2 in column_five:
        if files2.islower() == False and files2.isupper() == False:
            i = i+1
        else:
            i = i+0
    print(i, 'teams use camelcase')
    return i


def write_data():
    names_netids = glob.glob('*.csv')
    rename_to_json = glob.glob('/Users/deeptigopinath/bme590s18_lecture03/json_files/*.csv')
    names_netids.remove('mlp6.csv')
    names_netids.remove('everyone.csv')
    for files3 in names_netids:
        shutil.copy(files3, '/Users/deeptigopinath/bme590s18_lecture03/json_files')
    for files4 in rename_to_json:
        os.rename(files4, files4.replace('.csv', '.json'))


if __name__ == "__main__":
    main()
