import pandas as pd
from sqlalchemy import create_engine

teams = pd.read_csv("datasets/teams_toload.csv")
medals = pd.read_csv("datasets/medals_toload.csv")
#print(medals.head())

engine = create_engine('mysql+pymysql://root:@localhost/jeux_olympique_db')
teams.to_sql('teams', con=engine, if_exists='append', index=False)
medals.to_sql('medals', con=engine, if_exists='append', index=False)