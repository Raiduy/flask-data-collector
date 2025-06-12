import os
import signal
import subprocess
from flask import Flask, signals

app = Flask(__name__)
measurement_process = None

@app.route('/start/<id>')
def start_measuring(id):
    print(f"Starting measurement for id {id}")
    global measurement_process
    measure_command = f'watch -n 3 nvidia-smi'
    measurement_process = subprocess.Popen(measure_command, shell=True)
    return f"Running {id}\n"

@app.route('/stop/<id>')
def stop_measuring(id):
    print(f"Stopping measurement for id {id}")
    global measurement_process
    measurement_process.terminate()
    measurement_process.wait()
    print(f"Process returned with code: {measurement_process.returncode}")
    # os.killpg(os.getpgid(measurement_process.pid), signal.SIGTERM)
    return f"Stopped {id} with pid {measurement_process.returncode}\n"

if __name__=='__main__':
    app.run(port=8080)
