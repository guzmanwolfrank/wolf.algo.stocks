# 10 day moving average on a stock of users choice within Yfinance Yticker library
#coded for Firefox default browser, Windows 10 OS, Python language 



import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


#define user input 

user_input = input('Enter Stock Symbol: ')


#User Input as stock 
stock = yf.Ticker(user_input)


#Yfinance Defs 
recco = stock.recommendations


#look back period 
stock.history(period='6mo') 
eureka = pd.DataFrame(stock.history(period='90d'))

#List columns 1-5
N = 5
data = eureka.iloc[:, :N]
df = data

df_ma = df.copy()

df_ma['MA_10'] = df_ma.Close.rolling(window=10).mean()

df_ma.dropna(inplace=True)

df_plot = df_ma.iloc[-100:].copy()

fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.add_trace(go.Candlestick(
    x=df_plot.index, open=df_plot.Open, high=df_plot.High, low=df_plot.Low, close=df_plot.Close,
    line=dict(width=1), opacity=1,
    increasing_fillcolor='#24A06B',
    decreasing_fillcolor="#CC2E3C",
    increasing_line_color='#2EC886',  
    decreasing_line_color='#FF3A4C'
))
fig.add_trace(go.Scatter(x=df_plot.index, 
    y=df_plot.MA_10,
    line=dict(color="#027FC3", width=2),
    line_shape='spline',
    name='MA_10'
    ))
fig.update_layout(width=1000,height=800,
    margin=dict(l=10,r=60,b=10,t=40),
    font=dict(size=10,color="#e1e1e1"),
    paper_bgcolor="#1e1e1e",
    plot_bgcolor="#1e1e1e",
    title =str(stock) +"chart",
    xaxis_title="Time",
    yaxis_title= "Price")
fig.update_xaxes(
    gridcolor="#1f292f",
    showgrid=True,fixedrange=True,rangeslider=dict(visible=False),
    rangeselector=dict(

)                                                                                   
)

fig.update_yaxes(
    gridcolor="#1f292f",
    showgrid=True
)
fig.show()
#fig.write_image('chart.png')


print(recco)


