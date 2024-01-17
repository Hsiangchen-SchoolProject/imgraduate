# import 必要的函式庫
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, PostbackEvent
from module import qa_func, gracheck_func, lrntrack_func, clscheck_func, cycuevent_func, guide_func, account_link
from urllib.parse import parse_qsl
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
# 圖文選單
                    if mtext == "問題大全":
                        qa_func.graduate_rule(event)

                    elif mtext == "畢業審查":
                        gracheck_func.graduate_check(event)

                    elif mtext == "學習足跡":
                        lrntrack_func.learn_track(event)

                    elif mtext == "課程查詢":
                        clscheck_func.class_check(event)

                    elif mtext == "通識活動":
                        cycuevent_func.cycuevent(event)

                    elif mtext == "使用指引":
                        guide_func.user_guide(event)

                    elif mtext == "我沒問題囉":
                        gracheck_func.end(event)
# 畢業審查
     # 畢業學分
                    elif mtext == "我還差哪些學分？":
                        gracheck_func.credit(event)

                    elif mtext == "我能畢業嗎？":
                        gracheck_func.graduate(event)

     # 其他畢業條件
                    elif mtext == "我的體育畢業門檻過了嗎？":
                        gracheck_func.PE_class(event)

                    elif mtext == "我的環服畢業門檻過了嗎？":
                        gracheck_func.environment_service(event)

                    elif mtext == "特殊生畢業規定":
                        gracheck_func.else_special_rule(event)

                    elif mtext == "提前畢業":
                        gracheck_func.graduate_in_advance(event)

                    elif mtext == "延畢生":
                        gracheck_func.delay_graduation(event)

                    elif mtext == "預備研究生":
                        gracheck_func.postgraduate(event)

                    elif mtext == "復學生":
                        gracheck_func.reinstate(event)

                    elif mtext == "交換生":
                        gracheck_func.exchange(event)

                    elif mtext == "境外生/中五生":
                        gracheck_func.foreign_students(event)
    # 英文門檻
                    elif mtext == "我的英文畢業門檻過了嗎？":
                        gracheck_func.en_gra(event)

                    elif mtext == "全英語課程有哪些？":
                        gracheck_func.en_class(event)

                    elif mtext == "全英語課程規定":
                        gracheck_func.en_rule(event)

# 使用指引
                    elif mtext == "功能介紹":
                        guide_func.function_Introduction(event)

                    elif mtext == "如何連結帳號？":
                        guide_func.connect_account(event)

                    elif mtext == "沒登入能查詢個人資料嗎？":
                        guide_func.nonlogin_check(event)

# 學習足跡
                    elif mtext == "已修過課程與成績":
                        lrntrack_func.already_class(event)

                    elif mtext == "正在修課":
                        lrntrack_func.now_class(event)

                    elif mtext == "待修課清單":
                        lrntrack_func.notyet_class(event)

                    elif mtext == "待修系必修":
                        lrntrack_func.my_compulsory(event)

                    elif mtext == "待修系選修":
                        lrntrack_func.my_elective(event)

                    elif mtext == "待修基礎通識":
                        lrntrack_func.my_generaledu(event)

                    elif mtext == "待修延伸通識":
                        lrntrack_func.my_extend_generaledu(event)
 # 課程查詢
    # 系上課程
                    elif mtext == "系必修":
                        clscheck_func.compulsory(event)

                    elif mtext == "系選修":
                        clscheck_func.elective(event)

                    elif mtext == "四管選兩管只能大三修嗎？":
                        clscheck_func.manage(event)

                    elif mtext == "企業倫理是延伸通識嗎？":
                        clscheck_func.business_ethics(event)

                    elif mtext == "環服注意事項":
                        clscheck_func.environment_service_rule(event)
    # 通識課程
                    elif mtext == "基礎通識":
                        clscheck_func.generaledu(event)

                    elif mtext == "延伸通識":
                        clscheck_func.extend_generaledu(event)
    # 其他課程
                    elif mtext == "體育課程":
                        clscheck_func.PE(event)

                    elif mtext == "軍訓課程":
                        clscheck_func.military(event)
 # 問題大全
                    elif mtext == "自由選修是什麼":
                        qa_func.free_elective(event)

                    elif mtext == "體育課有什麼規定嗎":
                        qa_func.PE(event)

                    elif mtext == "什麼是通識選修":
                        qa_func.extend_generaledu(event)

                    elif mtext == "什麼是基礎必修通識":
                        qa_func.generaledu(event)

                    elif mtext == "aaa":
                        account_link.aaa(event)
#  綁定帳號
                    elif mtext == "綁定帳號":
                        account_link.account_link(event)

            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  #取得data資料
                if backdata.get('action') == 'Link':
                    token = line_bot_api.issue_link_token(event.Source.UserId)
                    line_bot_api.reply_message(event.reply_token, "https://ibottestapi.azurewebsites.net/user/login?linkToken={token}")
        return HttpResponse()
    else:
        return HttpResponseBadRequest()
