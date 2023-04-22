import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
import openpyxl

MYTHS = [
    "Mýtus o možnosti oběti se ubránit (She wanted it)",
    "Mýtus o správné oběti znásilnění",
    "Mýtus o lineárním průběhu viktimizace aneb problém pozdního oznámení",
    "Pociťovaná věrohodnost (Emotional truth bias)",
    "Chyba retrospektivního úsudku (Rückschaufehler, Hindsight bias)",
    "Mýtus o rozdílných dopadech znásilnění, kterého se dopustí známý a neznámý pachatel",
    "K (domácímu) násilí dochází proto, že oběť provokuje",
    "Kdyby chtěla, mohla ho již dávno opustit",
    "Mýtus o atraktivitě oběti",
    "Mýtus o nulové újmě (No harm was done)",
    "Mýtus o pomstychtivé oběti, mýtus neexistence spravedlivého trestu pro pachatele",
    "Mýtus o “pravém znásilnění”, které probíhá formou přepadení, kdy je pachatel pro oběť neznámý",
    "Pachatel vnímán jako patologický jedinec (parafilik, např. pedofil).",
    "Znásilnění způsobuje hlavně těžkou újmu na tělesném zdraví",
    "Většina žen si znásilnění užívá. Ženy vnímají znásilnění jako agresivní sexuální styk nebo špatný sex",
    "Mýtus černobílého vnímání aktérů násilí",
    "Mýtus o nevyhnutelnosti násilí",
    "Mýtus o typickém pachateli násilí",
    "Mýtus o typické oběti násilí",
    "Mýtus o příčinném vlivu alkoholu nebo drog",
]

def Upload():
    st.title("Nahrajte rozsudek k analýze")

    with st.container():
        st.write("Rozsudek musí splňovat následující podmínky:")
        st.write("- Formát PDF (čitelný strojový text, ne fotografie)\n - Anonymizovaný")

    uploaded_file = st.file_uploader("Vyberte .pdf soubor", type="pdf")

    if uploaded_file is not None:
        st.success('Document uploaded successfully', icon="✅")
        # st.title(uploaded_file.name)
        df1 = pd.read_csv(
            "https://docs.google.com/spreadsheets/d/1Y7dVjKqs-3G1xYvAntZJ2kcJuKd59HDctJvcFq6FsS0/export?format=csv&gid=1378157160"
        )
        # df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
        
        st.subheader("Přehled rozsudkových mýtů")

        df = df1.loc[df1['court_document'] == uploaded_file.name.split(".")[0]]

        for item in df.itertuples():
            with st.container():
                includes = (item.gpt_confidence != None) & (item.gpt_confidence > 5);

                st.title("#" + str(item.myth) + " " + MYTHS[item.myth - 1]);

                if includes:
                    st.info("Rozsudek obsahuje citaci na tento mýtus")

                    # st.write(item.context_excerpts)

                    items = item.context_excerpts.replace("[", "").split("(Document(page_content=")

                    st.write("Citace z rozsudku indikující mýtus:")

                    print(len(items))

                    for i in range(1, len(items)):
                        item = items[i].split(", metadata=")[0]
                        st.info(item)

                else:
                    st.info("Rozsudek neobsahuje citaci na tento mýtus")

        # AgGrid(df1)
            
