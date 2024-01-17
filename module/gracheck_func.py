from django.conf import settings
from linebot import LineBotApi
from linebot.models import FlexSendMessage, MessageAction, QuickReplyButton, QuickReply, ButtonsTemplate, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def graduate_check(event):     #畢業審查
    try:
        message = [
            TextSendMessage(text='想畢業嗎？就讓熹熹來幫你看看 ლ(∘◕‵ƹ′◕ლ)'),

            FlexSendMessage(
                alt_text="畢業審查",
                contents=
                {
                  "type": "carousel",
                  "contents": [
                    {
                      "type": "bubble",
                      "size": "kilo",
                      "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "畢業學分",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "lg",
                            "gravity": "center",
                            "margin": "none"
                          },
                          {
                            "type": "text",
                            "text": "106學年的畢業學分為128學分喔",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "sm",
                            "gravity": "center",
                            "margin": "md"
                          }
                        ],
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px",
                        "height": "110px"
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "text": "我能畢業嗎？",
                              "label": "我能畢業嗎？"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#58C9B9"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "我還差哪些學分？",
                              "text": "我還差哪些學分？"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#58C9B9"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "待修課清單",
                              "text": "待修課清單"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#58C9B9"
                          }
                        ],
                        "paddingAll": "12px"
                      },
                      "styles": {
                        "header": {
                          "backgroundColor": "#58C9B9",
                          "separator": True
                        },
                        "footer": {
                          "separator": False
                        }
                      }
                    },
                    {
                      "type": "bubble",
                      "size": "kilo",
                      "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "英文門檻",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "lg",
                            "gravity": "center",
                            "margin": "none"
                          },
                          {
                            "type": "text",
                            "text": "畢業前要通過指定門檻呦",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "sm",
                            "gravity": "center",
                            "wrap": True,
                            "margin": "md"
                          }
                        ],
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px",
                        "backgroundColor": "#FF6B6E",
                        "height": "110px"
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "我的英文檢定過了嗎？",
                              "text": "我的英文檢定過了嗎？"
                            },
                            "style": "link",
                            "color": "#FF6B6E",
                            "height": "sm"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "全英語課程有哪些？",
                              "text": "全英語課程有哪些？"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#FF6B6E"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "全英語課程規定",
                              "text": "全英語課程規定"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#FF6B6E"
                          }
                        ],
                        "paddingAll": "12px"
                      },
                      "styles": {
                        "header": {
                          "backgroundColor": "#FF6B6E",
                          "separator": True
                        },
                        "footer": {
                          "separator": False
                        }
                      }
                    },
                    {
                      "type": "bubble",
                      "size": "kilo",
                      "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "其他畢業條件",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "lg",
                            "gravity": "center",
                            "margin": "none"
                          },
                          {
                            "type": "text",
                            "text": "體育、環服等畢業條件審查",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "sm",
                            "gravity": "center",
                            "margin": "md"
                          }
                        ],
                        "paddingTop": "19px",
                        "paddingAll": "12px",
                        "paddingBottom": "16px",
                        "backgroundColor": "#A593E0",
                        "height": "110px"
                      },
                      "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "我的體育畢業門檻過了嗎？",
                              "text": "我的體育畢業門檻過了嗎？"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#A593E0"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "我的環服畢業門檻過了嗎？",
                              "text": "我的環服畢業門檻過了嗎？"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#A593E0"
                          },
                          {
                            "type": "button",
                            "action": {
                              "type": "message",
                              "label": "特殊生畢業規定",
                              "text": "特殊生畢業規定"
                            },
                            "height": "sm",
                            "style": "link",
                            "color": "#A593E0"
                          }
                        ],
                        "paddingAll": "12px"
                      },
                      "styles": {
                        "header": {
                          "backgroundColor": "#A593E0",
                          "separator": True
                        },
                        "footer": {
                          "separator": False
                        }
                      }
                    }
                  ]
                }
            )   #FlexSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def credit(event):      #我還差哪些學分？
    try:
        message = TextSendMessage(
            text = "你目前還差23學分喔！",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(
                        action = MessageAction(label = '待修課清單', text = '待修課清單')
                    ),   #QuickReplyButton
                    QuickReplyButton(
                        action = MessageAction(label = '我能畢業嗎？', text = '我能畢業嗎？')
                    ),   #QuickReplyButton
                    QuickReplyButton(
                        action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                    ),   #QuickReplyButton
                ]   #items
            )   #QuickReply
        )   #TextSendMessage
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def end(event):      #我沒問題囉
    try:
        message = TextSendMessage(
            text = '熹熹感謝你的使用，有問題馬上問我喔~(´∀`)~'
        )   #TextSendMessage
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def graduate(event):      #我能畢業嗎？
    try:
        message = TextSendMessage(
            text = "顯示結果",
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(
                        action = MessageAction(label = '我還差哪些學分？', text = '我還差哪些學分？')
                    ),   #QuickReplyButton
                    QuickReplyButton(
                        action = MessageAction(label = '待修課清單', text = '待修課清單')
                    ),   #QuickReplyButton
                    QuickReplyButton(
                        action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                    ),   #QuickReplyButton
                ]   #items
            )   #QuickReply
        )   #TextSendMessage
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def PE_class(event): #我的體育畢業門檻過了嗎？
    try:
        message = [
            TextSendMessage(
                text='你尚缺少一個學期的體育課喔',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '我的環服畢業門檻過了嗎？', text = '我的環服畢業門檻過了嗎？')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='特殊生畢業規定' , text = '特殊生畢業規定')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def environment_service(event): #我的環服畢業門檻過了嗎？
    try:
        message = [
            TextSendMessage(
                text='你尚缺少一個學期的環境服務學習喔',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '我的體育畢業門檻過了嗎？', text = '我的體育畢業門檻過了嗎？')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='特殊生畢業規定' , text = '特殊生畢業規定')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def else_special_rule(event): #特殊生情況查詢
    try:
        message = [
            TextSendMessage(text='轉學生：\n如符合中原大學辦理學生抵免學分審核要點所列資格者，可申請抵免，並得提高編級，但大學畢業生入學者，其修業年限不得少於一年'),
            TextSendMessage(text='轉學生所繳證明文件，如有偽造、變造、假借、或冒用等情事，一經查明，即予開除學籍，除由本校通知其家長外，不發給任何證明。如畢業後始發現者，除應予繳銷其畢業證書外，並撤銷其畢業資格。'),
            TextSendMessage(text='轉系生：\n降級轉系（學位學程）者，其修業年限、學費繳交規定，均依轉入學系之年級重新計算，惟轉入前曾休學者，其休學期限照算，合計不得超過二學年。'),
            TextSendMessage(text='轉系（學位學程）學生須修畢轉入學系（學位學程）所規定之 畢業條件，方可畢業。'),

            TextSendMessage(
                text = '有其他特殊生規定想問的嗎？',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '提前畢業', text = '提前畢業')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '延畢生', text = '延畢生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='預備研究生' , text = '預備研究生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='復學生' , text = '復學生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='交換生' , text = '交換生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='境外生/中五生' , text = '境外生/中五生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def graduate_in_advance(event):        #提前畢業
    try:
        message = [
            TextSendMessage(
                text='1. 在規定修業期限屆滿前一學期或一學年修滿該學系應修畢業學分。\n2. 前三年級每學期學業平均成績名次在該系該年級學生數前百分之五以內。\n3. 曾擔任二學期以上班代表、社團負責人或通過全人教育活動手冊甲級認證者。\n4. 未曾受記過二次以上之處分。\n5. 體育、軍訓各科成績達七十分以上。',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '延畢生', text = '延畢生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='預備研究生' , text = '預備研究生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='復學生' , text = '復學生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='交換生' , text = '交換生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='境外生/中五生' , text = '境外生/中五生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def delay_graduation(event):        #延畢生
    try:
        message = [
            TextSendMessage(
                text='1. 學期學分若是0學分需繳交最低2學分費。\n2. 學期學分若少於9學分則繳交學分費。\n3. 學期學分若多於9學分需繳交全額學費。\n4. 延長修業期限是一學期至二學年。\n5. 雙主修學生可申請再延長修業年限，由一學年增為二學年。',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '提前畢業', text = '提前畢業')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='預備研究生' , text = '預備研究生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='復學生' , text = '復學生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='交換生' , text = '交換生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='境外生/中五生' , text = '境外生/中五生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def postgraduate(event):        #預備研究生
    try:
        message = [
            TextSendMessage(
                text='1. 預研生須於次學年度參加本校碩士班甄試入學或一般入學考試並獲錄取者，其在大學部階段所修碩士班課程學分不受抵免學分低於二分之一之限制。\n2. 本校三年級(建築學系及財經法律學系四年級)以上學生符合下列資格之一者，均得提出申請：\n     一、歷年學業平均成績系排名次在該年級（或該組）學生數前百分之七十五以內，或申請前二學期班排名百分之七十五以上者。\n      二、取得認可之學分數達應修學分數百分之七十五以上。\n     三、有特殊表現足以證明經學系主任簽准者。\n3. 學期學分若多於9學分需繳交全額學費。\n4. 預研生的大學畢業門檻同一般生。\n5. 本所學生應於擬畢業學期之前一學期結束前提交論文(或技術報告)計畫書，得以書面審查或公開審查方式進行計畫書審查。計畫書審查通過後始得申請本校之學位考試。',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '提前畢業', text = '提前畢業')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='延畢生' , text = '延畢生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='復學生' , text = '復學生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='交換生' , text = '交換生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='境外生/中五生' , text = '境外生/中五生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def reinstate(event):        #復學生
    try:
        message = [
            TextSendMessage(
                text='1. 學生另因懷孕、生產之需要，並持證明文件向學校再申請延長修業年限，至多一學年；因哺育幼兒之需要，並持證明文件向學校再申請延長修業年限，至多三學年。\n2. 延長修業年限之第一學期無學分修習者，得於註冊前申請休學，免予註冊，註冊者至少應選修一科目。\n3. 復學時，應入原肄業學系（學位學程）相銜接之學年或學期肄業。但學期中途休學者，復學時，應入原休學之學年或學期肄業。原肄業學系變更或停辦時，得輔導學生至適當學系肄業。\n4. 休學滿一學期或三學期復學者，該復學之學期須修足規定學分數，已修及格之科目，不得重複修習。\n5. 休學期間入營服兵役，須於原應復學年月前持休學證明書及服役證明，申請延長休學期限。俟服役期滿，再檢同退伍令申請復學。未申請延長休學者依第四十九、五十二條處理。服兵役之期限不併入休學期限之累計。',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '提前畢業', text = '提前畢業')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='延畢生' , text = '延畢生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='預備研究生' , text = '預備研究生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='交換生' , text = '交換生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='境外生/中五生' , text = '境外生/中五生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def exchange(event):       #交換生
    try:
        message = [
            TextSendMessage(
                text='跟一般學生一樣，不過要注意抵免狀況喔！',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '提前畢業', text = '提前畢業')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='延畢生' , text = '延畢生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='預備研究生' , text = '預備研究生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='復學生' , text = '復學生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='境外生/中五生' , text = '境外生/中五生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def foreign_students(event):        #境外生/中五生
    try:
        message = [
            TextSendMessage(
                text='1. 107學年度 - 全校性規定中五生應加修通識課程6學分及專業課程6學分，其中專業課程係指本系開設之選修課程(系選)。\n2. 107學年度之前 - 中五生應加修通識課程6學分及專業課程6學分，通識課程由\n「哲學概論/(天)」\n「品格與領導/(人)」\n「自然科學導論/(物)」\n「中文經典閱讀/(我)」\n「文化思想史/(歷史)」\n等課程中五選三；專業課程為系選修6學分。',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '提前畢業', text = '提前畢業')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='延畢生' , text = '延畢生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='預備研究生' , text = '預備研究生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='復學生' , text = '復學生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='交換生' , text = '交換生')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def en_gra(event):        #我的英文畢業門檻過了嗎？
    try:
        message = [
            TextSendMessage('登入拉'),
            TextSendMessage(
                text='另外若您還未通過畢業門檻可以透過以下方式來替代：ㄌ拉拉拉',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '全英語課程有哪些？', text = '全英語課程有哪些？')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='全英語課程規定' , text = '全英語課程規定')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def en_class(event):        #全英語課程有哪些？
    try:
        message = [
            TextSendMessage(
                text='查詢資料',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '我的畢業門檻過了嗎？', text = '我的畢業門檻過了嗎？')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='全英語課程規定' , text = '全英語課程規定')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def en_rule(event):        #全英語課程規定
    try:
        message = [
            TextSendMessage(
                text='自104學年度起學士班入學學生，必須於畢業前曾修2門全校開設之全英語授課課程（不含英文、英聽、實用英文(一)(二)及商學院學生修習之實用英文(一)(二)(三)(四)）。',
                quick_reply = QuickReply(
                    items = [
                        QuickReplyButton(
                            action = MessageAction(label = '我的畢業門檻過了嗎？', text = '我的畢業門檻過了嗎？')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label ='全英語課程有哪些？' , text = '全英語課程有哪些？')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]   #items
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
