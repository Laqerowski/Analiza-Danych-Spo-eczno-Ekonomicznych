from data import df_combined
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import seaborn as sns

# Funkcja wykresu punktowego
def WykresPunktowy(column_name, title1, title2, show_stats=False):
    plt.figure(figsize=(8, 6))
    plt.scatter(df_combined.index, df_combined[column_name], alpha=0.5, color='b', marker='o')
    plt.title(title1)
    plt.xlabel(title2)
    plt.ylabel(column_name)
    if show_stats:
        mean_val = df_combined[column_name].mean()
        median_val = df_combined[column_name].median()
        max_val = df_combined[column_name].max()
        min_val = df_combined[column_name].min()

        stats_text = f'Średnia: {mean_val:.2f}\nMediana: {median_val:.2f}\nMaksimum: {max_val}\nMinimum: {min_val}'
        plt.text(0.95, 0.95, stats_text, transform=plt.gca().transAxes, 
                 fontsize=12, verticalalignment='top', horizontalalignment='right', 
                 bbox=dict(facecolor='white', alpha=0.5))
    
    plt.grid(True)
    plt.show()

# Funkcja wykresu słupkowego
def WykresSlupkowy(column_name, title1, title2, hue=False, section=None, use_palette=True, show_stats=False, legend=False):
    plt.figure(figsize=(10, 6))
    if use_palette and hue:
        sns.countplot(x=column_name, hue=section, data=df_combined, palette='pastel')
    elif use_palette:
        sns.countplot(x=column_name, data=df_combined, palette='pastel')
    else:
        sns.countplot(x=column_name, data=df_combined, color='skyblue')
    
    plt.title(title1)
    plt.xlabel(column_name)
    plt.ylabel(title2)
    if show_stats:
        mean_val = df_combined[column_name].mean()
        median_val = df_combined[column_name].median()
        max_val = df_combined[column_name].max()
        min_val = df_combined[column_name].min()

        stats_text = f'Średnia: {mean_val:.2f}\nMediana: {median_val:.2f}\nMaksimum: {max_val}\nMinimum: {min_val}'
        plt.text(0.2, 0.95, stats_text, transform=plt.gca().transAxes, 
                 fontsize=12, verticalalignment='top', horizontalalignment='right', 
                 bbox=dict(facecolor='white', alpha=0.5))
    
    if legend:
        plt.legend(title=section)
    plt.show()

# Funkcja wykresu średniej w dwóch grupach
def WykresSredniaGrupa(group1, group2, label1, label2, use_palette=True):
    
    sredni = df_combined.groupby(group1)[group2].mean().reset_index()

    plt.figure(figsize=(10, 6))
    if use_palette:
        sns.barplot(data=sredni, x=group1, y=group2, palette='pastel')
    else:
        sns.barplot(data=sredni, x=group1, y=group2, color='skyblue')
    plt.xlabel(group1)
    plt.ylabel(label1)
    plt.title(label2)
    plt.show()

# Funkcja wykresu zależności
def WykresZaleznosc(group1, group2, title, grupowanie=False, hue=None, style=None, regresja=False, korelacja=False):
    plt.figure(figsize=(10, 6))
    if grupowanie:
        sns.scatterplot(data=df_combined, x=group1, y=group2, hue=hue, style=style)
        plt.legend(loc='lower right', title=hue)
    else:
        sns.scatterplot(data=df_combined, x=group1, y=group2)
    plt.xlabel(group1)
    plt.ylabel(group2)
    plt.title(title)
    
    if regresja:
        sns.regplot(data=df_combined, x=group1, y=group2, scatter=False, color='red')

    if korelacja:
        korelacja_ = df_combined[group1].corr(df_combined[group2])

        plt.annotate(f'Współczynnik korelacji: {korelacja_:.2f}', 
                xy=(0.05, 0.95), 
                xycoords='axes fraction', 
                fontsize=12, 
                color='red',
                bbox=dict(facecolor='white', alpha=0.5))
        
    plt.show()

# Funkcja wykresu pudełkowego
def WykresPudelkowy(group1, group2, title, label1, label2):
    plt.figure(figsize=(12,6))
    sns.boxenplot(x=group1, y=group2, data=df_combined, palette='pastel')
    plt.title(title)
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.show()

# Funkcja analizy korelacji
def MacierzKorelacji(columns, title):
    korelacje = df_combined[columns].corr()

    plt.figure(figsize=(10,8))
    sns.heatmap(korelacje, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(title)
    plt.show()

# Funkcja rozrzutu 
def WykresRozrzutu(columns):
    sns.pairplot(df_combined[columns], kind='reg', plot_kws={'line_kws':{'color':'red'}})
    plt.show()

# Funkcja procentowego udziału
def WykresProcent(main_column, columns, title):
    plt.figure(figsize=(10,6))
    total = df_combined[main_column].sum()
    procent = (total / df_combined[columns].sum()) * 100
    procent.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel', len(columns)))
    plt.title(title)
    plt.ylabel('')
    plt.show()

# Funkcja wykresu słupkowego średnich 
def WykresSrednia(dane, title, label1, label2):
    srednia = dane.mean()
    srednia.plot(kind='bar', color=sns.color_palette('pastel', 2))
    plt.title(title)
    plt.xlabel(label1)
    plt.ylabel(label2)
    plt.xticks(rotation=0)
    plt.show()

# Funkcja wykresu słupkowego lepszego
def WykresSlupkowyLepszy(factor, columns, name1, name2, title, label):
    plt.figure(figsize=(10, 6))
    df_melted = df_combined.melt(id_vars=[factor], value_vars=columns, var_name=name1, value_name=name2)
    
    sns.barplot(data=df_melted, x=factor, y=name2, hue=name1, palette='pastel')
    plt.title(title)
    plt.xlabel(factor)
    plt.ylabel(label)
    plt.legend(title=name1)
    plt.show()

# Wykres procentowego stosunki 3 zmiennych
def WykresProcentDochod(main_column, column, group_column, title):
    plt.figure(figsize=(10,6))
    
    grouped_data = pd.DataFrame(df_combined).groupby(group_column).sum()
    total = grouped_data[main_column].sum()
    
    procent = (grouped_data[column] / total) * 100
    procent.plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel', len(grouped_data)))
    plt.title(f"{title}")
    plt.ylabel('')
    plt.show()

# Funkcja wykresu debetu
def WykresDebet(column, title, second_column=None):
    plt.figure(figsize=(12, 8))
    df_combined['Debet'] = df_combined['Kredyty'] + df_combined['Karty_kredytowe']
    df_combined['Równowaga_budżetowa'] = df_combined['Roczny_dochód'] - df_combined['Debet']
    
    if second_column:
        grouped_data = df_combined.groupby([column, second_column]).sum()
        grouped_data.reset_index(inplace=True)
        
        sns.barplot(data=grouped_data, x=column, y='Równowaga_budżetowa', hue=second_column, palette='pastel', ci=None)
        plt.title(title)
        plt.xlabel(column)
    else:
        sns.barplot(data=df_combined, x=column, y='Równowaga_budżetowa', palette='pastel', ci=None)
        plt.title(title)
        plt.xlabel(column)
    
    plt.ylabel('Równowaga budżetowa')
    plt.axhline(y=0, color='red', linestyle="--")
    plt.show()