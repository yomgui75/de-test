def journal_mentionned_ditinct_number() -> dict:
    """
    return the number of disctinct drug associated to a journal
    """
    from Common.json_tool import read_json
    from variables import output_path

    relationships =  read_json(output_path)

    journal_rate = {}
    for drug in [*relationships]:
        for dataset in relationships[drug]:
            for journal in relationships[drug][dataset]:
                journal_name = journal["journal"]
                if journal_rate.get(journal_name, "") and drug not in journal_rate[journal_name]:
                    journal_rate[journal_name] += [drug]
                else:
                    journal_rate[journal_name] = [drug]
    for journal_name in [*journal_rate]:
        journal_rate[journal_name] = len(journal_rate[journal_name])
    return journal_rate


def sort_dict_value(d: dict, reverse=True) -> dict:
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


def largest_value(d: dict) -> list:
    """
    return journal name corrsponding to largest values"""
    d = sort_dict_value(d)
    journals = []
    for count, journal_name in enumerate([*d]):
        if count==0:
            largest_value = d[journal_name]
        
        if largest_value==d[journal_name]:
            journals.append(journal_name)
    return journals

journals = largest_value(journal_mentionned_ditinct_number())
if len(journals)==0:
    print(f"There are no journals")
elif len(journals)==1:
    print(f"Journal which mentionned the largest number of distinct drugs is {journals[0]}")
else:
    print(f"""Journals which mentionned the largest number of distinct drugs are "{'", "'.join(journals)}" """)
