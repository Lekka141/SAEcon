from flask import Blueprint, render_template
import pandas as pd
import plotly.express as px

gdp_bp = Blueprint('gdp', __name__)

@gdp_bp.route('/gdp')
def gdp():
    # Load the relevant GDP data files for conventional sectors
    sector_files = {
        'Manufacturing': 'data/trade/Manufacturing_value_added_percent_of_GDP.csv',
        'Services': 'data/trade/Services_value_added_percent_of_GDP.csv',
    }

    # Source information
    source = "Source: World Bank (http://www.worldbank.org)"

    sector_data = []
    for sector, file in sector_files.items():
        df = pd.read_csv(file)
        # Assuming the data has 'Year' and 'Value' columns, take the most recent year data
        recent_data = df[df['Year'] == df['Year'].max()]
        total_value = recent_data['Value'].sum()
        sector_data.append({'Sector': sector, 'Value': total_value})

    # Adding Agriculture manually as a placeholder with an assumed value if no direct data is found
    sector_data.append({'Sector': 'Agriculture', 'Value': 10})  # Placeholder value, adjust as necessary

    # Convert the list to a DataFrame
    sector_df = pd.DataFrame(sector_data)

    # Normalize the values to sum up to 100%
    sector_df['Value'] = sector_df['Value'] * 100 / sector_df['Value'].sum()

    # Generate the pie chart
    fig_gdp_sector = px.pie(sector_df, values='Value', names='Sector', title='Sectoral Contribution to GDP',
                            labels={'Sector': 'Sector', 'Value': 'Contribution to GDP (%)'})
    graphJSON3 = fig_gdp_sector.to_json()

    # GDP Growth Rate
    gdp_growth = pd.read_csv('data/gdp/GDP_growth_annual_percent.csv')
    fig_gdp_growth = px.line(gdp_growth, x='Year', y='Value', title='GDP Growth Rate (Annual %)',
                             labels={'Year': 'Year', 'Value': 'Growth Rate (%)'})
    graphJSON1 = fig_gdp_growth.to_json()

    # GDP Per Capita
    gdp_per_capita = pd.read_csv('data/gdp/GDP_per_capita_current_USD.csv')
    fig_gdp_per_capita = px.line(gdp_per_capita, x='Year', y='Value', title='GDP Per Capita (Current USD)',
                                 labels={'Year': 'Year', 'Value': 'GDP Per Capita (USD)'})
    graphJSON2 = fig_gdp_per_capita.to_json()

    # GDP (Current USD) - Bar Chart
    gdp_current_usd = pd.read_csv('data/gdp/GDP_current_USD.csv')
    fig_gdp_current_usd = px.bar(gdp_current_usd, x='Year', y='Value', title='GDP (Current USD)',
                                  labels={'Year': 'Year', 'Value': 'GDP (USD)'})
    graphJSON4 = fig_gdp_current_usd.to_json()

    # GDP Per Unit of Energy Use
    gdp_per_energy = pd.read_csv('data/gdp/GDP_per_unit_of_energy_use_PPP_per_kg_of_oil_equivalent.csv')
    fig_gdp_per_energy = px.line(gdp_per_energy, x='Year', y='Value', title='GDP Per Unit of Energy Use (PPP per kg of oil equivalent)',
                                 labels={'Year': 'Year', 'Value': 'GDP Per Unit of Energy Use'})
    graphJSON5 = fig_gdp_per_energy.to_json()

    # GDP Deflator
    gdp_deflator = pd.read_csv('data/gdp/GDP_deflator_base_year_varies_by_country.csv')
    fig_gdp_deflator = px.line(gdp_deflator, x='Year', y='Value', title='GDP Deflator',
                               labels={'Year': 'Year', 'Value': 'GDP Deflator'})
    graphJSON6 = fig_gdp_deflator.to_json()

    return render_template('gdp.html', graph_gdp_growth=graphJSON1, graph_gdp_per_capita=graphJSON2, graph_sectoral_gdp=graphJSON3, graph_gdp_current_usd=graphJSON4, graph_gdp_per_energy=graphJSON5, graph_gdp_deflator=graphJSON6, source=source)
