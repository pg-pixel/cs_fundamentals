'''
We are creating a builder for creating and sending emails
'''
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self):
        self.To = None 
        self.From = None 
        self.Subject = None 
        self.Body = None 
        self.Salutation = None 
        self.Pswd = None
        self.Attachements = []
        
    def send(self):
        #logic to send mail 
        
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            
            server.login(self.From, self.Pswd)
            message = MIMEMultipart()
            message['From'] = self.From
            message['To'] = self.To
            message['Subject'] = self.Subject
            message.attach(MIMEText(self.Body, 'plain'))
            server.send_message(message)
            
            server.quit()
            return (f'Mail Sent to {self.To}')
        except  Exception as e :
            return e 
        
        
class EmailBuilder:
    def __init__(self):
        self.mail= Email()
        
    def set_To(self, mail):
        self.mail.To = mail 
        return self 
    
    def set_From(self, mail):
        self.mail.From = mail 
        return self 
    
    def set_subject(self, subj):
        self.mail.Subject = subj 
        return self 
    
    def set_from_pswd(self, pswd):
        self.mail.Pswd = pswd
        return self
    
    def set_body(self, _body):
        self.mail.Body = _body 
        return self
    
    def build(self):
        return self.mail.send()
    
email_builder = EmailBuilder()
email_builder.set_To('gautam.priyansh98@gmail.com')
email_builder.set_From('gautam.priyansh98@gmail.com')
email_builder.set_subject('subject')
email_builder.set_body("This is the body of the email")
email_builder.set_from_pswd('umowphecydhgemci') 

print(email_builder.build())