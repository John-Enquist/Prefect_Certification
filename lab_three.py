import httpx
from prefect import flow, task, get_run_logger
from prefect.tasks import task_input_hash
import pandas as pd
import requests
from prefect.blocks.system import Secret

# secret_block = Secret.load("alphavantage")

# # Access the stored secret
# secret_block.get()


@task(cache_key_fn=task_input_hash, retries=2, retry_delay_seconds=5)
def get_alphavantage_info():
    try:
        secret_block = Secret.load("alphavantage")
        api_key = secret_block.get()
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'
        r = requests.get(url)
        data = r.json()

        print(data)
    except:
        pass


@flow()
def alpha_flow():
    get_alphavantage_info()

if __name__ == "__main__":
    alpha_flow()
