from django.apps import AppConfig
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

class GraduateappConfig(AppConfig):
    name = 'graduateapp'

app = Flask(__name__)

line_bot_api = LineBotApi('LYrHwmTn+fBU6xwYm2AZPQ/oPt0zjwwyMK1lMbzdtpCla4glUC6RJInrdPK8B9p8Y2LGJqn6C9aKfebZZEwOsoq76FYnY/PpaGLzDNXModGECK9a7aSbcWtgEH32luugr3LeDfMWOdOOY78aouUWBQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0c67abbb3b9ac34f96f225aa00a90821')


@app.route("/")
def home():
    return 'home OK'

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
