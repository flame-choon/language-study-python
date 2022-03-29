class SMS:
    def send(self, from_number, to_number, body):
        print(from_number + " 에서 " + to_number + " 로 문자를 보냈습니다: " + body)

    def ping(self, to_number):
        print(to_number + " 로 핑을 보냈습니다.")