vowels = ["ア","イ","ウ","エ","オ"]
k_cons = ["カ","キ","ク","ケ","コ"]
s_cons = ["サ","シ","ス","セ","ソ"]
t_cons = ["タ","チ","ツ","テ","ト"]
n_cons = ["ナ","ニ","ヌ","ネ","ノ"]
h_cons = ["ハ","ヒ","フ","ヘ","ホ"]
m_cons = ["マ","ミ","ム","メ","モ"]
y_cons = ["ヤ","ユ","ヨ"]
r_cons = ["ラ","リ","ル","レ","ロ"]
wa = ["ワ", "ヲ"]
x_tsu = ["ッ"]
n = ["ン"]
long_vowel = ["ー"]

def get_standard_characters():
    return (vowels + k_cons + s_cons +
            t_cons + n_cons + h_cons +
            m_cons + y_cons + r_cons + 
            wa + x_tsu + n
            + long_vowel)