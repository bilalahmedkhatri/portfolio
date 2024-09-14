from pywhatkit import sendwhatmsg_instantly, sendwhatmsg

def send_message_whatsapp():
    try:
        sendwhatmsg("+923213009321", "testing message")
        print("sended")
    except:
        print("message not send")
    
send_message_whatsapp()