**Context**
Forex is the largest market in the world, predicting the movement of prices is not a simple task, this dataset pretends to be the gateway for people who want to conduct trading using machine learning.

**About the Dataset**
This dataset contains 4479 simulated winning transactions (real data, fictitious money) (3 years 201408-201708) with buy transactions (2771 operations 50.7%) and sell (2208 transactions, 49.3%), to generate this data a script of metatrader was used, operations were performed in time frame 4Hour and fixed stop loss and take profits of 50 pips (4 digits) were used to determine if the operation is winning. Each operation contains a set of classic technical indicators like rsi, mom, bb, emas, etc. (last 24 hours)

**Note**
The problem of predicting price movement is reduced with this dataset to a classification problem:
"use the variables rsi1 to dayOfWeek to predict the type of correct operation to be performed (field=tipo)"
tipo = 0 ==> Operation buy
tipo= 1 ==> Operation = sell: