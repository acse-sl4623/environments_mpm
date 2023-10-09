from envtest import my_sum

import pandas as pd

df=pd.DataFrame({'col 1':[1,2],'col 2':[3,4]})
x=my_sum(df['col 1'][0],df['col 2'][0])

print(x)