ka_v = ["ヴァ", "ヴィ", "ヴ", "ヴェ", "ヴォ"]
ka_w = ["ウィ", "ウェ", "ウォ"]
ka_f = ["ファ", "フィ", "フェ", "フォ"]
ka_che = ["チェ"] 
ka_didu = ["ディ", "ドゥ"] 
ka_titu = ["ティ", "トゥ"]
ka_je = ["ジェ"]
ka_she = ["シェ"]


### TO ADD
ka_fyu = ["フュ"]
ka_dyu = ["デュ"]
ka_tyu = ["テュ"]
ka_twi = ["ツァ","ツィ", "ツェ", "ツォ"]
ka_kw = ["クァ"]

def get_foreign_sounds():
    return (ka_v + ka_w + ka_f + ka_che +
            ka_didu + ka_titu + ka_je + ka_she +
            ka_fyu + ka_dyu + ka_tyu + ka_twi + ka_kw)