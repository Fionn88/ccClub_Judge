"""
小雷愛攀岩 II
描述

呈上，小雷很感謝你幫他判斷出每面牆有的路線，他也決定好自己要爬的路線等級了，不過，對於昨天熬夜寫報告的小雷來說，沒有精力再看岩點想要怎麼爬了，所以他希望你能直接告訴他應該要怎麼爬，將小雷指定的路線座標位置直接報給小雷聽，讓他當小廢物吧！

注意：

輸入的牆面左下角座標為 (0,0)，接著往右的話為 (0,1)，往上為 (1,0)以此類推，所以 (1,3) 代表由下面數上來的第二列，由左至右的第四個岩點
若同一列有大於一個指定等級的路線，則先跟小雷說要怎麼橫移（先輸出同一列的座標），才跟他說往上的下一個岩點在哪（再輸出下一列的座標）
若該牆面沒有指定的岩點路線，則輸出 'Not a valid route'

輸入
第 1 列為小雷指定的等級，輸入格式會是 'Vx'，x = 0 ~ 8

第 2 列開始為牆面，牆面上的每個數字都是一個岩點，岩點上的數字為其岩點的等級，牆面的長寬一樣不會超過 10

注意：

牆面為不定行輸入，終止條件為不輸入（白話文：就是一個空字串啦）

輸出
1. 輸出型態應為 list

2. list 中為小雷應攀爬的岩點順序

3. 若該牆面沒有指定的岩點路線，則輸出 'Not a valid route'


輸入範例 1 
V2
34526
56562
34263
32671
12364

輸出範例 1
[(0, 1), (1, 1), (2, 2), (3, 4), (4, 3)]

輸入範例 2 
V2
34526
56562
34223
32671
12364

輸出範例 2
[(0, 1), (1, 1), (2, 2), (2, 3), (3, 4), (4, 3)]

提示

以 sample 1 來說，其具體的路線圖像及座標如下圖所示，因起點為第 0 列，因此要從下方的對應路線座標開始輸出，一直到最後的 (4,  3)。

=======
圖片請至 judge 查看
=======
另以 sample 2 來說，在第 2 列的時候可以發現到有兩的位置都有 "2"，因此要先輸出靠左邊的 (2, 2)，才輸入在右方的 (2, 3)，再往第三列移動。
"""

level = input().replace('V', '')

points = []
while True:
    s = input()
    if s == '':
        break
    else:
        points.append([i for i in s])
# 確認路線
check = True
for i in points:
    if level not in i:
        check = False
        print('Not a valid route')
        break

if check:
    # 取得點座標
    route = []
    for i in range(len(points)):
        for j in range(len(points[i])):
            if points[i][j] == level:
                route.append((len(points)-1-i, j))

    route.sort()
    print(route)
