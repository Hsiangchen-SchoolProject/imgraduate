from django.conf import settings
from linebot import LineBotApi
from linebot.models import MessageAction, QuickReplyButton, QuickReply, ButtonsTemplate, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def graduate_rule(event):	#問題大全
    try:
        message = TextSendMessage(text='找不到你想詢問的問題嗎？沒問題！任何問題都可以直接打字詢問的')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def free_elective(event):	#自由選修是什麼
    try:
        message = TextSendMessage(text='106學年度起學士班入學學生，每學系自由選修學分應達12學分以上，且學習範圍為輔系、雙主修、跨領域學分學程、就業學程、微型學程（他系）、PBL課程。')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def PE(event):	#體育課有什麼規定嗎
    try:
        message = TextSendMessage(text='大學部：\n1.學則第 19 條：體育為一至三年級之必修科目，每週授課二小時，不計學分，未修足者不得畢業。 重修或補修體育，每學期以加修一門為限。\n2.學則第 22 條：學生重複修習科目名稱相同之課程，其重複之學分不列入畢業學分之計算。\n3.學則第 23 條：體育科目內容經開課單位認定為有先後次序者，不得顛倒修習。')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def extend_generaledu(event):   #什麼是通識選修
    try:
        message = TextSendMessage(text='通識延伸選修課程：分為天、人、物、我四大學類，每學類最少各需修滿2學分，合計須修滿14學分。\n\n也就是說呢天、人、物、我必須各修一堂，剩下的6學分可以自由選擇想修的學類。')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def generaledu(event):   #什麼是基礎必修通識
    try:
        message = TextSendMessage(text='通識基礎必修課程：「物類」及「我類」基礎課程須於大一完成修習，「我類」基礎課程-文學經典閱讀須於大一上學期修習，語文與修辭須於大一下學期修習。')
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
