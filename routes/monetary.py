from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

monetary_bp = Blueprint('monetary', __name__)

@monetary_bp.route('/monetary')
def monetary():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # Deposit Interest Rate
    deposit_interest_rate = pd.read_csv('data/monetary/Deposit_interest_rate_percent.csv')
    fig_deposit_interest_rate = px.line(deposit_interest_rate, x='Year', y='Value', title='Deposit Interest Rate (%)',
                                        labels={'Year': 'Year', 'Value': 'Deposit Interest Rate (%)'})
    graphJSON1 = fig_deposit_interest_rate.to_json()

    # Domestic Credit Provided by Financial Sector
    domestic_credit_financial_sector = pd.read_csv('data/monetary/Domestic_credit_provided_by_financial_sector_percent_of_GDP.csv')
    fig_domestic_credit_financial_sector = px.line(domestic_credit_financial_sector, x='Year', y='Value', title='Domestic Credit Provided by Financial Sector (% of GDP)',
                                                   labels={'Year': 'Year', 'Value': 'Domestic Credit (% of GDP)'})
    graphJSON2 = fig_domestic_credit_financial_sector.to_json()

    # Real Interest Rate
    real_interest_rate = pd.read_csv('data/monetary/Real_interest_rate_percent.csv')
    fig_real_interest_rate = px.line(real_interest_rate, x='Year', y='Value', title='Real Interest Rate (%)',
                                     labels={'Year': 'Year', 'Value': 'Real Interest Rate (%)'})
    graphJSON3 = fig_real_interest_rate.to_json()

    return render_template('monetary.html', graph_deposit_interest_rate=graphJSON1, graph_domestic_credit_financial_sector=graphJSON2,
                           graph_real_interest_rate=graphJSON3, source=source)
