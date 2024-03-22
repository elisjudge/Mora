import modules.config as c
import modules._readers as reader


def preprocess_load_data():
    mora_stats = load_mora_count_stats()
    mora_stats, overall_stats = spilt_stats(mora_stats)
    total_dict_words = get_total_number_dictionary_words(overall_stats)
    overall_stats = preprocess_overall_stats(overall_stats)
    max_key = find_max_mora(mora_stats)
    mora_stats = sort_keys(mora_stats, max_key)

    return mora_stats, overall_stats, total_dict_words


def load_mora_count_stats() -> dict:
    return reader.read_json_file(c.COUNT_STAT_PATH)


def spilt_stats(mora_stats) -> dict:
    overall_stats = {key: value for key, value in mora_stats.items() if key in ['total', 'err', 'expr']}
    mora_stats = {key: value for key, value in mora_stats.items() if key not in ['total', 'err', 'expr']}
    return mora_stats, overall_stats


def find_max_mora(mora_stats) -> int:
    max_key = 0
    for key in mora_stats.keys():
        curr_key = int(key)
        max_key = curr_key if curr_key > max_key else max_key
    return max_key


def sort_keys(mora_stats, max_key) -> dict:
    sorted_mora_stats = {}
    for num in range(max_key):
        search_key = str(num + 1)
        if search_key in mora_stats:
            sorted_mora_stats[search_key] = mora_stats[search_key]
        else:
            continue
    return sorted_mora_stats


def get_total_number_dictionary_words(overall_stats) -> int:
    return overall_stats['total']


def preprocess_overall_stats(overall_stats):
    overall_stats['counted_words'] = overall_stats['total'] - (overall_stats['expr'] + overall_stats['err'])
    del overall_stats['total']
    return overall_stats


def get_number_of_words_with_mora_count_9_or_higher(mora_stats):
    number_words = 0
    for key, value in mora_stats.items():
        if int(key) >= 9:
            number_words += value
    return number_words


def get_proportion_of_words_with_mora_count_9_or_higher(mora_stats, overall_stats):
    number_words_great_equal_nine = get_number_of_words_with_mora_count_9_or_higher(mora_stats)
    total_words = overall_stats['counted_words']
    return float((number_words_great_equal_nine/total_words)*100)

def get_proportion_of_words_with_mora_count_x(mora_stats, overall_stats, mora_count):
    number_words = mora_stats[str(mora_count)]
    total_words = overall_stats['counted_words']
    return float((number_words/total_words)*100)





    