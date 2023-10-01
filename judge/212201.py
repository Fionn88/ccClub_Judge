"""
直線等加速度
描述

高中一年級的強強，在物理課上學到直線等加速度的三條公式，由於老師出了很多題目當作業，他覺得計算很麻煩，於是他決定用程式來協助寫作業。

直線等加速度的三條公式如下:

======
公式至 judge 查看
======
v = 速度、v0 = 初速、a = 加速度、S = 位移、t = 時間

但由於程式的計算和一般的數學式不同，要先把公式做轉換，以下是轉換後的公式：

======
公式至 judge 查看
======
 
已知所有題目都給定 v0 = 1，但不一定會給其他的參數，他認為直接依照題目給的參數，輸出所有的參數，再抄下來就好。


輸入
輸入為 1 行，為一個字串，字串中的元素依序為速度 v、加速度 a、位移 S、時間 t。



輸出
輸出為 1 行，為一個字串，包括所有的參數，皆為浮點數，順序為 v、v0、a、S、t，參數之間以逗號加空格分隔。


輸入範例 1 
,0.16,75,25

輸出範例 1
v=5.0, v0=1.0, a=0.16, S=75.0, t=25.0

輸入範例 2 
0,,2,4

輸出範例 2
v=0.0, v0=1.0, a=-0.25, S=2.0, t=4.0

提示
不用考慮進位問題
所有的測資必定有解
不一定所有公式都會用到
"""