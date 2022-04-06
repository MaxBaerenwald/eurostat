# This is a sample Python script.
import pandas as pd
import eurostat
import datetime


if __name__ == '__main__':

    df = eurostat.get_data_df("ei_bsco_m")
    df[["indic", "s_adj", "unit", "geo\\time"]].describe()
    df = pd.DataFrame(df)

    print(df)
    """
    de_cci = df[(df["country"] == "DE") & (df["indic"] == "BS-CSMCI") & (df["s_adj"]
                                                                         == "NSA")]
    de_cci = de_cci[[c for c in de_cci.columns if isinstance(c, datetime) and
                     (c.year == 2020 or c.year == 2019)]]
    de_cci.index = ["Consumer confidence indicator"]
    de_cci.transpose()[::-1].plot.bar(figsize=(16, 9))
"""



