
# 조건문 , 함수

# 조건문 
# if, elif, else 로 원하는 분기처리를 한다
if( 1 + 1 == 2):
    print("1 + 1은 2이다")

chuck_age = 19
if(chuck_age >= 30):
    print("척은 아재입니다")
elif (chuck_age >= 19):
    print("척은 성인입니다")
else:
    print("척은 미성년자입니다") 


# 함수
# 인자들을 받아서 결과 값을 도출
def greet(name):
    # f를 앞에 붙여주면 '{}' 내 값은 동일한 변수의 값으로 치환
    print(f'안녕 {name}아~~, 잘 지내니?')

greet('광진')    


def greeting(name, location, age):
    print(f"안녕 {name}아, 넌 {age} 살이고 {location}에 사는구나.")

# 키워드 아규먼트 (kwarg)
# 함수 생성 시, 의도된 파라미터의 타입에 맞게 입력을 전달하기 위해 사용
greeting(name = "광진", age = 20, location = "서울")    
