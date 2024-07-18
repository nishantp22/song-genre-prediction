import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df=pd.read_csv('datasets/dataset.csv')
features = ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms']
# df = df[features]


#histogram for modes - major/minor
def histogramModes():
    grouped = df.groupby(['genre', 'mode']).size().reset_index(name='frequency')
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='genre', y='frequency', hue='mode', data=grouped)
    
    plt.xlabel('Genre')
    plt.ylabel('Frequency')
    plt.title('Frequency of Modes for Each Genre')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()



# histogram for keys - c,c#....and so on
def histogramKeys():
    grouped_key = df.groupby(['genre', 'key']).size().reset_index(name='frequency')

    plt.figure(figsize=(10, 6))
    sns.barplot(x='genre', y='frequency', hue='key', data=grouped_key)

    plt.xlabel('Genre')
    plt.ylabel('Frequency')
    plt.title('Frequency of Keys for Each Genre')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.legend(title='Key')
    plt.show()



# histogram for time signatures
def histogramTimeSignatures():
    grouped_time_signature = df.groupby(['genre', 'time_signature']).size().reset_index(name='frequency')

    plt.figure(figsize=(10, 6))
    sns.barplot(x='genre', y='frequency', hue='time_signature', data=grouped_time_signature)

    plt.xlabel('Genre')
    plt.ylabel('Frequency')
    plt.title('Frequency of Time Signatures for Each Genre')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.legend(title='Time Signature')
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





