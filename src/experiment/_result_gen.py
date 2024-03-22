import config
import numpy as np
import utils.helper._writers as writer


def load_experiment_features():
    word_list = set()
    rankings = []
    frequencies = []
    mora_lengths = []
    unranked_count = 0

    return word_list, rankings, frequencies, mora_lengths, unranked_count


def write_wago_results(result:dict, word_list, rankings, frequencies, mora_lengths, unranked_count):
    result['hiragana']['word_list'] = word_list
    result['hiragana']['list_length'] = len(word_list)
    result['hiragana']['average_normalized_frequency'] = np.mean(frequencies)
    result['hiragana']['average_ranking'] = np.mean(rankings)
    result['hiragana']['average_mora_length'] = np.mean(mora_lengths)
    result['hiragana']['unranked_words'] = unranked_count
    result['hiragana']['unranked_prop'] = unranked_count / result['hiragana']['list_length']


def write_gairaigo_results(result:dict, word_list, rankings, frequencies, mora_lengths, unranked_count):
    result['katakana']['word_list'] = word_list
    result['katakana']['list_length'] = len(word_list)
    result['katakana']['average_normalized_frequency'] = np.mean(frequencies)
    result['katakana']['average_ranking'] = np.mean(rankings)
    result['katakana']['average_mora_length'] = np.mean(mora_lengths)
    result['katakana']['unranked_words'] = unranked_count
    result['katakana']['unranked_prop'] = unranked_count / result['katakana']['list_length']


def generate_populate_wordlist(pairlist:dict, results, word_list, rankings, frequencies, mora_lengths, unranked_count, wago=False, gairaigo=False):   
    for value in pairlist.values():
        if value is not None and 'word' in value and value['word'] is not None:
            if value['word'] not in word_list:
                word_list.add(value['word'])
                frequencies.append(value['norm_freq'])
                mora_lengths.append(value['mora_count'])

                if value['rank'] != "N/A":
                    rankings.append(value['rank'])
                else:
                    unranked_count += 1

    word_list = list(word_list)
    rankings = np.array(rankings)
    frequencies = np.array(frequencies)
    mora_lengths = np.array(mora_lengths)

    if wago:
        write_wago_results(results, word_list, rankings, frequencies, mora_lengths, unranked_count)
    elif gairaigo:
        write_gairaigo_results(results, word_list, rankings, frequencies, mora_lengths, unranked_count)
    
    return results

def write_results_to_file(result, wordlist_no, experiment_no):
    if experiment_no == 1:
        path = config.EXPERIMENT1_DIR_PATH + str(wordlist_no) + '_result.json'
        writer.write_file(path, result)
    elif experiment_no == 2:
        path = config.EXPERIMENT2_DIR_PATH + str(wordlist_no) + '_result.json'
        writer.write_file(path, result)
    elif experiment_no == 3:
        path = config.EXPERIMENT3_DIR_PATH + str(wordlist_no) + '_result.json'
        writer.write_file(path, result)
    