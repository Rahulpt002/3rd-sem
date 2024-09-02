import pandas as pd

sr = pd.Series(pd.date_range('2021-05-01','2021-05-12',freq = 'D'))
# To avoid dtype
# Series.to_string
print(sr.to_string(index=False))
