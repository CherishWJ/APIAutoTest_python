#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
class SendEmail:
    global send_user
    global email_host
    global password
    #发送邮件的用户名
    send_user = "18311447530@163.com"
    #发送邮件的服务器
    email_host ="smtp.163.com"
    #发送邮件的密码，需要使用授权码
    password="an1234"

    def send_mail(self,user_list,sub,content):
        sender=""+"<"+send_user+">"
        #构建格式
        message = MIMEText(content,_subtype='plain',_charset='utf-8')

        message['Subject']=sub
        message['From']=sender
        message['To']=";".join(user_list)


        server = smtplib.SMTP()
        server.connect(email_host,25)
        server.login(send_user,password)
        server.sendmail(sender,user_list,message.as_string())
        server.close()
    def send_main(self,pass_list,fail_list):
        pass_num=float(len(pass_list))
        fail_num=float(len(fail_list))
        count_num = pass_num + fail_num

        pass_result="%.2f%%" %(pass_num/count_num*100)
        fail_result="%.2f%%" %(fail_num/count_num*100)

        user_list=['18311447530@163.com']
        sub ='接口测试报告'
        content='此次一共运行接口测试用例个数为%s个，通过个数为%s个。失败个数为%s个，通过率为%s,失败率为%s'%(count_num,pass_num,fail_num,pass_result,fail_result)
        self.send_mail(user_list,sub,content)
if __name__=="__main__":
        sen=SendEmail()
        sen.send_main([1,2,3,4],[2,3,4,5,6,7])


