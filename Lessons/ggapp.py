#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 09:39:55 2019

@author: tunn8
"""

## Read file

import pandas as pd
#import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#%% OVERALL
_path = "F:/temp/democlass NC/googleplaystore.csv"
data = pd.read_csv(_path)
data.shape

# nan cleaning
total = data.isnull().sum().sort_values(ascending=False)
data.dropna(how ='any', inplace = True)
data.shape

# duplicate records
dup = data[data.duplicated(keep=False)]
data = data.drop_duplicates(keep="first")
# duplicate app 
dup_app = data[data["App"].duplicated(keep=False)]
data = data.drop_duplicates("App", keep="first")

#%% RATING
data['Rating'].describe()

plot = sns.kdeplot(data["Rating"], shade=True)
plot.set_xlabel("Rating")
plot.set_ylabel("Frequency")
plt.title("Distribution of Rating", size=20)

plot = sns.distplot(data["Rating"], bins=50)
plot.set_xlabel("Rating")
plot.set_ylabel("Frequency")
plt.title("Distribution of Rating", size=20)

#%% CATEGORY
data["Category"].value_counts()

sns.countplot(x="Category",data=data, palette="Set1")
plt.xticks(rotation=90)
plt.title("Count of app in each category")

plt.figure(figsize=(8, 5))
sns.boxplot(data=data, x="Category", y="Rating")
plt.xticks(rotation=90)
plt.title("Boxplot of Rating VS Category")

"""
QUANTILE
"""
temp = data[data["Category"]=="ENTERTAINMENT"]

q5 = temp["Rating"].quantile(.5)
q25 = temp["Rating"].quantile(.25)
q75 = temp["Rating"].quantile(.75)
d = q75-q25

q0 = max(min(temp["Rating"]), q25 - d)
q99 = min(max(temp["Rating"]), q75 + d)

# other chart
sns.countplot(y="Category",data=data, palette="Set1")
plt.xticks(rotation=90)
plt.title("Count of app in each category")

plt.figure(figsize=(5, 7))
sns.boxplot(data=data, y="Category", x="Rating")
plt.grid()
plt.title("Boxplot of Rating VS Category")

#%% TYPE
"""
pandas also have their own plot function
https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
"""
temp = pd.DataFrame(data["Type"].value_counts())
plt.figure(figsize=(15, 5))
temp.plot.pie(y="Type", figsize=(5, 5), autopct='%1.1f%%',
              legend=False, startangle=90)

plt.figure(figsize=(15, 5))
sns.boxplot(data=data, x="Category", y="Rating", hue="Type",
            fliersize=0, palette="Set2")
plt.xticks(rotation=90)
plt.tight_layout()

#%% SIZE
data["Size"].describe()
data["Size"].unique()

"""
more about lambda:
https://www.w3schools.com/python/python_lambda.asp
"""
data['Size'] = data['Size'].apply(lambda x: str(x).replace('Varies with device', 'NaN') if 'Varies with device' in str(x) else x)
data['Size'] = data['Size'].apply(lambda x: str(x).replace('M', '') if 'M' in str(x) else x)
data['Size'] = data['Size'].apply(lambda x: str(x).replace(',', '') if 'M' in str(x) else x)
data['Size'] = data['Size'].apply(lambda x: float(str(x).replace('k', '')) / 1000 if 'k' in str(x) else x)
data['Size'] = data['Size'].astype(float)

plt.figure(figsize = (7,7))
sns.jointplot(x="Size", y="Rating",color = 'orangered', data=data, size = 8, kind="reg");
plt.savefig("F:/temp/democlass NC/size_rating.jpg", dpi=300)

corr = data[["Rating", "Size"]].corr()

#%% REVIEWS
data["Reviews"] = data["Reviews"].astype(int)

#plt.figure(figsize = (10,10))
sns.regplot(x="Reviews", y="Rating", color = 'darkorange',data=data[data['Reviews']<1000000]);


#%% GENRES
"""
split column into multiple columns
"""
temp = data['Genres'].str.split(';', expand=True)
temp = pd.merge(data[["App", "Rating", "Content Rating"]], temp, left_index=True, right_index=True)
temp = pd.melt(temp, id_vars=["App", "Content Rating"], value_name="Genre", value_vars=[0, 1])
temp = temp.dropna(subset=["Genre"])

#%% PRICE
data['Price'] = data['Price'].apply(lambda x: str(x).replace('$', '') if '$' in str(x) else str(x))
data['Price'] = data['Price'].astype(float)

#%% INSTALL
check = data.groupby(["Content Rating", "Installs"])["App"].count().unstack(0)
check = check.fillna(0)
sns.heatmap(data=check, cmap="YlGnBu")

data['Installs'] = data['Installs'].apply(lambda x: x.replace('+', '') if '+' in str(x) else x)
data['Installs'] = data['Installs'].apply(lambda x: x.replace(',', '') if ',' in str(x) else x)
data['Installs'] = data['Installs'].astype(int)

plt.figure(figsize = (10,10))
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data);
plt.title('Rating VS Installs',size = 20)
