# 모듈 , 패키지

import ch06_sms     # 모듈 이름 = 파일 이름
import ch06_email

s = ch06_sms.SMS()
e = ch06_email.Email()

s.send("010-1111-1111", "010-2222-2222", "BYE!!")
e.send("sweetmandoo@kakao.com", "chemi0110@gmail.com", "HI!!")


