import utils.dictionary._wordpool_func as wp


def generate_wordpool():
    """ This function will set up the analysis features and generate the wordpool to
    generate the word lists. First it will create the morapairs from hiragana and katakana
    characters. It will then generate a word frequency dictionary, followed by counting the
    number of mora within each word in the dictionary, if valid. It will then find every mora
    pair within each word, if valid. Then it will look at each valid word and find its frequency
    from the frequency dictionary. Finally, it will remove any mora pair that does not exist in the
    dictionary and then randomize the words into a final word pool and then split these into a 
    ranked and unranked word pool"""

    wp.create_pairlists()
    wp.build_frequency_dictionary()
    wp.create_mora_counts()
    wp.compute_mora_pairs()
    wp.get_frequencies()
    wp.write_valid_pairlists()
    wp.finalize_wordpool()
    wp.delete_temp_wordpool()


def generate_ranked_wordpools():
    word_pool = wp.load_wordpool()
    wp.generate_ranked_unranked_pools(word_pool)


def is_wordpool():
    return wp.is_wordpool()