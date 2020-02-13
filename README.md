# Natural Gas Prices 

# Henry Hub Natural Gas Spot Price(Dollars per Million BTU)

## Criteria

- Prices should be Henry Hub gas prices. Use EIA data here: http://www.eia.gov/dnav/ng/hist/rngwhhdm.htm
- Main data wanted is daily prices
- Resulting CSV should have two columns: Date and Price.

**_For more description and criteria's to complete the project,go through the gist https://gist.github.com/rufuspollock/f295e6d2fd6fecb705ff_**

## Libraries Used

- Pandas: _to express the data in a structural way_
- Beautiful Soup: _for parsing html and xml documents_
- CSV : _to export the data to the csv file_
- URLLIB: _to open the url and read the data_
- Datatime: _to manipulate dates and times_

## How to get the data and convert it into csv

- Using `URLLIB` to open the url in webpage.
- Using `Beautiful Soup` to get and extract all page source code.
- Using `CSV` to create a csv file and exporting the data to the file.
- Using `pandas` to remove rows with null values and reading the csv file created while extracting table from the webpage and creating a new dataframe to manipulate data and produce final csv file.
- Using `Datetime` to splitting the date string and putting it into a structured format in the dataframe.
- Setting the two columns {Date, Price} in a final csv file and retrieving the data from the new dataframe to the final csv file.

## Run The Script

To run the script, go to the terminal and use the command:
\$ python datap.py

- This creates two csv file.
  - One is the initial csv file from the source page.
  - Another is the required csv file based on the criteria.


