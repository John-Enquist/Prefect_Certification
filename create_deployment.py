
from prefect.orion.schemas.schedules import CronSchedule
from prefect.deployments import Deployment
from lab_three import alpha_flow

#lab 105


#in this example we are creating a deployment for the alpha flow
#with a cron job schedule. this is cool because you can store your schedules for flows in code
#instead of in the Prefect UI (so you can use source control)
cron_test = Deployment.build_from_flow(
    alpha_flow,
    "certif",
    schedule=(CronSchedule(cron="0 0 * * *", timezone="America/Chicago")),
    apply= True,
    output= True
)