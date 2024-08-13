import numpy as np
import pandas as pd
from typing import (Tuple)
from datetime import (datetime, timedelta)

# Defining a Function to convert the string dates of the dataset into datetime object instances
def str_to_datetime(string_date:str) -> datetime:
    """
    := param: string_date -> String that we want to convert into a datetime type object [Eg: '2003-10-10']
    := return: Instance of Datetime based on the given date string
    """
    # Fetching the year, month and day from the string and convert them into int
    year, month, day = list(map(int, string_date.split('-')))

    # Return a instance of datetime with the respective extracted attributes from the given string
    return datetime(year=year, month=month, day=day)


# Since we are going to use a LSTM model, we need to convert the problem into a supervised learning problem
def df_to_windowed_df(dataframe:pd.DataFrame, first_date_str:str, last_date_str:str, n:int=3) -> pd.DataFrame:
    # This function creates a Dataframe with multiple target columns which are going to be used within the long short-term memory model
    # It focus at each instant and it's previous n values to which it will use to train the model and use the real value to control the error fluctuation of the model
    """
    := param: dataframe - Pandas Dataframe with the csv file of the Stock Market History
    := param: first_date_str - First date to consider for the data extraction
    := param: last_date_str - Last date to consider for the data extraction
    := param: n - Number of previous instances to consider when predicting a n+1 instance of the stock market value

    := return: Dataframe with the Target Values alongside the Nth previous values as well as with the corresponding dates
    """
    # Converting the string dates
    first_date = str_to_datetime(first_date_str)
    last_date = str_to_datetime(last_date_str)

    # Defining a current date to be iterated over
    target_date = first_date
    dates, X, Y = [], [], []
    
    # Creating a flag to determine the last time...
    last_time = False

    while True:
        # Selecting a Subset of the datafrane 
        df_subset = dataframe.loc[:target_date].tail(n+1)

        if df_subset.shape[0] != n+1:
            print(f'[ERROR]: Window of Size {n} is too large for date {target_date}')
            return

        # Getting the closing values for the current subset (Current time interval [initial_date - current_date(updates at each new iteration on the while cycle)])
        values = df_subset['Close'].to_numpy()
        
        # Spliting the values into 
        x, y = values[:-1], values[-1]
        
        # Update the initial lists with the new values
        dates.append(target_date)
        X.append(x)
        Y.append(y)
        
        # Getting the date for the next week -> We consider consecutive entries the ones that are 1 week apart
        next_week = dataframe.loc[target_date:target_date + timedelta(days=7)]
        next_datetime_str = str(next_week.head(2).tail(1).index.values[0])
        next_date_str = next_datetime_str.split('T')[0]
        
        # Extracting the year, month and day
        year, month, day = list(map(int, next_date_str.split('-')))
        
        # Create a new instance of datetime for the next date (date to consider for the next iteration)
        next_date = datetime(year=year, month=month, day=day)

        # Reached the Final / Target date
        if last_time:
            break

        # Updating the Target Date
        target_date = next_date

        # Current Date == Last Date to consider
        if target_date == last_date:
            last_time = True

    # Initializing the Target Dataframe with all the valid dates to which we want to train the model with
    target_df = pd.DataFrame({})
    target_df['Target_Date'] = dates
    
    # Converting the X list into a numpy array
    X = np.array(X, dtype='object')
    
    # For each entry in the dataset, we look for the i - <n> entry and add it as a new column to the dataframe
    for i in range(0, n):
        # X[:, i]
        target_df[f'Target-{n-i}'] = X[:, i]

    target_df['Target'] = Y

    # Return the new dataframe
    return target_df

def windowed_df_to_date_X_y(windowed_df:pd.DataFrame) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    := param: windowed_df - Dataframe with the proper extracted and formated data to later feed models / Tensors
    := return: A list of Dates, a multi-dimensional (Nth Dimensional to be precise) input matrix X and the target values y
    """
    # Convert the whole dataframe into a numpy array
    df_numpy = windowed_df.to_numpy()

    # Get a list with the dates
    dates = df_numpy[:, 0]

    # Filter the input values and reshape them into a matrix
    input_matrix = df_numpy[:, 1:-1]
    X = input_matrix.reshape((len(dates), input_matrix.shape[1], 1))

    # Get the ouput vector
    y = df_numpy[:, -1]

    # Return the dates, the input and output vectors
    return dates, X.astype(np.float32), y.astype(np.float32)