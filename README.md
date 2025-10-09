# Assignment 2 (Lite, Split) — Single-Table Patient Roster in SQLite

The purpose of this assignment is to learn how to load patient data from a CSV file using Pandas/SQLAlchemy in SQLite to run simple queries. 

## Repo Scaffold
Create repo in the following way: 
```
health-sqlite-lite/
├─ data/
│  └─ patients.csv
├─ sql/
│  ├─ schema.sql
│  └─ analysis.sql
├─ src/
│  ├─ create_db.py         
│  └─ import_csv.py        
├─ clinic_simple.db        
├─ requirements.txt
└─ README.md
```

## Run Steps
1. Make sure Python, Pandas, and AQLAlchemy are installed and that the `patients.csv` is in the correct folder. 
2. Install dependencies: `pip install -r requirements.txt`
3. Run `src/create_db.py` to create `clinic_simple.db` 
4. Run `src/import_csv.py` to load data from `data/patients.csv` into the database.
5. Open `clinic_simple.db` by selecting **Reveal in File Explorer**
6. Select **Open Database** on SQLite and load the `clinic_simple.db` file
7. Then select **Execute SQL** and select the **Open** button to load the `sql.analysis.sql` file 
8. Click the **Execute** button to run the queries line by line to get the results for each section (A-D).
9. Lastly go to the **Browse Data** and in the **Table** dropdown bar, select `patients`, this will show you our results. 


### Query A: Counts total number of patients in the table
- There are 500 rows of patients in the dataset which matches the number of patients in the CSV file. 

![Query A](health-sqlite-lite/images/query_a.png)

### Query B: Generates top primary diagnoses by count
- There were 16 common primary icd10 codes with I10 *(Essential Hypertension)* being the most common.

<img src="health-sqlite-lite/images/query_b.png" alt="Query B" width="300">


### Query C: Generates office-visit CPTs since Jan 1, 2025 (CPT codes starting with 992)
- There were 94 office-visit CPTs since Jan 1, 2025 (CPT codes starting with 992).

![Query C](health-sqlite-lite/images/query_c.png)


### Query D: Gives us the approximate age at last visit for the 5 oldest patients
- This is the age of the five oldest patients at their last visit. All five patients were 85 years old. 

![Query D](health-sqlite-lite/images/query_d.png)

### Query E: Quick data quality check: any blank codes?
- This query checks for missing `primary_icd10` OR missing `last_cpt`. The result was 0 blank codes which indicates good data quality. 

![Query E](health-sqlite-lite/images/query_e.png)