from django.conf import settings
from linebot import LineBotApi
from linebot.models import MessageAction, QuickReplyButton, QuickReply, ButtonsTemplate, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def learn_track(event):	#學習足跡
    try:
        message = [
            TextSendMessage(text='忘記過去的課程與成績拉？還是不知道還要修什麼課？\n真拿你沒辦法，就讓熹熹來幫你查查看吧～'),

            TemplateSendMessage(
                alt_text = '學習足跡',
                template = ButtonsTemplate(
                    title = '想查哪一方面的呢？',
                    text = '請選擇：',
                    actions = [
                        MessageTemplateAction(
                            label='已修過課程與成績',
                            text = '已修過課程與成績'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='正在修課',
                            text = '正在修課'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='待修課清單',
                            text = '待修課清單'
                        ),   #MessageTemplateAction
                    ]   #actions
                )   #ButtonsTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def already_class(event):	#已修過課程與成績
    try:
        message = [
            TextSendMessage(text='顯示資料'),

            TextSendMessage(
                text = '還想問甚麼呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '正在修課', text = '正在修課')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修課清單', text = '待修課清單')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def now_class(event):	#正在修課
    try:
        message = [
            TextSendMessage(text='顯示資料'),

            TextSendMessage(
                text = '還想問甚麼呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '已修過課程與成績', text = '已修過課程與成績')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修課清單', text = '待修課清單')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def notyet_class(event):	#待修課清單
    try:
        message = [
            TextSendMessage(
                text = '你想查詢的是哪一部分？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '待修系必修', text = '待修系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修系選修', text = '待修系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修基礎通識', text = '待修基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修延伸通識', text = '待修延伸通識')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def my_compulsory(event):	#系必修
    try:
        message = [
            TextSendMessage(text='顯示資料'),

            TextSendMessage(
                text = '還想問甚麼呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '待修系選修', text = '待修系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修基礎通識', text = '待修基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修延伸通識', text = '待修延伸通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '已修過課程與成績', text = '已修過課程與成績')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '正在修課', text = '正在修課')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def my_elective(event):	#系選修
    try:
        message = [
            TextSendMessage(text='顯示資料'),

            TextSendMessage(
                text = '還想問甚麼呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '待修系必修', text = '待修系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修基礎通識', text = '待修基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修延伸通識', text = '待修延伸通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '已修過課程與成績', text = '已修過課程與成績')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '正在修課', text = '正在修課')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def my_generaledu(event):	#基礎通識
    try:
        message = [
            TextSendMessage(text='顯示資料'),

            TextSendMessage(
                text = '還想問甚麼呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '待修系必修', text = '待修系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修系選修', text = '待修系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修延伸通識', text = '待修延伸通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '已修過課程與成績', text = '已修過課程與成績')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '正在修課', text = '正在修課')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def my_extend_generaledu(event):	#延伸通識
    try:
        message = [
            TextSendMessage(text='顯示資料'),

            TextSendMessage(
                text = '還想問甚麼呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '待修系必修', text = '待修系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修系選修', text = '待修系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '待修基礎通識', text = '待修基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '已修過課程與成績', text = '已修過課程與成績')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '正在修課', text = '正在修課')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
