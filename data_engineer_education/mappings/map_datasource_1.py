import pandas as pd

def map_to_standard(df):
    # Renombrar columnas
    data_df = pd.DataFrame()
    data_df["accepts_financial_aid"] = ""
    data_df["ages_served"] = ""
    data_df["capacity"] = ""
    data_df["certificate_expiration_date"] = df["Expiration Date"]
    data_df["city"] = df["Address"].str.extract(r"\s([A-Z\s]+),?\s+[A-Z]{2}\s+\d{5}$")[0].str.strip()
    data_df["address1"] = df["Address"]
    data_df["address2"] = ""
    data_df["company"] = df["Name"]
    data_df["phone"] = df["Phone"]
    data_df["phone2"] = ""
    data_df["county"] = df["County"]
    data_df["curriculum_type"] = ""
    data_df["email"] = ""
    data_df["first_name"] = ""
    data_df["language"] = ""
    data_df["last_name"] = ""
    data_df["license_status"] = df["Status"]
    data_df["license_issued"] = df["First Issue Date"]
    data_df["license_number"] = df["Credential Number"]
    data_df["license_renewed"] = ""
    data_df["license_type"] = df["Credential Type"]
    data_df["licensee_name"] = df["Primary Contact Name"]
    data_df["max_age"] = ""
    data_df["min_age"] = ""
    data_df["operator"] = df["Primary Contact Name"]
    data_df["provider_id"] = ""
    data_df["schedule"] = ""
    data_df["state"] = ""
    data_df["title"] = df["Primary Contact Role"]
    data_df["website_address"] = ""
    data_df["zip"] = df["Address"].str.extract(r"(\d{5})$")
    data_df["facility_type"] = df["Credential Type"]

    return data_df