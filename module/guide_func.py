from django.conf import settings
from linebot import LineBotApi
from linebot.models import StickerSendMessage, MessageAction, QuickReplyButton, QuickReply, ButtonsTemplate, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def user_guide(event):  #使用指引
    try:
        message = [
            TextSendMessage(text='吼嘿~\n歡迎光臨 資想要你畢業♡♥♡♥\n熹熹提供CYIM學生一個更清楚明自己是否符合畢業資格的途徑。\n現在就讓熹熹帶領你一起發掘我的妙用吧！'),

            StickerSendMessage('11539','52114117'),

            TemplateSendMessage(
                alt_text = '使用指引',
                template = ButtonsTemplate(
                    title = '功能指引',
                    text = '有什麼不懂的，直接輸入問題也可以呦！',
                    actions = [
                        MessageTemplateAction(
                            label='功能介紹',
                            text='功能介紹'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='如何連結帳號？',
                            text='如何連結帳號？'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='沒登入能查詢個人資料嗎？',
                            text='沒登入能查詢個人資料嗎？'
                        ),   #MessageTemplateAction
                    ]   #actions
                )   #ButtonsTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def function_Introduction(event):   #功能介紹
    try:
        message = TextSendMessage(text='問題大全 📖\n畢業有太多規定讓你頭昏眼花嗎？點選問題大全就對了，所有畢業相關規定都可在這裡做查詢！\n\n畢業審查 👀\n在這個功能中，你可以通過熹熹的問題引導，幫助確認畢業應修的剩餘學分，最後得出能否畢業的結果。\n\n學習足跡 👣\n想知道你過去的學習路程嗎？來到學習足跡就對了！不只過去修過的課程成績以及正在修課的資料，還有應修科目可以查詢喔。\n\n課程查詢 🔍\n還缺少學分但不知道該修什麼課程嗎？透過課程查詢來找出你最想修的課程！\n\n通識活動 📅\n學校所有的通識活動皆可透過這個頁面做報名登記喔～\n\n使用指引 📝\n忘記熹熹可以幹嘛了嗎？趕快來使用指引看看吧！')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def connect_account(event):     #如何連結帳號？
    try:
        message = TextSendMessage(text='傳流程圖')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def nonlogin_check(event):      #沒登入能查詢個人資料嗎？
    try:
        message = TextSendMessage(text='不可以呦')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
