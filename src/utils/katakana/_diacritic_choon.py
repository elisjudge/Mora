a_diacritic = ["ガー","ザー","ダー","バー","パー"]
a_diacritic_yoon = ["ギャー","ジャー","ヂャー","ビャー","ピャー"]
i_diacritic = ["ギー", "ジー","ヂー","ビー","ピー"]
u_diacritic = ["グー","ズー","ヅー","ブー","プー"]
u_diacritic_yoon = ["ギュー","ジュー","ヂュー","ビュー","ピュー"]
e_diacritic = ["ゲー","ゼー","デー","ベー","ペー"]
o_diacritic = ["ゴー","ゾー","ドー","ボー","ポー"]
o_diacritic_yoon = ["ギョー","ジョー","ヂョー","ビョー","ピョー"]

def get_diacritic_choon():
    return (a_diacritic + a_diacritic_yoon + i_diacritic +
            u_diacritic + u_diacritic_yoon + e_diacritic +
            o_diacritic + o_diacritic_yoon)