import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split

df=pd.read_csv('datasets/dataset.csv')
features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
# df = df[features]


#histogram for modes
def histogramModes():
    grouped = df.groupby(['genre', 'mode']).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.35
    positions = range(len(grouped.index))

    for i, mode in enumerate(grouped.columns):
        ax.bar([p + (i * bar_width) for p in positions], grouped[mode], bar_width, label=mode)

    ax.set_xlabel('Genre')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Modes for Each Genre')
    ax.set_xticks([p + bar_width / 2 for p in positions])
    ax.set_xticklabels(grouped.index)
    ax.legend()

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()



# histogram for keys
def histogramKeys():
    grouped_key = df.groupby(['genre', 'key']).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 6))

    total_keys = len(grouped_key.columns)
    bar_width = 0.8 / total_keys  # Adjust this value for spacing between bars

    # Set the positions for the bars
    positions_key = range(len(grouped_key.index))

    # Plot bars for each key
    for i, key in enumerate(grouped_key.columns):
        ax.bar([p + (i * bar_width) for p in positions_key], grouped_key[key], bar_width, label=key)

    # Set labels and title for key plot
    ax.set_xlabel('Genre')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Keys for Each Genre')
    ax.set_xticks([p + ((total_keys - 1) / 2) * bar_width for p in positions_key])
    ax.set_xticklabels(grouped_key.index)
    ax.legend(title='Key')

    # Show plot
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()



# histogram for time signatures
def histogramTimeSignatures():
    grouped_time_signature = df.groupby(['genre', 'time_signature']).size().unstack(fill_value=0)

    fig, ax = plt.subplots(figsize=(10, 6))

    total_time_signatures = len(grouped_time_signature.columns)
    bar_width = 0.8 / total_time_signatures  # this is for spacing between bars

    positions_time_signature = range(len(grouped_time_signature.index))

    for i, time_signature in enumerate(grouped_time_signature.columns):
        ax.bar([p + (i * bar_width) for p in positions_time_signature], grouped_time_signature[time_signature], bar_width, label=time_signature)

    ax.set_xlabel('Genre')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Time Signatures for Each Genre')
    ax.set_xticks([p + ((total_time_signatures - 1) / 2) * bar_width for p in positions_time_signature])
    ax.set_xticklabels(grouped_time_signature.index)
    ax.legend(title='Time Signature')

    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


#box plots for various features for different genres.
def boxPlotFeatures(feature):               # pass the y feature as argument
    sns.set_theme(style="ticks")

    colors = sns.color_palette("pastel")

    plt.figure(figsize=(12, 8))
    sns.boxplot(x='genre', y=feature, data=df, palette=colors)  
    plt.title(f'Distribution of {feature} for Each Genre', fontsize=16, fontweight='bold')
    plt.xlabel('Genre', fontsize=14)
    plt.ylabel(feature, fontsize=14)
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.yticks(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# correlation matrix
def correlation():
    correlation_matrix = df[features].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

# histogramModes()
# histogramKeys()           #call functions as desired
# histogramTimeSignatures()           #call functions as desired
# boxPlotFeatures('liveness')  #pass the desired feature for box plot
correlation()





