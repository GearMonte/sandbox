import pandas as pd
from io import StringIO

# Your data as a multi-line string
data = """
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
1,0,3,"Braund, Mr. Owen Harris",male,22.0,1,0,A/5 21171,7.2500,,S
2,1,1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38.0,1,0,PC 17599,71.2833,C85,C
3,1,3,"Heikkinen, Miss. Laina",female,26.0,0,0,STON/O2. 3101282,7.9250,,S
4,1,1,"Futrelle, Mrs. Jacques Heath (Lily May Peel)",female,35.0,1,0,113803,53.1000,C123,S
5,0,3,"Allen, Mr. William Henry",male,35.0,0,0,373450,8.0500,,S
"""

# Use StringIO to simulate a file object
data = StringIO(data)

# Create a DataFrame
df = pd.read_csv(data)

# Convert the DataFrame to JSON
json_data = df.to_json(orient='records', lines=True)

# Print the JSON data
print(json_data)

# To save the JSON data to a file, uncomment the following line:
# with open('data.json', 'w') as file:
#     file.write(json_data)
