# jinal rajawat
# stockCPT
# program that retrieves and prints information about 5 different stocks in the market

# here is the reader than reads information from Yahoo Finance
import pandas_datareader as pdr
import datetime
print("Welcome to your Stock Portfolio!")
print("You have invested in five different stocks:")
print("Apple, Amazon, IBM, Starbucks and Walmart")
print("You will be able to see different statistics about them as long as you input valid options.")
# variable is set here just to start loop
option = "1"
while option == "1" or option == "2" or option == "3" or option == "4" or option == "5":
   # menu for user is displayed each time loop is run
   print("\nOption 1: See the closing or current prices of each of the five stock investments from the last 30 days.")
   print("Option 2: See the opening prices of each of the five stock investments from the last 30 days.")
   print("Option 3: See the Highs of each of the five stock investments from the last business day.")
   print("Option 4: See the Lows of each of the five stock investments from the last business day.")
   print("Option 5: See the Volume of each of the five stock investments from the last business day.")
   option = input("Choose an option")

   if option == "1":
       # if user inputs 1, they will see all the info about 5 stocks' closing or current prices from last 30 days
       print("\nClosing or current prices of each of the five stock investments from the last 30 days:")
       print("All values are in CAD.")

       # here the program indicates which stocks are to be retrieved and printed, the variable is set
       stocks = ["AAPL", "AMZN", "IBM", "SBUX", "WMT"]
       # here the program sets the date for when the information is to be from
       start = datetime.date.today() + datetime.timedelta(-30)
       end = datetime.date.today()
       # here the program retrieves the info from Yahoo Finance
       reader = pdr.DataReader(stocks, 'yahoo', start, end)
       close = reader['Close']
       # here the program prints all information concerning 5 stocks' current or closing prices
       print(close)

   elif option == "2":
       # if user inputs 2, they will see all the info about 5 stocks' opening prices from last 30 days
       print("\nOpening prices of each of the five stock investments from the last 30 days:")
       print("All values are in CAD.")

       stocks = ["AAPL", "AMZN", "IBM", "SBUX", "WMT"]
       start = datetime.date.today() + datetime.timedelta(-30)
       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', start, end)
       open = reader['Open']
       print(open)

   elif option == "3":
       # if the user inputs 3, they will see the info about the 5 stocks' highs from last business day
       print("\nHighs of each of the stock investments from the last business day:")
       print("All values are in CAD.")

       stocks = ["AAPL", "AMZN", "IBM", "SBUX", "WMT"]
       # don't need "start" variable here because only need one business day
       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', end, end)
       high = reader['High']

   elif option == "4":
       # if user inputs 4, they will see info about 5 stocks' lows from last business day
       print("\nLows of each of the five stock investments from the last business day:")
       print("All values are in CAD.")

       stocks = ["AAPL", "AMZN", "IBM", "SBUX", "WMT"]
       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', end, end)
       low = reader['Low']
       print(low)
       print("")

   elif option == "5":
       # if user inputs 5, they will see info about 5 stocks' volume from last business day
       print("\nVolume of each of the five stock investments from the last business day:")

       stocks = ["AAPL", "AMZN", "IBM", "SBUX", "WMT"]
       end = datetime.date.today()
       reader = pdr.DataReader(stocks, 'yahoo', end, end)
       volume = reader['Volume']

       print(volume)

   else:
       # if user inputs anytthing other than 1, 2, 3, 4, or 5, the loop will break
       # program prints the following comments and program ends
       print("\nYou have entered an invalid option.")
       print("Thank you for looking at your stock portfolio.")


