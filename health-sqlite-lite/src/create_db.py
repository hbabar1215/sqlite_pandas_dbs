import sqlite3

DB_PATH = "clinic_simple.db"
CSV_PATH = "health-sqlite-lite/data/patients.csv"
SCHEMA_PATH = "health-sqlite-lite/sql/schema.sql"

def main():

    # Read the schema SQL file.
   with open(SCHEMA_PATH, encoding="utf-8") as f:
    schema_sql = f.read()


    # Create (or overwrite) the database and apply the schema.
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        conn.commit()

    print(f"Created database: {DB_PATH}")

if __name__ == "__main__":
    main()
