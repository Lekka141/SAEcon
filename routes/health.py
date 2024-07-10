from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

health_bp = Blueprint('health', __name__)

@health_bp.route('/health')
def health():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # Life Expectancy
    life_expectancy_female = pd.read_csv('data/health/Life_expectancy_at_birth_female_years.csv')
    life_expectancy_male = pd.read_csv('data/health/Life_expectancy_at_birth_male_years.csv')
    life_expectancy_total = pd.read_csv('data/health/Life_expectancy_at_birth_total_years.csv')
    
    fig_life_expectancy = px.line(life_expectancy_total, x='Year', y='Value', title='Life Expectancy at Birth (Years)',
                                  labels={'Year': 'Year', 'Value': 'Life Expectancy (Years)'})
    fig_life_expectancy.add_scatter(x=life_expectancy_female['Year'], y=life_expectancy_female['Value'], mode='lines', name='Female')
    fig_life_expectancy.add_scatter(x=life_expectancy_male['Year'], y=life_expectancy_male['Value'], mode='lines', name='Male')
    graphJSON1 = fig_life_expectancy.to_json()

    # Infant Mortality Rate
    infant_mortality = pd.read_csv('data/health/Mortality_rate_infant_per_1000_live_births.csv')
    fig_infant_mortality = px.line(infant_mortality, x='Year', y='Value', title='Infant Mortality Rate (Per 1,000 Live Births)',
                                   labels={'Year': 'Year', 'Value': 'Infant Mortality Rate'})
    graphJSON2 = fig_infant_mortality.to_json()

    # Health Expenditure Per Capita
    health_expenditure = pd.read_csv('data/health/Current_health_expenditure_per_capita_current_USD.csv')
    fig_health_expenditure = px.line(health_expenditure, x='Year', y='Value', title='Health Expenditure Per Capita (Current USD)',
                                     labels={'Year': 'Year', 'Value': 'Health Expenditure (USD)'})
    graphJSON3 = fig_health_expenditure.to_json()

    return render_template('health.html', graph_life_expectancy=graphJSON1, graph_infant_mortality=graphJSON2,
                           graph_health_expenditure=graphJSON3, source=source)
