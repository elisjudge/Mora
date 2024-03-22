a_diacritic = ["があ","ざあ","だあ","ばあ","ぱあ"]
a_diacritic_yoon = ["ぎゃあ","じゃあ","ぢゃあ","びゃあ","ぴゃあ"]
i_diacritic = ["ぎい", "じい","ぢい","びい","ぴい"]
u_diacritic = ["ぐう","ずう","づう","ぶう","ぷう"]
u_diacritic_yoon = ["ぎゅう","じゅう","ぢゅう","びゅう","ぴゅう"]
e_diacritic = ["げえ","ぜえ","でえ","べえ","ぺえ",
               "げい","ぜい","でい","べい","ぺい"]
o_diacritic = ["ごお","ぞお","どお","ぼお","ぽお",
               "ごう","ぞう","どう","ぼう","ぽう"]
o_diacritic_yoon = ["ぎょお","じょお","ぢょお","びょお","ぴょお",
                    "ぎょう","じょう","ぢょう","びょう","ぴょう"]

def get_diacritic_choon():
    return (a_diacritic + a_diacritic_yoon + i_diacritic +
            u_diacritic + u_diacritic_yoon + e_diacritic +
            o_diacritic + o_diacritic_yoon)