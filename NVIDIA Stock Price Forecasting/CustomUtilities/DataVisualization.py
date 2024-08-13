import numpy as np
import matplotlib.pyplot as plt

def plot_model_performance(dates_vector:np.ndarray, predictions_vector:np.ndarray, y_vector:np.ndarray, plot_legend:list) -> None:
    # This function helps plot the performance of the model during Trainning, Validation and Testing
    """
    := param: dates_vector - Array with the corresponding dates
    := param: predictions_vector - Array with the corresponding predictions made by the model
    := param: y_vector - Array with the real values from the stock market price history
    := param: plot_legend - Description to differentiate the multiple vectors
    """
    plt.plot(dates_vector, predictions_vector)
    plt.plot(dates_vector, y_vector)
    plt.legend(plot_legend)

def plot_model_overall_performance(dates_list:list, preds_list:list, y_list:list, plot_legend:list) -> None:
    # This function allows to Visualize the Model's performance throughout Train, Validation and Testing
    """
    := param: dates_list - Python List with all the vectors composed by the dates at each phase: Train, Validation and Test
    := param: preds_list - Python List with all the vectors composed by the model's prediction during Trainning, Valdiation and Testing
    := param: y_list - Python List with all the vectors composed by the actual / real values used in Trainning, Validation and Testing
    := param: plot_legend - Description to differentiate the multiple vectors
    """
    
    # Checking the size of the given lists to make sure they match
    assert len(dates_list) == len(preds_list) and len(preds_list) == len(y_list), "Lists with different sizes!"
    
    # Iterate through the data and add it to the plot
    for i in range(len(dates_list)):
        plt.plot(dates_list[i], preds_list[i])
        plt.plot(dates_list[i], y_list[i])

    # Add a Legend
    plt.legend(plot_legend)