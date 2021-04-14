import pandas as pd
import numpy as np


class Split_df():
    def __init__(self):
        return

    def night_df(self, df: object):

        isNightRun = df.columns[0].lower()

        isDayRun_idx = df[df.iloc[:, 0].str.lower().eq(
            "day runs")].any(True).values

        if isNightRun == "night runs" and isDayRun_idx:

            dayRunStart_idx = df[df.iloc[:, 0].str.lower().eq(
                "day runs")].index[0]

            return df.iloc[0:dayRunStart_idx]
        else:
            print("Night runs doesnt work")

    def day_df(self, df: object):

        isDayRun = df[df.iloc[:, 0].str.lower().eq("day runs")
                      ].any(True).values
        isVisy = df[df.iloc[:, 0].str.lower().eq("visy")].any(True).values
        isRicky = df[df.iloc[:, 0].str.lower().eq("ricky li")].any(True).values

        if isDayRun:
            dayRunStart_idx = df[df.iloc[:, 0].str.lower().eq(
                "day runs")].index[0]
            if isVisy:
                visyStart_idx = df[df.iloc[:, 0].str.lower().eq(
                    "visy")].index[0]
                return df.iloc[dayRunStart_idx:visyStart_idx]

            elif isRicky:
                visyStart_idx = df[df.iloc[:, 0].str.lower().eq(
                    "ricky li")].index[0]
                return df.iloc[dayRunStart_idx:visyStart_idx]
        else:
            print("No Day Run")

    def visy_df(self, df: object):

        isVisy = df[df.iloc[:, 0].str.lower().eq("visy")].any(True).values
        isRicky = df[df.iloc[:, 0].str.lower().eq("ricky li")].any(True).values
        isUOS = df[df.iloc[:, 0].str.lower().eq("university")].any(True).values

        if isVisy.size > 0:
            visyStart_idx = df[df.iloc[:, 0].str.lower().eq("visy")].index[0]

            if isUOS:

                uosStart_idx = df[df.iloc[:, 0].str.lower().eq("university")].index[0]
                return df.iloc[visyStart_idx:uosStart_idx]

        elif isRicky:

            visyStart_idx = df[df.iloc[:, 0].str.lower().eq("ricky li")].index[0]

            if isUOS:

                uosStart_idx = df[df.iloc[:, 0].str.lower().eq("university")].index[0]
                return df.iloc[visyStart_idx:uosStart_idx] 
        else:
            print("No Visy")

    def uos_df(self, df: object):

        isUOS = df[df.iloc[:, 0].str.lower().eq("university")].any(True).values
        isEmptyrow = df.iloc[:,0].isna().values.any()

        if isUOS:
            uosStart_idx = df[df.iloc[:, 0].str.lower().eq("university")].index[0]
            if isEmptyrow:
                uosEnd_idx = df[df.iloc[:,0].isna()].index[0]
                return df.iloc[uosStart_idx:uosEnd_idx]
        else:

            print("No UOS")
