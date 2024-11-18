from data import df_combined
import analize as ana
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import seaborn as sns

# Tworzenie jednego wykresu dla połączonych danych
fig, ax = plt.subplots(figsize=(10, 10))

# Tabela dla połączonych danych
ax.axis('off')
table = ax.table(cellText=df_combined.head(30).values, colLabels=df_combined.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(6)

plt.tight_layout()
plt.show()

########################### Analiza demograficzna #####################################

# Wiek
ana.WykresSlupkowy('Wiek', "Rozkład wieku osób", "Liczba wystąpień", use_palette=False, show_stats=True)
ana.WykresPunktowy('Wiek',"Rozkład wieku osób", "Index", show_stats=True)
# Płeć
ana.WykresSlupkowy('Płeć', "Rozkład płci", "Liczba osób", use_palette=True)
# Wykształcenie
ana.WykresSlupkowy('Wykształcenie', "Rozkład poziomu wykształcenia", "Liczba osób", use_palette=True)

############################## Analiza finansowa #######################################

# Suma wydatków z różnych kolumn
df_combined['Wydatki_total'] = df_combined[['Wydatki_mieszkanie', 'Wydatki_transport', 'Wydatki_żywność', 'Wydatki_edukacja']].sum(axis=1)
df_combined['Zadluzenie'] = df_combined[['Kredyty', 'Karty_kredytowe']].sum(axis=1)

# Średni dochód w poszczególnych grupach wiekowych
ana.WykresSredniaGrupa('Wiek', 'Roczny_dochód', "Średni dochód roczny", "Średni dochód roczny w różnych grupach wiekowych", use_palette=False)
# Średnie wydatki w różnych grupach wiekowych 
ana.WykresSredniaGrupa('Wiek', 'Wydatki_total', "Średnie wydatki", "Średnie wydatki poszczególnych grupach wiekowych", use_palette=False)

# Średni dochód według płci
ana.WykresSredniaGrupa('Płeć', 'Roczny_dochód', "Średni dochód roczny", "Średni dochód roczny zależny od płci", use_palette=True)
# Średnie wydatki w zależności od płci
ana.WykresSredniaGrupa('Płeć', 'Wydatki_total', "Średnie wydatki", "Średnie wydatki w zależności od płci", use_palette=True)

# Średni dochód w zależności od wykształcenia
ana.WykresSredniaGrupa('Wykształcenie', 'Roczny_dochód', "Średni dochód roczny", "Średni dochód roczny w zależności od wykształcenia", use_palette=True)
# Średnie wydatki w zależności od wykształcenia
ana.WykresSredniaGrupa('Wykształcenie', 'Wydatki_total', "Średnie wydatki", "Średnie wydatki w zależności od wykształcenia", use_palette=True)

# Zależność miedzy rocznym dochodem a oszczędnościami
ana.WykresZaleznosc('Roczny_dochód', 'Oszczędności', "Zależność między dochodem rocznym a oszczędnościami", grupowanie=False, korelacja=True)
# Zależność miedzy wydatkami na mieszkanie a zadłużeniem
ana.WykresZaleznosc('Wydatki_mieszkanie', 'Zadluzenie', "Zależność miedzy wydatkiem na mieszkanie a zadłużeniem", grupowanie=False, korelacja=True)

################################ Analiza zawodowa #######################################

# Różnica zarobków w zależności od stanowiska
ana.WykresPudelkowy('Stanowisko', 'Roczny_dochód', 'Roczne zarobki w zależności od stanowiska', 'Stanowisko', 'Zarobki')

# Różnica zarobków w zależności od branży
ana.WykresPudelkowy('Branża', 'Roczny_dochód', 'Roczne zarobki w zależności od branży', 'Branża', 'Zarobki')

# Trend zarobków w zależności od lat doświadczenia
ana.WykresZaleznosc('Lata_doświadczenia', 'Roczny_dochód', "Trend zarobków w zależności od doświadczenia", grupowanie=True, hue='Branża', style='Stanowisko', korelacja=True)

# Dominujące stanowiska w branży
ana.WykresSlupkowy('Branża', "Dominujące stanowiska w poszczególnych branżach", 'Liczba stanowisk', hue=True, section='Stanowisko', legend=True)

################################ Analiza korelacji zmiennych #############################

# Kolumny biorące udział w analizie
columns = ['Roczny_dochód', 'Wydatki_total', 'Wiek', 'Oszczędności', 'Lata_doświadczenia']
para = ['Wiek', 'Wykształcenie', 'Lata_doświadczenia', 'Oszczędności', 'Branża']

# Analiza korelacji zmiennych
ana.MacierzKorelacji(columns, "Macierz korelacji")

# Analiza rorzutu par zmiennych
ana.WykresRozrzutu(para)

############################# Analiza dochodu i wydatków #################################

# Kolumny wydatków
kolumny_wydatki = ['Wydatki_mieszkanie', 'Wydatki_żywność', 'Wydatki_transport', 'Wydatki_edukacja']

# Prcentowy udział wydatków w dochodzie rocznym
ana.WykresProcent('Roczny_dochód', kolumny_wydatki, "Procentowy udział wydatków w dochodzie")

############################### Analiza inwestycji #######################################

# Łączenie kolumn w jednej zmiennej/kolumnie
df_combined['Inwestycje'] = df_combined[['Inwestycje_akcje', 'Inwestycje_nieruchomości']].sum(axis=1)
dane = df_combined[['Inwestycje_akcje', 'Inwestycje_nieruchomości']]

# Średnia kwota inwestycji
ana.WykresSrednia(dane, "Średnie kwoty inwestycji", "Rodzaj inwestycji", "Średnia kwota")

# Analiza wpływu wieku na inwestycje
ana.WykresZaleznosc('Wiek', 'Inwestycje', "Wpływ wieku na inwestycje", regresja=True)

# Analiza wpływu dochodu na inwestycje
ana.WykresZaleznosc('Roczny_dochód', 'Inwestycje', "Wpływ dochodu na inwestycje", regresja=True)

# Analiza wpływu wykształcenia na inwestycje
ana.WykresSlupkowyLepszy('Wykształcenie', dane, 'Rodzaj_inwestycji', 'Kwota', "Wpływ wyksztalcenia na inwestycje", "Średnia kwota inwestycji" )

# Analiza zależności rodzaju inwestycji
ana.WykresZaleznosc('Inwestycje_akcje', 'Inwestycje_nieruchomości', "Zależnośc miedzy inwestycjami", korelacja=True)

############################### Analiza zadłużenia #########################################

# Analiza zadłużenia względem wieku
ana.WykresZaleznosc('Wiek', 'Zadluzenie',"Zależność między wiekiem a zadłużeniem" ,korelacja=True, grupowanie=True, hue='Osoby_zależne')

# Analiza zadłużenia względem dochodu
ana.WykresZaleznosc('Roczny_dochód', 'Zadluzenie',"Zależność między dochodem a zadłużeniem" ,korelacja=True, grupowanie=True, hue='Osoby_zależne')

############################### Wskażniki #################################################

# Wskażnik wydatków w dochodzie
ana.WykresProcent('Roczny_dochód', kolumny_wydatki, "Procentowy udział wydatków w dochodzie")

# Wskażnik oszczędności w dochodzie w zależności od wykształcenia
ana.WykresProcentDochod('Roczny_dochód', 'Oszczędności', 'Wykształcenie', "Procentowy udział oszczędności w dochodzie w zależności od wykształcenia")

# Wskażnik zadłużenia do dochodu
debet = ['Kredyty', 'Karty_kredytowe']
ana.WykresProcent('Roczny_dochód', debet, "Procentowy udział zadłużenia w dochodzie")

# Wskaźnik równowagi budżetowej w zależności od stanowiska/branży
ana.WykresDebet('Stanowisko', "Wskaźnik równowagi budżetowej w zależności od wykształcenia", second_column='Branża')