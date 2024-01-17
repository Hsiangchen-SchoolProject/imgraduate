from django.conf import settings
from linebot import LineBotApi
from linebot.models import MessageAction, QuickReplyButton, QuickReply, ButtonsTemplate, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def cycuevent(event):	#通識活動
    try:
        message = TextSendMessage(text='顯示資料')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))