
# Import statements
from bs4 import BeautifulSoup
import requests

# local variables
owner_last_name = "Timsina"
year="2021"
summit_county_search_url = "https://fiscaloffice.summitoh.net/pls/apex/thothrefintg2.opt?doland=ON&docard=ON&cardnum=ALL&dosales=ON&dopermits=ON&dotaxes=ON&doassess=ON&docauv=OFF&donotes=ON&dogeinf=ON&LIENYEAR={year}&parcel=&route=&addr=&own={owner_last_name}%25&action=Search".format(year=year, owner_last_name=owner_last_name)

# For Production
# html_text = requests.get(summit_county_search_url).text

# For development
local_file = "timsina_search_result.html"
html_text = open(local_file, "r")

# Setup beautiful soup instance
soup = BeautifulSoup(html_text, 'lxml')

# Get desired property
properties = soup.find_all('table', class_ = "results")

# Variable to hold parcel list
parcel_lists = []

# loop thru each property and get the parcel number
for each_parcel in properties[2].find_all('input'):
    # append parcel number to the list
    parcel_lists.append(each_parcel.get('value'))

# print parcel list
print(parcel_lists)
