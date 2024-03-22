import utils.mora_pair._pair_func as pf
import utils.helper._readers as reader
import utils.helper._writers as writer
from utils.helper._general import is_hiragana, is_katakana
import os
import config


def populate_mora_pair_tables():
    mp_stats_dict, mixed_hirakata, mora_pair_errors, unknown_errors = pf.load_mora_pair_tables()
    hiragana_pairlist, katakana_pairlist = pf.load_pairlists()
    filepath = config.MORA_COUNT_COUNTS_PATH
    word_pool = []

    for file in os.listdir(filepath):
        if int(file.split("_")[0]) == 1:
            continue
        
        mora_count = int(file.split('_')[0])
        mora_word_list = reader.read_json_lines(f'{filepath}{file}')

        for line in mora_word_list:
            kana = pf.fetch_kana(line)
            kana_pairs = pf.gather_mora_pairing_list(kana)

            
            if not kana_pairs:
                mixed_hirakata.append({'word': line['word'], 'kana': line['kana'], 'mora_count': mora_count})
                mp_stats_dict['words']['mixed_hirakata_count'] += 1
                mp_stats_dict["words"]['total_count'] += 1
                continue


            if is_hiragana(kana):
                if not pf.contains_valid_mora_pairs(hiragana_pairlist, kana_pairs):
                    missing_pairs = pf.find_invalid_mora_pair(hiragana_pairlist, kana_pairs)
                    
                    for missing_pair in missing_pairs:
                        if missing_pair not in mora_pair_errors['hiragana']:
                            mora_pair_errors['hiragana'][missing_pair] = []
                            mora_pair_errors['hiragana'][missing_pair].append({'word': line['word'], 
                                                                            'kana': line['kana'], 
                                                                            'mora_count': mora_count})
                        else:
                            mora_pair_errors['hiragana'][missing_pair].append({'word': line['word'], 
                                                                            'kana': line['kana'], 
                                                                            'mora_count': mora_count})
                    mp_stats_dict['words']['unassigned_hiragana_error_count'] +=1
                    mp_stats_dict['words']['unassigned_total_error_count'] +=1
                    mp_stats_dict["words"]['total_count'] += 1


                else:
                    for kana_pair in kana_pairs:
                        hiragana_pairlist[kana_pair]['count'] += 1 
                        hiragana_pairlist[kana_pair]['words'].append({'word': line['word'], 
                                                                    'kana': line['kana'], 
                                                                    'mora_count': mora_count})
                    mp_stats_dict['words']['assigned_words'] += 1
                    mp_stats_dict['words']['wago'] += 1
                    mp_stats_dict["words"]['total_count'] += 1

                    word_pool.append({'word': line['word'],
                                'kana': line['kana'],
                                'mora_count': mora_count,
                                'kana_pairs': kana_pairs,
                                'wago': True,
                                'gairaigo': False
                                })


            elif is_katakana(kana):
                if not pf.contains_valid_mora_pairs(katakana_pairlist, kana_pairs):
                    missing_pairs = pf.find_invalid_mora_pair(katakana_pairlist, kana_pairs)
                    
                    for missing_pair in missing_pairs:
                        if missing_pair not in mora_pair_errors['katakana']:
                            mora_pair_errors['katakana'][missing_pair] = []
                            mora_pair_errors['katakana'][missing_pair].append({'word': line['word'], 
                                                                            'kana': line['kana'], 
                                                                            'mora_count': mora_count})
                        else:
                            mora_pair_errors['katakana'][missing_pair].append({'word': line['word'], 
                                                                            'kana': line['kana'], 
                                                                            'mora_count': mora_count})
                    mp_stats_dict['words']['unassigned_katakana_error_count'] +=1
                    mp_stats_dict['words']['unassigned_total_error_count'] +=1
                    mp_stats_dict["words"]['total_count'] += 1

                
                else:
                    for kana_pair in kana_pairs:
                        katakana_pairlist[kana_pair]['count'] += 1 
                        katakana_pairlist[kana_pair]['words'].append({'word': line['word'], 
                                                                    'kana': line['kana'], 
                                                                    'mora_count': mora_count})

                    word_pool.append({'word': line['word'],
                                'kana': line['kana'],
                                'mora_count': mora_count,
                                'kana_pairs': kana_pairs,
                                'wago': False,
                                'gairaigo': True
                                })
                    
                    mp_stats_dict['words']['assigned_words'] += 1
                    mp_stats_dict['words']['gairaigo'] += 1
                    mp_stats_dict["words"]['total_count'] += 1


            else:
                unknown_errors.append({'word': line['word'], 
                                    'kana': line['kana'], 
                                    'mora_count': mora_count})
                mp_stats_dict["words"]['unknown_error'] += 1
                mp_stats_dict["words"]['total_count'] += 1


        pf.write_mora_pair_files(hiragana_pairlist, katakana_pairlist, mp_stats_dict, 
                        mixed_hirakata, mora_pair_errors, unknown_errors, word_pool)


def split_pairs():
    wago_pairs = reader.read_json_file(config.HIRAGANA_PAIRLIST_PATH)
    gairaigo_pairs = reader.read_json_file(config.KATAKANA_PAIRLIST_PATH)
    mp_stats_dict = reader.read_json_file(config.MORA_PAIR_STATS)
    w_no_pairs, g_no_pairs = [], []
    w_pairs, g_pairs = [], []

    for key in wago_pairs:
        count = wago_pairs[key]["count"]
        if count == 0:
            w_no_pairs.append(key)
            mp_stats_dict["pairs"]["wago"]["no_pairs_count"] += 1
            mp_stats_dict["pairs"]["total"]["no_pairs_count"] += 1
        else:
            w_pairs.append({key: count})
            mp_stats_dict["pairs"]["wago"]["pairs_count"] += 1
            mp_stats_dict["pairs"]["total"]["pairs_count"] += 1
        mp_stats_dict["pairs"]["wago"]["total_count"] += 1
        mp_stats_dict["pairs"]["total"]["total_count"] += 1

    for key in gairaigo_pairs:
        count = gairaigo_pairs[key]["count"]
        if count == 0:
            g_no_pairs.append(key)
            mp_stats_dict["pairs"]["gairaigo"]["no_pairs_count"] += 1
            mp_stats_dict["pairs"]["total"]["no_pairs_count"] += 1
        else:
            g_pairs.append({key: count})
            mp_stats_dict["pairs"]["gairaigo"]["pairs_count"] += 1
            mp_stats_dict["pairs"]["total"]["pairs_count"] += 1
        mp_stats_dict["pairs"]["gairaigo"]["total_count"] += 1
        mp_stats_dict["pairs"]["total"]["total_count"] += 1

    write_files = [(config.MORA_PAIR_HIRAGANA_PAIRS, w_pairs), 
                    (config.MORA_PAIR_HIRAGANA_NOPAIRS, w_no_pairs),
                    (config.MORA_PAIR_KATAKANA_PAIRS, g_pairs),
                    (config.MORA_PAIR_KATAKANA_NOPAIRS, g_no_pairs),
                    (config.MORA_PAIR_STATS, mp_stats_dict)]
    
    for path, data in write_files:
        writer.write_file(path, data)


def create_valid_pairlists(hira_path = None, hira_write_path= None,
                           kata_path = None, kata_write_path = None):
    if not hira_path:
        hira_path = config.MORA_PAIR_HIRAGANA_PAIRS
        hira_write_path = config.VALID_WAGO_PATH
    if not kata_path:
        kata_path = config.MORA_PAIR_KATAKANA_PAIRS
        kata_write_path = config.VALID_GAIRAIGO_PATH
    
    wago_pairlist = {}
    gairaigo_pairlist = {}

    for line in reader.read_json_lines(hira_path):
        pair = list(line.keys())[0]
        wago_pairlist[pair] = None

    for line in reader.read_json_lines(kata_path):
        pair = list(line.keys())[0]
        gairaigo_pairlist[pair] = None

    write_files = [(hira_write_path, wago_pairlist), 
                    (kata_write_path, gairaigo_pairlist)]
    
    for path, data in write_files:
        writer.write_file(path, data)


def create_nth_percentile_pairlists():
    hira_path = config.MORA_PAIR_HIRAGANA_NTH_PCT_PAIRS
    hira_write_path = config.VALID_NTH_WAGO_PATH 
    kata_path = config.MORA_PAIR_KATAKANA_NTH_PCT_PAIRS
    kata_write_path = config.VALID_NTH_GAIRAIGO_PATH
    
    valid_hiragana, valid_katakana = pf.preprocess_load_valid_data()
    nth_hiragana = pf.fetch_top_nth_percentile_data(valid_hiragana, 10)
    nth_katakana = pf.fetch_top_nth_percentile_data(valid_katakana, 5)
    pf.write_nth_mora_pair_files(nth_hiragana, nth_katakana)

    create_valid_pairlists(hira_path = hira_path, hira_write_path= hira_write_path,
                           kata_path = kata_path, kata_write_path = kata_write_path)
    










    