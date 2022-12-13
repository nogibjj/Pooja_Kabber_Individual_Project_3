import psycopg2
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import fill_between
import os

host = os.environ.get('RDS_HOSTNAME')
user = os.environ.get('RDS_USER')
password = os.environ.get('RDS_PASSWORD')
database = os.environ.get('RDS_DATABASE')

#Stylistic Options
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]  

for i in range(len(tableau20)):    
    r, g, b = tableau20[i]    
    tableau20[i] = (r / 255., g / 255., b / 255.)

def connect_to_db():

    connection = psycopg2.connect(
        host=host, port=5432, user=user, password=password, database="titanic"
    )
    cursor = connection.cursor()

    return cursor

def main():

    years = list()
    values = list()

    cursor = connect_to_db()
    cursor.execute(
   """SELECT * FROM import.indicators where countryname='India' and indicatorcode='EG.ELC.ACCS.RU.ZS';"""
    )
    for i in cursor.fetchall():
        years.append(i[-2])
        values.append(i[-1])

    df_rural = pd.DataFrame({"Year":years, "Value":values})
    df_rural = df_rural.astype({"Year":int, "Value":float})
    df_rural = df_rural.sort_values(by=['Year'])
    print(df_rural)

    fig = plt.figure()
    plt.plot(df_rural.Year,df_rural.Value,'o-',label='Rural',color=tableau20[0])
    fig.savefig('access_electricity.pdf',format='pdf', dpi=300)

if __name__ == '__main__':
    main()