from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

investment_bp = Blueprint('investment', __name__)

@investment_bp.route('/investment')
def investment():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # Gross Capital Formation Annual Growth
    gross_capital_formation_growth = pd.read_csv('data/investment/Gross_capital_formation_annual_growth_percent.csv')
    fig_gross_capital_formation_growth = px.line(gross_capital_formation_growth, x='Year', y='Value', title='Gross Capital Formation (Annual Growth %)',
                                                 labels={'Year': 'Year', 'Value': 'Growth Rate (%)'})
    graphJSON1 = fig_gross_capital_formation_growth.to_json()

    # Foreign Direct Investment Net Inflows
    fdi_net_inflows = pd.read_csv('data/investment/Foreign_direct_investment_net_inflows_percent_of_GDP.csv')
    fig_fdi_net_inflows = px.line(fdi_net_inflows, x='Year', y='Value', title='Foreign Direct Investment (FDI), Net Inflows (% of GDP)',
                                  labels={'Year': 'Year', 'Value': 'FDI Net Inflows (% of GDP)'})
    graphJSON2 = fig_fdi_net_inflows.to_json()

    # Gross Fixed Capital Formation
    gross_fixed_capital_formation = pd.read_csv('data/investment/Gross_fixed_capital_formation_percent_of_GDP.csv')
    fig_gross_fixed_capital_formation = px.line(gross_fixed_capital_formation, x='Year', y='Value', title='Gross Fixed Capital Formation (% of GDP)',
                                                labels={'Year': 'Year', 'Value': 'Gross Fixed Capital Formation (% of GDP)'})
    graphJSON3 = fig_gross_fixed_capital_formation.to_json()

    return render_template('investment.html', graph_gross_capital_formation_growth=graphJSON1, graph_fdi_net_inflows=graphJSON2,
                           graph_gross_fixed_capital_formation=graphJSON3, source=source)
