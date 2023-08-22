from concurrent.futures import ThreadPoolExecutor
import random
import time

import flask

executor = ThreadPoolExecutor(max_workers=1)

task_queue = []
app = flask.Flask(__name__)


global requests


def do_work():
    # Perform a computationally intensive task
    i = 0
    print("start")
    while i < 99999:
        print(i * i)
        i += 1
    print("stop")
    return i

@app.route('/compute', methods=['POST'])
def compute():
    executor.submit(do_work())
    return {'result': "result"}

    def thread_func():
        # This function is run in a thread
        do_work()
        
    
    
    if len(task_queue) > 1:
        # Wait for the previous task to complete before returning the result
        task_queue[0].result()
        task_queue.pop(0)
        
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

