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

Start the server with
`sudo python3 app.py` (`sudo` is needed because port `80` will be used)

To get a dale gif, make the following request

`curl -X POST localhost/dale_gif`

It should return something sililar to the snippet below

```sh
{
  "response_type": "in_channel",
  "attachments": [{
    "title": "Vamo dale",
    "image_url": "https://media.giphy.com/media/8FGM7VT9bre1TqKRds/giphy.gif"
  }]
}
```

## Deploy

Make sure you've got `/.aws/credentials` setup with your AWS secret access key and access key, then, execute the following

```sh
terraform init
terraform plan (not necessary but nice to double check the changes)
terraform apply
```

## Kubernetes

This application is my pet project for Kubernetes. There are the following structures (inside `/kubernetes` folder):

- `web-pod.yml` creates a pod with a single container, exposing the port 5000
- `web-svc.yml` creates a NodePort service for this pod, allowing it to be accessed externally via the node `IP` and the pod `port` defined in this service.

To test it locally:
  1) Install `minikube` and `kubectl`
  2) Start `minikube` with `minikube start`
  3) Check the cluster if alright with `kubectl cluster-info`
  4) If yes, then create the web service and pod, `kubectl create -f web-pod.yml` and `kubectl create -f web-svc.yml`
  5) Check that they were created with `kubectl get pods` and `kubectl get svc`
  6) Now make a `POST` request to this service, first get the node's IP (`Kubernetes master`) with `kubectl cluster-info` and the service's `port` with `kubectl get svc` (search for the `web` service and for the exposed port between `30000-32767`). For example: `curl -X POST 192.168.99.100:31321/dale_gif`
