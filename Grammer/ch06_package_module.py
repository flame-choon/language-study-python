# 모듈 , 패키지

# import <패키지 이름>.<모듈 이름>
import ch06_package.ch06_sms as ch06_sms     
import ch06_package.ch06_email as ch06_email

s = ch06_sms.SMS()
e = ch06_email.Email()

s.send("010-1111-1111", "010-2222-2222", "BYE!!")
s.ping("010-3333-3333")
e.send("sweetmandoo@kakao.com", "chemi0110@gmail.com", "HI!!")


