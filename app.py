from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)



def generate_plot_html(tickers):
    
    fig = px.line()
    for ticker in tickers:
        df = yf.download(ticker, period="1y", interval="1d")
        fig.add_scatter(x=df.index, y=df['Close'], mode='lines', name=ticker)
    
    fig.update_layout(
        title='Stock Prices',
        xaxis_title='Date',
        yaxis_title='Price',
        autosize=True,  

        margin=dict(l=0, r=0, t=30, b=0), 
        paper_bgcolor='#fff',  
        plot_bgcolor='#fff',  
        font=dict(family='Arial, sans-serif', size=10, color='#333'), 
         legend=dict(
            orientation="v",  # Default to vertical orientation
            yanchor="top",
            y=1,
            xanchor="right",
            x=1,
               bgcolor='rgba(255, 255, 255, 0.8)',  # White background with 80% opacity
            bordercolor='rgba(0, 0, 0, 0.1)',   # Light border color
            borderwidth=1
        )

    )

    plot_html = pio.to_html(fig, full_html=False, include_plotlyjs='cdn', config={'responsive': True})
    return plot_html




def get_tickers():
    tickers = []
    with open('ticker.txt', 'r') as file:
        tickers = [line.strip() for line in file]

    return tickers


@app.route('/', methods=['GET', 'POST'])
def index():
    tickers = request.form.getlist('tickers')
    if not tickers:
        tickers = ['RELIANCE.NS']  
    
    plot_html = generate_plot_html(tickers)
    
    all_tickers = get_tickers()
    
    return render_template('index.html', plot_html=plot_html, all_tickers=all_tickers, selected_tickers=tickers)

if __name__ == '__main__':
    app.run(debug=True)
