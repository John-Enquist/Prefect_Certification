import httpx
from prefect import flow

@flow
def test_flow():
    res = httpx.get("https://example.com")
    print(res)

if __name__ == "__main__":
    test_flow()
