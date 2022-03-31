import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


EMAIL_LOGIN = 'deabcontato88@gmail.com'
EMAIL_SENHA = 'contato@2021'


def enviar_email():
    corpo = '''<h2>E AI MUNDO!!!</<h2>
                
                <b>E ai JOW</b>   
            '''
    
    msg = MIMEMultipart()
    msg['Subject'] = 'Nosso Assunto'
    msg['From'] = 'deabcontato88@gmail.com'
    msg['To'] = 'deabcontato88@gmail.com'

    msg.attach(MIMEText(corpo, 'plain'))
    
    nomearquivo = 'teste.txt'
    
    anexo = open('secret.txt', 'rb')
    
    configs = MIMEBase('application', 'octet-stream')
    configs.set_payload(anexo.read())
    encoders.encode_base64(configs)
    configs.add_header('Content-Disposition', "attachment; filename= %s" % nomearquivo)
    
    msg.attach(configs)
    
    anexo.close()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as servidor:
        servidor.login(EMAIL_LOGIN, EMAIL_SENHA)
        servidor.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    

enviar_email()