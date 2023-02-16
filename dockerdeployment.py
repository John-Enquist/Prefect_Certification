from prefect.infrastructure.docker import DockerContainer
from prefect.deployments import Deployment
from lab_three import alpha_flow

dock_block = DockerContainer.load("basic-docker-block")

#this example pulls a docker image i created in the ui (base python slim image for docker)
#and creates a deployment for alpha flow that will run inside the docker container
#also added some tags
docker_test = Deployment.build_from_flow(
    alpha_flow,
    "docker_two",
    apply= True,
    output= True,
    infrastructure=dock_block,
    tags=['test', 'shame', 'fear', 'docker'],
    work_queue_name = 'test_env'
)

