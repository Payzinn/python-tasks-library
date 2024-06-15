import requests
from flask import Flask, request

def send_telegram(dm):

    tg_token = '6465585711:AAHCcwHuZW4yMagrHTqXnB9hT6wIsT7ObZY'
    tg_chat_id = '6465585711'

    message = f"New user visited site. IP address: {dm['ip_address']}, User-agent: {dm['user_agent']}"

    api_url = f"https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={tg_chat_id}&text={message}"

    response = requests.get(api_url)

    return response.status_code == 200

app = Flask(__name__)

@app.route('/visitor', methods=['POST'])
def send_telegram_on_visit():
    visitor_data = request.json
    send_telegram(visitor_data)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
