from utils.pairlist import _pairlist as pl

import config 
import os

import utils.dictionary._frequency as freq
import utils.helper._exists as exists
import utils.helper._readers as reader
import utils.helper._random as rand
import utils.helper._writers as writer
import utils.mora_count.counter as mc
import utils.mora_pair.mora_pair as mp


def create_mora_counts():
    mc.mora_counter()


def compute_mora_pairs():
    mp.populate_mora_pair_tables()
    mp.split_pairs()


def create_pairlists():
    pl.create_pairlist()


def build_frequency_dictionary():
    freq.build_frequency_dict()


def get_frequencies():
    freq.fetch_frequencies()


def write_valid_pairlists():
    mp.create_valid_pairlists()


def load_temp_wordpool():
    return reader.read_json_file(config.WORDPOOL_TEMP_PATH)


def load_wordpool():
    return reader.read_json_file(config.WORDPOOL_PATH)


def generate_ranked_unranked_pools(wordpool):
    ranked_pool = {}
    unranked_pool = {}

    r_i = 0
    ur_i = 0
    for value in wordpool.values():
        if value['rank'] != 'N/A':
            ranked_pool[r_i] = value
            r_i += 1
        else:
            unranked_pool[ur_i] = value
            ur_i += 1

    write_files = [(config.RANKED_POOL_PATH, ranked_pool), 
                (config.UNRANKED_POOL_PATH, unranked_pool)]

    for path, data in write_files:
        writer.write_file(path, data)


def finalize_wordpool():
    word_pool = {}
    temp_pool = load_temp_wordpool()
    word_pool_stats = initialize_wordpool_stats()
    remaining_nwords = len(temp_pool)
    pool_index = 0

    while remaining_nwords > 0:
        pos = rand.get_random_int(min_value = 0, 
                                  max_value = remaining_nwords - 1)

        line = temp_pool.pop(pos)
        word_pool[pool_index] = line
        calculate_stats(line, word_pool_stats)
        pool_index += 1
        remaining_nwords -= 1

    write_files = [(config.WORDPOOL_PATH, word_pool), 
                    (config.WORDPOOL_STATS_PATH, word_pool_stats)]

    for path, data in write_files:
        writer.write_file(path, data)


def initialize_wordpool_stats() -> dict:
    return {
        'total': 0,
        'n_ranked': 0,
        'n_wago': 0,
        'n_ranked_wago': 0,
        'n_gairaigo': 0,
        'n_ranked_gairaigo': 0
    }


def calculate_stats(line:dict, word_pool_stats:dict):
    if line["rank"] != "N/A":
        word_pool_stats["n_ranked"] += 1
        if line["wago"] == True:
            word_pool_stats["n_wago"] += 1
            word_pool_stats["n_ranked_wago"] += 1
        
        elif line['gairaigo'] == True:
            word_pool_stats["n_gairaigo"] += 1
            word_pool_stats["n_ranked_gairaigo"] += 1
    else:
        if line["wago"] == True:
            word_pool_stats["n_wago"] += 1
        
        elif line['gairaigo']== True:
            word_pool_stats["n_gairaigo"] += 1
    word_pool_stats['total'] += 1

def delete_temp_wordpool():
    os.remove(config.WORDPOOL_TEMP_PATH)


def is_wordpool():
    return exists.path_exists(config.WORDPOOL_PATH)
