# Analysis-of-stock-prices
tech assessment for interview
You are an analyst at Maria Artichokes(MA). 
As with any company, MA has had some very good times as well as some bad ones. 
You are responsible for conducting trending analysis of the stock prices for MA, and you want to determine the largest decline in stock prices over various time spans.
For example, if over a span of time the stock prices were 19, 12, 13, 11, 20 and 14, then the largest decline would be 8 between the first and fourth price.
If the last price had been 10 instead of 14, then the largest decline would have been 10 between the last two prices. 
You have done some previous analyses and have found that the stock price over any period of time can be modelled reasonably accurately 
with the following equation: price(k) = p · (sin(a · k + b) + cos(c · k + d) + 2) Where p, a, b, c and d are constants. 
You would like you to write a program to determine the largest price decline over a given sequence of prices. 
You have to consider the prices only for integer values of k.

The input consists of a single line containing 6 integers p (1 ≤ p ≤ 1000), a, b, c, d (0 ≤ a, b, c, d ≤ 1000) and n (1 ≤ n ≤ 106 ). 
The sequence of stock prices to consider is price (1), price (2), . . ., price (n).

Result:
Display the maximum decline in the stock prices. 
If there is no decline, display the number 0. Your output should have an absolute or relative error of at most 10^−6.

Test 1
42 1 23 4 8 10

Expected output (1)
104.855110

Test 2
100 7 615 998 801 3

Expected output (2)
0.000000
