#!/user/bin/python
import datetime
import pandas
import sys

def main():
    if len(sys.argv) <= 0 or len(sys.argv) >2:
        sys.exit("Usage: python main.py [filename.csv]")
    data = pandas.read_csv(sys.argv[1])
    data.sort_values('Date')
    # acb stores a map of stock->(avg_price, total_unit)
    acb = {}
    # gain stores a map of year->{stock->gain}
    gain = {}
    for index, row in data.iterrows():
        date =  datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        stock = row['Stock']
        action = row['Action']
        unit = float(row['Unit'])
        price = float(row['Price'])
        ex = 1.0
        comm = 0.0
        if 'Ex' in row:
            ex = float(row['Ex'])
        if 'Commission' in row:
            comm = float(row['Commission'])
        print('Processing: {}, {}, {}, {}, {}, {}, {}'.format(date, stock, action, unit, price, comm, ex))
        if action == 'Buy':
            up = (price*unit+comm)*ex/unit
            n = (up, unit)
            if stock in acb.keys():
                cur = acb[stock]
                acb[stock] = ((cur[0]*cur[1]+n[0]*n[1])/(cur[1]+n[1]), cur[1]+n[1])
            else:
                acb[stock] = n
        elif action == 'Sell':
            if stock in acb.keys():
                cur = acb[stock]
                if cur[1] < unit:
                    sys.exit('Selling more than existing for stock {} on date {}'.format(stock, date))
                g = (price*ex-cur[0])*unit-comm*ex
                if date.year not in gain.keys():
                    gain[date.year] = {}
                if stock in gain[date.year].keys():
                    gain[date.year][stock] = g + gain[date.year][stock]
                else:
                    gain[date.year][stock] = g
                acb[stock] = (cur[0], cur[1]-unit)
            else:
                sys.exit('No info of previous Buy of stock {} on date {}'.format(stock, date))
        else:
            sys.exit('Action must be either Buy or Sell; got {} on date {}'.format(action, date))
    print ''
    # print('Rolling ACB: {}'.format(acb))
    print('Gain: {}'.format(gain))


if __name__ == "__main__":
    main()
