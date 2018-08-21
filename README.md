# "Vamo Dale" Slack slash command

![Vamo dale](https://media.giphy.com/media/5bd09I7JVypLQdxERF/giphy.gif)

Little project for [Magrathea Labs](http://magrathealabs.com) Slack workspace that works like the following:
 1) A person types `/dale` slash command
 2) The app returns a gif of a person doing a "Dale" hand movement.

It is being hosted on AWS and using the EC2 resource. All the infra configuration is done with Terraform; the file `data.ft` contains the needed data, in specific the default VPC and default subnet where the instance will be launched; `main.tf` has the configuration for the EC2 instance and the security group attached to it. Only connections via ssh, port 22, and http, port 80, are allowed with the instance.

- [Dependencies](#deṕendencies)
- [Setup](#setup)
- [Development](#development)
- [Deploy](#deploy)
- [Kubernetes](#kubernetes)

## Dependencies

- Python 3.x
- Terraform (for deploy)

## Setup

After cloning it, install the dependencies with `pip3 install -r requirements.txt`

## Development

Start the server with `python3 app.py`

### Get a gif

To get a dale gif, make the following request

`curl -X POST localhost:5000/dale_gif`

It should return something similar to the snippet below

```sh
{
  "response_type": "in_channel",
  "attachments": [{
    "title": "Vamo dale",
    "image_url": "https://media.giphy.com/media/8FGM7VT9bre1TqKRds/giphy.gif"
  }]
}
```
### Register a gif

First upload your dale gif to [Giphy](https://giphy.com/) and get its id. For example, the following gif url, ´https://media.giphy.com/media/8FGM7VT9bre1TqKRds/giphy.gif`, has the id as `8FGM7VT9bre1TqKRds`

With the id, make the following request:

`curl -X POST localhost:5000/register_dale_gif -d '{"gif_id": "8FGM7VT9bre1TqKRds"}' -H "content-type: application/json"`

## Deploy

Make sure you've got `/.aws/credentials` setup with your AWS secret access key and access key, then, execute the following

```sh
terraform init
terraform plan (not necessary but nice to double check the changes)
terraform apply
```

## Kubernetes

This application is my pet project for Kubernetes. There are the following structures (inside `/kubernetes` folder):

- `web-deployment.yml` creates a deployment with 3 replicas, each with a single container running the python application and exposing port 5000.
- `web-svc.yml` creates a NodePort service for the pods created above, allowing them to be accessed externally via the node `IP` and the pod `port` defined in this service.
- `db-statefulset.yml` creates a statefulset for Redis in order to maintain state if its pods are restarted.
- `db-svc.yml` creates a service for the redis pod created above.

To test it locally:
  1) Install `minikube` and `kubectl`
  2) Start `minikube` with `minikube start`
  3) Check the cluster if alright with `kubectl cluster-info`
  4) If yes, then create the following objects
  ```sh
  kubectl create -f web-deployment.yml -f web-svc.yml -f db-statefulset.yml -f db-svc.yml
  ```
  5) Check that they were created with `kubectl get pods`. `kubectl get svc` and `kubectl get deployments`
  6) Now make a `POST` request to this service, first get the node's IP (`Kubernetes master`) with `kubectl cluster-info` and the service's `port` with `kubectl get svc` (search for the `web` service and for the exposed port between `30000-32767`). For example: `curl -X POST 192.168.99.100:31321/dale_gif`
