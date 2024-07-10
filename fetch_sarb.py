import requests
import os
import json
import pandas as pd

# Directory to save JSON files
DATA_DIR = "data"

# Create directory if it doesn't exist
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Endpoints with placeholders for graph numbers
GRAPH_ENDPOINTS = {
    "international_economics_graphs": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData/InternationalEconomicsGraphs/{}",
    "capital_markets_graphs": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData/CapitalMarketsGraphs/{}",
    "economic_indicators_graphs": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData/EconomicIndicators/{}",
    "money_and_banking_graphs": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData/MoneyAndBankingGraphs/{}",
    "national_government_graphs": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData/NationalGovernmentGraphs/{}"
}

# Graph numbers to try
GRAPH_NUMBERS = [1, 2, 3, 4]  # Adjust based on the actual graph numbers available

# Other endpoints
ENDPOINTS = {
    "home_page_rates": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/HomePageRates",
    "historical_exchange_rates_daily": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/HistoricalExchangeRatesDaily",
    "historical_exchange_rates_monthly": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/HistoricalExchangeRatesMonthly",
    "current_market_rates": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/CurrentMarketRates",
    "cpd_rates": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/CPDRates",
    "population_data": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/GetPopulationData",
    "real_sector_data": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/GetRealSectorData",
    "business_cycles_data": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/GetBusinessCyclesData",
    "fiscal_sector_data": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/GetFiscalSectorData",
    "financial_sector_data": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/GetFinancialSectorData",
    "external_sector_data": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/GetExternalSectorData",
    "historical_dates_of_rate_changes": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/OtherIndicators/HistoricalDatesOfRateChanges",
    "release_of_selected_data": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData",
    "monthly_indicators": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData/MonthlyIndicators/{}",
    "monthly_indicators_all": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/ReleaseOfSelectedData/MonthlyIndicatorsAll/{}",
    "last_update_period": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/LastUpdatePeriod",
    "foot_notes": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/EconFinDataForSA/GetFootNotes",
    "other_indicators": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/OtherIndicators",
    "timeseries_observations": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/Shared/GetTimeseriesObservations/{}",
    "timeseries_observations_range": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/Shared/GetTimeseriesObservations/{}/{}/{}",
    "category_information": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/Shared/GetCategoryInformation/{}",
    "type_information": "https://custom.resbank.co.za/SarbWebApi/WebIndicators/Shared/GetTypeInformation/{}"
}

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def save_as_csv(data, file_path):
    if isinstance(data, list):
        df = pd.DataFrame(data)
    elif isinstance(data, dict):
        df = pd.json_normalize(data)
    else:
        print(f"Unsupported data type for {file_path}")
        return
    
    df.to_csv(file_path, index=False)
    print(f"Saved data to {file_path}")

def main():
    data = {}

    # Fetch non-graph data
    for key, url in ENDPOINTS.items():
        try:
            data[key] = fetch_data(url)
            print(f"Fetched data for {key}")
        except Exception as e:
            print(f"Failed to fetch data for {key}: {e}")

    # Fetch graph data
    for key, url_template in GRAPH_ENDPOINTS.items():
        graph_data = {}
        for number in GRAPH_NUMBERS:
            url = url_template.format(number)
            try:
                graph_data[number] = fetch_data(url)
                print(f"Fetched data for {key} graph {number}")
            except Exception as e:
                print(f"Failed to fetch data for {key} graph {number}: {e}")
        data[key] = graph_data

    # Save the data to CSV files in the data directory
    for key, value in data.items():
        file_path = os.path.join(DATA_DIR, f"{key}.csv")
        save_as_csv(value, file_path)

if __name__ == "__main__":
    main()
