import qqbot

token = qqbot.Token("{appid}","{token}")
api = qqbot.UserAPI(token, False)

user = api.me()
# 打印机器人名字
print(user.username)

# 需要监听机器人被@后消息并进行相应的回复
token = qqbot.Token("{appid}","{token}")
# 注册事件类型和回调，可以注册多个
# 定义需要监听的事件（部分事件可能需要权限申请）
qqbot_handler = qqbot.Handler(qqbot.HandlerType.AT_MESSAGE_EVENT_HANDLER, _message_handler)
# 注册需要监听的事件
qqbot.listen_events(token, False, qqbot_handler)

# 定义注册事件回调执行函数
def _message_handler(event, message: Message):
    msg_api = qqbot.MessageAPI(token, False)
    # 打印返回信息
    qqbot.logger.info("event %s" % event + ",receive message %s" % message.content)
    # 构造消息发送请求数据对象
    send = qqbot.MessageSendRequest("<@%s>谢谢你，加油" % message.author.id, message.id)
    # 通过api发送回复消息
    msg_api.post_message(message.channel_id, send)
    #