# jinal rajawat
# stockCPT
# program that retrieves and prints information about any number of stocks

# here is the reader than reads information from Yahoo Finance
import pandas_datareader as pdr
import datetime

print("Welcome to your Stock Portfolio!")
print("You are able to analyze different stocks")
numOfStocks = int(input("Please enter how many stocks you would like to analyze: "))
counter = 0
stocks = []
while counter < numOfStocks:
    stock = input("Please enter a ticker symbol: ")
    stocks.append(stock)  
    counter +=1

print("\nYou will be able to see different statistics about them as long as you input valid options.")

# variable is set here just to start loop
option = "1"
while option == "1" or option == "2" or option == "3" or option == "4" or option == "5":
   # menu for user is displayed each time loop is run
   print("\nOption 1: See the closing or current prices of each of the stock investments from the last 30 days.")
   print("Option 2: See the opening prices of each of the stock investments from the last 30 days.")
   print("Option 3: See the Highs of each of the stock investments from the last business day.")
   print("Option 4: See the Lows of each of the stock investments from the last business day.")
   print("Option 5: See the Volume of each of the stock investments from the last business day.")
   option = input("Choose an option: ")

# if user inputs 1, they will see all the info about stocks' closing or current prices from last 30 days
   if option == "1":
       print("\nClosing or current prices of each of the stock investments from the last 30 days:")
       print("All values are in CAD.")

       # here the program sets the date for when the information is to be from
       start = datetime.date.today() + datetime.timedelta(-30)
       end = datetime.date.today()
       # here the program retrieves the info from Yahoo Finance
       reader = pdr.DataReader(stocks, 'yahoo', start, end)
       close = reader['Close']
       # here the program prints all information concerning stocks' current or closing prices
       print(close)

# if user inputs 2, they will see all the info about stocks' opening prices from last 30 days
   elif option == "2":
       print("\nOpening prices of each of the stock investments from the last 30 days:")
       print("All values are in CAD.")

       start = datetime.date.today() + datetime.timedelta(-30)
       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', start, end)
       open = reader['Open']
       print(open)

# if the user inputs 3, they will see the info about the stocks' highs from last business day
   elif option == "3":
       print("\nHighs of each of the stock investments from the last business day:")
       print("All values are in CAD.")
       
       # don't need "start" variable here because only need one business day
       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', end, end)
       high = reader['High']
     
# if user inputs 4, they will see info about stocks' lows from last business day
   elif option == "4":
       print("\nLows of each of the stock investments from the last business day:")
       print("All values are in CAD.")

     
       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', end, end)
       low = reader['Low']
       print(low)
       print("")

# if user inputs 5, they will see info about 5 stocks' volume from last business day
   elif option == "5":
       print("\nVolume of each of the stock investments from the last business day:")

       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', end, end)
       volume = reader['Volume']

       print(volume)
     
# if user inputs anytthing other than 1, 2, 3, 4, or 5, the loop will break
# program prints the following comments and program ends
   else:
       print("\nYou have entered an invalid option.")
       print("Thank you for looking at your stock portfolio.")