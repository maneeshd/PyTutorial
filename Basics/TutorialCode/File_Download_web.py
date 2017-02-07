"""
@author: Maneesh D
@email: maneeshd77@gmail.com
Historical Stock Price Data of Google in CSV
"""

from urllib import request


def down_stock_historical_prices(csv_url):
    resp = request.urlopen(csv_url)
    csv = resp.read().decode()
    lines = csv.split("\\n")
    with open("GOOG.csv", "w") as fw:
        for line in lines:
            fw.write(line + "\n")


def main():
    goog_url = "http://real-chart.finance.yahoo.com/table.csv?s=GOOG&a=07&b=19&c=2004&d=01&e=7&f=2017&g=d&ignore=.csv"
    down_stock_historical_prices(goog_url)

if __name__ == '__main__':
    main()
