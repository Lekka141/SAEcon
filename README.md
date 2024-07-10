# South African Economy Visualizer (SAEcon)

## Overview

SAEcon is a web-based application designed to visualize key economic metrics of South Africa. The platform provides interactive charts and detailed explanations across various economic categories such as GDP, Demographics, Fiscal Health, Inflation, Trade, and more.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Routes](#routes)
- [Templates](#templates)
- [Data Sources](#data-sources)
- [Progress](#progress)
- [Challenges](#challenges)
- [Screenshots](#screenshots)

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/SAEcon.git
    cd SAEcon
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    flask run
    ```

## Usage

1. **Home Page**: Access the home page at `http://127.0.0.1:5000/`. It provides an overview of the platform and navigation to different economic categories.
2. **Category Pages**: Navigate to specific economic categories via the navbar. Each category page includes interactive charts and detailed explanations of key metrics.

## Routes

The application defines routes for different economic categories, each with its own blueprint and corresponding template:

- `/`: Home page
- `/demographics`: Demographics data
- `/environment`: Environmental sustainability
- `/fiscal`: Fiscal health
- `/gdp`: GDP
- `/health`: Health metrics
- `/inflation`: Inflation data
- `/investment`: Investment data
- `/monetary`: Monetary policy
- `/poverty`: Poverty and inequality
- `/trade`: Trade data

### Route Details

#### `/demographics`
- **Description**: Provides visualizations for demographic data.
- **Metrics**:
  - Population Growth Rate
  - Population Density (People per Sq Km)
  - Urban Population (% of Total)

#### `/environment`
- **Description**: Visualizes environmental sustainability metrics.
- **Metrics**:
  - CO2 Emissions (Metric Tons per Capita)
  - Renewable Energy Consumption (% of Total)
  - Forest Area (% of Land Area)

#### `/fiscal`
- **Description**: Displays fiscal health indicators.
- **Metrics**:
  - Government Debt (% of GDP)
  - Government Revenue (Current USD)
  - Government Expenditure (Current USD)
  - Fiscal Balance

#### `/gdp`
- **Description**: Shows GDP-related metrics.
- **Metrics**:
  - GDP (Current USD)
  - GDP Growth Rate
  - GDP Per Capita (Current USD)
  - GDP Per Unit of Energy Use
  - GDP Deflator

#### `/health`
- **Description**: Provides visualizations for health data.
- **Metrics**:
  - Life Expectancy at Birth
  - Mortality Rate
  - Health Expenditure (% of GDP)

#### `/inflation`
- **Description**: Visualizes inflation data.
- **Metrics**:
  - Consumer Price Index (CPI)
  - GDP Deflator
  - Inflation Rate (Annual %)

#### `/investment`
- **Description**: Displays investment metrics.
- **Metrics**:
  - Gross Capital Formation
  - Foreign Direct Investment (FDI)
  - Investment as a Percentage of GDP

#### `/monetary`
- **Description**: Provides visualizations for monetary policy data.
- **Metrics**:
  - Interest Rates
  - Money Supply
  - Inflation Rate

#### `/poverty`
- **Description**: Shows metrics related to poverty and inequality.
- **Metrics**:
  - Poverty Gap at $2.15/day
  - Poverty Gap at $3.65/day
  - Poverty Gap at $6.85/day
  - Poverty Headcount Ratio at $2.15/day
  - Poverty Headcount Ratio at $3.65/day
  - Poverty Headcount Ratio at $6.85/day
  - Gini Index

#### `/trade`
- **Description**: Displays trade-related metrics.
- **Metrics**:
  - Exports of Goods and Services (Current USD)
  - Imports of Goods and Services (Current USD)
  - Trade Balance
  - Trade as a Percentage of GDP

## Templates

Templates are located in the `templates` directory. Each category has its own template extending from the base template. The base template includes the common layout and navigation structure.

### Template Details

- **base.html**: The base template containing the common layout and navigation.
- **index.html**: The home page template.
- **demographics.html**: Template for demographics visualizations.
- **environment.html**: Template for environmental sustainability visualizations.
- **fiscal.html**: Template for fiscal health visualizations.
- **gdp.html**: Template for GDP visualizations.
- **health.html**: Template for health metrics visualizations.
- **inflation.html**: Template for inflation visualizations.
- **investment.html**: Template for investment data visualizations.
- **monetary.html**: Template for monetary policy visualizations.
- **poverty.html**: Template for poverty and inequality visualizations.
- **trade.html**: Template for trade data visualizations.
- **404.html**: Custom 404 error page template.
- **500.html**: Custom 500 error page template.

## Data Sources

Data files are located in the `data` directory, organized by category. CSV files are used for loading data into the application. Ensure the data files are correctly formatted and placed in the appropriate subdirectories.
