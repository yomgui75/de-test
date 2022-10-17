# Introduction
This repository is a pre-interview test used to shortlist developper. 
The test is described through the pdf named "test_python_de.pdf"

# Installation 
To deal with this project, I am using the IDE named VSCode 
I also installed some packages that I deeply recommand in order to deal with documents : 
* raimbow csv : helps to visualize csv in VSCode
* vscode-pdf : helps to display pdf 

Besides, I have a package named "Git Graph" that helps to describe all branches and commits of a repository

# Data 

The folder named "Data" is composed of files needed to resolve the test. 
* pubmed.json (list of json):  
  * id (string / int / empty string) : id of the article
  * title (string) : title of the article
  * date (string (format dd/mm/YYYY)) : date of publication
  * journal (string): newspaper where the article is published
* pubmed.csv :
  * id (int) : id of the article
  * title (string) : title of the article
  * date (date (format dd/mm/YYYY)) : date of publication
  * journal (string): newspaper where the article is published
* drug.csv :
  * atccode (string): id of the drug
  * drug (string) : name of the drug 
* clinical_trials.csv : 
  * id (string / empty string) : id of the publication
  * scientific_title (string / empty string) : title of the publication
  * date (date dd month YYYY) : date of the publication
  * journal (string) : newspaper where the article is published

**Remarks :** 
* pubmed's id and date are of a different types between both format 
* data cleaning must be done. The sample is very small then I did it very quickly. This exercise reminds the one I have done during my study, you can have a look to my thesis.

# Launch the repository
When running the file "main.py", it uploads a new json file named "Data/results.json". 

This file has this shape :
* name of the drug 
  * clinical_trials 
    * list of id, date of publication, journal's name
  * pubmed
    * list of id, date of publication, journal's name
  * journal 
    * list of id, date of publication, journal's name

# Ad-hpoc questions :

By running "ad_hoc.py" file we get the name of the newpaper that mentionned the number of most different drugs. 

# Questions to go further :

 **Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?**

If we use our computer to deal with the data then we could use the library named "dask". This library aims to reduce data loaded in memory by working on chunks of data. It also parallelize the work. As spark, dask is evaluating the operation when you ask for, in fact all code writtes before evaluation composed the final query. 

If we can use public cloud, then we can use cloud managed services. This implies that we terraform the creation of every services if we can. 
Therefore we could use :
* GCS : store the csv and json file 
* BQ : store the csv and json file into a relational databases
* BQ engine : to build sql queries that do the work

If we prefer coding in python, it is possible to use kubernetes cluster to do the transformation. But kubernetes cluster can be expansive if we have only one application, therefore it is better to use Dataflow service.

 **Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?**

It could be interessting to partionnate the BQ tables in order to optimize the read.
If you like to use SQL queries, you could use a DAG tool, for example DBT or Matillion
If you like to use Python coding, you could use Airflow to build task. These tasks could call cloud services, in order to transform the data, via API calls.

Also, if we use tera bytes of data and cloud services, with python code, it could be interesting to keep this example in order to build unitary tests. Mocking different services and launch the test each time we commit a changement. Besides, we could have a deployement pipeline such as Jenkins, this is usefull when deploying infra via terraform and build a mirorring with the application repository to automatically propagate the code to the cloud services. Therefore, we build two repositories : application (contains python code) and infrastructure (contains IaC coding in terraform)

Finally, if the user doesn't want to deal with infrastructure issues and maintenance then he could use a SaaS cloud plateform such as Snwoflake.

**We can of course give more accurate answers, I will be happy to talk about it during an interview.**