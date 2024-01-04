from fastapi import FastAPI, HTTPException, Header
import pandas as pd

app = FastAPI()

df = pd.read_csv("waiter-tip-prediction/tips.csv")


API_KEY = "testingapitokenkey1234" #testing api token key 1234

@app.get("/") #root endpoint
def home():
  return df.head().to_dict(orient='records')

@app.get("/protected/{time}") #protected api
def protect(time:str,api_key: str = Header(None)):

  if api_key is None or api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
  else:
    query = df[df['time']==time.capitalize()].to_dict(orient='records')
    if len(query)==0:
       raise HTTPException(status_code=404, detail="Data Not Found")
    else:
        return query 