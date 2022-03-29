class Email:
    def send(self, from_address, to_address, body):
        print(from_address + " 에서 " + to_address + " 로 이메일을 보냈습니다." + body)