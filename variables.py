data_path = {
    "drugs": "python_test_de/Data/drugs.csv",
    "clinical_trials": "python_test_de/Data/clinical_trials.csv",
    "pubmed.csv": "Python_test_de/Data/pubmed.csv",
    "pubmed.json": "python_test_de/Data/pubmed.json"
}

output_path = "python_test_de/Data/results.json"

to_clean = [["\xc3\x28", ""], ["\xc3\xb1", ", "], ["\u00e8ve", ""], ["\u00f4", "o"], ["\\xc3\\x28", ""]]
