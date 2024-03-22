import config
import experiment._result_gen as rg
import os
import utils.mora_pair.mora_pair as mora_pair
import utils.helper._random as rand
import utils.helper._writers as writer
import utils.helper._readers as reader


def generate_random_trial_seeds(n_trials = 100):
    seed = config.SEED
    random_trial_seeds = rand.generate_random_trial_seeds(seed, n_trials)
    writer.write_file(config.TRIAL_SEEDS_PATH, random_trial_seeds)


def generate_random_word_locations(trial_seed, n_words):
    random_word_seeds = rand.generate_random_word_seeds(trial_seed, n_words)
    writer.write_file(config.WORD_LOCATIONS_PATH, random_word_seeds)


def load_trial_seeds():
    return reader.read_json_lines(config.TRIAL_SEEDS_PATH)


def load_word_locations():
    return reader.read_json_lines(config.WORD_LOCATIONS_PATH)


def delete_word_location():
    os.remove(config.WORD_LOCATIONS_PATH)

def get_number_words():
    stats = reader.read_json_file(config.WORDPOOL_STATS_PATH)
    return stats['total']

def get_number_ranked_words():
    stats = reader.read_json_file(config.WORDPOOL_STATS_PATH)
    return stats['n_ranked']


def initialize_result_stats():
    return {
        'hiragana': {
            'word_list': None,
            'list_length': 0,
            'average_normalized_frequency': 0,
            'average_ranking': 0,
            'average_mora_length': 0,
            'unranked_words': 0,
            'unranked_prop': 0
        },
        'katakana': {
            'word_list': None,
            'list_length': 0,
            'average_normalized_frequency': 0,
            'average_ranking': 0,
            'average_mora_length': 0,
            'unranked_words': 0,
            'unranked_prop': 0
        },
    }

def load_pairlists():
    wago_pairlist = reader.read_json_file(config.VALID_WAGO_PATH)
    gairaigo_pairlist = reader.read_json_file(config.VALID_GAIRAIGO_PATH)
    return wago_pairlist, gairaigo_pairlist


def create_nth_pairlists():
    mora_pair.create_nth_percentile_pairlists()


def load_nth_pairlists():
    wago_pairlist = reader.read_json_file(config.VALID_NTH_WAGO_PATH)
    gairaigo_pairlist = reader.read_json_file(config.VALID_NTH_GAIRAIGO_PATH)
    return wago_pairlist, gairaigo_pairlist


def load_wordpool():
    return reader.read_json_file(config.WORDPOOL_PATH)


def load_ranked_wordpool():
    return reader.read_json_file(config.RANKED_POOL_PATH)


def load_unranked_wordpool():
    return reader.read_json_file(config.UNRANKED_POOL_PATH)


def load_nth_ranked_wordpool():
    return reader.read_json_file(config.RANKED_NTH_POOL_PATH)


def load_nth_unranked_wordpool():
    return reader.read_json_file(config.UNRANKED_NTH_POOL_PATH)


def create_nth_wordpools():
    ranked_word_pool = load_ranked_wordpool()
    unranked_word_pool = load_unranked_wordpool()
    wago_pairlist, gairaigo_pairlist = load_nth_pairlists()

    ranked_items_to_remove = []
    unranked_items_to_remove = []

    for key, value in ranked_word_pool.items():
        for pair in value['kana_pairs']:
            if pair not in wago_pairlist and pair not in gairaigo_pairlist:
                ranked_items_to_remove.append((key, pair))

    for key, value in unranked_word_pool.items():
        for pair in value['kana_pairs']:
            if pair not in wago_pairlist and pair not in gairaigo_pairlist:
                unranked_items_to_remove.append((key, pair))


    for key, pair in ranked_items_to_remove:
        ranked_word_pool[key]['kana_pairs'].remove(pair)

    for key, pair in unranked_items_to_remove:
        unranked_word_pool[key]['kana_pairs'].remove(pair)

    writer.write_file(config.RANKED_NTH_POOL_PATH, ranked_word_pool)
    writer.write_file(config.UNRANKED_NTH_POOL_PATH, unranked_word_pool)



def add_word_to_pairlist(word_location:str, wordpool:dict, wago_pairlist:dict, gairaigo_pairlist:dict):
    line = wordpool[word_location]
    pairs = line['kana_pairs']
    if line['wago']:
        for pair in pairs:
            if wago_pairlist[pair] is None:
                wago_pairlist[pair] = line
    elif line['gairaigo']:
        for pair in pairs:
            if gairaigo_pairlist[pair] is None:
                gairaigo_pairlist[pair] = line


   

def is_pairlists_full(wago_pairlist:dict, gairaigo_pairlist:dict):
    if (all(value is not None for value in wago_pairlist.values()) and 
        all(value is not None for value in gairaigo_pairlist.values())):
        return True
    return False


def generate_experiment_result(word_list_no, wago_pairlist, gairaigo_pairlist, result, experiment_no:int):
    w_word_list, w_rankings, w_frequencies, w_mora_lengths, w_unranked_count = rg.load_experiment_features()
    g_word_list, g_rankings, g_frequencies, g_mora_lengths, g_unranked_count = rg.load_experiment_features()
    
    result = rg.generate_populate_wordlist(wago_pairlist, result, w_word_list, w_rankings, w_frequencies, w_mora_lengths, w_unranked_count, wago=True)
    result = rg.generate_populate_wordlist(gairaigo_pairlist, result, g_word_list, g_rankings, g_frequencies, g_mora_lengths, g_unranked_count, gairaigo=True)
    rg.write_results_to_file(result, word_list_no, experiment_no)
