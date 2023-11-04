import pandas as pd

data_url = "https://raw.githubusercontent.com/AdamSpannbauer/rand-daily-records/master/yesterdays-records.txt"

df = pd.read_csv(data_url)

# have someone on the team with database access write the sql alchemy (or whatever
# library you use) to load the data into your database and bingo.

# INSERT DATABSE CODE HERE
