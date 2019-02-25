from flask import Flask, Response
from kafka import KafkaConsumer

consumer = KafkaConsumer('my-topic', bootstrap_servers='localhost:9092')

app = Flask(__name__)


def kafkastream():
    for message in consumer:
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + message.value + b'\r\n\r\n')


@app.route('/')
def index():
    return Response(kafkastream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
