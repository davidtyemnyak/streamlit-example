import pandas as pd

data = [    
    ['66T 103/2015-173', 'Krajský soud v Brně', 'krajský soud', 'vinen', 'nepodmíněný', '2 roky', '10 000 Kč', 2015, 'Brno', '49.1951,16.6068', 'Jihomoravský kraj', 'Mýtus o možnosti oběti se ubránit', 'no', 8],
    ['66T 103/2015-175', 'Okresní soud v Brně', 'okresní soud', 'nevinný', 'podmíněný', '',  '5 000 Kč', 2017, 'Brno', '49.1951,16.6068', 'Jihomoravský kraj', 'Mýtus o možnosti oběti se ubránit', 'yes', 9],
    ['66T 103/2015-174', 'Okresní soud v Ostravě', 'okresní soud', 'vinen', 'nepodmíněný', '1 rok', '', 2019, 'Ostrava', '49.8345,18.282', 'Moravskoslezský kraj', 'Mýtus o možnosti oběti se ubránit', 'no', 7],
    ['66T 103/2015-173', 'Krajský soud v Brně', 'krajský soud', 'vinen', 'nepodmíněný', '2 roky', '10 000 Kč', 2015, 'Brno', '49.1951,16.6068', 'Jihomoravský kraj', 'Mýtus o možnosti oběti se ubránit', 'no', 8],
    ['66T 103/2015-175', 'Okresní soud v Brně', 'okresní soud', 'nevinný', 'podmíněný', '', '5 000 Kč', 2017, 'Brno', '49.1951,16.6068', 'Jihomoravský kraj', 'Mýtus o možnosti oběti se ubránit', 'yes', 9],
    ['66T 103/2015-174', 'Okresní soud v Ostravě', 'okresní soud', 'vinen', 'nepodmíněný', '1 rok', '', 2019, 'Ostrava', '49.8345,18.282', 'Moravskoslezský kraj', 'Mýtus o možnosti oběti se ubránit', 'no', 7],
    ['66T 103/2015-176', 'Krajský soud v Praze', 'krajský soud', 'vinen', 'podmíněný', '1 rok', '5 000 Kč', 2020, 'Praha', '50.0755,14.4378', 'Hlavní město Praha', 'Mýtus o nutnosti tvrdého trestu', 'yes', 6],
    ['66T 103/2015-177', 'Okresní soud v Plzni', 'okresní soud', 'vinen', 'nepodmíněný', '3 roky', '', 2018, 'Plzeň', '49.7475,13.3776', 'Plzeňský kraj', 'Mýtus o neefektivnosti soudního systému', 'no', 7]
]

pandas_frame = pd.DataFrame(data, columns=['Spisová značka ID', 'Název soudu', 'Typ soudu', 'Výsledek rozsudku', 'Druh trestu', 'Délka trestu', 'Kompenzace', 'Rok vyhotovení', 'Město', 'Souřadnice', 'Kraj', 'GPT output', 'Myth', 'Confidency Level'])
