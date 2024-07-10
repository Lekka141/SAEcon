import os
import pandas as pd
import plotly.express as px
from jinja2 import Environment, FileSystemLoader

# Define directories
template_dir = 'templates'
output_dir = 'docs'
data_dir = 'data'

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader(template_dir))

def static_url(endpoint, **values):
    filename = values.get('filename', '')
    return os.path.join('static', filename)

env.globals['url_for'] = static_url

def load_gdp_data():
    gdp_growth = pd.read_csv(os.path.join(data_dir, 'gdp/GDP_growth_annual_percent.csv'))
    gdp_per_capita = pd.read_csv(os.path.join(data_dir, 'gdp/GDP_per_capita_current_USD.csv'))
    gdp_current_usd = pd.read_csv(os.path.join(data_dir, 'gdp/GDP_current_USD.csv'))
    gdp_per_energy = pd.read_csv(os.path.join(data_dir, 'gdp/GDP_per_unit_of_energy_use_PPP_per_kg_of_oil_equivalent.csv'))
    gdp_deflator = pd.read_csv(os.path.join(data_dir, 'gdp/GDP_deflator_base_year_varies_by_country.csv'))
    sector_files = {
        'Manufacturing': 'trade/Manufacturing_value_added_percent_of_GDP.csv',
        'Services': 'trade/Services_value_added_percent_of_GDP.csv',
    }

    sector_data = []
    for sector, file in sector_files.items():
        df = pd.read_csv(os.path.join(data_dir, file))
        recent_data = df[df['Year'] == df['Year'].max()]
        total_value = recent_data['Value'].sum()
        sector_data.append({'Sector': sector, 'Value': total_value})

    sector_data.append({'Sector': 'Agriculture', 'Value': 10})
    sector_df = pd.DataFrame(sector_data)
    sector_df['Value'] = sector_df['Value'] * 100 / sector_df['Value'].sum()

    fig_gdp_growth = px.line(gdp_growth, x='Year', y='Value', title='GDP Growth Rate (Annual %)')
    fig_gdp_per_capita = px.line(gdp_per_capita, x='Year', y='Value', title='GDP Per Capita (Current USD)')
    fig_gdp_current_usd = px.bar(gdp_current_usd, x='Year', y='Value', title='GDP (Current USD)')
    fig_gdp_per_energy = px.line(gdp_per_energy, x='Year', y='Value', title='GDP Per Unit of Energy Use (PPP per kg of oil equivalent)')
    fig_gdp_deflator = px.line(gdp_deflator, x='Year', y='Value', title='GDP Deflator')
    fig_gdp_sector = px.pie(sector_df, values='Value', names='Sector', title='Sectoral Contribution to GDP')

    return {
        'graph_gdp_growth': fig_gdp_growth.to_json(),
        'graph_gdp_per_capita': fig_gdp_per_capita.to_json(),
        'graph_gdp_current_usd': fig_gdp_current_usd.to_json(),
        'graph_gdp_per_energy': fig_gdp_per_energy.to_json(),
        'graph_gdp_deflator': fig_gdp_deflator.to_json(),
        'graph_sectoral_gdp': fig_gdp_sector.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_demographics_data():
    population_growth = pd.read_csv(os.path.join(data_dir, 'demographics/Population_growth_annual_percent.csv'))
    population_density = pd.read_csv(os.path.join(data_dir, 'demographics/Population_density_people_per_sq_km_of_land_area.csv'))
    urban_population = pd.read_csv(os.path.join(data_dir, 'demographics/Population_in_urban_agglomerations_of_more_than_1_million_percent_of_total_population.csv'))
    population_age_groups = pd.read_csv(os.path.join(data_dir, 'demographics/Population_ages_0-14_total.csv'))
    population_age_groups['Age Group'] = '0-14'
    age_group_15_64 = pd.read_csv(os.path.join(data_dir, 'demographics/Population_ages_15-64_total.csv'))
    age_group_15_64['Age Group'] = '15-64'
    age_group_65_above = pd.read_csv(os.path.join(data_dir, 'demographics/Population_ages_65_and_above_total.csv'))
    age_group_65_above['Age Group'] = '65+'

    population_age_groups = pd.concat([population_age_groups, age_group_15_64, age_group_65_above])

    fig_population_growth = px.line(population_growth, x='Year', y='Value', title='Population Growth (Annual %)')
    fig_population_density = px.bar(population_density, x='Year', y='Value', title='Population Density (People per sq km)')
    fig_urban_population = px.line(urban_population, x='Year', y='Value', title='Urban Population (% of Total Population)')
    fig_population_age_groups = px.bar(population_age_groups, x='Year', y='Value', color='Age Group', title='Population by Age Group')

    return {
        'graph_population_growth': fig_population_growth.to_json(),
        'graph_population_density': fig_population_density.to_json(),
        'graph_urban_population': fig_urban_population.to_json(),
        'graph_population_age_groups': fig_population_age_groups.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_environment_data():
    co2_emissions = pd.read_csv(os.path.join(data_dir, 'environmental/CO2_emissions_kt.csv'))
    freshwater_resources = pd.read_csv(os.path.join(data_dir, 'environmental/Renewable_internal_freshwater_resources_per_capita_cubic_meters.csv'))
    protected_areas = pd.read_csv(os.path.join(data_dir, 'environmental/Terrestrial_and_marine_protected_areas_percent_of_total_territorial_area.csv'))
    air_pollution = pd.read_csv(os.path.join(data_dir, 'environmental/PM2.5_air_pollution_mean_annual_exposure_micrograms_per_cubic_meter.csv'))

    fig_co2_emissions = px.line(co2_emissions, x='Year', y='Value', title='CO2 Emissions (kt)')
    fig_freshwater_resources = px.bar(freshwater_resources, x='Year', y='Value', title='Renewable Internal Freshwater Resources (per capita)')
    fig_protected_areas = px.bar(protected_areas, x='Year', y='Value', title='Protected Areas (% of Total Territorial Area)')
    fig_air_pollution = px.line(air_pollution, x='Year', y='Value', title='Air Pollution (PM2.5)')

    return {
        'graph_co2_emissions': fig_co2_emissions.to_json(),
        'graph_freshwater_resources': fig_freshwater_resources.to_json(),
        'graph_protected_areas': fig_protected_areas.to_json(),
        'graph_air_pollution': fig_air_pollution.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_fiscal_data():
    govt_debt = pd.read_csv(os.path.join(data_dir, 'fiscal/Central_government_debt_total_percent_of_GDP.csv'))
    fig_govt_debt = px.line(govt_debt, x='Year', y='Value', title='Central Government Debt (% of GDP)')

    govt_revenue = pd.read_csv(os.path.join(data_dir, 'fiscal/Tax_revenue_percent_of_GDP.csv'))
    fig_govt_revenue = px.line(govt_revenue, x='Year', y='Value', title='Government Revenue (% of GDP)')

    govt_expenditure = pd.read_csv(os.path.join(data_dir, 'fiscal/General_government_final_consumption_expenditure_percent_of_GDP.csv'))
    fig_govt_expenditure = px.line(govt_expenditure, x='Year', y='Value', title='Government Expenditure (% of GDP)')

    fiscal_balance = pd.read_csv(os.path.join(data_dir, 'fiscal/Net_lending_net_borrowing_percent_of_GDP.csv'))
    fig_fiscal_balance = px.line(fiscal_balance, x='Year', y='Value', title='Fiscal Balance (% of GDP)')

    return {
        'graph_govt_debt': fig_govt_debt.to_json(),
        'graph_govt_revenue': fig_govt_revenue.to_json(),
        'graph_govt_expenditure': fig_govt_expenditure.to_json(),
        'graph_fiscal_balance': fig_fiscal_balance.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_health_data():
    life_expectancy_female = pd.read_csv(os.path.join(data_dir, 'health/Life_expectancy_at_birth_female_years.csv'))
    life_expectancy_male = pd.read_csv(os.path.join(data_dir, 'health/Life_expectancy_at_birth_male_years.csv'))
    life_expectancy_total = pd.read_csv(os.path.join(data_dir, 'health/Life_expectancy_at_birth_total_years.csv'))

    fig_life_expectancy = px.line(life_expectancy_total, x='Year', y='Value', title='Life Expectancy at Birth (Years)')
    fig_life_expectancy.add_scatter(x=life_expectancy_female['Year'], y=life_expectancy_female['Value'], mode='lines', name='Female')
    fig_life_expectancy.add_scatter(x=life_expectancy_male['Year'], y=life_expectancy_male['Value'], mode='lines', name='Male')

    infant_mortality = pd.read_csv(os.path.join(data_dir, 'health/Mortality_rate_infant_per_1000_live_births.csv'))
    fig_infant_mortality = px.line(infant_mortality, x='Year', y='Value', title='Infant Mortality Rate (Per 1,000 Live Births)')

    health_expenditure = pd.read_csv(os.path.join(data_dir, 'health/Current_health_expenditure_per_capita_current_USD.csv'))
    fig_health_expenditure = px.line(health_expenditure, x='Year', y='Value', title='Health Expenditure Per Capita (Current USD)')

    return {
        'graph_life_expectancy': fig_life_expectancy.to_json(),
        'graph_infant_mortality': fig_infant_mortality.to_json(),
        'graph_health_expenditure': fig_health_expenditure.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_inflation_data():
    inflation_consumer_prices = pd.read_csv(os.path.join(data_dir, 'inflation/Inflation_consumer_prices_annual_percent.csv'))
    fig_inflation_consumer_prices = px.line(inflation_consumer_prices, x='Year', y='Value', title='Inflation, Consumer Prices (Annual %)')

    inflation_gdp_deflator = pd.read_csv(os.path.join(data_dir, 'inflation/Inflation_GDP_deflator_annual_percent.csv'))
    fig_inflation_gdp_deflator = px.line(inflation_gdp_deflator, x='Year', y='Value', title='Inflation, GDP Deflator (Annual %)')

    consumer_price_index = pd.read_csv(os.path.join(data_dir, 'inflation/Consumer_price_index_2010_base_100.csv'))
    fig_consumer_price_index = px.line(consumer_price_index, x='Year', y='Value', title='Consumer Price Index (2010 = 100)')

    return {
        'graph_inflation_consumer_prices': fig_inflation_consumer_prices.to_json(),
        'graph_inflation_gdp_deflator': fig_inflation_gdp_deflator.to_json(),
        'graph_consumer_price_index': fig_consumer_price_index.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_investment_data():
    gross_capital_formation_growth = pd.read_csv(os.path.join(data_dir, 'investment/Gross_capital_formation_annual_growth_percent.csv'))
    fig_gross_capital_formation_growth = px.line(gross_capital_formation_growth, x='Year', y='Value', title='Gross Capital Formation (Annual Growth %)')

    fdi_net_inflows = pd.read_csv(os.path.join(data_dir, 'investment/Foreign_direct_investment_net_inflows_percent_of_GDP.csv'))
    fig_fdi_net_inflows = px.line(fdi_net_inflows, x='Year', y='Value', title='Foreign Direct Investment (FDI), Net Inflows (% of GDP)')

    gross_fixed_capital_formation = pd.read_csv(os.path.join(data_dir, 'investment/Gross_fixed_capital_formation_percent_of_GDP.csv'))
    fig_gross_fixed_capital_formation = px.line(gross_fixed_capital_formation, x='Year', y='Value', title='Gross Fixed Capital Formation (% of GDP)')

    return {
        'graph_gross_capital_formation_growth': fig_gross_capital_formation_growth.to_json(),
        'graph_fdi_net_inflows': fig_fdi_net_inflows.to_json(),
        'graph_gross_fixed_capital_formation': fig_gross_fixed_capital_formation.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_monetary_data():
    deposit_interest_rate = pd.read_csv(os.path.join(data_dir, 'monetary/Deposit_interest_rate_percent.csv'))
    fig_deposit_interest_rate = px.line(deposit_interest_rate, x='Year', y='Value', title='Deposit Interest Rate (%)')

    domestic_credit_financial_sector = pd.read_csv(os.path.join(data_dir, 'monetary/Domestic_credit_provided_by_financial_sector_percent_of_GDP.csv'))
    fig_domestic_credit_financial_sector = px.line(domestic_credit_financial_sector, x='Year', y='Value', title='Domestic Credit Provided by Financial Sector (% of GDP)')

    real_interest_rate = pd.read_csv(os.path.join(data_dir, 'monetary/Real_interest_rate_percent.csv'))
    fig_real_interest_rate = px.line(real_interest_rate, x='Year', y='Value', title='Real Interest Rate (%)')

    return {
        'graph_deposit_interest_rate': fig_deposit_interest_rate.to_json(),
        'graph_domestic_credit_financial_sector': fig_domestic_credit_financial_sector.to_json(),
        'graph_real_interest_rate': fig_real_interest_rate.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_poverty_data():
    gini_index = pd.read_csv(os.path.join(data_dir, 'poverty/Gini_index.csv'))
    fig_gini_index = px.line(gini_index, x='Year', y='Value', title='Gini Index')

    poverty_2_15 = pd.read_csv(os.path.join(data_dir, 'poverty/Poverty_headcount_ratio_at_2.15_a_day_2017_PPP_percent_of_population.csv'))
    fig_poverty_2_15 = px.line(poverty_2_15, x='Year', y='Value', title='Poverty Headcount Ratio at $2.15 a Day (2017 PPP) (% of Population)')

    poverty_national = pd.read_csv(os.path.join(data_dir, 'poverty/Poverty_headcount_ratio_at_national_poverty_lines_percent_of_population.csv'))
    fig_poverty_national = px.line(poverty_national, x='Year', y='Value', title='Poverty Headcount Ratio at National Poverty Lines (% of Population)')

    return {
        'graph_gini_index': fig_gini_index.to_json(),
        'graph_poverty_2_15': fig_poverty_2_15.to_json(),
        'graph_poverty_national': fig_poverty_national.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_trade_data():
    exports_growth = pd.read_csv(os.path.join(data_dir, 'trade/Exports_of_goods_and_services_annual_growth.csv'))
    fig_exports_growth = px.line(exports_growth, x='Year', y='Value', title='Exports of Goods and Services (Annual Growth %)')

    imports_growth = pd.read_csv(os.path.join(data_dir, 'trade/Imports_of_goods_and_services_annual_growth.csv'))
    fig_imports_growth = px.line(imports_growth, x='Year', y='Value', title='Imports of Goods and Services (Annual Growth %)')

    exports_usd = pd.read_csv(os.path.join(data_dir, 'trade/Exports_of_goods_and_services_current_US.csv'))
    fig_exports_usd = px.bar(exports_usd, x='Year', y='Value', title='Exports of Goods and Services (Current USD)')

    imports_usd = pd.read_csv(os.path.join(data_dir, 'trade/Imports_of_goods_and_services_current_US.csv'))
    fig_imports_usd = px.bar(imports_usd, x='Year', y='Value', title='Imports of Goods and Services (Current USD)')

    trade_gdp = pd.read_csv(os.path.join(data_dir, 'trade/Trade_percent_of_GDP.csv'))
    fig_trade_gdp = px.line(trade_gdp, x='Year', y='Value', title='Trade as a Percentage of GDP')

    return {
        'graph_exports_growth': fig_exports_growth.to_json(),
        'graph_imports_growth': fig_imports_growth.to_json(),
        'graph_exports_usd': fig_exports_usd.to_json(),
        'graph_imports_usd': fig_imports_usd.to_json(),
        'graph_trade_gdp': fig_trade_gdp.to_json(),
        'source': "Source: World Bank (http://www.worldbank.org)"
    }

def load_data():
    data = {
        'gdp': load_gdp_data(),
        'demographics': load_demographics_data(),
        'environment': load_environment_data(),
        'fiscal': load_fiscal_data(),
        'health': load_health_data(),
        'inflation': load_inflation_data(),
        'investment': load_investment_data(),
        'monetary': load_monetary_data(),
        'poverty': load_poverty_data(),
        'trade': load_trade_data()
    }
    return data

def render_static(template_name, output_name, **context):
    template = env.get_template(template_name)
    rendered_html = template.render(**context)
    output_path = os.path.join(output_dir, output_name)
    
    if os.path.exists(output_path):
        with open(output_path, 'r') as f:
            existing_content = f.read()
        merged_content = existing_content + "\n" + rendered_html
        with open(output_path, 'w') as f:
            f.write(merged_content)
    else:
        with open(output_path, 'w') as f:
            f.write(rendered_html)

def main():
    data = load_data()
    templates = [
        'gdp.html', 'demographics.html', 'fiscal.html', 'inflation.html',
        'health.html', 'trade.html', 'monetary.html', 'poverty.html',
        'environment.html', 'investment.html'
    ]
    
    for template_name in templates:
        context_key = template_name.replace('.html', '')
        if context_key in data:
            render_static(template_name, template_name, **data[context_key])
        else:
            print(f"Data for template {template_name} not found.")
    
if __name__ == '__main__':
    main()
