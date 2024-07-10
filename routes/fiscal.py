from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

fiscal_bp = Blueprint('fiscal', __name__)

@fiscal_bp.route('/fiscal')
def fiscal():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # Central Government Debt
    govt_debt = pd.read_csv('data/fiscal/Central_government_debt_total_percent_of_GDP.csv')
    fig_govt_debt = px.line(govt_debt, x='Year', y='Value', title='Central Government Debt (% of GDP)',
                            labels={'Year': 'Year', 'Value': 'Debt (% of GDP)'})
    graphJSON1 = fig_govt_debt.to_json()

    # Government Revenue
    govt_revenue = pd.read_csv('data/fiscal/Tax_revenue_percent_of_GDP.csv')
    fig_govt_revenue = px.line(govt_revenue, x='Year', y='Value', title='Government Revenue (% of GDP)',
                               labels={'Year': 'Year', 'Value': 'Revenue (% of GDP)'})
    graphJSON2 = fig_govt_revenue.to_json()

    # Government Expenditure
    govt_expenditure = pd.read_csv('data/fiscal/General_government_final_consumption_expenditure_percent_of_GDP.csv')
    fig_govt_expenditure = px.line(govt_expenditure, x='Year', y='Value', title='Government Expenditure (% of GDP)',
                                   labels={'Year': 'Year', 'Value': 'Expenditure (% of GDP)'})
    graphJSON3 = fig_govt_expenditure.to_json()

    # Fiscal Balance
    fiscal_balance = pd.read_csv('data/fiscal/Net_lending_net_borrowing_percent_of_GDP.csv')
    fig_fiscal_balance = px.line(fiscal_balance, x='Year', y='Value', title='Fiscal Balance (% of GDP)',
                                 labels={'Year': 'Year', 'Value': 'Fiscal Balance (% of GDP)'})
    graphJSON4 = fig_fiscal_balance.to_json()

    return render_template('fiscal.html', graph_govt_debt=graphJSON1, graph_govt_revenue=graphJSON2,
                           graph_govt_expenditure=graphJSON3, graph_fiscal_balance=graphJSON4, source=source)
