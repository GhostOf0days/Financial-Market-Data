# Financial-Market-Data
This repository is a collection of financial market data and other relevant data.

** Large files **
Large files (over 100 Mb) may be gzipped (.gz file extension) to enable storage on Github. To un-gzip large files and return the original file, please run the decompress function in the *'gzipTool.py'* file within the Compression Tools folder (check the scripts folder). Please comment out the compress function. Example inputs are in comments for your convenience. To learn more about the gzip compression algorithm, please read the [documentation](https://www.gnu.org/software/gzip/manual/gzip.html).

A good source of alternative data is [Quiver Quantitative](https://www.quiverquant.com/).

**Feel free to add your own datasets!**

Note: For the hedge fund quality section, :heavy_check_mark: means the dataset is hedge fund quality, :test_tube: means the dataset is a research dataset, and :x: means the dataset is not hedge fund quality nor a research dataset.

| Source | Description | Last Updated | Hedge Fund Quality | Research Paper | Research Code |
| ------------ | ------------ | :----------: | :----------: | :----------: | :----------: |
| [Numerai Training Dataset](https://numer.ai/) | Clean and regularized, hedge fund quality stock market data | July 1, 2023 | :heavy_check_mark: | :x: | :x: |
| [FinGPT Dataset](https://github.com/AI4Finance-Foundation/FinGPT/tree/master) | Training data (Chinese and American) for a data-centric approach open-source financial large language model, FinGPT. | May 28, 2023 | :test_tube: | [Yang, H., Liu, X. Y., & Wang, C. D. (2023). FinGPT: Open-Source Financial Large Language Models. arXiv preprint arXiv:2306.06031.](https://arxiv.org/pdf/2303.17564.pdf) | [FinGPT Code](https://github.com/AI4Finance-Foundation/FinGPT/tree/master) |
| [StockNet Dataset](https://github.com/yumoxu/stocknet-dataset) | The StockNet dataset is a comprehensive dataset for stock movement prediction from tweets and historical stock prices. | Nov 2, 2018 | :test_tube: | [Yumo Xu and Shay B. Cohen. 2018. Stock Movement Prediction from Tweets and Historical Prices. In Proceedings of the 56st Annual Meeting of the Association for Computational Linguistics. Melbourne, Australia, volume 1.](https://aclanthology.org/P18-1183.pdf) | [StockNet Code](https://github.com/yumoxu/stocknet-code) |
| [EDT Dataset](https://github.com/Zhihan1996/TradeTheEvent/tree/main/data) | The EDT dataset is designed for corporate event detection and text-based stock prediction (trading strategy) benchmark. | 2 years ago as of July 2, 2023 | :test_tube: | [Zhihan Zhou, Liqian Ma, Han Liu. Trade the Event: Corporate Events Detection for News-Based Event-Driven Trading. In Findings of ACL 2021.](https://aclanthology.org/2021.findings-acl.186.pdf) | [TradeTheEvent Code](https://github.com/Zhihan1996/TradeTheEvent/tree/main) |
| [Stock Market Data Compilation 1](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs) | Historical daily prices and volumes of all U.S. stocks and ETFs | November 10th 2017 | :x: | :x: | :x: |
| [Stock Market Data Compilation 2](https://www.kaggle.com/datasets/paultimothymooney/stock-market-data) | Date, Volume, High, Low, and Closing Price (for all NASDAQ, S&P500, and NYSE listed companies) | 5 months ago as of July 2, 2023 | :x: | :x: | :x: |
| [Stock Market Data Compilation 3](https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset) | Historical daily prices for all tickers currently trading on NASDAQ | April 1, 2020 | :x: | :x: | :x: |
| [Apple Stock Dataset](https://www.kaggle.com/datasets/meetnagadia/apple-stock-price-from-19802021?resource=download) | Apple's stock performance from 1980 to 2022 | June 17, 2022 | :x: | :x: | :x: |
| [Microsoft Stock Dataset](https://www.kaggle.com/datasets/bilalwaseer/microsoft-stocks-from-1986-to-2023) | Microsoft Corporation's stock performance from 1986 to 2023 | 1 month ago as of July 2, 2023 | :x: | :x: | :x: |
| [S&P 500 Companies With Financials](https://datahub.io/core/s-and-p-500-companies-financials#data) | S&P 500 Companies with Key Financial Data | 2 years ago as of July 2, 2023 | :x: | :x: | :x: |
| [Index Price Dataset](https://www.kaggle.com/datasets/mattiuzc/stock-exchange-data) | Daily price data for indexes tracking stock exchanges from all over the world (United States, China, Canada, Germany, Japan, and more) | June 2, 2022 | :x: | :x: | :x: |
| [$AAPL Option Chains Dataset](https://www.kaggle.com/datasets/kylegraupe/aapl-options-data-2016-2020) | Historical Daily Options Price Quotes for $AAPL between 2016 and 2023 | March 31, 2023 | :x: | :x: | :x: |
| [$NVDA Option Chains Dataset](https://www.kaggle.com/datasets/kylegraupe/nvda-daily-option-chains-q1-2020-to-q4-2022) | Historical End of Day Options Price Quotes for $NVDA between Q1 2020 and Q4 2022 | December 30, 2022 | :x: | :x: | :x: |
| [$TSLA Option Chains Dataset](https://www.kaggle.com/datasets/kylegraupe/tsla-daily-eod-options-quotes-2019-2022) | Historical End of Day Options Price Quotes for $TSLA between 2019 and 2022 | December 30, 2022 | :x: | :x: | :x: |
| [$SPY Option Chains Dataset](https://www.kaggle.com/datasets/kylegraupe/spy-daily-eod-options-quotes-2020-2022) | Historical End of Day Options Price Quotes for $SPY between Q1 2019 and Q4 2022 | December 30, 2022 | :x: | :x: | :x: |
| [$QQQ Option Chains Dataset](https://www.kaggle.com/datasets/kylegraupe/qqq-daily-option-chains-q1-2020-to-q4-2022) | Historical Options data for Invesco QQQ Trust Series 1, $QQQ: Q1 2020 to Q4 2022 | December 30, 2022 | :x: | :x: | :x: |
| [Korean Stock Market Options Dataset](https://www.kaggle.com/datasets/ninetyninenewton/vkospi) | Korean Stock Market options dataset focused on volatility and other relevant factors | November 11, 2017 | :x: | :x: | :x: |
| [Europe Brent and WTI Spot Prices](https://datahub.io/core/oil-prices) | Europe Brent and WTI (Western Texas Intermediate) Spot Prices (Annual/ Monthly/ Weekly/ Daily) from the EIA U.S. (Energy Information Administration) | July 2, 2023 | :x: | :x: | :x: |
| [Gold Prices Dataset](https://datahub.io/core/gold-prices) | Monthly gold prices since 1950 in USD (London market). Data is sourced from the Bundesbank | 2 years ago as of July 2, 2023 | :x: | :x: | :x: |
| [Natural Gas Prices Dataset](https://datahub.io/core/natural-gas) | Time series of major natural gas prices including US Henry Hub. Data comes from U.S. Energy Information Administration EIA | 2 years ago as of July 2, 2023 | :x: | :x: | :x: |
| [VIX - CBOE Volatility Index Dataset](https://datahub.io/core/finance-vix) | CBOE Volatility Index (VIX) time-series dataset including daily open, close, high and low | 2 years ago as of July 2, 202 | :x: | :x: | :x: |
