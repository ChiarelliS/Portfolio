import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
import os


def main():
    # Load variables from .env file into environment
    load_dotenv()
    headers = {
        "User-Agent": os.getenv("USER_AGENT")
    }

    url = "https://www.sec.gov/files/company_tickers_exchange.json"
    res = requests.get(url, headers=headers)
    companies = res.json()
    header = companies["fields"]
    company_data = companies["data"]
    df = pd.DataFrame(company_data, columns=header)
    current_year = datetime.now().year

    # Output DataFrame
    df1 = pd.DataFrame(columns=[
        'name', 'ticker', 'cik', 'form', 'start', 'end', 'fp', 'fy', 'val', 'frame',
        'unit','street1','street2','city','zipCode', 'stateOrCountry', 'stateOrCountryDescription', 'isForeignLocation',
        'foreignStateTerritory', 'country'
    ])

    c = 0
    while df1['cik'].nunique() < 10 and c < len(df):
        cik = int(df.loc[c, 'cik'])  # CIK as int
        cik_str = f"{cik:010d}"      # 10-digit CIK
        c += 1

        try:
            facts_url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik_str}.json"
            facts_data = requests.get(facts_url, headers=headers)
            facts_data.raise_for_status()
            data = facts_data.json()

            # Check if revenue data exists
            revenues = data["facts"]["us-gaap"].get("Revenues", None)
            if not revenues or "units" not in revenues or "USD" not in revenues["units"]:
                continue

            # Fetch company location info for each company
            country_url = f"https://data.sec.gov/submissions/CIK{cik_str}.json"
            country_data_request = requests.get(country_url, headers=headers)
            country_data_request.raise_for_status()
            country_data = country_data_request.json()
            location = country_data.get("addresses", {}).get("business", {})

            revenue_entries = revenues["units"]["USD"]
            for entry in revenue_entries:
                if (
                    entry.get('form') == '10-K' and
                    entry.get('fp') == 'FY' and
                    ('Q' not in entry.get('frame', '')) and
                    entry.get('frame') and
                    (current_year - 5) <= int(entry.get('frame')[2:]) <= current_year  
                ):
                    row = {
                        'name': df.loc[c-1, 'name'],
                        'ticker': df.loc[c-1, 'ticker'],
                        'cik': cik,
                        'form': entry.get('form'),
                        'start': entry.get('start'),
                        'end': entry.get('end'),
                        'fp': entry.get('fp'),
                        'fy': entry.get('fy'),
                        'val': entry.get('val'),
                        'frame': entry.get('frame'),
                        'unit': 'USD'
                    }

                    for loc_key in ['street1','street2','city','zipCode','stateOrCountry', 'stateOrCountryDescription',
                                    'isForeignLocation', 'foreignStateTerritory', 'country']:
                        row[loc_key] = location.get(loc_key)

                    df1.loc[len(df1)] = row
  

        except Exception as e:
            print(f"Error processing CIK {cik_str}: {e}")
            continue

    # Save to CSV
    df2 = df1[['name','ticker','cik','form','frame','val','unit','street1','street2','city','zipCode','country','stateOrCountry','isForeignLocation']].copy()
    df2['year'] = df2['frame'].str[2:]
    df2['country'] = df2['country'].replace('', 'usa')
    #print(df2)
    df2.to_csv("sec_company_data.csv", index=False)
    print("Data saved to 'sec_company_data.csv'")


if __name__ == '__main__':
    main()