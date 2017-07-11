# sp500-descriptions

output.csv contains a list of S&P 500 companies with their sec-filed descriptions.  a few of them are missing, but it should
be good enough to use as dummy data for a test project, which is what i needed.

## data sources

i grabbed the list of tickers from https://github.com/datasets/s-and-p-500-companies , which was missing descriptions.

i got the descriptions using tiingo's free API.  this repo contains the script that loads the above CSV and appends the descriptions after looking them up through tiingo.  see steps.txt on how to use it.
