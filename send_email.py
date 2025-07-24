import smtplib, ssl, os, dotenv


def send_email(message):
    host = "mail.yigitac.com"
    port = 465

    username = "info@yigitac.com"
    dotenv.load_dotenv()
    password = os.getenv("PASSWORD")

    reciever = "info@yigitac.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)