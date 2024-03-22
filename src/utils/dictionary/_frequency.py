import config
import utils.helper._writers as writer
import utils.helper._readers as reader
import utils.helper._exists as exist

def build_frequency_dict():
    if not exist.path_exists(config.FREQ_OUT_PATH):
        frequency_dictionary = {}

        with open(config.FREQ_IN_PATH, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                line = line.strip()
                if line and line[0].isdigit():
                    rank, normalizedfreq, word = line.split()
                    entry = {'rank': int(rank),
                            'normalized_frequency': float(normalizedfreq)}
                    frequency_dictionary[word] = entry
        writer.write_file(config.FREQ_OUT_PATH, frequency_dictionary)


def load_frequency_dictionary():
    return reader.read_json_file(config.FREQ_OUT_PATH)


def fetch_frequencies():
    """ This will take the existing temp wordpool file and update it by writing
    frequencies to it"""
    wp = []
    freq_dict = load_frequency_dictionary()
    for line in reader.read_json_lines(config.WORDPOOL_TEMP_PATH):
        word = line['word']
        if word in freq_dict:
            line['rank'] = freq_dict[word]['rank']
            line['norm_freq'] = freq_dict[word]['normalized_frequency']
        else:
            line['rank'] = 'N/A'
            line['norm_freq'] = 0
        wp.append(line)
    writer.write_file(config.WORDPOOL_TEMP_PATH, wp)





