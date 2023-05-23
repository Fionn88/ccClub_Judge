"""
不知道要輸入幾行
描述

在設計程式的時候，如果知道輸入的長相，包含會有幾行、每行有幾個字等等，那會是最好的，因為我們可以根據這些規律去設計我們要怎麼接收輸入。但真實情況往往不是這樣，常常我們會不知道輸入是什麼，甚至是輸入有幾行，請設計一個程式來處理這樣的輸入，並且用「-」連結各行的輸入再輸出。

輸入
輸入有若干行。

輸出
輸出有一行，請用「-」連結各行的輸入。


輸入範例 1 
HoydeA
象牙舟
5:10a.m.
視線所及只剩生活
你終究不愛這世界

輸出範例 1
HoydeA-象牙舟-5:10a.m.-視線所及只剩生活-你終究不愛這世界

輸入範例 2 
怎麼了
咩噗
你好不好
以後別做朋友
如果雨之後
永不失聯的愛
我很快樂
愛情教會我的事

輸出範例 2
怎麼了-咩噗-你好不好-以後別做朋友-如果雨之後-永不失聯的愛-我很快樂-愛情教會我的事
"""
s = ''
count = 0
while True:
  try:
    user_input = input()
    if count == 0:
      s += user_input
    else:
      s += '-'+user_input
    count += 1
  except:
    break

print(s)
