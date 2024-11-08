import pandas as pd

# List of all CSV files
all_files = [
    "JC-202301-citibike-tripdata.csv",
    "JC-202302-citibike-tripdata.csv",
    "JC-202303-citibike-tripdata.csv",
    "JC-202304-citibike-tripdata.csv",
    "JC-202305-citibike-tripdata.csv",
    "JC-202306-citibike-tripdata.csv",
    "JC-202307-citibike-tripdata.csv",
    "JC-202308-citibike-tripdata.csv",
    "JC-202309-citibike-tripdata.csv",
    "JC-202310-citibike-tripdata.csv",
    "JC-202311-citibike-tripdata.csv",
    "JC-202312-citibike-tripdata.csv"
]

# Create an empty list to store DataFrames
df_list = []

# Iterate through each file and read it into a DataFrame
for filename in all_files:
    df = pd.read_csv(filename)
    df_list.append(df)

# Concatenate all DataFrames into a single DataFrame
merged_df = pd.concat(df_list, ignore_index=True)

# Write the merged DataFrame to a new CSV file
merged_df.to_csv("citibike_data_2023.csv", index=False)