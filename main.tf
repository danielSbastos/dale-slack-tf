provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ubuntu" {
  ami               = "ami-0ff8a91507f77f867"
  instance_type     = "t2.micro"
  availability_zone = "us-east-1a"
  key_name          = "dale"
  subnet_id         = "${data.aws_subnet.selected.id}"
  security_groups   = ["${aws_security_group.security-group.id}"]
  user_data         = "${file("user_data.sh")}"

  tags {
    Name = "Dale slack"
  }

}


resource "aws_security_group" "security-group" {
  name        = "allow_port_5000"
  description = "Allow inbound traffic from port 5000"
  vpc_id      = "${data.aws_vpc.vpc.id}"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
