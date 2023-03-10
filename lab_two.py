import httpx
from prefect import flow, task, get_run_logger
from prefect.tasks import task_input_hash
import yfinance as yf
import pandas as pd

#lab 102
#the purpose of this lab was to run a subflow within a flow, as well as try caching,
# and retry functionality

@task(cache_key_fn=task_input_hash, retries=2, retry_delay_seconds=5)
def yfinance_flow(ticker):
    try:
        df = yf.download(ticker)
        print(df)
        sub_flow = sub_flow_ex()
        return df
    except:
        print("god knows")
        pass

@flow()
def sub_flow_ex():
    try:
        ass_df = yfinance_flow("ASS")
        print("successful tick")
        return ass_df
    except:
        print("this may not be a real ticker...")
        pass


@flow()
def main_flow(ticker):
    msft_df = yfinance_flow(ticker)
    print("successful tick")

if __name__ == "__main__":
    main_flow("MSFT")
