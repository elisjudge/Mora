import matplotlib.pyplot as plt
import modules.config as c
import modules.mora_pairs.mp_func as mp
import modules._readers as reader
import multidict as multidict
import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib.font_manager import FontProperties
from PIL import Image
from wordcloud import WordCloud

def build_assigned_mora_pair_graph(word_stats:dict):
    with sns.axes_style("whitegrid"):
        wago = word_stats['wago']
        gairaigo = word_stats['gairaigo']
        mixed_hirakata = word_stats['mixed_hirakata_count']
        unassigned_hira = word_stats['unassigned_hiragana_error_count']
        unassigned_kata = word_stats['unassigned_katakana_error_count']

        # Sample data
        data = pd.DataFrame({
            'Category': ['Assigned Words', 'Mixed Hirakata Errors', 'Unassigned Errors'],
            'Wago': [wago, 0, 0],
            'Gairaigo': [gairaigo, 0, 0],
            'Mixed HiraKata': [0, mixed_hirakata, 0],
            'Unassigned': [0, 0, (unassigned_hira + unassigned_kata)]
        })

        # Set the index to 'Category' for easier plotting
        data.set_index('Category', inplace=True)

        # Create a horizontal stacked bar chart
        ax = data.plot(kind='barh', stacked=True, figsize=(10, 6))

        offset = 650

        # Add labels for non-zero integer values on the right side of each subcategory bar
        for category in data.index:
            left = 100
            for subcategory in data.columns:
                value = data.loc[category, subcategory]
                if value > 0:
                    ax.text(
                        left + (value / 2) + offset,
                        data.index.get_loc(category),
                        str(value),
                        va='center',
                        ha='center',
                        fontsize=9,
                        color='black'
                    )
                left += 100+value

        # Add labels and title
        plt.xlabel('Number of Words')
        plt.xlim((0,70000))
        plt.ylabel('')
        plt.title('Words Assigned Mora Pair')

        # Add a legend
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(reversed(handles), reversed(labels))
        plt.show()


def build_pair_no_pair_graph(wago_pair_stats:dict, gairaigo_pair_stats:dict):
    # Extract the counts for 'no_pairs' and 'pairs'
    with sns.axes_style(style='whitegrid'), sns.color_palette('Spectral'):
        wago_no_pairs_count = wago_pair_stats['no_pairs_count']
        wago_pairs_count = wago_pair_stats['pairs_count']

        gairaigo_no_pairs_count = gairaigo_pair_stats['no_pairs_count']
        gairaigo_pairs_count = gairaigo_pair_stats['pairs_count']

        # Create a DataFrame with the data
        data = pd.DataFrame({
            'Category': ['Wago', 'Gairaigo'],
            'Invalid Pair': [wago_no_pairs_count, gairaigo_no_pairs_count],
            'Valid Pair': [wago_pairs_count, gairaigo_pairs_count]
        })

        # Set the index to 'Category' for easier plotting
        data.set_index('Category', inplace=True)

        # Create a vertical stacked bar chart
        ax = data.plot(kind='bar', stacked=True, figsize=(10, 6))

        # Add labels for non-zero integer values above each bar
        for category in data.index:
            bottom = 0
            for subcategory in data.columns:
                value = data.loc[category, subcategory]
                if value > 0:
                    ax.text(
                        data.index.get_loc(category),
                        bottom + (value / 2),
                        str(value),
                        va='center',
                        ha='center',
                        fontsize=9,
                        color='black'
                    )
                bottom += value

        # Add labels and title
        plt.ylabel('Number of Possible Pair Combinations')
        plt.ylim((0,80000))
        plt.xlabel('')
        plt.title('Words Assigned Mora Pair')

        # Make x-axis category labels horizontal
        plt.xticks(rotation=0)

        # Add a legend
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(reversed(handles), reversed(labels))
        plt.show()


def build_top_20_graph(data:dict, color):
    with sns.axes_style("whitegrid"):
        top_20 = mp.fetch_top_20_valid_pairs(data)
        categories = [key for key in top_20.keys()]
        values = [value for value in top_20.values()]

        # Define your custom Japanese font path
        japanese_font_path = c.JAPANESE_FONT_PATH
        # Specify the font properties
        font_properties = FontProperties(fname=japanese_font_path, size=11)

        # Set the figure size
        plt.figure(figsize=(10, 6))

        # Define the bar width
        bar_width = 0.8  # Adjust this value as needed


        # Create the bar plot
        ax = plt.bar(x=categories, height=values, width=bar_width, color=color)

        # Annotate the bars with number values above them
        for p in ax:
            plt.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                        textcoords='offset points')

        # Set the x-axis labels and rotation
        plt.xticks(rotation=45, ha='center')

        # Set the y-axis limit, label, and title
        plt.ylim(0, 1600)
        plt.ylabel("Number of Words")
        plt.title("Mora Pairing by Number of Words (Top 20)")

        # Set the custom font properties
        plt.xticks(fontproperties=font_properties)

        # Show the plot
        plt.show()


def build_wordcloud(word_type, colormap):

    if word_type == 'k':
        path = c.WAGO_VALID_PAIRS_PATH
        mask_path = c.WAGO_IMAGE_MASK_PATH
    elif word_type == 'g':
        path = c.GAIRAIGO_VALID_PAIRS_PATH
        mask_path = c.GAIRAIGO_IMAGE_MASK_PATH

    wordcloud_dict = multidict.MultiDict()
    for line in reader.read_json_lines(path):
        for key, value in line.items():
            wordcloud_dict.add(key, value)

    mask = np.array(Image.open(mask_path))

    wordcloud = WordCloud(font_path=c.JAPANESE_FONT_PATH, 
                        width=1600, 
                        height=826, 
                        mask= mask,
                        background_color='black',
                        colormap=colormap,
                        random_state= 185
                        )

    wordcloud.generate_from_frequencies(wordcloud_dict)

    # output_file_path = './wordcloud_hiraganapairs.png'  # Change this to the desired output file path
    # wordcloud.to_file(output_file_path)

    plt.figure(figsize=(100, 50))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def build_boxplot(numpy_array):
    with sns.axes_style("darkgrid"):
        plt.boxplot(numpy_array, vert=False)
        plt.title("Boxplot of the Number of Words that include Each Mora Pair")
        plt.xlabel("Number of Words")
        plt.ylabel("Mora Pair")
        plt.yticks([])
        sns.set()
        sns.set(style="darkgrid")
        plt.show()
