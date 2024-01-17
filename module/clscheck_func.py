from django.conf import settings
from linebot import LineBotApi
from linebot.models import FlexSendMessage, ImageSendMessage, MessageAction, QuickReplyButton, QuickReply, ButtonsTemplate, TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageTemplateAction

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def class_check(event):	#課程查詢
    try:
        message = [
            TextSendMessage(text='不知道有什麼課可以修嗎，就讓熹熹來告訴你吧！'),

            TemplateSendMessage(
                alt_text='課程查詢',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            title='系上課程',
                            text='請選擇：',
                            actions=[
                                MessageTemplateAction(
                                    label='系必修',
                                    text='系必修'
                                ),  #MessageTemplateAction
                                MessageTemplateAction(
                                    label='系選修',
                                    text='系選修'
                                ),  #MessageTemplateAction
                            ]   #actions
                        ),  #CarouselColumn
                        CarouselColumn(
                            title='通識課程',
                            text='請選擇：',
                            actions=[
                                MessageTemplateAction(
                                    label='基礎通識',
                                    text='基礎通識'
                                ),  #MessageTemplateAction
                                MessageTemplateAction(
                                    label='延伸通識',
                                    text='延伸通識'
                                ),  #MessageTemplateAction
                            ]   #actions
                        ),   #CarouselColumn
                        CarouselColumn(
                            title='其他課程',
                            text='請選擇：',
                            actions=[
                                MessageTemplateAction(
                                    label='體育課程',
                                    text='體育課程'
                                ),  #MessageTemplateAction
                                MessageTemplateAction(
                                    label='軍訓課程',
                                    text='軍訓課程'
                                ),  #MessageTemplateAction
                            ]   #actions
                        )   #CarouselColumn
                    ]   #columns
                )   #CarouselTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def compulsory(event):  #系必修
    try:
        url = 'https://i.ibb.co/nryddkq/106-compulsory.png'
        message = [
            ImageSendMessage(url,url),
            TemplateSendMessage(
                alt_text = '系必修',
                template = ButtonsTemplate(
                    title = '另外有什麼疑問呢？',
                    text = '請選擇：',
                    actions = [
                        MessageTemplateAction(
                            label='四管選兩管只能大三修嗎？',
                            text = '四管選兩管只能大三修嗎？'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='企業倫理是延伸通識嗎？',
                            text = '企業倫理是延伸通識嗎？'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='環服注意事項',
                            text = '環服注意事項'
                        ),   #MessageTemplateAction
                    ]   #actions
                )   #ButtonsTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def manage(event):  #四管選兩管一定要大三修嗎？
    try:
        message = [
            TextSendMessage(text='沒有喔～你可以在大一大二就修習這些課程，另外如果你修超過2門，多出來的學分將列入自由學分計算！'),
            TemplateSendMessage(
                alt_text = '四管選兩管只能大三修嗎？',
                template = ButtonsTemplate(
                    title = '還有什麼疑問呢？',
                    text = '請選擇：',
                    actions = [
                        MessageTemplateAction(
                            label='企業倫理是延伸通識嗎？',
                            text = '企業倫理是延伸通識嗎？'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='環服注意事項',
                            text = '環服注意事項'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='我沒問題囉',
                            text = '我沒問題囉'
                        ),   #MessageTemplateAction
                    ]   #actions
                )   #ButtonsTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def business_ethics(event):  #企業倫理是延伸通識嗎？
    try:
        message = [
            TextSendMessage(text='企業倫理是屬於商學院必修的 "延伸通識" ！\n學校會在你大三時自動排休這堂課因此不用特地選修喔～'),
            TemplateSendMessage(
                alt_text = '企業倫理是延伸通識嗎？',
                template = ButtonsTemplate(
                    title = '還有什麼疑問呢？',
                    text = '請選擇：',
                    actions = [
                        MessageTemplateAction(
                            label='四管選兩管只能大三修嗎？',
                            text = '四管選兩管只能大三修嗎？'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='環服注意事項',
                            text = '環服注意事項'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='我沒問題囉',
                            text = '我沒問題囉'
                        ),   #MessageTemplateAction
                    ]   #actions
                )   #ButtonsTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def environment_service_rule(event):  #環服注意事項
    try:
        message = [
            TextSendMessage(text='同學們必須修滿兩學期且成績及格才能畢業。兩學期的定義為：環服(一)2次或環服(二)2次，或環服(一)、環服(二)各一次。'),
            TemplateSendMessage(
                alt_text = '還有什麼疑問呢？',
                template = ButtonsTemplate(
                    title = '還有什麼疑問呢？',
                    text = '請選擇：',
                    actions = [
                        MessageTemplateAction(
                            label='四管選兩管只能大三修嗎？',
                            text = '四管選兩管只能大三修嗎？'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='企業倫理是延伸通識嗎？',
                            text = '企業倫理是延伸通識嗎？'
                        ),   #MessageTemplateAction
                        MessageTemplateAction(
                            label='我沒問題囉',
                            text = '我沒問題囉'
                        ),   #MessageTemplateAction
                    ]   #actions
                )   #ButtonsTemplate
            )   #TemplateSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def elective(event):  #系選修
    try:
        url = 'https://i.ibb.co/bs1b5k8/elective.png'
        message = [
            ImageSendMessage(url,url),
            TextSendMessage(text='注意！！\n我們系上的畢業規定中系選修需要修至少13學分喔'),
            TextSendMessage(
                text = '還想查詢哪些類別的課程呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '系必修', text = '系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '基礎通識', text = '基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '延伸通識', text = '延伸通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '體育課程', text = '體育課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '軍訓課程', text = '軍訓課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def generaledu(event):  #基礎通識
    try:
        url = 'https://i.ibb.co/rmfhBYW/generaledu.png'
        message = [
            ImageSendMessage(url,url),
            TextSendMessage(text='學校雖然有規定"基礎的物學須於大一時完成修課"，但其實大二大三修也沒關係的！'),
            TextSendMessage(
                text = '還想查詢哪些類別的課程呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '系必修', text = '系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '系選修', text = '系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '延伸通識', text = '延伸通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '體育課程', text = '體育課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '軍訓課程', text = '軍訓課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def extend_generaledu(event):  #延伸通識
    try:
        url = 'https://i.ibb.co/X3gJqzP/extend-generaledu.png'
        message = [
            ImageSendMessage(url,url),
            TextSendMessage(text='記得天、人、物、我每個類別都要修到一門喔！別忘了～'),
            TextSendMessage(
                text = '還想查詢哪些類別的課程呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '系必修', text = '系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '系選修', text = '系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '基礎通識', text = '基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '體育課程', text = '體育課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '軍訓課程', text = '軍訓課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def PE(event):  #體育課程
    try:
        message = [
            FlexSendMessage(
                alt_text="體育課程",
                contents=
                {
                  "type": "bubble",
                  "size": "giga",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "體育課程",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#004e66"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "課程名稱",
                            "size": "sm"
                          }
                        ]
                      },
                      {
                        "type": "separator",
                        "margin": "xl",
                        "color": "#1f4e5f"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "排球",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "網球",
                                "align": "end"
                              },
                              {
                                "type": "text",
                                "text": "高爾夫",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "壘球",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "田徑",
                                "align": "end"
                              },
                              {
                                "type": "text",
                                "text": "爵士舞",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "籃球",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "飛盤",
                                "align": "end"
                              },
                              {
                                "type": "text",
                                "text": "有氧舞蹈",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "羽球",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "國術",
                                "align": "end"
                              },
                              {
                                "type": "text",
                                "text": "特別班體控組",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "桌球",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "氣排球",
                                "align": "end"
                              },
                              {
                                "type": "text",
                                "text": "特別班肢礙組",
                                "align": "end"
                              }
                            ]
                          },
                          {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                              {
                                "type": "text",
                                "text": "游泳",
                                "flex": 0
                              },
                              {
                                "type": "text",
                                "text": "保齡球",
                                "align": "end"
                              },
                              {
                                "type": "text",
                                "text": "特別班內礙組",
                                "align": "end"
                              }
                            ]
                          }
                        ],
                        "margin": "lg"
                      },
                      {
                        "type": "separator",
                        "margin": "xl",
                        "color": "#1f4e5f"
                      },
                      {
                        "type": "text",
                        "text": "備註：",
                        "margin": "lg",
                        "wrap": True,
                        "color": "#004e66",
                        "weight": "bold"
                      },
                      {
                        "type": "text",
                        "text": "田徑  限校隊選修"
                      },
                      {
                        "type": "text",
                        "text": "高爾夫 首次上課請到體育館",
                        "wrap": True
                      },
                      {
                        "type": "text",
                        "text": "保齡球 首次上課請到體育館",
                        "wrap": True
                      },
                      {
                        "type": "text",
                        "text": "特別班體控組 限BMI>34或BMI<16"
                      },
                      {
                        "type": "text",
                        "text": "特別班肢礙組、內礙組  需繳交醫生證明",
                        "wrap": True
                      }
                    ]
                  },
                  "styles": {
                    "body": {
                      "backgroundColor": "#cdf1cb"
                    },
                    "footer": {
                      "backgroundColor": "#cff0da"
                    }
                  }
                }
            ),  #FlexSendMessage
            TextSendMessage(text='▲體育大致上有這些課程\n\n體育須修足大一體育，並在大二到大四選擇4個學期修習體育課程\n另外請注意每門體育課所開設的性別限制喔！'),
            TextSendMessage(
                text = '還想查詢哪些類別的課程呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '系必修', text = '系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '系選修', text = '系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '基礎通識', text = '基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '延伸通識', text = '延伸通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '軍訓課程', text = '軍訓課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def military(event):  #軍訓課程
    try:
        message = [
            FlexSendMessage(
                alt_text="軍訓課程",
                contents=
                {
                  "type": "bubble",
                  "size": "mega",
                  "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "軍訓課程",
                        "weight": "bold",
                        "size": "xl",
                        "color": "#004e66"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                          {
                            "type": "text",
                            "text": "課程名稱",
                            "size": "sm"
                          }
                        ]
                      },
                      {
                        "type": "separator",
                        "margin": "xl",
                        "color": "#1f4e5f"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "國防軍訓 -- 國民國防"
                          },
                          {
                            "type": "text",
                            "text": "國防軍訓 -- 防衛動員"
                          },
                          {
                            "type": "text",
                            "text": "國防軍訓 -- 國防政策"
                          },
                          {
                            "type": "text",
                            "text": "國防軍訓 -- 國防科技"
                          },
                          {
                            "type": "text",
                            "text": "國防軍訓 -- 國際情勢"
                          }
                        ],
                        "margin": "lg"
                      },
                      {
                        "type": "separator",
                        "margin": "xl",
                        "color": "#1f4e5f"
                      },
                      {
                        "type": "text",
                        "text": "備註：相同名稱課程不得重複選修，否則無法折抵",
                        "margin": "lg",
                        "wrap": True
                      }
                    ]
                  },
                  "styles": {
                    "body": {
                      "backgroundColor": "#cdf1cb"
                    },
                    "footer": {
                      "backgroundColor": "#cff0da"
                    }
                  }
                }
            ),   #FlexMessage
            TextSendMessage(text='▲以上是我們的軍訓課程\n\n每修習一種就可以折抵兩天兵役，簡單來說修越多越早退伍❂❂'),
            TextSendMessage(
                text = '還想查詢哪些類別的課程呢？',
                quick_reply = QuickReply(
                    items =[
                        QuickReplyButton(
                            action = MessageAction(label = '系必修', text = '系必修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '系選修', text = '系選修')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '基礎通識', text = '基礎通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '延伸通識', text = '延伸通識')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '體育課程', text = '體育課程')
                        ),   #QuickReplyButton
                        QuickReplyButton(
                            action = MessageAction(label = '我沒問題囉', text = '我沒問題囉')
                        ),   #QuickReplyButton
                    ]
                )   #QuickReply
            )   #TextSendMessage
        ]   #message
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
