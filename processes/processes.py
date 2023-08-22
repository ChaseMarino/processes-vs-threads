from concurrent.futures import ThreadPoolExecutor

import flask

app = flask.Flask(__name__)

requests = 0
t1Requests = 0
t2Requests = 0
t3Requests = 0
t4Requests = 0
avgLatency = 0
totalLatency = 0
totalTime = 0


def do_work():
    i = 0
    print("start")
    while i < 99999:
        print(i * i)
        i += 1
    print("stop")

@app.route('/compute', methods=['POST'])
def compute():
    do_work()
    return {'result': "result"}

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

