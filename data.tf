data "aws_vpc" "vpc" {
  default = true
}


data "aws_subnet" "selected" {
  vpc_id = "${data.aws_vpc.vpc.id}"
  availability_zone =  "us-east-1a"
}
