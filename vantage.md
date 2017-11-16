# Vantage Points

## Questions

5.1. CSV files are much easier to parse than JSON files. Usually all that is needed is to split on commas and line breaks to get an array of rows containing elements.

5.2. JSON is ideal for maintaining the particular structure of data when being transmitted. More complex structures can be preserved in JSON rather than in CSV.

5.3. https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=NFLX&interval=1min&apikey=NAJXWIA8D6VN6A3K&datatype=csv

5.4. The time stamps should be inside of the brackets with their associated data. I imagine it looking like this:

           {
            "1. time": "2017-11-14 16:00:00",
            "2. open": "84.0400",
            "3. high": "84.0800",
            "4. low": "84.0100",
            "5. close": "84.0500",
            "6. volume": "1969597"
           },


## Debrief

a. https://www.quora.com/What-is-the-difference-between-parsing-a-CSV-and-JSON-file-What-common-algorithms-would-you-use-in-both

b. 30 minutes
