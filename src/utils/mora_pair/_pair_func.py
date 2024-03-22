from utils.hiragana import _hiragana_sound as h_sound
from utils.mora_pair import _pair_logic as logic
from utils.helper._general import is_hiragana, is_katakana
import config
import utils.helper._writers as writer
import utils.helper._readers as reader

def gather_mora_pairing_list(kana: str) -> list:
    kana_length = len(kana)
    kana_pairs = []
    previous_mora = None
    contains_hiragana, contains_katakana = False, False
    curr_loc = 0

    while curr_loc < kana_length:
        if is_hiragana(kana[curr_loc]):
            contains_hiragana = True
            if kana[curr_loc] in h_sound.a_sounds:
                current_mora, curr_loc= logic.check_a_long_vowel(curr_loc, kana, kana_length)
            elif kana[curr_loc] in h_sound.i_sounds:
                current_mora, curr_loc= logic.check_i_long_vowel_yoon(curr_loc, kana, kana_length)
            elif kana[curr_loc] in h_sound.u_sounds:
                current_mora, curr_loc= logic.check_u_long_vowel(curr_loc, kana, kana_length)
            elif kana[curr_loc] in h_sound.e_sounds:
                current_mora, curr_loc= logic.check_e_long_vowel(curr_loc, kana, kana_length)
            elif kana[curr_loc] in h_sound.o_sounds:
                current_mora, curr_loc= logic.check_o_long_vowel(curr_loc, kana, kana_length)
            else:
                current_mora = kana[curr_loc]  
                curr_loc = curr_loc + len(current_mora)
        elif is_katakana(kana[curr_loc]):
            contains_katakana = True
            current_mora, curr_loc= logic.check_katakana_long_vowel_yoon(curr_loc, kana, kana_length)
        
        if not previous_mora:
            previous_mora = current_mora
        else:
            current_pair = previous_mora + current_mora
            kana_pairs.append(current_pair)
            previous_mora = current_mora   
        
        if contains_hiragana and contains_katakana:
            return False
        
    if len(kana_pairs) == 0:
        kana_pairs.append(previous_mora)
    return kana_pairs  


def write_mora_pair_files(hiragana_pairlist, katakana_pairlist, mp_stats_dict, 
                          mixed_hirakata, mora_pair_errors, unknown_errors, words):

    write_files = [(config.HIRAGANA_PAIRLIST_PATH, hiragana_pairlist), 
                    (config.KATAKANA_PAIRLIST_PATH, katakana_pairlist),
                    (config.MORA_PAIR_STATS, mp_stats_dict),
                    (config.MORA_PAIR_MIXED, mixed_hirakata),
                    (config.MORA_PAIR_UNASSIGNED, mora_pair_errors),
                    (config.MORA_PAIR_UNKNOWN, unknown_errors),
                    (config.WORDPOOL_TEMP_PATH, words)]
    
    for path, data in write_files:
        writer.write_file(path, data)


def fetch_kana(line):
        if len(line["kana"]) == 0:
            return line["word"]
        else:
            return line["kana"]


def contains_valid_mora_pairs(pairlist, kana_pairs):
    return all(pair in pairlist for pair in kana_pairs)


def find_invalid_mora_pair(pairlist, kana_pairs):
    return [pair for pair in kana_pairs if pair not in pairlist]


def load_mora_pair_tables():
    mp_stats_dict = {"pairs": {"total": {"total_count": 0, "no_pairs_count": 0, "pairs_count": 0}, 
        "wago": {"total_count": 0, "no_pairs_count": 0, "pairs_count": 0},
        "gairaigo": {"total_count": 0, "no_pairs_count": 0, "pairs_count": 0}},
    "words": {
        "total_count": 0, "assigned_words": 0, "wago": 0, "gairaigo": 0, "mixed_hirakata_count": 0,
        "unassigned_total_error_count": 0, "unassigned_hiragana_error_count": 0, "unassigned_katakana_error_count": 0,
        "unknown_error": 0}
        }
    
    mixed_hirakata = []
    mora_pair_errors = {'hiragana': {}, 'katakana': {}}
    unknown_errors = []
    
    return mp_stats_dict, mixed_hirakata, mora_pair_errors, unknown_errors

def load_wordlist():
    return reader.read_json_lines(config.WORDPOOL_TEMP_PATH)


def load_pairlists():
    hiragana = reader.read_json_file(config.HIRAGANA_PAIRLIST_PATH)
    katakana = reader.read_json_file(config.KATAKANA_PAIRLIST_PATH)
    return hiragana, katakana


def preprocess_load_valid_data():
    valid_hiragana, valid_katakana = load_valid_pair()
    valid_hiragana = sort_valid_pairs(valid_hiragana)
    valid_katakana = sort_valid_pairs(valid_katakana)
    return valid_hiragana, valid_katakana


def load_valid_pair() -> list:
    hiragana = reader.read_json_file(config.MORA_PAIR_HIRAGANA_PAIRS) 
    katakana = reader.read_json_file(config.MORA_PAIR_KATAKANA_PAIRS) 
    return hiragana, katakana


def sort_valid_pairs(valid_pair_list:list) -> list:
    return sorted(valid_pair_list, key=lambda x: list(x.values())[0], 
                  reverse=True)


def fetch_top_nth_percentile_data(sorted_list:list, score) -> list:
    return [line for line in sorted_list if list(line.values())[0] >= score] 


def write_nth_mora_pair_files(nth_hiragana, nth_katakana):
    write_files = [(config.MORA_PAIR_HIRAGANA_NTH_PCT_PAIRS, nth_hiragana), 
                    (config.MORA_PAIR_KATAKANA_NTH_PCT_PAIRS, nth_katakana)]
    for path, data in write_files:
        writer.write_file(path, data)