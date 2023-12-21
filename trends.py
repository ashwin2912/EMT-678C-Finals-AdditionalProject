import pandas as pd
import pytrends
from pytrends.request import TrendReq
import time as timer 
from datetime import datetime, date, time, timedelta


if __name__ == "__main__":

    dates="2020-01-01"+" "+"2023-12-15"
    print(dates)

    keywords=["unemployment"]
    #--------------------------------------
    # the function
    #--------------------------------------
    pytrends = TrendReq(hl='en-US', tz=360)
    future_dataframe={}
    c=1
    for k in keywords:   
        try:
            pytrends.build_payload([k], timeframe=dates, geo='US', gprop='')
            future_dataframe[c]=pytrends.interest_over_time() 
            future_dataframe[c].drop(['isPartial'], axis=1,inplace=True)
            c+=1
            result = pd.concat(future_dataframe, axis=1)
        except:
            print("***","\n","Error with ",k,"or not enough trending percentaje","\n","***")

    result.columns = result.columns.droplevel(0)
    df1=result.unstack(level=-1)
    df2=pd.DataFrame(df1)
    df2.reset_index(inplace=True)
    df2.columns = ["keyword","date","trend_index"]
    df2.to_csv("unemployment_pytrends-2020.csv")