import pandas as pd
import matplotlib.pyplot as plt
import eurostat

df = eurostat.get_data_df("ei_bsco_m")
df[["indic", "s_adj", "unit", "geo\\time"]].describe()
test_value_of_germany = df[df["indic"].eq("BS-CSMCI") & df["unit"].eq("BAL") & df["s_adj"].eq("NSA") & df["geo\\time"]]
test_value_of_germany = test_value_of_germany.drop(columns=['indic', 's_adj', 'unit'])
test_value_of_germany = test_value_of_germany.set_index('geo\\time')

print(test_value_of_germany)
print(test_value_of_germany.loc['DE'])

test_value_of_germany.loc['DE'].plot.line()

plt.show()
