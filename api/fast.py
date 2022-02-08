from dataclasses import dataclass
import string
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"greeting": "Hello world"}

@app.get("/predict")
def predict(pickup_datetime, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude, passenger_count):
    return {'pickup_datetime: ': pickup_datetime, 'pickup_longitude: ': pickup_longitude, 'pickup_latitude: ': pickup_latitude,\
            'dropoff_longitude: ': dropoff_longitude, 'dropoff_latitude: ': dropoff_latitude, 'passenger_count: ': passenger_count}

import ipdb; ipdb.set_trace()
X_pred = pd.DataFrame({'key':pd.Series(dtype='object'), 'pickup_datetime':pd.Series(dtype='object')\
    ,'pickup_longitude':pd.Series(dtype='float') ,'pickup_latitude':pd.Series(dtype='float') ,'dropoff_longitude':pd.Series(dtype='float')\
        ,'dropoff_latitude':pd.Series(dtype='float') ,'passenger_count':pd.Series(dtype='int') })
