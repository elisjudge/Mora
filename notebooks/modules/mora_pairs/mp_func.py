import modules.config as c
import modules._readers as reader
import modules.mora_count.mc_func as mc
import numpy as np


def preprocess_load_data():
    stats = load_mora_pair_stats()
    mora_pair_stats, word_stats = split_word_pair_stats(stats)
    wago_pair_stats, gairaigo_pair_stats = split_mora_pair_stats(mora_pair_stats)
    return wago_pair_stats, gairaigo_pair_stats, word_stats
    
   
def preprocess_load_mora_count_data():    
    mora_count_stats = mc.load_mora_count_stats()
    mora_count_stats, mc_overall_stats = mc.spilt_stats(mora_count_stats)
    mc_overall_stats = mc.preprocess_overall_stats(mc_overall_stats)
    return mora_count_stats, mc_overall_stats


def load_mora_pair_stats() -> dict:
    return reader.read_json_file(c.MORA_PAIR_STAT_PATH)


def split_word_pair_stats(stats) -> dict:
    pair_stats = stats['pairs']
    word_stats = stats['words']
    return pair_stats, word_stats


def split_mora_pair_stats(mora_pair_stats) -> dict:
    wago = mora_pair_stats['wago']
    gairaigo = mora_pair_stats['gairaigo']
    return wago, gairaigo


def preprocess_load_valid_data(word_type):
    valid_pair = load_valid_pair(word_type)
    return sort_valid_pairs(valid_pair)


def load_valid_pair(word_type:str) -> list:
    if word_type == "k":
        return reader.read_json_file(c.WAGO_VALID_PAIRS_PATH) 
    elif word_type == 'g':
        return reader.read_json_file(c.GAIRAIGO_VALID_PAIRS_PATH) 
    


def sort_valid_pairs(valid_pair_list:list) -> list:
    return sorted(valid_pair_list, key=lambda x: list(x.values())[0], 
                  reverse=True)


def fetch_top_20_valid_pairs(sorted_valid_pair_list:list) -> dict:
    top_20 = sorted_valid_pair_list[:20]
    return {key: value for dictionary in top_20 for key, value in dictionary.items()}


def convert_list_to_numpy(sorted_list:list):
    return np.array([list(line.values())[0] for line in sorted_list])


def get_five_number_summary_stats(nums) -> list:
    return np.percentile(nums, [0, 25, 50, 75, 100], method="midpoint")


def find_percentile_rank(numpy_array, score):
    mask = numpy_array >= score
    filtered_array = numpy_array[mask]
    return  100 * (len(filtered_array) / len(numpy_array))


def fetch_top_nth_percentile_data(sorted_list:list, score) -> list:
    return [line for line in sorted_list if list(line.values())[0] >= score] 


def print_five_number_summary(min, q1, med, q3, max):
    print("FIVE NUMBER SUMMARY")
    print(f'Minimum: {min}')
    print(f'Lower Quartile: {q1}')
    print(f'Median: {med}')
    print(f'Upper Quartile: {q3}')
    print(f'Maximum: {max}')

