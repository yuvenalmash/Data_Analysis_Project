# Data_Analysis_Project

## Project Description
This project shows the analysis of the data of World Economic Outlook Database from International Monetary Fund (IMF) website.

## Features
-  Top 10 countries GDP per capita growth over the last
decade. [#1_GDP_Per_Capita_Growth](./notebooks/#1_GDP_Per_Capita_Growth.ipynb)
-  Draw OECD countries' "Population" growth over the last decade. [#2_OECD_Population_Growth](./notebooks/#2_OECD_Population_growth.ipynb)
- Create 5 clusters out of the countries using GDP and "Volume of exports of goods". [#4_GDP-Exports_Clusters](./notebooks/#4_GDP-Exports_Clusters.ipynb)
- Get data fields from the year 2015 that are present in most of the countries. [#5_None-null_2015](./notebooks/#5_None-null_2015.ipynb)
- predictor (use scikit) to predict GDP per capita. [#6_GDPPC_Predictor](./notebooks/#6_GDPPC_Predictor.ipynb)
- API to serve the predictor. [#7_API](./api/)

## Getting Started
1. Clone this repository using the command:
```sh
git clone git@github.com:yuvenalmash/Data_Analysis_Project.git
```

2. Navigate to the folder:
```sh
cd Data_Analysis_Project
```

3. Install the required packages:
```sh
pyton3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### API
To run the API:
```sh
cd api
python3 app.py
```

To run the tests:
```sh
python3 test_app.py
```

#### API Endpoints
- POST /predict_gdp_per_capita
  - Parameters:
    - "continent": string
    - "Population": float
    - "gross_national_savings": float
    - "features": list of strings
  - Returns:
    - "gdp_per_capita": float
