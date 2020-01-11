# program that gets the current market data from marketwatch

#make imports
import requests
from bs4 import BeautifulSoup

# connects to market watch
res = requests.get('https://www.marketwatch.com')

# sets up beautiful soup to parse the html from the response
soup = BeautifulSoup(res.text, 'html.parser')

# beautiful soup selectors

# selects rows of the table containing the market data
rows = soup.select('.element--markets .table--primary .table__row')

# selects names of the market in the rows 
# selects the price
# selects the percent
names = soup.select('.element--markets .table--primary .table__row .symbol')
prices = soup.select('.element--markets .table--primary .table__row .price')
percents = soup.select('.element--markets .table--primary .table__row .percent')


# this function receives the names and percents 
# it returns a dictionary that maps the markets to its percents
def readData(names, percents):
    marketsData = {}  #to store the names

    for index, item in enumerate(names):

        # gets their inner htmls
        # strips the texts, they had \n in them
        market = names[index].getText().strip()
        performance = percents[index].getText().strip()

        # prints data to the screen
        print(f'{market} : {performance}')

        # set up key value pairs
        marketsData[market] = performance
    
    return marketsData

readData(names, percents)
