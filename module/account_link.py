from django.conf import settings
from linebot import LineBotApi
from linebot.models import FlexSendMessage, MessageAction, QuickReplyButton, QuickReply, ButtonsTemplate, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def aaa(event):
    try:
        user_id = event.source.user_id
        message = TextSendMessage(
                text = "userid:" + user_id
            )   #TemplateSendMessage

        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


def account_link(event):      #綁訂帳號
    try:
        message = FlexSendMessage(
            alt_text="綁訂帳號",
            contents=
            {
              "type": "bubble",
              "size": "micro",
              "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "尚未綁定帳號",
                    "size": "md",
                    "contents": [],
                    "weight": "bold",
                    "align": "center",
                    "offsetTop": "8px"
                  }
                ],
                "spacing": "lg"
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                  {
                    "type": "button",
                    "style": "primary",
                    "height": "md",
                    "action": {
                      "type": "postback",
                      "label": "綁定帳號",
                      "data": "Link"
                    },
                    "color": "#58C9B9"
                  }
                ],
                "flex": 0,
                "cornerRadius": "10px"
              },
              "styles": {
                "body": {
                  "separator": True,
                  "separatorColor": "#379392",
                  "backgroundColor": "#fd999a"
                },
                "footer": {
                  "backgroundColor": "#fd999a"
                }
              }
            }
        )   #FlexSendMessage
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
