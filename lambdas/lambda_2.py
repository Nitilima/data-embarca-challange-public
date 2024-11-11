import os
import boto3
import pandas as pd
from datetime import datetime
import sqlite3
from dotenv import load_dotenv

load_dotenv()

s3_client = boto3.client('s3')

def lambda2(event, context):
    bucket_name = os.getenv('BUCKET_NAME')
    file_key = event.get('file_key')
    db_path = os.getenv('DB_PATH', 'database.db')

    response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    df = pd.read_csv(response['Body'])

    vehicles = ['automovel', 'bicicleta', 'caminhao', 'moto', 'onibus']
    result = df[df['vehicle'].isin(vehicles)].groupby('vehicle')['number_deaths'].sum().reset_index()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT,
            road_name TEXT,
            vehicle TEXT,
            number_deaths INTEGER
        )
    ''')

    for _, row in result.iterrows():
        cursor.execute('''
            INSERT INTO accidents (created_at, road_name, vehicle, number_deaths)
            VALUES (?, ?, ?, ?)
        ''', (datetime.now(), row['road_name'], row['vehicle'], row['number_deaths']))

    conn.commit()
    conn.close()

    return {"status": "Data processed and saved to DB"}