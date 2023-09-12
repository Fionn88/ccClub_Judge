"""
凱凱打棒球
描述

凱凱是個棒球鐵粉，時常跟著職棒場上的球星巡迴各地球場，不同於多數球迷，凱凱進場看球時不會跟著啦啦隊一起應援，而是緊盯著場上的打擊者，記錄著他們擊球的方向，以歸類每位打擊者的擊球習慣。

在棒球場上，若從捕手（C）、投手（P）、中外野手（CF）的連線切一刀，如下圖所示，可以將球場分成左半邊（SS、3B、LF）和右半邊（RF、2B、1B）。擊球習慣則大致可以分成拉打（順向攻擊）和推打（反向攻擊）兩種，慣用手為右手的右打者將球打到左半邊（SS、3B、LF）為拉打，打到右半邊（RF、2B、1B）則為推打。反之，慣用手為左手的左打者將球打到左半邊（SS、3B、LF）為推打，打到右半邊（RF、2B、1B）則為拉打。

截圖 2021-03-15 下午4.43.53.png


輸入
輸入有兩行

第一行有一個英文字母 R 或 L，代表打擊者慣用手，R 代表右打者，L 則代表左打者。

第二行是一個字串，代表著擊球位置（1B、2B、SS、3B、LF、RF 其中一種）。


輸出
輸出有一行，依照打擊者慣用手和擊球位置，判斷打擊結果為拉打還是推打。


輸入範例 1 

R
SS
輸出範例 1

拉打
輸入範例 2 

R
RF
輸出範例 2

推打
輸入範例 3 

L
1B
輸出範例 3

拉打
輸入範例 4 

L
3B
輸出範例 4

推打
"""