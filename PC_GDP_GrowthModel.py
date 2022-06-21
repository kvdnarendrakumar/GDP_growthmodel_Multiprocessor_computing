#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:40:47 2022
@author: narendrakoppuravuri
"""
import matplotlib.pyplot as plt  # to plot graph
from matplotlib import animation  # to animate lines
import multiprocessing as mp  # for parallelism
import time  # to track     
import csv



def read_excel():
#Reading csv
    file = open('GDP.csv',encoding = "ISO-8859-1")  
    type(file)

    csvreader = csv.reader(file)
    data_from_csv = []

    for row in csvreader:
        data_from_csv.append(row)
    return data_from_csv    

''' def find_average_gdp(country):
    average = 0
    sum = 0
    for i in data_from_csv:
        if i[0] == country:
            for j in range(1,len(i)):
                sum = sum+int(j)
            average = sum/(len(i)-1)
    
    print("averagae is ",average)
    return average 

narendra = find_average_gdp("India")
print(narendra)'''

'--------------------------------------------------------------------------------------------'

# calcluting the time for reading the data from excel
'''print('Reading excel file')
excel_read_start = time.perf_counter()
data_from_csv = read_excel()
excel_read_end = time.perf_counter()
print('Done reading in %s seconds' % (excel_read_end - excel_read_start))'''
    
'--------------------------------------------------------------------------------------------'    
def plot_country_gdp_growth(country_list):
    data = []
    data_from_csv = read_excel()
    for i in data_from_csv:
        for j in country_list:
            if i[0] == j:
                data.append(i[1:])
    
    #Converting the string values to numerical values
    
    for i in data:
        for j in range(0,len(i)):
            i[j] = float(i[j])
            
            
            
    for i in range(0,len(country_list)):
        plt.plot(data_from_csv[0][1:],data[i],marker = '.', label = country_list[i])
    
    plt.xlabel("years")
    plt.ylabel("Percentage change")  
    plt.title("GDP growth annually")
    plt.legend()


'--------------------------------------------------------------------------------------------'
'''def plot_country_gdp_growth_pp(country_list):
    no_of_processors = 8
    pool = mp.Pool(no_of_processors)
    print("Reading excel file using multiple processors")
    excel_mp_start =  time.perf_counter()
    data_from_csv_mp = pool.apply_async(read_excel())
    excel_mp_end = time.perf_counter()
    pool.close()
    pool.join()
    print("Time to read using multiple processers is % seconds" %(excel_mp_end-excel_mp_start))
    
    excel_plot_start =  time.perf_counter()
    plotting = pool.apply_async(plot_country_gdp_growth,country_list)
    pool.close()
    pool.join()
    excel_plot_end =  time.perf_counter()
    
    print("Time to plot using multiple processors in %seconds"%(excel_plot_end-excel_plot_start))'''
    
    
def main(countries_selected):
    print(countries_selected)
    no_of_processors = 4
    print("Number of processors: ", no_of_processors)
    pool = mp.Pool(no_of_processors)
    time_Start = time.time()
    #narendra = pool.apply_async(plot_country_gdp_growth,["India","Afghanistan","Angola","Brazil"])
    narendra = pool.apply_async(plot_country_gdp_growth,countries_selected)
    #narendra = pool.apply_async(plot_country_gdp_growth,["India"])
    print("Time taken using multiple processors is %s seconds"%(time.time()-time_Start))
    
    time_without = time.time()
    #narendra2 = plot_country_gdp_growth(["India","Afghanistan","Angola","Brazil"])
    narendra2 = plot_country_gdp_growth(countries_selected)

    #narendra2 = plot_country_gdp_growth(["India"])
    #print("time taken without mp is %seconds "%(time.time()-time_without))
    print("Time taken using serial processing is %s seconds "%(time.time()-time_without))
    
if __name__ == '__main__':
    main()
    
    
    
#https://data.worldbank.org/indicator/SP.POP.GROW?end=2020&start=2000
    
    
    

    
    
    