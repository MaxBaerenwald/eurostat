# This is a sample Python script.
import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import eurostat
import datetime

if __name__ == '__main__':
    df = eurostat.get_data_df("ei_bsco_m")
    df[["indic", "s_adj", "unit", "geo\\time"]].describe()
    test_value_of_germany = df[
        df["indic"].eq("BS-CSMCI") & df["unit"].eq("BAL") & df["s_adj"].eq("NSA") & df["geo\\time"].eq("DE")]
    print(test_value_of_germany.keys())
    test_value_of_germany = test_value_of_germany.drop(columns=['indic', 's_adj', 'unit'])
    print(test_value_of_germany)
    # df = pd.DataFrame(df).describe()
    # df = df.cumsum()
    # plt.figure()
    # df.plot()
