from utils.hiragana import _diacritic_choon as hdc
from utils.hiragana import _standard_choon as hsc
from utils.hiragana import _hiragana_yoon_lr as h_yoon_lr
from utils.katakana import _katakana_yoon_lr as k_yoon_lr
from utils.katakana import _diacritic_choon as kdc
from utils.katakana import _standard_choon as ksc
from utils.katakana import _foreign_sound_choon as kfsc

h_long_yoon = (hsc.a_yoon + hsc.u_yoon + hsc.o_yoon + 
               hdc.a_diacritic_yoon + hdc.u_diacritic_yoon + hdc.o_diacritic_yoon)

k_long_yoon = (ksc.a_yoon + ksc.u_yoon + ksc.o_yoon + 
               kdc.a_diacritic_yoon + kdc.u_diacritic_yoon + kdc.o_diacritic_yoon +
               kfsc.get_foreign_choon_sounds())

def check_a_long_vowel(curr_loc, kana, kana_length):
    mora = kana[curr_loc]
    next_loc = curr_loc + 1
    
    if next_loc < kana_length: 
        if kana[next_loc] == 'あ':
            mora = kana[curr_loc:next_loc + 1]

    new_curr_loc = curr_loc + len(mora)
    return mora, new_curr_loc


def check_i_long_vowel_yoon(curr_loc, kana, kana_length):
    mora = kana[curr_loc]
    next_loc = curr_loc + 1
    next_next_loc = curr_loc + 2
    
    if next_loc < kana_length: 
        if kana[next_loc] == 'い' or kana[next_loc] in h_yoon_lr.h_yoon_r:
            mora = kana[curr_loc:next_loc + 1]
        
        if next_next_loc < kana_length:
            if kana[curr_loc:next_next_loc + 1] in h_long_yoon:
                mora = kana[curr_loc:next_next_loc + 1]

    new_curr_loc = curr_loc + len(mora)
    return mora, new_curr_loc
    

def check_u_long_vowel(curr_loc, kana, kana_length):
    mora = kana[curr_loc]
    next_loc = curr_loc + 1
    if next_loc < kana_length: 
        if kana[next_loc] == 'う':
            mora = kana[curr_loc:next_loc + 1]
      
    new_curr_loc = curr_loc + len(mora)
    return mora, new_curr_loc


def check_e_long_vowel(curr_loc, kana, kana_length):
    mora = kana[curr_loc]
    next_loc = curr_loc + 1
    if next_loc < kana_length: 
        if kana[next_loc] in ["え", "い"]:
            mora = kana[curr_loc:next_loc + 1]

    new_curr_loc = curr_loc + len(mora)
    return mora, new_curr_loc

    
def check_o_long_vowel(curr_loc, kana, kana_length):
    mora = kana[curr_loc]
    next_loc = curr_loc + 1
    if next_loc < kana_length: 
        if kana[next_loc] in ["お", "う"]:
            mora = kana[curr_loc:next_loc + 1]

    new_curr_loc = curr_loc + len(mora)
    return mora, new_curr_loc


def check_katakana_long_vowel_yoon(curr_loc, kana, kana_length):
    mora = kana[curr_loc]
    next_loc = curr_loc + 1
    next_next_loc = curr_loc + 2
    if next_loc < kana_length: 
        if kana[next_loc] == 'ー' or kana[next_loc] in k_yoon_lr.k_yoon_r:
            mora = kana[curr_loc:next_loc + 1] 
        if next_next_loc < kana_length: 
            if kana[curr_loc:next_next_loc + 1] in k_long_yoon:
                mora = kana[curr_loc:next_next_loc + 1]
        

    new_curr_loc = curr_loc + len(mora)
    return mora, new_curr_loc


