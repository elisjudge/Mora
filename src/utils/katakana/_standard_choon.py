a_standard = ["アー","カー","サー","ター","ナー",
              "ハー","マー","ヤー","ラー","ワー"]
a_yoon = ["キャー","シャー","チャー","ニャー",
          "ヒャー","ミャー","リャー"]
i_standard = ["イー","キー","シー","チー",
              "ニー","ヒー", "ミー","リー"]
u_standard = ["ウー","クー","スー","ツー","ヌー",
              "フー","ムー","ユー","ルー"]
u_yoon = ["キュー","シュー","チュー","ニュー",
          "ヒュー","ミュー","リュー"]
e_standard = ["エー","ケー","セー","テー","ネー","ヘー","メー","レー"]           
o_standard = ["オー","コー","ソー","トー","ノー","ホー","モー","ヨー","ロー"]
o_yoon = ["キョー","ショー","チョー","ニョー","ヒョー","ミョー","リョー"]

def get_standard_choon():
    return (a_standard + a_yoon + i_standard +
            u_standard + u_yoon + e_standard +
            o_standard + o_yoon)