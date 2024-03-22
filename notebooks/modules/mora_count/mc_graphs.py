import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def build_dictionary_comp_graph(overall_stats):
    # sort the stats
    overall_stats = sorted(overall_stats.items())
    
    # Build DataFrame
    df = pd.DataFrame(overall_stats, columns=['Classification', 'Number of Words'])
    df["Classification"] = ['Non-Expressional Words', 'Hybrid Kana Words', 'Expressional Words']


    # Create the barplot using Seaborn
    sns.set(style="whitegrid")
    ax = sns.barplot(data=df, x='Classification', y='Number of Words', hue='Classification', legend= False, palette='Spectral')

    # Remove the x-label
    plt.xlabel(None)
    plt.ylim((0,70000))
    plt.title('Composition of Japanese Dictionary')

    # Add count labels on top of the bars
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=8, color='black', xytext=(0, 5),
                    textcoords='offset points')
    plt.show()


def build_mora_count_graph(mora_stats):
    sns.set(style="whitegrid")
    ax = sns.barplot(mora_stats, orient='h', palette="Spectral")

    for p in ax.patches:
        ax.annotate(f'{int(p.get_width())}', (p.get_width(), p.get_y() + p.get_height() / 2.),
                    va='center', fontsize=8, color='black', xytext=(3, 0),
                    textcoords='offset points')

    plt.xlabel('Number of Words')
    plt.xlim((0,30000))
    plt.ylabel('Number of Mora')
    plt.title('Composition of Mora Counts for Each Word in Japanese Dictionary')
    plt.plot()
        

