# ACBCalculator
This calculator takes a CSV file of stock transaction logs and produces the report of
adjusted cost-base and gain.

Adjusted cost-base is a method to calculate rolling average price of a stock. For
example, if you buy stock 5 shares of stock A at price 100, then you buy another 5
shares of stock A at prince 200 again. Your ACB average price of stock A is
`(5*100+5*200)/(5+5)=150`. When you sell 6 shares of stock A at price 300, your gain
is `(300-150)*6=900`.

The calculator expects the following format in the CSV file:

| Date       | Stock  | Action | Unit    | Price    | Commission | Ex     |
| :--------- | :----: | :----: | :-----: | :------: | :--------: | -----: |
| 2018-05-12 | GOOG   | Buy    | 10      | 700      | 3.5        | 1      |
| 2018-07-23 | MSFT   | Buy    | 10      | 300      | 0          | 1.2    |
| 2019-11-10 | APPL   | Buy    | 5       | 200      | 2.4        | 1.3    |
| 2019-11-12 | AMZN   | Buy    | 10      | 2000     | 5.6        | 1.32   |
| 2019-11-15 | APPL   | Sell   | 2       | 210      | 0          | 1.4    |
| 2020-01-05 | APPL   | Buy    | 2       | 205      | 0          | 1.3    |
| 2020-02-02 | APPL   | Sell   | 5       | 300      | 0          | 1.23   |
| 2020-02-03 | AMZN   | Sell   | 8       | 3000     | 0          | 1.4    |
| 2020-03-12 | GOOG   | Sell   | 5       | 1700     | 0          | 1      |
| 2020-04-23 | MSFT   | Sell   | 10      | 250      | 0          | 1.2    |

* `Date` column should be in the format of `YYYY-MM-DD`.
* `Stock` column contains the stock symbol.
* `Action` column contains either `Buy` or `Sell`.
* `Unit` column contains the number of shares in that transaction.
* `Price` column contains the unit price of that stock in that transaction.
* `Ex` column is optional. It contains the exchange rate of that date. The default is `1`.

Other columns may be included in the CSV file but they'll all be ignored.

```
# Run the calculator:
$ python main.py sample.csv
# Sample output:
$ GGain: {2019: {'APPL': 66.75199999999995}, 2020: {'GOOG': 4998.25, 'AMZN': 12474.0864, 'APPL': 530.1279999999999, 'MSFT': -600.0}}
```
