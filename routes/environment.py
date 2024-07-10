from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

environment_bp = Blueprint('environment', __name__)

@environment_bp.route('/environment')
def environment():
    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    # CO2 Emissions
    co2_emissions = pd.read_csv('data/environmental/CO2_emissions_kt.csv')
    fig_co2_emissions = px.line(co2_emissions, x='Year', y='Value', title='CO2 Emissions (kt)',
                                labels={'Year': 'Year', 'Value': 'CO2 Emissions (kt)'})
    graphJSON1 = fig_co2_emissions.to_json()

    # Renewable Internal Freshwater Resources per Capita
    freshwater_resources = pd.read_csv('data/environmental/Renewable_internal_freshwater_resources_per_capita_cubic_meters.csv')
    fig_freshwater_resources = px.bar(freshwater_resources, x='Year', y='Value', title='Renewable Internal Freshwater Resources (per capita)',
                                      labels={'Year': 'Year', 'Value': 'Freshwater Resources (cubic meters per capita)'})
    graphJSON2 = fig_freshwater_resources.to_json()

    # Protected Areas
    protected_areas = pd.read_csv('data/environmental/Terrestrial_and_marine_protected_areas_percent_of_total_territorial_area.csv')
    fig_protected_areas = px.bar(protected_areas, x='Year', y='Value', title='Protected Areas (% of Total Territorial Area)',
                                 labels={'Year': 'Year', 'Value': 'Protected Areas (%)'})
    graphJSON3 = fig_protected_areas.to_json()

    # Air Pollution (PM2.5)
    air_pollution = pd.read_csv('data/environmental/PM2.5_air_pollution_mean_annual_exposure_micrograms_per_cubic_meter.csv')
    fig_air_pollution = px.line(air_pollution, x='Year', y='Value', title='Air Pollution (PM2.5)',
                                labels={'Year': 'Year', 'Value': 'PM2.5 (µg/m³)'})
    graphJSON4 = fig_air_pollution.to_json()

    return render_template('environment.html', graph_co2_emissions=graphJSON1, graph_freshwater_resources=graphJSON2,
                           graph_protected_areas=graphJSON3, graph_air_pollution=graphJSON4, source=source)
