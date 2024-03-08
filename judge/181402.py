"""
文本相似度

描述
在文字探勘的領域中，時常使用向量空間模型（vector space model）來計算兩個文本之間的相似度。
大致概念如下：
詞向量
假設我們有兩個文本，文本A「今天|天氣|很好」，文本B「我|昨天|心情|很好|很好」。
我們可以用向量的方式來表這兩個文本，假設向量每個維度分別代表[今天, 昨天, 我, 天氣, 心情,很好]，文本A 即為 [1, 0, 0, 1, 0, 1]，文本B 則為 [0, 1, 1, 0, 1, 2]。
向量空間模型（vector space model）

當我們使用向量表示每個文本，我們就可以用向量空間模型來計算兩個文本之間的相似度。原理很直觀，我們可以直接計算兩個向量的夾角。
====
此處公式請至 judge 查看
====
兩個向量的 cos 值可以代表兩個向量的相似度，計算方式如上方公式。
分子為兩個向量的內積，分母為兩個向量的長度相乘。
文本A [1, 0, 0, 1, 0, 1] 和 文本B [0, 1, 1, 0, 1, 2] 的內積為 2
文本A [1, 0, 0, 1, 0, 1] 的長度為 根號（1^2 + 1^2 + 1^2）即 根號 3
文本B [0, 1, 1, 0, 1, 2]的長度為 根號（1^2 + 1^2 + 1^2 + 2^2）即 根號 7
因此兩者的相似度為 2/((根號3)*(根號7)) 即 0.4364357804719848
使用字典表示詞向量
實務上，為了方便起見，我們會使用字典來表示詞向量。
文本 A 為 {"今天":1, "天氣": 1, "很好":1}，文本 B 為 {"我":1, "昨天":1, "心情": 1, "很好": 2}
因為小數點會有精度問題，請分別算出
兩向量內積：dot_a_b
文本A長度：len_a
文本B長度：len_b
然後print(dot_a_b/(len_a*len_b))
請勿print(dot_a_b/len_a/len_b)

輸入
輸入有兩行，包含兩個字串，每行皆代表一個文本。每個文本內的詞會以「|」分開。

輸出
輸出為一行，包含一個浮點數，即兩個文本的相似度。

輸入範例 1
今天|天氣|很好
我|昨天|心情|很好|很好

輸出範例 1
0.4364357804719848

輸入範例 2
身材|高大|的|王建民|以四分|之|三|（|斜肩|投球|）|機制|投球|，|主戰|的|球路|為|伸卡球|（|二|縫線|快速球|）|與|滑球|，|另外|則|有|四|縫線|快速球|、|變速球|、|指叉球|等|球路|作為|陪襯|。
左投|的|郭泓志|以四分|之|三|(|斜肩|投球|)|的|姿勢|出手|，|身為|一|名|後援|投手|，|郭|的|主戰|球種|為四|縫線|速>球|和|品質|不錯|的|滑球|，|此|2|球種|合計|占|了|配球|中|超過|八成|的|比例|，|再|加上|部分|二|縫線|速球|與|少量|曲球|作為|配球|。

輸出範例 2
0.4479893351905204

輸入範例 3
球團|前|身為|兄弟象隊|，|洪家|兄弟|當時|主導|球隊|作風|以|日式|細膩|球風|為|主軸|，|更|因|常常|在|比賽|後|半段|比數|落後|時|急起直追|，|呈現出|永不|放棄|的|精神|，|加上|球團|要求|球員|為人|謙遜|不|驕傲|，|影響|及|感動|了|>許多|不同|世代|的|球迷|，|使|該隊|的|支持|者|忠誠度|從|創隊|到|現今|一直|相當|穩定|，|有百|萬象|迷之稱|。|球隊|於|兄弟象|時期|對於|球員|及|工作|人員|的|私德|及|品行|要求|需|以禮|對待|衣食父母|般|的|球迷|，|並|制定|了|相關|的|奬|懲|規範|，|當年|嚴謹|的|傳統|作風|，|經由|不同|媒介|上|的|大量|曝光|，|成為|此隊|在|許多|觀眾|間|的|共同|印象|。
義大利|統一|運動|（|義大利語|：|Risorgimento|，|意為|「|復興|」|，|故|中文|文|亦|有|譯為|「|復興|運動|」|）|是|19|世紀|至|20|世紀|初|期間|，|將|義大利|半島|內|各|個|國家|統一|為|義大利|的|政治|及|社會|過程|。|1861|年|3|月|17|號|薩丁尼亞|議會|在|都|靈|正式|宣布|義大利|王國|成立|。

輸出範例 3
0.2865633642153136

來源
ccClub Judge
"""