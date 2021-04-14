
import pandas as pd
import numpy as np
from split_df import Split_df
from restructure_df import Restructure_df

PATH_A = "/media/sf_BLOB_STORAGE/Roster/Weekdays/Copy of Drivers and Rosters MON 01.03 to TUE 02.03.xlsx"
PATH_B = "/media/sf_BLOB_STORAGE/Roster/Weekdays/Copy of Drivers and Rosters THU 08.04 to FRI 09.04.xlsx"

df = pd.read_excel(PATH_A)

night_ds = Split_df().night_df(df)
day_ds = Split_df().day_df(df)
visy_ds = Split_df().visy_df(df)
uos_ds = Split_df().uos_df(df)

nightRuns_date = Restructure_df().grep_date(night_ds)

# Reset Headers 
day_ds = Restructure_df().reset_header(day_ds)
visy_ds = Restructure_df().reset_header(visy_ds)
uos_ds = Restructure_df().reset_header(uos_ds)

dayRuns_date = Restructure_df().grep_date(day_ds)

uos_ds = Restructure_df().rename_cols(uos_ds)
print(uos_ds)

# print(nightRuns_date)

# print(dayRuns_date)

# print(visy_ds)

# print(uos_ds)


# ================================================================
# Features 
# 1. Split data frame 
#       **Extract Date, Run Type / Name of the df
#               Same Date - DayRuns, Visy and UOS
#        
#       a. Night Runs
#       
#   Except Night Runs, all df must replace header with first row 
#  
#       b. Day Runs
#       c. Visy - has problem 
#       d. UOS

# 2. Rename Dataframe - column name 
#       a. Rename Column names  
#       b. Reorder the Columns 
# 

# 3. Processing Name 
#       a. Split name 
#       b. When middle name exist
# 
# 4. Convert Name to EmployeeId
# 
 
# 5. Mutiple Drivers - Secondary Driver  
#       - Processing Name
#       

# 6. Route Number
#       a. Split Route Number 
#       b. if more than one within 5 

# 7. Truck number
#       a. Split Truck number 




# if df.columns[0].lower() == "night runs":

#     hasNightRuns = df[df.iloc[:, 0].str.lower().eq("day runs")].any(True).values

#     if hasNightRuns:
#         nightRuns_idx_end = df[df.iloc[:, 0].str.lower().eq("day runs")].index[0]
# #       To select Night Df
#         nightRuns_df = df.iloc[0:nightRuns_idx_end]
# #       
#         current_nightRuns_Date = df.columns[-1].date()
#         nightRuns_df['Date'] = current_nightRuns_Date
        
#         nightRuns_df[['Firstname', 'Lastname']] = nightRuns_df.iloc[:,0].str.split(" ", 1, expand=True)
#         df_2 = nightRuns_df.iloc[:,[1,2,4,5,6]]
#     else: 
#         print("No Night Runs")

# df_2.rename(columns={df_2.columns[0] : 'Route number', df_2.columns[1] : 'Truck number'})

