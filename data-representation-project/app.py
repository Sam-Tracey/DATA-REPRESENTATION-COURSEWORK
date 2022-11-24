from flask import Flask, render_template, request, redirect, url_for, session
import json
import pandas as pd
import plotly
import plotly.express as px
import plotly.graph_objects as go
from dataDAO import dataDAO

app = Flask(__name__)
app.secret_key='dataRepresentation'

@app.route('/')
def index():
    return render_template('login.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # search for user in database
        dataDAO.login(username, password)
        if dataDAO.login(username, password) is not None:
            session['username'] = username
            return render_template('home.html')
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
    

@app.route('/home')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('home.html')

@app.route('/about')
def about():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('about.html')

@app.route('/employee')
def employee():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('employee.html')

@app.route('/dash1')
def dash1():
    if not 'username' in session:
        return redirect(url_for('login'))
    data = dataDAO.readQuits()
    # convert data read from MySQL to dataframe
    df = pd.DataFrame(data)
    # convert date string to date
    df['date'] = pd.to_datetime(df['date'])     
    fig = px.scatter(df, x='date', y='num_quit', trendline="rolling",
                trendline_options=dict(window=5), trendline_color_override="red",
                width=1000, height=600)
    fig.update_layout(xaxis_title='Date', yaxis_title='Number of Quits')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "Employee Quits by Month With Quarterly Trendline"

    # Convert date to string to format properly in plotly table (otherwise it includes timestamp)
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    table = go.Figure(data=[go.Table(
                header=dict(values=['ID', 'Date', 'Number of Quits'],
                fill_color='#00008b',
                align='center', font_size=12, font_color='white'),
                cells=dict(values=[df.id, df.date, df.num_quit],
                fill_color='#e5ecf6',
                align='center', font_size=12))
            ])
    table.update_layout(width=600, height=525)
    table.update_layout(margin=dict(r=5, l=20, t=55, b=2))
    graphJSON1 = json.dumps(table, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dash1.html', graphJSON=graphJSON, header=header, graphJSON1=graphJSON1)
    

@app.route('/dash2')
def dash2():
    if not 'username' in session:
        return redirect(url_for('login'))
    data = dataDAO.readSCQuits()
    # convert data read from MySQL to dataframe
    df = pd.DataFrame(data)
    # convert date string to date
    df['date'] = pd.to_datetime(df['date'])     
    fig = px.scatter(df, x='date', y='num_quits', trendline="rolling",
                trendline_options=dict(window=5), trendline_color_override="red",
                width=1000, height=600)
    fig.update_layout(xaxis_title='Date', yaxis_title='Quits (Thousands)')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header = "All South Census Quits by Month With Quarterly Trendline"

    # Convert date to string to format properly in plotly table (otherwise it includes timestamp)
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    table = go.Figure(data=[go.Table(
                header=dict(values=['ID', 'Date', 'Quits (Thousands)'],
                fill_color='#00008b',
                align='center', font_size=12, font_color='white'),
                cells=dict(values=[df.id, df.date, df.num_quits],
                fill_color='#e5ecf6',
                align='center', font_size=12))
            ])
    table.update_layout(width=600, height=525)
    table.update_layout(margin=dict(r=5, l=20, t=55, b=2))
    graphJSON1 = json.dumps(table, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dash2.html', graphJSON=graphJSON, header=header, graphJSON1=graphJSON1)

@app.route('/dash3')
def dash3():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('dash3.html')




