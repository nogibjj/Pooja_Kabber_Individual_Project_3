import pandas as pd 
import matplotlib.pyplot as plt
from pylab import fill_between
import db_helper

#Stylistic Options
tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),    
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),    
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),    
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),    
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]  

for tab in range(len(tableau20)):    
    r, g, b = tableau20[tab]    
    tableau20[tab] = (r / 255., g / 255., b / 255.)

cursor = db_helper.connect_to_db()

def get_df(country, indicator):

    years = list()
    values = list()
    definitions = list()

    cursor.execute(
   """select i.year, i.value, s.longdefinition from import.indicators i
        left join import.series s
        on i.indicatorcode = s.seriescode
        where i.countryname = 'India' 
        and i.indicatorcode = 'EG.ELC.ACCS.ZS';"""
    )
    for i in cursor.fetchall():
        years.append(i[0])
        values.append(i[1])
        definitions.append(i[2])

    df_rural = pd.DataFrame({"Year":years, "Value":values, "Definition":definitions})
    df_rural = df_rural.astype({"Year":int, "Value":float, "Definition":str})
    df_rural = df_rural.sort_values(by=['Year'])
    
    return df_rural

def main():

    df_india_rural = get_df("India", "EG.ELC.ACCS.RU.ZS")
    df_india_urban = get_df("India", "EG.ELC.ACCS.UR.ZS")
    df_india_pop = get_df("India", "EG.ELC.ACCS.ZS")
    print(df_india_pop)
    
    # plt.plot(df_india_rural.Year,df_india_rural.Value,'o-',label='Rural',color=tableau20[0])
    # plt.plot(df_india_urban.Year,df_india_urban.Value,'o-',label='Urban',color=tableau20[1])
    # plt.plot(df_india_pop.Year,df_india_pop.Value,'o-',label='Population',color=tableau20[2])
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.xlabel('Years',  fontsize=14)
    # plt.ylabel('% of Population',  fontsize=14)
    # plt.title('Access to Electricity in India', fontsize=18)

    # df_south_asia = get_df("South Asia", "EG.ELC.ACCS.ZS")
    # df_afghanistan = get_df("Afghanistan", "EG.ELC.ACCS.ZS")
    # df_bangladesh = get_df("Bangladesh", "EG.ELC.ACCS.ZS")
    # df_bhutan = get_df("Bhutan", "EG.ELC.ACCS.ZS")
    # df_nepal = get_df("Nepal", "EG.ELC.ACCS.ZS")
    # df_pakistan = get_df("Pakistan", "EG.ELC.ACCS.ZS")
    # df_sri_lanka = get_df("Sri Lanka", "EG.ELC.ACCS.ZS")
    # df_maldives = get_df("Maldives", "EG.ELC.ACCS.ZS")

    # fig = plt.figure()
    # plt.plot(df_south_asia.Year,df_india_rural.Value,label='South Asia',color=tableau20[0])
    # plt.plot(df_afghanistan.Year,df_afghanistan.Value,label='Afghanistan',color=tableau20[1])
    # plt.plot(df_bangladesh.Year,df_bangladesh.Value,label='Bangladesh',color=tableau20[2])
    # plt.plot(df_bhutan.Year,df_bhutan.Value,label='Bhutan',color=tableau20[3])
    # plt.plot(df_nepal.Year,df_nepal.Value,label='Nepal',color=tableau20[4])
    # plt.plot(df_pakistan.Year,df_pakistan.Value,label='Pakistan',color=tableau20[5])
    # plt.plot(df_sri_lanka.Year,df_sri_lanka.Value,label='Sri Lanka',color=tableau20[6])
    # plt.plot(df_maldives.Year,df_maldives.Value,label='Maldives',color=tableau20[7])
    # plt.plot(df_india_pop.Year,df_india_pop.Value,label='India',color=tableau20[8])
    # plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.xlabel('Years',  fontsize=14)
    # plt.ylabel('% of Population',  fontsize=14)
    # plt.title('Access to Electricity for South Asian Countries', fontsize=14)
    # plt.ylim([0,110])
    
    # df_india_fossil = get_df("India", "EG.ELC.FOSL.ZS")
    # df_india_hydro = get_df("India", "EG.ELC.HYRO.ZS")
    # df_india_nuclear = get_df("India", "EG.ELC.NUCL.ZS")
    # df_india_renewable = get_df("India", "EG.ELC.RNWX.ZS")

    # plt.plot(df_india_fossil.Year,df_india_fossil.Value,label='Fossil fuel',color=tableau20[0])
    # plt.plot(df_india_hydro.Year,df_india_hydro.Value,label='Hydro',color=tableau20[1])
    # plt.plot(df_india_nuclear.Year,df_india_nuclear.Value,label='Nuclear',color=tableau20[2])
    # plt.plot(df_india_renewable.Year,df_india_renewable.Value,label='Renewable',color=tableau20[3])
    # fill_between(df_india_fossil.Year,df_india_fossil.Value,0,alpha=0.5,color=tableau20[0])
    # fill_between(df_india_hydro.Year,df_india_hydro.Value,0,alpha=0.5,color=tableau20[1])
    # fill_between(df_india_nuclear.Year,df_india_nuclear.Value,0,alpha=0.5,color=tableau20[2])
    # fill_between(df_india_renewable.Year,df_india_renewable.Value,0,alpha=0.5,color=tableau20[3])
    # plt.legend(loc=1, borderaxespad=1.)
    # plt.xlabel('Years',  fontsize=14)
    # plt.ylabel('% of Total Energy',  fontsize=14)
    # plt.title('Energy Mix in India (1971-2012)', fontsize=18)

if __name__ == '__main__':
    main()