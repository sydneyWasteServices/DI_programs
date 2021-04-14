import pandas as pd
import numpy as np


class Restructure_df():
    def __init__(self):
        return

    def grep_date(self, df):
        return df.columns[-1].date()

# Could be Problem 
    def reset_header(self, df):
        # Make sure Header is not Driver's info itself
        isRicky = df[df.iloc[:, 0].str.lower().eq("ricky li")].any(True).values
        # isJohn = df[df.iloc[:, 0].str.lower().eq("john justice")].any(True).values
        # or isJohn
        if isRicky:
            return df
        else:
            return df.rename(columns=df.iloc[0]).drop(df.index[0])

    def rename_cols(self, df):
        df = df.iloc[:, 0:3]

        col_name = np.array([
            'Primary_Driver',
            'Primary_Route',
            'Primary_Truck'
        ])

        additional_col_name = np.array([
            'Date',
            'Subcontracted_From/Special_Client',
            'Run_Type',
            'Primary_DriverID',
            'Secondary_DriverID',
            'Secondary_Driver',
            'Primary_Driver_Firstname',
            'Primary_Driver_Middlename',
            'Primary_Driver_Lastname',
            'Secondary_Driver_Firstname',
            'Secondary_Driver_Middlename',
            'Secondary_Driver_Lastname',
            'Satellite_Route_1',
            'Satellite_Route_2',
            'Satellite_Route_3',
            'Satellite_Route_4',
            'Satellite_Route_5',
            'Alternative_Truck',
            'Note'
        ])

        df = df.set_axis(col_name, axis='columns')
        
        df_1 = pd.DataFrame(columns=additional_col_name)
        df_2 = pd.concat([df, df_1])

        return df_2 
