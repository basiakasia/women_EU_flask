# women_EU_flask

Seats held by women in national parliaments and governments.
App provides visualization of data for EU countries over the years 2003-2022.

## Technology Stack
- Python
- Flask
- Pandas
- Plotly

## Installation
Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
 women_EU_flask
    ├── main.py
    ├── static
    │   └── styles.css
    ├── templates
    │   ├── base.html
    │   ├── plot.html
    │   ├── view.html
    ├── women_EU2.csv
    ├── requirements.txt
    └── README.md
```

## Run Flask
### Run flask for develop
```
$ python main.py
```
In flask, Default port is `5000`

Open to view in browser: `http://127.0.0.1:5000`

## Data description
The indicator measures the proportion of women in national parliaments and national governments.

## Unit of measure
% of seats

## Source of data
Gender Statistics Database of the European Institute for Gender Equality (EIGE)
