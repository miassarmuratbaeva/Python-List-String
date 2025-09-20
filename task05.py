def format_messages(messages):
    message_list = messages.split('|')
    for message in message_list:
        print(message)
input_messages = "Salom|Qalesiz?|Yaxshi otdimi bugun?"
format_messages(input_messages)
