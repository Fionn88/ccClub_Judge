"""
阿偉管監獄 II

描述
承上題，監獄的生物數量變動快讓阿偉記到瘋掉了。於是聰明的阿偉決定引入總量管制，阿偉現在規定監獄只能出現最多 n 隻腳。
監獄收容兩種對象，分別為 A 和 B，腳的數量分別為 a, b。
給定 a, b, n ，請列出所有最滿(無法繼續收容生物)且總腳數小於 n 的可行組合。

輸入
給定
n a b
其中 n>a>b 且三數皆為正整數

輸出
請將組合按照 [A的數量, B的數量] 逐行列出。
排列順序為A數；B數由大至小排

輸入範例 1
4 2 1

輸出範例 1
[2, 0]
[1, 2]
[0, 4]

輸入範例 2
10 3 2

輸出範例 2
[3, 0]
[2, 2]
[1, 3]
[0, 5]
"""