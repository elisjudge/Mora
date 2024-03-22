vowels = ["あ","い","う","え","お"]
k_cons = ["か","き","く","け","こ"]
s_cons = ["さ","し","す","せ","そ"]
t_cons = ["た","ち","つ","て","と"]
n_cons = ["な","に","ぬ","ね","の"]
h_cons = ["は","ひ","ふ","へ","ほ"]
m_cons = ["ま","み","む","め","も"]
y_cons = ["や","ゆ","よ"]
r_cons = ["ら","り","る","れ","ろ"]
wa = ["わ"]
x_tsu = ["っ"]
n = ["ん"]



def get_standard_characters():
    return (vowels + k_cons + s_cons +
            t_cons + n_cons + h_cons +
            m_cons + y_cons + r_cons + 
            wa + x_tsu + n)