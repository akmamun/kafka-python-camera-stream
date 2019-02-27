# Real time Video Streaming with Kafka and Python
<p align="center">
  <img width="400" height="200" src="https://cdn-images-1.medium.com/max/600/1*iUWxneAQ_kozzLPkFsrakw.png">
</p>
 
Install And Configure [Apache Kafka](https://en.wikipedia.org/wiki/Apache_Kafka), [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) and [ZooKeeper](https://en.wikipedia.org/wiki/Apache_ZooKeeper) 
### Let's making your Ubuntu up to date
```sh
sudo apt-get update -y
sudo apt-get upgrade -y
```
### Installing Java
Before installing Kafka, you will need to install Java, add this repository
```sh
sudo add-apt-repository -y ppa:webupd8team/java
```
Next, update the metadata of the new repository and install JDK 8
```sh
sudo apt-get update
sudo apt-get install oracle-java8-installer -y
```

## Install ZooKeeper
```sh
sudo apt-get install zookeeperd
```
## Install And Start Kafka Server
```sh
wget https://www-eu.apache.org/dist/kafka/2.1.1/kafka_2.11-2.1.1.tgz 
``` 
If not work, download latest binary of apache kafka from [Kafka](https://kafka.apache.org/downloads) official site

Next, create a directory for Kafka installation
```sh
sudo mkdir /opt/Kafka
cd /opt/Kafka
```
Extract the downloaded archive using tar command in /opt/Kafka
```sh
sudo tar -xvf kafka_2.11-2.1.1.tgz -C /opt/Kafka/
```
Make Sure Server is Running 
```sh
sudo /opt/Kafka/kafka_2.11-2.1.1/bin/kafka-server-start.sh /opt/Kafka/kafka_2.11-2.1.1/config/server.properties
```
Now create a sample topic with name "testing"
```sh
sudo /opt/Kafka/kafka_2.11-2.1.1/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1  --partitions 1 --topic testing
```
Now create environment and install Kafka-Python, Open-CV and Flask Server
```sh
pip install -r requirements.txt
```
Lets run Producer
```sh
python producer.py 
```
Consumer
```sh
python consumer.py
```
Now Browse this
http://localhost:5000/

Credit
- [Distributed video stream with python](https://scotch.io/tutorials/build-a-distributed-streaming-system-with-apache-kafka-and-python)