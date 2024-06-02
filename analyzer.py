import pandas as pd

df_bkl_2018_2022_filename = "polaczona-baza-danych-z-badania-pracodawcow-bkl-2018-2022 (1).sav"
df_bkl_2017_2022_filename = "Połączona baza danych z badania ludności BKL 2017-2022 (SAV-SPSS).sav"

# kolumny wskazujące kluczowe stanowiska dla przedsiebiorstwa
p5_columns = ["P5_1kod", "P5_2kod", "P5_3kod", "P5_4kod", "P5_5kod"]

# kolumny wskazujace POSZUKIWANYCH OBECNIE stanowisk
p3_columns = ["P3_1_1kod", "P3_2_1kod", "P3_3_1kod", "P3_4_1kod", "P3_5_1kod", "P3_6_1kod"]

# brane pod uwage stanowiska
job_titles = [
    'Administrator baz danych',
    'Administrator bezpieczeństwa informacji (Inspektor ochrony danych)',
    'Administrator stron internetowych',
    'Administrator systemów komputerowych',
    'Analityk baz danych',
    'Analityk sieci komputerowych',
    'Analityk systemów teleinformatycznych',
    'Architekt stron internetowych',
    'Asystent usług telekomunikacyjnych',
    'Bioinformatyk',
    'Grafik komputerowy DTP',
    'Inżynier teleinformatyk',
    'Inżynier telekomunikacji',
    'Kierownik działu informatyki',
    'Kierownik rozwoju technologii informatycznych',
    'Kierownik sieci informatycznych',
    'Konserwator sieci i systemów komputerowych',
    'Monter sieci i urządzeń telekomunikacyjnych',
    'Nauczyciel informatyki / technologii informacyjnej',
    'Nauczyciel informatyki w szkole podstawowej',
    'Nauczyciel technologii informatycznych w placówkach pozaszkolnych',
    'Operator aplikacji komputerowych',
    'Programista aplikacji',
    'Programista aplikacji mobilnych',
    'Projektant / architekt systemów teleinformatycznych',
    'Projektant baz danych',
    'Serwisant sprzętu komputerowego',
    'Specjalista do spraw rozwoju oprogramowania systemów informatycznych',
    'Specjalista zastosowań informatyki',
    'Statystyk',
    'Technik analityk',
    'Technik cyfrowych procesów graficznych',
    'Technik informatyk',
    'Technik teleinformatyk',
    'Technik telekomunikacji',
    'Technolog inżynierii telekomunikacyjnej',
    'Tester oprogramowania komputerowego',
]

kompetencje_wartosci_2018_2020 = {
    "": 0,
    "niepotrzebne": 0,
    "w stopniu podstawowym": 1,
    "w średnim stopniu": 2,
    "w wysokim stopniu": 3,
    "w bardzo wysokim stopniu": 4,
}

kompetencje_wartości_2022 = {
    "" : 0,
    "znacznie straci" : 0,
    "trochę straci" : 1,
    "nie zmieni się" : 2,
    "trochę zyska" : 3,
    "znacznie zyska" : 4
}

kompetencje_klucz_nazwa = {
    'K1': 'analiza informacji i wyciągania wniosków',
    'K2': "uczenie się nowych rzeczy",
    'K3': "posługiwanie się komputerem, tabletem smartfonem",
    'K4': "obsługa specjalistycznych programów komputerowych",
    'K5': "obsługa maszyn, narzędzi i urządzeń technicznych",
    'K6': "montaż i naprawa maszyn i urządzeń technicznych",
    'K7': "wykonywanie prostych rachunków",
    'K8': "wykonywanie zaawansowanych obliczeń matematycznych",
    'K9': "zdolności artystyczne",
    'K10': "sprawność fizyczna",
    'K11': "radzenie sobie w sytuacjach stresujących",
    'K12': "gotowość do brania na siebie odpowiedzialności za wykonanie zadań",
    'K13': "pomysłowość, kreatywność",
    'K14': "zarządzanie czasem i terminowość",
    'K15': "samodzielna organizacja pracy",
    'K16': "praca w grupie",
    'K17': "łatwe nawiązywanie kontaktów z ludźmi",
    'K18': "bycie komunikatywnym i jasne przekazywanie myśli",
    'K19': "współpraca z osobami różnych narodowości",
    'K20': "praca administracyjna i prowadzenie dokumentacji",
    'K21': "koordynowanie pracy innych osób",
    'K22': "rozwiązywanie konfliktów między ludźmi",
    'K23': "gotowość do częstych wyjazdów i zmiany miejsca pracy",
    'K24': "gotowość do pracy w nietypowych godzinach wymaganych przez pracodawcę",
    'K25': "biegłe posługiwanie się językiem polskim w mowiei piśmie (poprawność językowa, bogate słownictwo, łatwość wysławiania się)",

    'KP1': 'analiza informacji i wyciągania wniosków',
    'KP2': "uczenie się nowych rzeczy",
    'KP3': "posługiwanie się komputerem, tabletem smartfonem",
    'KP4': "obsługa specjalistycznych programów komputerowych",
    'KP5': "obsługa maszyn, narzędzi i urządzeń technicznych",
    'KP6': "montaż i naprawa maszyn i urządzeń technicznych",
    'KP7': "wykonywanie prostych rachunków",
    'KP8': "wykonywanie zaawansowanych obliczeń matematycznych",
    'KP9': "zdolności artystyczne",
    'KP10': "sprawność fizyczna",
    'KP11': "radzenie sobie w sytuacjach stresujących",
    'KP12': "gotowość do brania na siebie odpowiedzialności za wykonanie zadań",
    'KP13': "pomysłowość, kreatywność",
    'KP14': "zarządzanie czasem i terminowość",
    'KP15': "samodzielna organizacja pracy",
    'KP16': "praca w grupie",
    'KP17': "łatwe nawiązywanie kontaktów z ludźmi",
    'KP18': "bycie komunikatywnym i jasne przekazywanie myśli",
    'KP19': "współpraca z osobami różnych narodowości",
    'KP20': "praca administracyjna i prowadzenie dokumentacji",
    'KP21': "koordynowanie pracy innych osób",
    'KP22': "rozwiązywanie konfliktów między ludźmi",
    'KP23': "gotowość do częstych wyjazdów i zmiany miejsca pracy",
    'KP24': "gotowość do pracy w nietypowych godzinach wymaganych przez pracodawcę",
    'KP25': "biegłe posługiwanie się językiem polskim w mowiei piśmie (poprawność językowa, bogate słownictwo, łatwość wysławiania się)",

}

def debug_print(dataframe, columnslist):
    for index, row in dataframe.iterrows():
        for column in columnslist:
            print(str(row[column]) + " | ", end="")
        print()


def count_scores_for_given_competitions(df):
    # 2018 2020
    kolumny_K = [f'K{i}' for i in range(1, 26)]
    # 2022
    kolumny_KP = [f'KP{i}' for i in range(1, 26)]

    # tłumaczenie string -> int
    df[kolumny_K] = df[kolumny_K].map(kompetencje_wartosci_2018_2020.get)
    df[kolumny_KP] = df[kolumny_KP].map(kompetencje_wartości_2022.get)

    debug_print(df, kolumny_K + kolumny_KP)



if __name__ == '__main__':
    df2018 = pd.read_spss(df_bkl_2018_2022_filename)
    print(df_bkl_2018_2022_filename + " ok")

    print(df2018.columns)
    columns = df2018.columns.tolist()
    print("XXXXXX")

    # filtrowanie po kluczowych stanowiskach
    filtered_kluczowe = df2018.loc[(df2018["P5_1kod"].isin(job_titles)) | (df2018["P5_2kod"].isin(job_titles))
                                   | (df2018["P5_3kod"].isin(job_titles)) | (df2018["P5_4kod"].isin(job_titles))
                                   | (df2018["P5_5kod"].isin(job_titles))].copy()

    # filtrowanie po poszukiwanych stanowiskach
    filtered_poszukiwane = df2018.loc[(df2018["P3_1_1kod"].isin(job_titles)) | (df2018["P3_2_1kod"].isin(job_titles))
                                      | (df2018["P3_3_1kod"].isin(job_titles)) | (df2018["P3_4_1kod"].isin(job_titles))
                                      | (df2018["P3_5_1kod"].isin(job_titles)) | (
                                          df2018["P3_6_1kod"].isin(job_titles))].copy()

    ## odfiltrowane: 194
    print(len(filtered_kluczowe))

    ## odfiltrowane: 34
    print(len(filtered_poszukiwane))

    # debug_print(filtered_poszukiwane, p3_columns)

    # pokazać dane z bulldoga i porównać nasze, można wziąć gotowe wykresy
