from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

poverty_bp = Blueprint('poverty', __name__)

@poverty_bp.route('/poverty')
def poverty():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # Gini Index
    gini_index = pd.read_csv('data/poverty/Gini_index.csv')
    fig_gini_index = px.line(gini_index, x='Year', y='Value', title='Gini Index',
                             labels={'Year': 'Year', 'Value': 'Gini Index'})
    graphJSON1 = fig_gini_index.to_json()

    # Poverty Headcount Ratio at $2.15 a Day (2017 PPP)
    poverty_2_15 = pd.read_csv('data/poverty/Poverty_headcount_ratio_at_2.15_a_day_2017_PPP_percent_of_population.csv')
    fig_poverty_2_15 = px.line(poverty_2_15, x='Year', y='Value', title='Poverty Headcount Ratio at $2.15 a Day (2017 PPP) (% of Population)',
                               labels={'Year': 'Year', 'Value': 'Poverty Headcount Ratio (%)'})
    graphJSON2 = fig_poverty_2_15.to_json()

    # Poverty Headcount Ratio at National Poverty Lines
    poverty_national = pd.read_csv('data/poverty/Poverty_headcount_ratio_at_national_poverty_lines_percent_of_population.csv')
    fig_poverty_national = px.line(poverty_national, x='Year', y='Value', title='Poverty Headcount Ratio at National Poverty Lines (% of Population)',
                                   labels={'Year': 'Year', 'Value': 'Poverty Headcount Ratio (%)'})
    graphJSON3 = fig_poverty_national.to_json()

    return render_template('poverty.html', graph_gini_index=graphJSON1, graph_poverty_2_15=graphJSON2,
                           graph_poverty_national=graphJSON3, source=source)
