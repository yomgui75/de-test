import pandas as pd
from Common.json_tool import read_json, write_json


def lower_clean_data(text: str) -> str:
    from variables import to_clean
    
    for word, replacement in to_clean:
        text = text.replace(word, replacement)
    return text.lower()


def load_data():
    """
    return all data loaded
    """
    from variables import data_path

    #CSV LOAD
    df_drugs = pd.read_csv(data_path["drugs"])
    df_clinical_trials = pd.read_csv(data_path["clinical_trials"])
    df_pubmed = pd.read_csv(data_path["pubmed.csv"])
    
    #JSON LOAD
    json_pubmed = read_json(data_path["pubmed.json"])
    return df_drugs, df_clinical_trials, df_pubmed, json_pubmed


def convert_date(date: str):
    """
    params date :
    return date with format dd/mm/YYYY
    """
    from dateutil.parser import parse
    return parse(date, fuzzy_with_tokens=True)[0].strftime("%d/%m/%Y")
    


def drug_mentionned_in_csv(drug: str, title_name: str, id_name: str, date_name: str, journal_name: str, df: pd.DataFrame) -> list:
    """
    params drug (string): drug name
    params title_name (string): title column's name
    params id_name (string): id column's name
    params date_name (string): date column's name
    params journal_name (string): journal column's name
    params df (datafarame): dataframe that contains the data
    return (list of dict) id and date of the article
    """
    titles = df[title_name].to_list()
    ids = df[id_name].to_list()
    dates = df[date_name].to_list()
    journals = df[journal_name].to_list()
    return [{"id": id, "date_mention": convert_date(date), "journal": lower_clean_data(journal)} 
            for id, title, date, journal in zip(ids, titles, dates, journals) 
            if lower_clean_data(drug) in lower_clean_data(title)]


def drug_mentionned_in_list_json(drug: str, title: str, id: str, date: str, journal: str, list_json_file: list) -> list:
    """
    params drug (string): drug name
    params title (string): title column's name
    params id (string): id column's name
    params date (string): date column's name
    params journal (string): journal column's name
    params list_json_file (list of dicts): contains the data
    return (list of dict) id and date of the article
    """
    return [{"id": pub[id], "date_mention": convert_date(pub[date]), "journal": lower_clean_data(pub[journal])} 
            for pub in list_json_file 
            if lower_clean_data(drug) in lower_clean_data(pub[title])]


def json_relationship() -> dict: 
    df_drugs, df_clinical_trials, df_pubmed, json_pubmed = load_data()
    relationships = {}
    for drug_name in df_drugs["drug"]:
        articles = {}
        articles["clinical_trials"] = drug_mentionned_in_csv(drug_name, "scientific_title", "id", "date", "journal", df_clinical_trials)
        articles["pubmed"] = drug_mentionned_in_csv(drug_name, "title", "id", "date", "journal", df_pubmed)
        articles["journal"] = drug_mentionned_in_list_json(drug_name, "title", "id", "date", "journal", json_pubmed)
        relationships[drug_name] = articles
    return relationships


def write_output(d: dict):
    from variables import output_path
    import json
    write_json(output_path, d)


write_output(json_relationship())