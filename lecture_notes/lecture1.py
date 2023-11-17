

import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
df.to_csv('qan_stk_prc.csv')

a = 2
b = 5 ** a

x = 1
x = x + 1





