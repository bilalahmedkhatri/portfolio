from pywhatkit import sendwhatmsg_instantly, sendwhatmsg

def send_message_whatsapp():
    # try:
    sendwhatmsg_instantly("+923213009321", "testing message", 12, 22)
    print("sended")
    # except:
    #     print("message not send")
    
send_message_whatsapp()

# not working======================