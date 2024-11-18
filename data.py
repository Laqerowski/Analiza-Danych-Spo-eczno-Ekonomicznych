import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import seaborn as sns

# Zmiana kodowania wyjścia w Pythonie
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Wczytanie danych z odpowiednim kodowaniem
d1 = pd.read_csv('dane_dla_studentow.csv', sep=';', encoding='cp1250')
d2 = pd.read_csv('dodatkowe_dane.csv', sep=';', encoding='cp1250')

# Połączenie danych z obu plików CSV w jedną ramkę danych
df_combine = pd.concat([d1, d2])
df_combined = df_combine[df_combine['Wiek'] < 75]
# Ustawienie czcionki, która obsługuje polskie znaki
prop = fm.FontProperties(fname=fm.findSystemFonts(fontpaths=None, fontext='ttf')[0])
plt.rcParams['font.family'] = 'Arial'
