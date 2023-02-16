from prefect.filesystems import S3
from prefect import flow
from lab_three import alpha_flow
from prefect.deployments import Deployment

#201 Lab


#this block was created in the prefect ui
s3 = S3.load("je-s3-bucket")

# this moves all code in the current filesystem to the s3 bucket, 
# as well as creates a deployment for the "alpha_flow" (really regret that name) 
# that can run from s3 instead of my local project
deploy = Deployment.build_from_flow(
    flow=alpha_flow,
    name="S3 Example",
    storage=s3,
)

if __name__ == "__main__":
    deploy.apply() #dont need an offical function to run this