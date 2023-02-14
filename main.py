from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import json
import plotly
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Create a new app 
app = Flask(__name__)

# Load data from file
df = pd.read_csv('women_EU2.csv', sep=',')

# Index route with side search dropdown to choose country
@app.route('/', methods=['GET','POST'])
def search():
	if request.method == 'POST':
		country_name = request.form.get('country')
		return redirect(f"/{country_name}")
	else:
		return render_template('base.html', table=df)

# Route with side search and plots for choosen country
@app.route('/<country>')
def country_plot(country):
	# Filter data for selected country	
	df_country = df[df['country'] == country]
	# Create two plots in two columns
	fig = make_subplots(rows=1, cols=2)
	# Create Bar chart
	fig.add_trace(go.Bar(name="goverment", x=df_country['year'], y=df_country['GOV']), 1,1)
	fig.add_trace(go.Bar(name="parlament", x=df_country['year'], y=df_country['PARL']), 1,2)
	# Change y-axis title
	fig.update_yaxes(title_text="%")
	# Configure y-axis range to show better percentage
	fig.update_yaxes(range=[0, 100])
	fig.update_xaxes(tickangle= -90, showticklabels=True, type='category') # to show all x-axis tick values 
	# Create graphJSON
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) 
	# Use render_template to pass graphJSON to html
	return render_template('plot.html', graphJSON=graphJSON, country=country, table=df)

if __name__ == '__main__':
	app.run(debug=True)