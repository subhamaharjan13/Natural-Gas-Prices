import pandas as pd
import csv
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from datetime import datetime, date, timedelta


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def main(argv):
    r = urlopen("https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm")
    # This line opens the webpage
    soup = BeautifulSoup(r, 'lxml')
    # uses Beautiful soup to get all page source

    table = soup.findAll("table", attrs={"cellpadding": "2"})[0]
    # used to find the table with the attribute cellpadding=2
    # TODO: confusion on use of [0]

    csvFile = open("extracted_data.csv", 'w')
    # opens a file "extracted_data.csv" in write mode.
    # If the file exists then the previous data is deleted.
    # If the file doesn't exist then new file is created.

    for tr in table.findAll("tr"):
        # find all the tr in the table object(variable) that was created
        csvRow = []
        for th in tr.findAll("th"):
            writer = csv.writer(csvFile)
            csvRow.append(th.get_text().strip().replace(
                '-', ' ').replace('  ', ' '))
        for td in tr.findAll("td"):
            writer = csv.writer(csvFile)
            csvRow.append(td.get_text().strip().replace(
                '-', ' ').replace('  ', ' '))
        print(csvRow)
        writer.writerow(csvRow)
        # use writer to write in the data in csvRow to the csvFile
    csvFile.close()
    # closes the file open in csvFile object.

    df = pd.read_csv('extracted_data.csv')
    df.dropna(axis=0, how='all', inplace=True)
    # since there were multiple empty lines in the extracted data.
    # removing the rows if all the data cell are empty.
    # axis=0 === says that we are selecting rows whereas axis=1 means columns.
    # how='all' === says to remove the row only if all data are missing.
    # inplace=True === says to make and save edits to the same dataframe.
    df.reset_index(inplace=True, drop=True)
    # resets the index to serialize the index order where some values were missing due to deleted rows from previous lines.
    dd = df.iloc[:, 1:7]
    # .iloc[] is primarily integer position based (from 0 to length-1 of the axis), but may also be used with a boolean array.
    # from the df DataFrame selecting all the rows and columns 1,2,3,4,5,6( since in 1:7, 7 is exclusive).
    # and storing the result in a new DataFrame dd

    vals = []
    days = []
    # variables to store the values of columns for required dataframe format.
    for x in dd.index:
        vals.append(df['Mon'][x])
        vals.append(df['Tue'][x])
        vals.append(df['Wed'][x])
        vals.append(df['Thu'][x])
        vals.append(df['Fri'][x])

        review_date = df['Week Of'][x]
        review_date = review_date.split()

        y = []
        for date_list in review_date:
            if (date_list == "to"):
                continue
            else:
                y.append(date_list)

        min_date = y[0] + " " + y[1] + " " + y[2]

        begin_object = datetime.strptime(min_date, "%Y %b %d")
        # print(begin_object)

        end_object = begin_object + timedelta(days=5)
        # print(end_object)

        for single_date in daterange(begin_object, end_object):
            date_oneval = single_date.strftime("%Y %m %d %a")
            days.append(date_oneval)

    data = [list(x) for x in zip(days, vals)]
    # print(data)

    final_data = pd.DataFrame(
        data, columns=['Date', 'Dollars per Million Btu'])
    final_data.to_csv('new_req.csv', index=True)


if (__name__ == "__main__"):
    main(sys.argv)
