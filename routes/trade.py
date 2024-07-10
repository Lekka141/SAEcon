from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

trade_bp = Blueprint('trade', __name__)

@trade_bp.route('/trade')
def trade():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # Define and generate visualizations
    try:
        # Exports Growth Rate (Annual %)
        exports_growth = pd.read_csv('data/trade/Exports_of_goods_and_services_annual_growth.csv')
        fig_exports_growth = px.line(exports_growth, x='Year', y='Value', title='Exports of Goods and Services (Annual Growth %)',
                                     labels={'Year': 'Year', 'Value': 'Growth Rate (%)'})
        graphJSON1 = fig_exports_growth.to_json()

        # Imports Growth Rate (Annual %)
        imports_growth = pd.read_csv('data/trade/Imports_of_goods_and_services_annual_growth.csv')
        fig_imports_growth = px.line(imports_growth, x='Year', y='Value', title='Imports of Goods and Services (Annual Growth %)',
                                     labels={'Year': 'Year', 'Value': 'Growth Rate (%)'})
        graphJSON2 = fig_imports_growth.to_json()

        # Exports of Goods and Services (Current USD)
        exports_usd = pd.read_csv('data/trade/Exports_of_goods_and_services_current_US.csv')
        fig_exports_usd = px.bar(exports_usd, x='Year', y='Value', title='Exports of Goods and Services (Current USD)',
                                 labels={'Year': 'Year', 'Value': 'Exports (USD)'})
        graphJSON3 = fig_exports_usd.to_json()

        # Imports of Goods and Services (Current USD)
        imports_usd = pd.read_csv('data/trade/Imports_of_goods_and_services_current_US.csv')
        fig_imports_usd = px.bar(imports_usd, x='Year', y='Value', title='Imports of Goods and Services (Current USD)',
                                 labels={'Year': 'Year', 'Value': 'Imports (USD)'})
        graphJSON4 = fig_imports_usd.to_json()

        # Trade as a Percentage of GDP
        trade_gdp = pd.read_csv('data/trade/Trade_percent_of_GDP.csv')
        fig_trade_gdp = px.line(trade_gdp, x='Year', y='Value', title='Trade as a Percentage of GDP',
                                labels={'Year': 'Year', 'Value': 'Trade as % of GDP'})
        graphJSON5 = fig_trade_gdp.to_json()

    except FileNotFoundError as e:
        return f"File not found: {e}", 404

    return render_template('trade.html', source=source, 
                           graph_exports_growth=graphJSON1, 
                           graph_imports_growth=graphJSON2, 
                           graph_exports_usd=graphJSON3, 
                           graph_imports_usd=graphJSON4, 
                           graph_trade_gdp=graphJSON5)
