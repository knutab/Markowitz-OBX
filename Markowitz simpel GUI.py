import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
from numpy import linalg

#Function for downloading the stock data



#Function to run all the other function when clicking the RUN button.
def calculate():
    ticker1 = stock1.get()
    ticker2 = stock2.get()
    ticker3 = stock3.get()
    ticker4 = stock4.get()
    ticker5 = stock5.get()
    
    stockone = pd.io.parsers.read_csv('http://www.netfonds.no/quotes/paperhistory.php?paper=%s.OSE&csv_format=csv' %(ticker1),index_col='quote_date',parse_dates=True)
    stocktwo = pd.io.parsers.read_csv('http://www.netfonds.no/quotes/paperhistory.php?paper=%s.OSE&csv_format=csv' %(ticker2),index_col='quote_date',parse_dates=True)
    stockthree = pd.io.parsers.read_csv('http://www.netfonds.no/quotes/paperhistory.php?paper=%s.OSE&csv_format=csv' %(ticker3),index_col='quote_date',parse_dates=True)
    stockfour = pd.io.parsers.read_csv('http://www.netfonds.no/quotes/paperhistory.php?paper=%s.OSE&csv_format=csv' %(ticker4),index_col='quote_date',parse_dates=True)
    stockfive = pd.io.parsers.read_csv('http://www.netfonds.no/quotes/paperhistory.php?paper=%s.OSE&csv_format=csv' %(ticker5),index_col='quote_date',parse_dates=True)

    stockone = stockone['close']
    stocktwo = stocktwo['close']
    stockthree = stockthree['close']
    stockfour = stockfour['close']
    stockfive = stockfive['close']
    
#Want to calculate the returns on the different stocks.
    return1 = -((stockone.shift(-1) - stockone)/stockone.shift(-1))
    return2 = -((stocktwo.shift(-1) - stocktwo)/stocktwo.shift(-1))
    return3 = -((stockthree.shift(-1) - stockthree)/stockthree.shift(-1))
    return4 = -((stockfour.shift(-1) - stockfour)/stockfour.shift(-1))
    return5 = -((stockfive.shift(-1) - stockfive)/stockfive.shift(-1))


    data = pd.DataFrame(dict(return1 = return1, return2 = return2, return3 = return3, return4 = return4, return5 = return5), index = return1.index)
    data.columns = ticker1, ticker2, ticker3, ticker4, ticker5

    VCV = data.cov()
    
    returns = data.mean()

    npVCV = VCV.as_matrix()
    npVCVI = linalg.inv(npVCV)
    npReturns = returns.as_matrix()
    
    RISKFREE = float(riskfree.get())
    RETURNVECTOR = (npReturns-RISKFREE)
    
    ONEVEC =np.matrix([1,1,1,1,1])
    part1 = np.dot(npVCVI, RETURNVECTOR)
    part2 = np.dot(np.dot(ONEVEC, npVCVI),RETURNVECTOR)
   
    weightvector = (part1/part2)

    one1 = float(np.extract([1,0,0,0,0],weightvector))*100
    two1 = float(np.extract([0,1,0,0,0],weightvector))*100
    three1 = float(np.extract([0,0,1,0,0],weightvector))*100
    four1 = float(np.extract([0,0,0,1,0],weightvector))*100
    five1 = float(np.extract([0,0,0,0,1],weightvector))*100
    
    one.set(round(one1, 3))
    two.set(round(two1, 3))
    three.set(round(three1, 3))
    four.set(round(four1, 3))
    five.set(round(five1, 3))
    
    

#GUI part of the program
root =tk.Tk()
root.title('Test GUI')
root.geometry('600x600')


#String to hold the user inputs
stock1 = tk.StringVar()
stock2 = tk.StringVar()
stock3 = tk.StringVar()
stock4 = tk.StringVar()
stock5 = tk.StringVar()
riskfree = tk.StringVar()

#Entrybokses
entry1 = tk.Entry(root, width=10, textvariable=stock1).place(x=50, y=100)
entry2 = tk.Entry(root, width=10, textvariable=stock2).place(x=50, y=130)
entry3 = tk.Entry(root, width=10, textvariable=stock3).place(x=50, y=160)
entry4 = tk.Entry(root, width=10, textvariable=stock4).place(x=50, y=190)
entry5 = tk.Entry(root, width=10, textvariable=stock5).place(x=50, y=220)

entry6 = tk.Entry(root, width=10, textvariable=riskfree).place(x=50, y=290)

#Strings to hold output for stock possitions
one = tk.StringVar()
two = tk.StringVar()
three = tk.StringVar()
four = tk.StringVar()
five =tk.StringVar()

#Output from calculations
output1 = ttk.Label(root, width=10, textvariable=one, background="grey").place(x=150, y=100)
output2 = ttk.Label(root, width=10, textvariable=two, background="grey").place(x=150, y=130)
output3 = ttk.Label(root, width=10, textvariable=three, background="grey").place(x=150, y=160)
output4 = ttk.Label(root, width=10, textvariable=four, background="grey").place(x=150, y=190)
output5 = ttk.Label(root, width=10, textvariable=five, background="grey").place(x=150, y=220)

#Labels for the program
label1 = tk.Label(root, text='Stock Tickers').place(x=45, y=75)
label2 = tk.Label(root, text='Stock Weights').place(x=145, y=75)
label3 = tk.Label(root, text='Daily risk free rate').place(x=40, y=265)

#Calculate button to run the program commands and produce the output
button1 = ttk.Button(root, text='RUN', width=10, command=calculate).place(x=50, y=340)




root.mainloop()
