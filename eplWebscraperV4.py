# %%
# Import dependencies

# Import basic libraries
import pandas as pd
import numpy as np # might not be used after all

# Import visualization libraries
from IPython.display import HTML
import matplotlib.pyplot as plt
import seaborn as sns
import dataframe_image as dfi

# Import preprocessing libraries
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Import machine learning libraries
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

# Import metrics libraries
from sklearn.metrics import r2_score

# Import webscraping libraries
import requests
from bs4 import BeautifulSoup as soup
import json

# Import functions
from myFunctions import *
# %%
# Set up the connection to the API for download
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json_data = r.json()

# %%
json_data.keys()
# %%
# %%
# Create the dataframes that will be combined into our main dataframe
elementsDf = pd.DataFrame(json_data['elements'])
elementTypesDf = pd.DataFrame(json_data['element_types'])
teamsDf = pd.DataFrame(json_data['teams'])
# %%
eventsDf = pd.DataFrame(json_data['events'])
#%%
game_settingsDf = pd.DataFrame(json_data['game_settings'])
#%%
phasesDf = pd.DataFrame(json_data['phases'])
#%%
total_playersDf = pd.DataFrame(json_data['total_players'])
#%%
element_statsDf = pd.DataFrame(json_data['element_stats'])

# %%
print(json_data)
# %%
