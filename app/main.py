import telegram, json, logging
from dateutil import parser
from flask import Flask
from flask import request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

chatID = "-553226721"
bot = telegram.Bot(token="1915502574:AAHnc-Ugr-LdYHkWkRG-Ts7LD8GykQZSdbw")

@app.route('/')
def main():
    return "It is page!"

@app.route('/alert', methods = ['POST'])
def postAlertmanager():
    content = json.loads(request.get_data())
    bot.sendMessage(chat_id=chatID, text="Start")
    for alert in content['alerts']:
        if alert['status'] == 'firing':
            message = alert['status']
        bot.sendMessage(chat_id=chatID, text=message)
        return "Alert OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')