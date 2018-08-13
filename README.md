## Dale slack

Little project for [Magrathea Labs](http://magrathealabs.com) Slack workspace that works like the following:
 1) A person types `/dale` slash command
 2) The app returns a gif of a person doing a "Dale" hand movement.

It is being hosted on AWS and using the EC2 resource. All the infra configuration is done with Terraform; the file `data.ft` contains the needed data, in specific the default VPC and default subnet where the instance will be launched; `main.tf` has the configuration for the EC2 instance and the security group attached to it. Only connections via ssh, port 22, and http, port 80, are allowed with the instance.

- [Dependencies](#deṕendencies)
- [Setup](#setup)
- [Development](#development)
- [Deploy](#deploy)


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
