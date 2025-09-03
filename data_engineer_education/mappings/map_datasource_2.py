import pandas as pd

def map_to_standard(df):
    data_df = pd.DataFrame()
    data_df['accepts_financial_aid'] = df['Accepts Subsidy'].apply(lambda x: 'Yes' if 'Accepts' in str(x) else 'No')
    data_df["ages_served"] = df[['Ages Accepted 1', 'AA2', 'AA3', 'AA4']].astype(str).agg(', '.join,
                                                                                          axis=1).str.replace('nan',
                                                                                                              '').str.strip(
        ', ')
    data_df["capacity"] = df['Total Cap']
    data_df["certificate_expiration_date"] = ""
    data_df['city'] = df['City'].str.title()
    data_df['address1'] = df['Address1'].str.strip()
    data_df['address2'] = df['Address2'].fillna('').str.strip()
    data_df["company"] = df['Company'].str.strip()
    data_df["phone"] = df['Phone']
    data_df["phone2"] = ""
    data_df["county"] = ""
    data_df["curriculum_type"] = df['Star Level']
    data_df["email"] = df['Email']
    data_df["language"] = ""
    data_df["license_status"] = ""
    data_df['license_issued'] = df['License Monitoring Since'].str.extract(r'(\d{4}-\d{2}-\d{2})')
    data_df['license_number'] = df['Type License'].str.extract(r'-\s*(K\d+)', expand=False)
    data_df["license_renewed"] = ""
    data_df["license_type"] = df['Type License'].str.extract(r'^(.*?)\s*-', expand=False).str.strip()
    data_df["licensee_name"] = df['Primary Caregiver'].str.extract(r'^"?([^\n"]+)')[0].str.strip()
    data_df["max_age"] = ""
    data_df["min_age"] = ""
    data_df['operator'] = df['Primary Caregiver'].str.extract(r'^"?([^\n"]+)')[0].str.strip()
    data_df[['first_name', 'last_name']] = data_df['operator'].str.extract(r'^(\w+)\s+(.*)$')
    data_df['title'] = df['Primary Caregiver'].str.extract(r'\n+\s*([^\n"]+)\s*"?$', expand=False).str.strip()
    data_df["provider_id"] = ""
    data_df["schedule"] = df[['Mon', 'Tues', 'Wed', 'Thurs', 'Friday', 'Saturday', 'Sunday']].astype(str).agg(
        ' | '.join, axis=1)
    data_df['state'] = df['State']
    data_df["website_address"] = ""
    data_df['zip'] = df['Zip'].astype(str).str.zfill(5)
    data_df["facility_type"] = data_df["license_type"]

    ordered_cols = [
        "accepts_financial_aid", "ages_served", "capacity", "certificate_expiration_date",
        "city", "address1", "address2", "company", "phone", "phone2", "county",
        "curriculum_type", "email", "first_name", "language", "last_name", "license_status",
        "license_issued", "license_number", "license_renewed", "license_type",
        "licensee_name", "max_age", "min_age", "operator", "provider_id", "schedule",
        "state", "title", "website_address", "zip", "facility_type"
    ]

    data_df = data_df[ordered_cols]

    return data_df