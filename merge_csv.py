import pandas as pd
import glob
import os

# merging the files
path =r'/home/gaurav/pythonProject/hcl/files'
# A list of all joined files is returned
joined_list = glob.glob(path + "/*.csv")
# Finally, the files are joined

# columns = ['', 'EMAIL', 'FIRST NAME', 'LAST NAME', 'PHONE NUMBER', 'DATE JOINED', 'BALANCE', 'IS OFFER', 'IS PHONE CONFIRMED', 'COMMENT', 'GET DESC', 'GET APP STATUS', 'GET APP TYPE', 'PREMIUM TAG', 'COUNTRY OF ORIGIN', 'REFERRER CODE', 'REFEREE CODE']

df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
# df.columns = columns
df.to_csv('output.csv', index=False)
print(df)
