import modules.config as c
import modules._readers as reader
import modules._writers as writer
import os


def load_experiment_results_data(experiment_no):
    if experiment_no == 1:
        path = c.EXPERIMENT_1_PATH
    elif experiment_no == 2:
        path = c.EXPERIMENT_2_PATH
    elif experiment_no == 3:
        path = c.EXPERIMENT_3_PATH

    hiragana_dict = {'Normalized Frequency (Avg)': [], 'Word List Length': [], 'labels':[]}
    katakana_dict = {'Normalized Frequency (Avg)': [], 'Word List Length': [], 'labels':[]}

    hiragana_wordlists = {}
    katakana_wordlists = {}

    filenames = os.listdir(path)
    sorted_filenames = sorted(filenames, key=lambda x: int(x.split('_')[0]) if x.split('_')[0].isdigit() else x)

    for file in sorted_filenames:
        trial_no = file.split('_')[0]
        filepath = path + file
        
        data = reader.read_json_file(filepath)
        
        hiragana_dict['Normalized Frequency (Avg)'].append(data['hiragana']['average_normalized_frequency'])
        hiragana_dict['Word List Length'].append(data['hiragana']['list_length'])
        hiragana_dict['labels'].append({trial_no: {"average_ranking": data['hiragana']['average_ranking'],
                                                "average_mora_length": data['hiragana']['average_mora_length'],
                                                "unranked_words": data['hiragana']['unranked_words'],
                                                "unranked_prop": data['hiragana']['unranked_prop']}})
        
        hiragana_wordlists[trial_no] = data['hiragana']['word_list']

        katakana_dict['Normalized Frequency (Avg)'].append(data['katakana']['average_normalized_frequency'])
        katakana_dict['Word List Length'].append(data['katakana']['list_length'])
        katakana_dict['labels'].append({trial_no: {"average_ranking": data['katakana']['average_ranking'],
                                                "average_mora_length": data['katakana']['average_mora_length'],
                                                "unranked_words": data['katakana']['unranked_words'],
                                                "unranked_prop": data['katakana']['unranked_prop']}})
        
        katakana_wordlists[trial_no] = data['katakana']['word_list']

    return hiragana_dict, katakana_dict, hiragana_wordlists, katakana_wordlists


def save_wordlist(k_word_list, g_word_list, experiment_no):
    path = c.RESULTS_PATH

    if experiment_no <= 2:
        writer.write_file(f'{path}exp_{experiment_no}_kanwago_list_long.json', k_word_list)
        writer.write_file(f'{path}exp_{experiment_no}_gairaigo_list_long.json', g_word_list)

    if experiment_no == 3:
        writer.write_file(f'{path}exp_{experiment_no}_kanwago_list_short.json', k_word_list)
        writer.write_file(f'{path}exp_{experiment_no}_gairaigo_list_short.json', g_word_list)
    
    


