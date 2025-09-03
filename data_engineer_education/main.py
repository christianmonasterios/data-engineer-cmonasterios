import pandas as pd
import importlib
import json
from pathlib import Path
import sqlite3

INPUT_DIR = "/Users/teracode/Documents/workspace/data-engineer-cmonasterios/data_engineer_education"
# My Database
conn = sqlite3.connect("/Users/teracode/Documents/workspace/ia/ia/dataDE.db")

def get_sources(config_path=f'{INPUT_DIR}/config/data_sources.json'):
    with open(config_path) as f:
        return json.load(f)


if __name__ == "__main__":
    # Get Source List to process:
    sources = get_sources()
    print(sources)

    for source in sources:
        file_path = f'{INPUT_DIR}/datasets/{source["filename"]}.csv'
        mapping_module = importlib.import_module(f'mappings.{source["mapping"]}')

        # READING INPUT FILE:
        print(f"Processing: {file_path}")
        df = pd.read_csv(file_path)
        df_mapped = mapping_module.map_to_standard(df)

        # READING TARGET TABLE:
        query = "select distinct phone, address1 from educations"
        df_target = pd.read_sql_query(query, conn)

        # CHECK IF THE RECORD WAS ALREADY PROCESSED
        # LEFT JOIN BY PHONE + ADDRESS1

        df_merged = df_mapped.merge( df_target, on=["phone", "address1"], how="left", indicator=True)
        df_to_target = df_merged[df_merged["_merge"] == "left_only"]
        df_to_target = df_to_target.drop(columns=["_merge"])

        # Load Data into Target Table:

        df_to_target.to_sql("educations", conn, if_exists="append", index=False)

    conn.close()

