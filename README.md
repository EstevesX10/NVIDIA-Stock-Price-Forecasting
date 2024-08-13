<div align="center">
    <h1>NVIDIA Stock Price Forecasting</h1>
</div>

<p align="center" width="100%">
    <img src="./NVIDIA Stock Price Forecasting/Assets/StockForecasting.gif" width="60%" height="60%" />
</p>

<div align="center">
    <a>
        <img src="https://img.shields.io/badge/Made%20with-Python-BD162C?style=for-the-badge&logo=Python&logoColor=BD162C">
    </a>
    <a>
        <img src="https://img.shields.io/badge/Made%20with-Jupyter-BD162C?style=for-the-badge&logo=Jupyter&logoColor=BD162C">
    </a>
</div>

<br/>

<div align="center">
    <a href="https://github.com/EstevesX10/NVIDIA-Stock-Price-Forecasting/blob/main/LICENSE">
        <img src="https://img.shields.io/github/license/EstevesX10/NVIDIA-Stock-Price-Forecasting?style=flat&logo=gitbook&logoColor=BD162C&label=License&color=BD162C">
    </a>
    <a href="">
        <img src="https://img.shields.io/github/repo-size/EstevesX10/NVIDIA-Stock-Price-Forecasting?style=flat&logo=googlecloudstorage&logoColor=BD162C&logoSize=auto&label=Repository%20Size&color=BD162C">
    </a>
    <a href="">
        <img src="https://img.shields.io/github/stars/EstevesX10/NVIDIA-Stock-Price-Forecasting?style=flat&logo=adafruit&logoColor=BD162C&logoSize=auto&label=Stars&color=BD162C">
    </a>
    <a href="https://github.com/EstevesX10/NVIDIA-Stock-Price-Forecasting/blob/main/requirements.txt">
        <img src="https://img.shields.io/badge/Dependencies-DEPENDENCIES.md-white?style=flat&logo=anaconda&logoColor=BD162C&logoSize=auto&color=BD162C"> 
    </a>
</div>

## Project Overview

This Project mainly focuses on trying to predict the ``NVIDIA Stock's Market Price`` using data from the yahoo Finance market history alongside with ``Long Short-Term Memory Models`` (LSTM's).

The prediction methodology is based on ``Univariate Forecasting``, which means that we are only to consider ``n`` previous values to predict the subsequent/next one.

## Project Development (Dependencies & Execution)

This project was developed using a `Notebook`. Therefore if you're looking forward to test it out yourself, keep in mind to either use a **[Anaconda Distribution](https://www.anaconda.com/)** or a 3rd party software that helps you inspect and execute it. 

Therefore, for more informations regarding the **Virtual Environment** used in Anaconda, consider checking the [DEPENDENCIES.md](https://github.com/EstevesX10/NVIDIA-Stock-Price-Forecasting/blob/main/DEPENDENCIES.md) file.


## Important Considerations [REVIEW LATER]

The Notebook contains executable code that allows to properly extract the dataset from the yahoo finance market, and consequently preprocess them to be later fed to a LSTM model. The code which allows to perform these tasks is not fully developed on the Notebook bu rather on the CustomUtilities python package developed. 

Moreover, it is possible to change the configuration used in the project so that the user can perform other stock price forecastings. Therefore, the user can change not only the Stock being studied but also the time interval to be considered in the model's trainning.

## Project Results

> ADD A PLOT WITH THE FINAL GRAPH AND A DESCRIPTION OF IT 
> MENTION: THE IMPACT OF THE TRAINNING DATA ON THE MODEL'S TEST PERFORMANCE AND HOW IT CAN BE AVOIDED TO OBTAIN BETTER RESULTS

### CHANGE THE REPO'S NAME

<div align="right">
<sub>

<!-- <sup></sup> -->
`README.md by Gonçalo Esteves`
</sub>
</div>