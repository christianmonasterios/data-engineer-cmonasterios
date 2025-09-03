import pandas as pd

def map_to_standard(df):
    data_df = pd.DataFrame()

    data_df["accepts_financial_aid"] = ""
    data_df["ages_served"] = df[['Infant', 'Toddler', 'Preschool', 'School']].apply(
        lambda row: ', '.join([age for age, val in row.items() if val.strip().upper() == 'Y']),
        axis=1
    )

    data_df["capacity"] = df['Capacity']
    data_df["certificate_expiration_date"] = ""
    data_df["city"] = df['City']
    data_df["address1"] = df['Address']
    data_df["address2"] = ""
    data_df["company"] = df['Operation Name']
    data_df["phone"] = df['Phone']
    data_df["phone2"] = ""
    data_df["county"] = df['County'].str.title()
    data_df["curriculum_type"] = ""
    data_df["email"] = df['Email Address']
    data_df["first_name"] = ""
    data_df["language"] = ""
    data_df["last_name"] = ""
    data_df["license_status"] = df['Status']
    data_df["license_issued"] = df['Issue Date']
    data_df["license_number"] = df['Facility ID']  # could also df['Operation']
    data_df["license_renewed"] = ""
    data_df["license_type"] = df['Type']
    data_df["licensee_name"] = ""
    data_df["max_age"] = ""
    data_df["min_age"] = ""
    data_df["operator"] = ""
    data_df["provider_id"] = df['Operation']  # could also df['Facility ID']
    data_df["schedule"] = ""
    data_df["state"] = df['State']
    data_df["title"] = ""
    data_df["website_address"] = ""
    data_df["zip"] = df['Zip']
    data_df["facility_type"] = df['Type']

    return data_df