"""
綜合2-4：計算機 again
描述

給定一個字串 s ，代表希望計算的運算式。內容包含加減乘除四種運算符號（由左至右，先乘除，後加減）以及數字，數字與運算符號之間可能有「數個空格」或「沒有空格」。

請計算運算式 s 的結果，並將其印出，輸出值的型態請使用 float 浮點數。


輸入
輸入為一行，包含一個字串s


輸出
輸出為一行，包含一個浮點數


輸入範例 1 
-1.5 +-2.5 *   -3.5 /2

輸出範例 1
2.875

輸入範例 2 
   -1     --3.5/   2
   
輸出範例 2
0.75

來源
ccClub Judge
"""
s = input()
print(float(eval(s)))
