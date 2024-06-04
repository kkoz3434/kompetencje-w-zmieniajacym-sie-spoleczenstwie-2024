import pandas as pd
import matplotlib.pyplot as plt
import os

df_bkl_2018_2022_filename = "polaczona-baza-danych-z-badania-pracodawcow-bkl-2018-2022 (1).sav"
df_bkl_2017_2022_filename = "Połączona baza danych z badania ludności BKL 2017-2022 (SAV-SPSS).sav"

# kolumny wskazujące kluczowe stanowiska dla przedsiebiorstwa
p5_columns = ["P5_1kod", "P5_2kod", "P5_3kod", "P5_4kod", "P5_5kod"]

# kolumny wskazujace POSZUKIWANYCH OBECNIE stanowisk
p3_columns = ["P3_1_1kod", "P3_2_1kod", "P3_3_1kod", "P3_4_1kod", "P3_5_1kod", "P3_6_1kod"]

# brane pod uwage stanowiska
job_titles_filename = 'lista_zawodow_filtrowana.csv'
job_titles_df = pd.read_csv(job_titles_filename)
job_titles = dict(zip(job_titles_df['zawód'], job_titles_df['typ']))

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

def filter_it(df):
    return  df.loc[df[p5_columns].isin(job_titles.keys()).any(axis=1)].copy()

def separate_by_most_wanted_job_types(df):
    # Initialize empty lists to collect rows for each type
    rows_a = []
    rows_p = []
    rows_t = []

    # Iterate through each row and count job types
    for idx, row in df.iterrows():
        counts = {"a": 0, "p": 0, "t": 0}
        for col in p5_columns:
            job_name = row[col]
            job_type = job_titles.get(job_name, None)
            if job_type:
                counts[job_type] += 1
        
        # Determine the max job type count
        max_job_type = max(counts, key=counts.get)
        
        # Append the row to the corresponding list
        if max_job_type == "a":
            rows_a.append(row)
        elif max_job_type == "t":
            rows_t.append(row)
        else:
            rows_p.append(row)

    # Convert lists to dataframes
    df_a = pd.DataFrame(rows_a)
    df_p = pd.DataFrame(rows_p)
    df_t = pd.DataFrame(rows_t)

    return df_a, df_p, df_t

def divide_by_year_and_job_type(df):
    years = [2018, 2020, 2022]
    job_types = ['a', 'p', 't']
    dfs = {year: {type: None for type in job_types} for year in years}

    for year in years:
        df_year = df[df['edycja'] == year]
        df_a, df_p, df_t = separate_by_most_wanted_job_types(df_year)
        dfs[year]['a'] = df_a
        dfs[year]['p'] = df_p
        dfs[year]['t'] = df_t
    
    return dfs

def count_competencies(df):
    combined_competency_values = {**kompetencje_wartosci_2018_2020, **kompetencje_wartości_2022}
    competency_sums = {key: 0 for key in kompetencje_klucz_nazwa.keys() if not key.startswith('KP')}
    
    for competency in competency_sums.keys():
        kp_competency = 'KP' + competency[1:]
        if competency in df.columns:
            competency_sums[competency] += df[competency].map(combined_competency_values).sum()
        if kp_competency in df.columns:
            competency_sums[competency] += df[kp_competency].map(combined_competency_values).sum()
    
    return competency_sums

def determine_popularities(competency_sums):
    values = list(competency_sums.values())
    sorted_indices = sorted(range(len(values)), key=lambda i: values[i], reverse=True)
    top_5_most = {list(competency_sums.keys())[i]: list(competency_sums.values())[i] for i in sorted_indices[:5]}
    top_5_least = {list(competency_sums.keys())[i]: list(competency_sums.values())[i] for i in sorted_indices[-5:]}
    return top_5_most, top_5_least

def plot_competencies(competency_sums, top_5_most, top_5_least, title, filename):
    # Extract the keys and values from the competency sums dictionary
    competencies = list(competency_sums.keys())
    values = list(competency_sums.values())
    
    # Create a color list where default color is skyblue
    colors = ['skyblue'] * len(values)
    
    # Assign colors to the top 5 most and least popular competencies
    for comp in top_5_most.keys():
        idx = competencies.index(comp)
        colors[idx] = 'green'
    for comp in top_5_least.keys():
        idx = competencies.index(comp)
        colors[idx] = 'red'
    
    # Create the bar plot
    plt.figure(figsize=(10, 6))
    plt.bar(competencies, values, color=colors)
    
    # Add title and labels
    plt.title(title)
    plt.xlabel('Competencies')
    plt.ylabel('Total Value')
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=90)
    
    # Save plot as PNG file
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

if __name__ == '__main__':
    df = pd.read_spss(df_bkl_2018_2022_filename)

    # Filter rows based on key positions
    df_it = filter_it(df)
    print("IT related rows:", df_it.shape[0])

    # Divide by year and job type
    dfs = divide_by_year_and_job_type(df_it)
    
    # Count competencies for each df and save results
    years = [2018, 2020, 2022]
    job_types = ['a', 'p', 't']
    job_type_names = {'a': 'Analysts', 'p': 'Programmers', 't': 'Technicians'}
    
    # Prepare results list for CSV
    results = []

    # Ensure results directories exist
    os.makedirs('results/plots', exist_ok=True)
    
    for year in years:
        for job_type in job_types:
            competencies_count = count_competencies(dfs[year][job_type])
            top_5_most, top_5_least = determine_popularities(competencies_count)
            
            # Save plot
            title = f"Competencies for {job_type_names[job_type]} in {year}"
            filename = f"results/plots/{job_type_names[job_type]}_{year}.png"
            plot_competencies(competencies_count, top_5_most, top_5_least, title, filename)
            
            # Add results to the list for CSV
            result_row = {
                'year': year,
                'job_type': job_type_names[job_type],
                **{f'top_{i+1}': kompetencje_klucz_nazwa[comp] for i, comp in enumerate(top_5_most.keys())},
                **{f'least_{i+1}': kompetencje_klucz_nazwa[comp] for i, comp in enumerate(top_5_least.keys())}
            }
            results.append(result_row)
    
    # Save results to CSV
    results_df = pd.DataFrame(results)
    results_df.to_csv('results/results.csv', index=False)