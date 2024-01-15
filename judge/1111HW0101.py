"""
阿偉當助教 I

描述
阿偉是通識課的助教，教授要他登記上課有發言的同學以利加分，班上同學的代號用26個英文字母代替。
阿偉登記小寫字母表示發言一次加一分，若是登記大寫字母表示發言內容很有價值加兩分。
阿偉還做了一些註記有關教授的特殊指令，請幫阿偉算出所有人的成績，並幫他標註特殊指令的位置吧。

輸入
輸入只有 1 行，出現的字有可能是英文字或特殊符號。長度不定。

輸出
輸出為兩個 list：
第一個 list 紀錄每個人的分數，形式為[['小寫字母', 分數], ...]。按照字母序排序，若那個人發言次數為 0 則不印出。
第二個 list 紀錄老師的特殊指令，形式為[('特殊符號', 位置), ...]。位置是他在這個字串的 Index。
若上述 list 為空則不印出。

輸入範例 1
hlzakdhoybzeow\uytQWCN?K///jhg

輸出範例 1
[['a', 1], ['b', 1], ['c', 2], ['d', 1], ['e', 1], ['g', 1], ['h', 3], ['j', 1], ['k', 3], ['l', 1], ['n', 2], ['o', 2], ['q', 2], ['t', 1], ['u', 1], ['w', 3], ['y', 2], ['z', 2]]
[('\', 14), ('?', 22), ('/', 24), ('/', 25), ('/', 26)]

輸入範例 2
AAAAAAAAAAAAAAAAAAA

輸出範例 2
[['a', 38]]
"""