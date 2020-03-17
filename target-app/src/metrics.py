from flask import Flask
import requests
app = Flask(__name__)

@app.route('/metrics')
def metrics():
    r1 = requests.get('https://httpstat.us/503')
    r2 = requests.get('https://httpstat.us/200')

    response = ('sample_external_url_up{url="https://httpstat.us/503"}  = ' + str(1 if r1.status_code == 200 else 0) + '\n'
    'sample_external_url_response_ms{url="https://httpstat.us/503"}  = [' + str(r1.elapsed.total_seconds()) + ']\n'
    'sample_external_url_up{url="https://httpstat.us/200"}  = ' + str(1 if r2.status_code == 200 else 0) + '\n'
    'sample_external_url_response_ms{url="https://httpstat.us/200"}  = [' + str(r2.elapsed.total_seconds()) + ']')

    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
