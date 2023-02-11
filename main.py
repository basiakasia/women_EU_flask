from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import json
import plotly
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
 
app = Flask(__name__)

df = pd.read_csv('women_EU2.csv', sep=',')

@app.route('/', methods=['GET','POST'])
def search():
	df = pd.read_csv('women_EU2.csv', sep=',')
	if request.method == 'POST':
		country_name = request.form.get('country')
		return redirect(f"/{country_name}")
		#return redirect(url_for("country_plot", country=country_name))
	return render_template('base.html', table=df)



@app.route('/<country>')
def country_plot(country):
	df = pd.read_csv('women_EU2.csv', sep=',')
	
	df_country = df[df['country'] == country]

	fig = make_subplots(rows=1, cols=2)
	# Create Bar chart
	fig.add_trace(go.Bar(name="goverment", x=df_country['year'], y=df_country['GOV']), 1,1)
	fig.add_trace(go.Bar(name="parlament", x=df_country['year'], y=df_country['PARL']), 1,2)

	
	fig.update_yaxes(title_text="%")

	fig.update_yaxes(range=[0, 100])
	fig.update_xaxes(tickangle= -90, showticklabels=True, type='category') # to show all x-axis tick values 
	# Create graphJSON
	#layout = go.Layout(title='Seats held by women in PL', xaxis={'title':'Year'}, yaxis={'title':'GOV'})

	#fig = px.Figure(data=[plot], layout=layout)
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder) 
	# Use render_template to pass graphJSON to html
	return render_template('plot.html', graphJSON=graphJSON, country=country, table=df)



if __name__ == '__main__':
	app.run(debug=True)