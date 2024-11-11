import os
import boto3
import requests
import yaml
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

s3_client = boto3.client('s3')

def lambda1(event, context):
    bucket_name = os.getenv('BUCKET_NAME')
    link_name = event.get('link_name')

    with open('links.yml', 'r') as file:
        links = yaml.safe_load(file)

    link = next((item['url'] for item in links['links'] if item['nome'] == link_name), None)

    if not link:
        return {"status": "Link not found"}

    response = requests.get(link)
    if response.status_code == 200:
        file_key = f"data_{datetime.now().isoformat()}.csv"
        s3_client.put_object(Bucket=bucket_name, Key=file_key, Body=response.content)
        return {"status": "CSV downloaded and saved to S3", "file_key": file_key}
    else:
        return {"status": "Failed to download CSV"}