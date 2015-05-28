# Markowitz-OBX
Simple program that downloads stock data for stocks notet on OBX by requesting the data from www.netfonds.no, and uses the 
Markowitz mean variance framework to generate optimal portfolio weights

This program only works with stocks notet on OBX and not on Oslo Axess. The program handels missing values vell, but can
create some problems when the stocks history have large variations in available data due to beeing notet at different times.

The program does not yet have an option to select start and end dates of the data, and just uses all the close prices that
are available.
