import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "mahid.mahmudur@gmail.com"
    password = "tyms wxcp xnfw bxwl"

    receiver = "mahid.mahmudur@gmail.com"
    context = ssl.create_default_context()

    # message = """\
    # Hi, 
    # How are you?
    # Bye
    # """

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
