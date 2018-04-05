import csv
import datetime
f = open("guns.csv")
data = list(csv.reader(f))
headers = data[0]
data = data[1:]
print(headers)
print(data[0:5])
years = [y[1] for y in data]
year_count={}
for y in years:
    if y in year_count:
        year_count[y] = year_count[y] + 1
    else:
        year_count[y] = 1
print(year_count)

dates = [datetime.datetime(year=int(y[1]),month=int(y[2]),day=1) for y in data]
date_counts = {}
for d in dates:
    if d in date_counts:
        date_counts[d] = date_counts[d] + 1
    else:
        date_counts[d] = 1
print(date_counts)
sex_counts = {}
race_counts = {}
for d in data:
    if d[5] in sex_counts:
        sex_counts[d[5]] = sex_counts[d[5]] + 1
    else:
        sex_counts[d[5]] = 1
    if d[7] in race_counts:
        race_counts[d[7]] = race_counts[d[7]] + 1
    else:
        race_counts[d[7]] = 1
print(sex_counts)
print(race_counts)
import csv
pointer = open("census.csv")
census = list(csv.reader(pointer))
census
mapping = {}
mapping['White'] = int(census[1][10])
mapping['Hispanic']=int(census[1][11])
mapping['Black']=int(census[1][12])
mapping['Native American/Native Alaskan']=int(census[1][13])
mapping['Asian/Pacific Islander']=int(census[1][14]) + int(census[1][15])
mapping
race_per_hundredk = {}
for r in race_counts.keys():
    if r in mapping:
        race_per_hundredk[r] = (race_counts[r]/mapping[r])*100000
print(race_per_hundredk)
intents = [d[3] for d in data]
races = [d[7] for d in data]
homicide_race_per_hundredk = {}
for i,r in enumerate(races):
    if intents[i] == 'Homicide':
        homicide_race_per_hundredk[r] += 1
    else:
        homicide_race_per_hundredk[r] = 1
homicide_race_per_hundredk
homicide = {}
for h in homicide_race_per_hundredk.keys():
    if h in mapping:
        homicide[h] = (homicide_race_per_hundredk[h]/mapping[h])*100000
print(homicide)

def refine_education():
    for row in data:
        try:
            row[10] = int(row[10])
        except Exception as excep:
            row[10] = -1
refine_education()
print(data[0:10])
import matplotlib.pyplot as plt
import numpy as np
def calculate_literacy_rate(edu_level,race):
    education = {}
    for row in data:
        if row[10] == edu_level and row[7]==race:
            if row[9] in education:
                education[row[9]] = education[row[9]] + 1
            else:
                education[row[9]] = 1
    print(len(education))
    return education
ret_data = calculate_literacy_rate(4,'Hispanic')
x_axis = list(np.random.randint(1,len(ret_data),len(ret_data)))
y_axis = list(ret_data.values())
print(ret_data)
plt.scatter(x_axis,y_axis)
plt.show()
def cal_death_rate(intent,race,year):
    formatted_data = []
    for row in data:
        if row[1] == year and row[3]== intent and row[7] == race:
            formatted_data.append(row)
    return formatted_data
pd.DataFrame

import pandas as pd
my_data = cal_death_rate('Suicide','Black','2012')
my_series = pd.DataFrame(my_data)
homi_white_100k = (len(my_data)/mapping['Black'])*100000
len(my_data),homi_white_100k





