from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

demographics_bp = Blueprint('demographics', __name__)

@demographics_bp.route('/demographics')
def demographics():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"
    
    # Population Growth
    population_growth = pd.read_csv('data/demographics/Population_growth_annual_percent.csv')
    fig_population_growth = px.line(population_growth, x='Year', y='Value', title='Population Growth (Annual %)',
                                    labels={'Year': 'Year', 'Value': 'Growth Rate (%)'})
    graphJSON1 = fig_population_growth.to_json()

    # Population Density
    population_density = pd.read_csv('data/demographics/Population_density_people_per_sq_km_of_land_area.csv')
    fig_population_density = px.bar(population_density, x='Year', y='Value', title='Population Density (People per sq km)',
                                    labels={'Year': 'Year', 'Value': 'Population Density (people/sq km)'})
    graphJSON2 = fig_population_density.to_json()

    # Urban Population
    urban_population = pd.read_csv('data/demographics/Population_in_urban_agglomerations_of_more_than_1_million_percent_of_total_population.csv')
    fig_urban_population = px.line(urban_population, x='Year', y='Value', title='Urban Population (% of Total Population)',
                                   labels={'Year': 'Year', 'Value': 'Urban Population (%)'})
    graphJSON3 = fig_urban_population.to_json()

    # Population by Age Group
    population_age_groups = pd.read_csv('data/demographics/Population_ages_0-14_total.csv')
    population_age_groups['Age Group'] = '0-14'
    age_group_15_64 = pd.read_csv('data/demographics/Population_ages_15-64_total.csv')
    age_group_15_64['Age Group'] = '15-64'
    age_group_65_above = pd.read_csv('data/demographics/Population_ages_65_and_above_total.csv')
    age_group_65_above['Age Group'] = '65+'

    population_age_groups = pd.concat([population_age_groups, age_group_15_64, age_group_65_above])
    fig_population_age_groups = px.bar(population_age_groups, x='Year', y='Value', color='Age Group',
                                       title='Population by Age Group',
                                       labels={'Year': 'Year', 'Value': 'Population', 'Age Group': 'Age Group'})
    graphJSON4 = fig_population_age_groups.to_json()

    return render_template('demographics.html', graph_population_growth=graphJSON1, graph_population_density=graphJSON2,
                           graph_urban_population=graphJSON3, graph_population_age_groups=graphJSON4, source=source)
