from datetime import datetime
import pandas as pd
from swagger_client.api_client import ApiClient
from swagger_client.api.balancing_mechanism_dynamic_api import BalancingMechanismDynamicApi


api_client = ApiClient()

# Initialize the BalancingMechanismDynamicApi instance
balancing_api = BalancingMechanismDynamicApi(api_client)

try:
    print("\n--- Balancing Mechanism Dynamic Data ---")

    settlement_date = datetime.now().date()
    settlement_period = 1  # Adjust as needed

    # Call the API method to fetch balancing mechanism dynamic data
    response = balancing_api.balancing_dynamic_all_get(
        settlement_date=settlement_date,
        settlement_period=settlement_period
    )

    print("Response type:", type(response))
    if hasattr(response, 'data'):
        # Convert response data to a DataFrame
        df = pd.DataFrame([data.to_dict() for data in response.data])
        print(df.head())
    else:
        print("Response object does not contain 'data' attribute.")

except Exception as e:
    print(f"Error fetching balancing mechanism dynamic data: {str(e)}")
