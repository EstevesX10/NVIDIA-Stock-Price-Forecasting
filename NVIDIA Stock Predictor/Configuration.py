def load_config() -> dict:
    # This Funtion serves to define a configuration to be used within the Project's development
    return {'Stock':'NVDA', # Selecting a Stock to be studied
            'N':3, # Number of previous data to be considered when predicting a next value
            'max_period':False, # Flag to determine whether or not to consider all the historical data, i.e, all the information available 
            'start_date':None, # Start date of the data to be considered
            'end_date':None # End date of the data to be considered
            }