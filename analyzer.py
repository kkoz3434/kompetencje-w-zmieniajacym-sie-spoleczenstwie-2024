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


Kompetencje_mapa = {
    "niepotrzebne": 0,
    "w stopniu podstawowym": 1,
    "w średnim stopniu": 2,
    "w wysokim stopniu": 3,
    "w bardzo wysokim stopniu": 4,
}
def debug_print(dataframe, columnslist):
    for index, row in dataframe.iterrows():
        for column in columnslist:
            print(str(row[column]) + " | ", end="")
        print()


if __name__ == '__main__':
    df2018 = pd.read_spss(df_bkl_2018_2022_filename)
    print(df_bkl_2018_2022_filename + " ok")

    print(df2018.columns)
    columns = df2018.columns.tolist()
    print("XXXXXX")

    # filtrowanie po kluczowych stanowiskach
    filtered_kluczowe = df2018.loc[(df2018["P5_1kod"].isin(job_titles)) | (df2018["P5_2kod"].isin(job_titles))
                                   | (df2018["P5_3kod"].isin(job_titles)) | (df2018["P5_4kod"].isin(job_titles))
                                   | (df2018["P5_5kod"].isin(job_titles)), p5_columns].copy()

    # filtrowanie po poszukiwanych stanowiskach
    filtered_poszukiwane = df2018.loc[(df2018["P3_1_1kod"].isin(job_titles)) | (df2018["P3_2_1kod"].isin(job_titles))
                                      | (df2018["P3_3_1kod"].isin(job_titles)) | (df2018["P3_4_1kod"].isin(job_titles))
                                      | (df2018["P3_5_1kod"].isin(job_titles)) | (
                                          df2018["P3_6_1kod"].isin(job_titles)), p3_columns].copy()

    ## odfiltrowane: 194
    print(len(filtered_kluczowe))

    ## odfiltrowane: 34
    print(len(filtered_poszukiwane))

    # debug_print(filtered_kluczowe, p5_columns)
    # debug_print(filtered_poszukiwane, p3_columns)

