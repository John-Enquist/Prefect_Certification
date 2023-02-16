from prefect import flow


#just mucking around
@flow
def add(num_one, num_two):
    print(f"the sum is: {num_one + num_two}")

if __name__ == "__main__":
    add(8, 4)
