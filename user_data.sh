sudo yum update -y
sudo yum install -y docker git

git clone https://github.com/danielSbastos/dale-slack-tf.git
cd dale-slack-tf

sudo usermod -a -G docker ec2-user
sudo curl -L https://github.com/docker/compose/releases/download/1.9.0/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
sudo chmod +x /usr/local/bin/docker-compose
sudo service docker start
sudo chkconfig docker on

docker-compose build
docker-compose up
