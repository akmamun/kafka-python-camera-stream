Video Streaming with Kafka and Python

Install And Configure Apache Kafka, Java, ZooKeeper and Kafka Server
## [Install And Configure Apache Kafka](https://devops.ionos.com/tutorials/install-and-configure-apache-kafka-on-ubuntu-1604-1/)

```python
pip install -r requirements.txt
```

Make Sure Server is Running 
```bash
sudo /opt/Kafka/kafka_2.11-2.1.1/bin/kafka-server-start.sh /opt/Kafka/kafka_2.11-2.1.1/config/server.properties
```
Producer:

```bash
python src/producer.py 
```

Consumer:

```bash
python src/consumer.py
```
Now Browse this
http://localhost:5000/