import pandas as pd
import requests

url = "http://www.stata-press.com/data/r8/cancer.dta"
response = requests.get(url)

with open("cancer.dta", "wb") as file:
    file.write(response.content)

data = pd.read_stata("cancer.dta")
print(data.head())
