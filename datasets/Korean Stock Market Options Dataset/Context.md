# About Dataset
**Context**
The implied volatility of the Korean market is represented by the index called VKOSPI. An underlying asset of VKOSPI is KOSPI200, which is widely known as a Korean blue-chip index. VKOSPI is calculated based on KOSPI200 options. To put it simple, KOSPI200 and VKOSPI is analogous to S&P500 and VIX in the US.

**For more info:**
[KOSPI200](https://global.krx.co.kr/contents/GLB/02/0201/0201010100/GLB0201010100.jsp)
[VKOSPI](https://global.krx.co.kr/contents/GLB/02/0201/0201010100/GLB0201010100.jsp)

**About the data**
Each row represents a trading day. Note that trading days don't include the weekends and holidays.
For stands for Foreigners, while Indiv stands for Individuals.
Amount in the column names represents (Price)*(Quantity), while Quantity only represents the quantity.
Call, Put, and Future represent Call option of KOSPI200, Put option of KOSPI200, and Future of KOSPI200 respectively.
Day_till_expiration refers to the days left untill the expiration day of options. Note that every second Thursday is the expiration day.
Usage of dataset
The dataset includes data mainly related to options.

**Background Knowledge**
*Options*
Options are financial instruments that are derivatives based on the value of underlying securities such as stocks. An options contract offers the buyer the opportunity to buy or sell—depending on the type of contract they hold—the underlying asset. Unlike futures, the holder is not required to buy or sell the asset if they choose not to.

Call options allow the holder to buy the asset at a stated price within a specific timeframe.
Put options allow the holder to sell the asset at a stated price within a specific timeframe.
Each option contract will have a specific expiration date by which the holder must exercise their option.

*Volatility*
In finance, volatility (symbol σ) is the degree of variation of a trading price series over time, usually measured by the standard deviation of logarithmic returns.
Historic volatility measures a time series of past market prices. Implied volatility looks forward in time, being derived from the market price of a market-traded derivative (in particular, an option).

*Open Interest*
Open interest is the total number of outstanding derivative contracts, such as options or futures that have not been settled for an asset.

*P/C Ratio*
The put-call ratio is calculated by dividing the number of traded put options by the number of traded call options.

**For more info:**
[Options Definition](https://www.investopedia.com/terms/o/option.asp)
[Volatility Definition](https://www.investopedia.com/terms/v/volatility.asp)
[Open Interest Definition](https://www.investopedia.com/terms/o/openinterest.asp)
[P/C Ratio Definition](https://www.investopedia.com/ask/answers/06/putcallratio.asp)