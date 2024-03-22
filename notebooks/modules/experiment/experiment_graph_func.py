import matplotlib.pyplot as plt
import seaborn as sns


def build_combined_histograms(results):
    with sns.axes_style("dark"), sns.color_palette("pastel"):
        fig, axes = plt.subplots(2, 2, figsize=(8, 5))  
        
        # First subplot: Normalized Frequency Histogram
        ax1 = axes[0,0]
        norm_freq = results['Normalized Frequency (Avg)']
        ax1.hist(norm_freq, color='blue')
        ax1.set_xlabel('Normalized Frequency (Avg)')

        
        # Second subplot: Word List Length Histogram
        ax2 = axes[0,1]
        list_len = results['Word List Length']
        ax2.hist(list_len, color='green')
        ax2.set_xlabel('Word List Length')

        
        # Third subplot: Unranked Proportion Histogram
        ax3 = axes[1,0]
        unranked_prop = [val['unranked_prop'] for point in results['labels'] for val in point.values()]
        ax3.hist(unranked_prop, color='red')
        ax3.set_xlabel('Proportion of words that are unranked')


        # Third subplot: Average Mora Length
        ax4 = axes[1,1]
        average_mora = [val['average_mora_length'] for point in results['labels'] for val in point.values()]
        ax4.hist(average_mora, color='purple')
        ax4.set_xlabel('Mora Length (Avg)')
  

        fig.suptitle('Word List: Descriptive Statistics')
        
        plt.tight_layout()  # Ensure that the subplots don't overlap
        plt.show()


def build_list_length_vs_norm_freq_scatterplot(results):
    norm_freq = results['Normalized Frequency (Avg)']
    list_len = results['Word List Length']
    plt.scatter(norm_freq, list_len)
    plt.xlabel('Normalized Frequency (Avg)')
    plt.ylabel('Word List Length')
    plt.title('Scatterplot with Labels (Associations)')
    plt.show()


def build_pareto_optimal_scatterplot(results):
    norm_freq = results['Normalized Frequency (Avg)']
    list_len = results['Word List Length']
    data_points = [(ll, nf) for ll, nf in zip(norm_freq, list_len)]

    # Initialize lists to store Pareto front points and their indices
    pareto_front = []
    pareto_front_indices = []

    # Check each data point against all others
    for index, point1 in enumerate(data_points):
        is_pareto_optimal = True
        for point2_index, point2 in enumerate(data_points):
            if index != point2_index and dominates(point2, point1):
                is_pareto_optimal = False
                break
        if is_pareto_optimal:
            pareto_front.append(point1)
            pareto_front_indices.append(index)

    # Separate Pareto and non-Pareto points
    non_pareto_front = [point for index, point in enumerate(data_points) if index not in pareto_front_indices]

    np_normfreq = [point[0] for point in non_pareto_front]
    np_listlen = [point[1] for point in non_pareto_front]

    p_normfreq = [point[0] for point in pareto_front]
    p_listlen = [point[1] for point in pareto_front]

    # Create the scatterplot
    plt.scatter(np_normfreq, np_listlen, label='Non-Pareto')
    plt.scatter(p_normfreq, p_listlen, c='red', label='Pareto')

    # Add labels for Pareto points
    for i, label in enumerate(pareto_front_indices):
        plt.annotate(f'{label}', (p_normfreq[i], p_listlen[i]), fontsize=6, textcoords="offset points", 
                    xytext=(0, 10), ha='center', bbox=dict(boxstyle="round,pad=0.2", edgecolor="black", facecolor="white"))


    plt.xlabel('Normalized Frequency (Avg)')
    plt.ylabel('Word List Length')
    plt.title('Scatterplot with Pareto Front and Labels')
    plt.legend()
    plt.grid(True)

    plt.show()


def dominates(point1, point2):
    # Check if point1 dominates point2
    return point1[0] >= point2[0] and point1[1] <= point2[1]