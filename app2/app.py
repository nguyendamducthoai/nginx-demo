from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Define a metric to track the total number of HTTP requests
REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests')

@app.route('/')
def index():
    REQUEST_COUNT.inc()  # Increment the request count by 1
    return 'Hello, world!'

# Expose metrics endpoint so Prometheus can scrape metrics
@app.route('/metrics')
def metrics():
    data = generate_latest()
    return Response(data, mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    # Listen on all interfaces, port 8080
    app.run(host='0.0.0.0', port=8080)
