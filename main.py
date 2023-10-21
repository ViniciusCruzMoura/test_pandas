import pandas as pd

df = pd.read_csv('data.csv')

# use to_string() to print the entire DataFrame.
#print(df.to_string()) 
print(df)

#Check the number of maximum returned rows:
print(pd.options.display.max_rows) 

#Increase the maximum number of rows to display the entire DataFrame:
#pd.options.display.max_rows = 9
#df = pd.read_csv('data.csv')
#print(df)


# Load the JSON file 
df = pd.read_json('data.json')
print(df.to_string())


# Load a Python Dictionary
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df)

# Print first 10 rows
df = pd.read_csv('data.csv')
print(df.head(10))
# Print first 5 rows
print(df.head())

# csv to json
df = pd.read_csv('data.csv')
df.to_json('new_data.json')

# json to csv
df = pd.read_json('data.json')
df.to_csv ('new_data.csv', index = None)


#Get a list of a particular column values of a Pandas DataFrame
# dictionary
dict = {'Name': ['Martha', 'Tim',
                'Rob', 'Georgia'],
         'Marks': [87, 91, 
                  97, 95]}
# create a dataframe object
df = pd.DataFrame(dict)
# show the dataframe
print(df)
# list of values of 'Marks' column
marks_list = df['Marks'].tolist()
# show the list
print(marks_list)
