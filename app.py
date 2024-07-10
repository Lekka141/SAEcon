from flask import Flask, render_template, jsonify
from routes.gdp import gdp_bp
from routes.demographics import demographics_bp
from routes.fiscal import fiscal_bp
from routes.inflation import inflation_bp
from routes.health import health_bp
from routes.trade import trade_bp
from routes.monetary import monetary_bp
from routes.poverty import poverty_bp
from routes.environment import environment_bp
from routes.investment import investment_bp
import json

app = Flask(__name__, static_folder='static')

# Register blueprints
app.register_blueprint(gdp_bp)
app.register_blueprint(demographics_bp)
app.register_blueprint(fiscal_bp)
app.register_blueprint(inflation_bp)
app.register_blueprint(health_bp)
app.register_blueprint(trade_bp)
app.register_blueprint(monetary_bp)
app.register_blueprint(poverty_bp)
app.register_blueprint(environment_bp)
app.register_blueprint(investment_bp)
 
# Home route
@app.route('/')
def index():
    # Placeholder for graph data
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('index.html', graph_json=graph_json)

# Route for GDP page
@app.route('/gdp')
def gdp():
    # Placeholder for graph data
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('gdp.html', graph_json=graph_json)

# Route for Demographics page
@app.route('/demographics')
def demographics():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('demographics.html', graph_json=graph_json)

# Route for Inflation page
@app.route('/inflation')
def inflation():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('inflation.html', graph_json=graph_json)

# Route for Trade page
@app.route('/trade')
def trade():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('trade.html', graph_json=graph_json)

# Route for Fiscal page
@app.route('/fiscal')
def fiscal():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('fiscal.html', graph_json=graph_json)

# Route for Monetary page
@app.route('/monetary')
def monetary():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('monetary.html', graph_json=graph_json)

# Route for Investment page
@app.route('/investment')
def investment():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('investment.html', graph_json=graph_json)

# Route for Poverty & Inequality page
@app.route('/poverty')
def poverty():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('poverty.html', graph_json=graph_json)

# Route for Health page
@app.route('/health')
def health():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('health.html', graph_json=graph_json)

# Route for Environmental Sustainability page
@app.route('/environment')
def environment():
    graph_data = {
        'data': [],  # Add your graph data here
        'layout': {}  # Add your graph layout here
    }
    graph_json = json.dumps(graph_data)
    return render_template('environment.html', graph_json=graph_json)

# Custom error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
