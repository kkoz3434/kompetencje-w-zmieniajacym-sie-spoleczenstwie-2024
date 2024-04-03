import pandas as pd

df_bkl_2018_2022_filename = "polaczona-baza-danych-z-badania-pracodawcow-bkl-2018-2022 (1).sav"
df_bkl_2017_2022_filename ="Połączona baza danych z badania ludności BKL 2017-2022 (SAV-SPSS).sav"

job_titles = [
    "Administrator baz danych",
    "Administrator bezpieczeństwa informacji (Inspektor ochrony danych)",
    "Administrator stron internetowych",
    "Administrator systemów komputerowych",
    "Analityk baz danych",
    "Analityk sieci komputerowych",
    "Analityk systemów teleinformatycznych",
    "Architekt stron internetowych",
    "Asystent usług telekomunikacyjnych",
    "Bioinformatyk",
    "Grafik komputerowy DTP",
    "Inżynier teleinformatyk",
    "Inżynier telekomunikacji",
    "Kierownik działu informatyki",
    "Kierownik rozwoju technologii informatycznych",
    "Kierownik sieci informatycznych",
    "Konserwator sieci i systemów komputerowych",
    "Monter sieci i urządzeń telekomunikacyjnych",
    "Nauczyciel informatyki / technologii informacyjnej",
    "Nauczyciel informatyki w szkole podstawowej",
    "Nauczyciel technologii informatycznych w placówkach pozaszkolnych",
    "Operator aplikacji komputerowych",
    "Programista aplikacji",
    "Programista aplikacji mobilnych",
    "Projektant / architekt systemów teleinformatycznych",
    "Projektant baz danych",
    "Serwisant sprzętu komputerowego",
    "Specjalista do spraw rozwoju oprogramowania systemów informatycznych",
    "Specjalista zastosowań informatyki",
    "Statystyk",
    "Technik analityk",
    "Technik cyfrowych procesów graficznych",
    "Technik informatyk",
    "Technik teleinformatyk",
    "Technik telekomunikacji",
    "Technolog inżynierii telekomunikacyjnej",
    "Tester oprogramowania komputerowego"
]

df2018 = pd.read_spss(df_bkl_2018_2022_filename)
print(df_bkl_2018_2022_filename + " ok")


# df2017 = pd.read_spss(df_bkl_2017_2022_filename)
# print(df_bkl_2017_2022_filename + " ok")
#

print(df2018.columns)
columns = df2018.columns.tolist()
print("XXXXXX")
# print(df2017.columns)

## lista zawodów - dostanę
## te rekordy które będą miały wymienione zapotrzebowanie na coś z listy - weź
## wyciągnij info jakie kompetencje są potrzebne

p5_columns = ["P5_1kod", "P5_2kod", "P5_3kod", "P5_4kod", "P5_5kod"]

# print(df2018.loc[df2018["P5_1kod"] == "Dyrektor szkoły", p5_columns])

filtered = df2018.loc[(df2018["P5_1kod"].isin(job_titles))  | (df2018["P5_2kod"].isin(job_titles)), p5_columns].copy()
print(filtered)



# mask to filter out the records which contains jobs we want
# mask = df2018[p5_columns].isin(job_titles).any()
# filtered_df2018 = df2018[mask]
# print(filtered_df2018)