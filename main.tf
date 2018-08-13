provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ubuntu" {
  ami               = "ami-2e1ef954"
  instance_type     = "t2.micro"
  availability_zone = "us-east-1a"
  key_name          = "terraform"

  tags {
    Name = "Dale slack"
  }

  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install python-pip python-dev build-essential
              apt-get install git
              pip install -r requirements.txt
              python app.py
              EOF
}
