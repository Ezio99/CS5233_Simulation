import numpy as np
import pandas as pd
import os

# Load the main dataset
arrival_file_path = "arrivals.xlsx"
df = pd.read_excel(arrival_file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Keep only relevant columns
df = df.iloc[:, :2]
df.columns = ["Station", "ArrivalTime"]

# Drop missing values
df = df.dropna()

# Convert TimeSpent to float
df["ArrivalTime"] = df["ArrivalTime"].astype(float)

# Loop through each attraction and save to separate files
for station in ["A", "B", "C", "D"]:
    df_station = df[df["Station"] == station]
    folder_name = f"./{station}_Arrival_Data"
    os.makedirs(folder_name, exist_ok=True)
    interarrival_file = os.path.join(folder_name, f"{station}_Interarrival_time.txt")
    arrival_file_path = os.path.join(folder_name, f"{station}_Arrival_time.txt")
    with open(arrival_file_path, "w") as f:
        for value in df_station["ArrivalTime"]:
            f.write(f"{value:.2f}\n")

    interarrivals = np.diff(df_station["ArrivalTime"])
    with open(interarrival_file, "w") as f:
        for value in interarrivals:
            f.write(f"{value:.2f}\n")


# print("Files created: A.xlsx, B.xlsx, C.xlsx, D.xlsx")
