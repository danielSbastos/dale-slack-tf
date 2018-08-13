provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "ubuntu" {
  ami               = "ami-2e1ef954"
  instance_type     = "t2.micro"
  availability_zone = "us-east-1a"
  key_name          = "terraform"
  subnet_id         = "${data.aws_subnet.selected.id}"
  security_groups   = ["${aws_security_group.security-group.id}"]
  user_data         = "${file("user_data.sh")}"

  tags {
    Name = "Dale slack"
  }

}


resource "aws_security_group" "security-group" {
  name        = "allow_port_80"
  description = "Allow inbound traffic from port 80"
  vpc_id      = "${data.aws_vpc.vpc.id}"

  ingress {
    from_port   = 80
    to_port     = 80
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
