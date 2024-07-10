from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

inflation_bp = Blueprint('inflation', __name__)

@inflation_bp.route('/inflation')
def inflation():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # Inflation Consumer Prices
    inflation_consumer_prices = pd.read_csv('data/inflation/Inflation_consumer_prices_annual_percent.csv')
    fig_inflation_consumer_prices = px.line(inflation_consumer_prices, x='Year', y='Value', title='Inflation, Consumer Prices (Annual %)',
                                            labels={'Year': 'Year', 'Value': 'Inflation Rate (%)'})
    graphJSON1 = fig_inflation_consumer_prices.to_json()

    # Inflation GDP Deflator
    inflation_gdp_deflator = pd.read_csv('data/inflation/Inflation_GDP_deflator_annual_percent.csv')
    fig_inflation_gdp_deflator = px.line(inflation_gdp_deflator, x='Year', y='Value', title='Inflation, GDP Deflator (Annual %)',
                                         labels={'Year': 'Year', 'Value': 'GDP Deflator (%)'})
    graphJSON2 = fig_inflation_gdp_deflator.to_json()

    # Consumer Price Index
    consumer_price_index = pd.read_csv('data/inflation/Consumer_price_index_2010_base_100.csv')
    fig_consumer_price_index = px.line(consumer_price_index, x='Year', y='Value', title='Consumer Price Index (2010 = 100)',
                                       labels={'Year': 'Year', 'Value': 'CPI (2010 = 100)'})
    graphJSON3 = fig_consumer_price_index.to_json()

    return render_template('inflation.html', graph_inflation_consumer_prices=graphJSON1, graph_inflation_gdp_deflator=graphJSON2,
                           graph_consumer_price_index=graphJSON3, source=source)
