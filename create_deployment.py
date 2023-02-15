
from prefect.orion.schemas.schedules import CronSchedule
from prefect.deployments import Deployment
from lab_three import alpha_flow


cron_test = Deployment.build_from_flow(
    alpha_flow,
    "certif",
    schedule=(CronSchedule(cron="0 0 * * *", timezone="America/Chicago")),
    apply= True,
    output= True
)