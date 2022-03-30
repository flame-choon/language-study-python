# API 연습

# 목표 : 주식정보 조회
# 기능 
# - 사용자의 관심 종목을 추가
# - 실시간 인기 종목 알아보기
# - 종목의 시세 변동 알아보기

# 참고
# https://api.finance.naver.com/service/itemSummary.naver?itemcode=035720


# request 패키지를 이용하여 API를 요청 할 수 있다
import requests
import pandas as pd

# 사용자의 관심 종목을 추가
# 1. API에 정보를 요청
# 2. API에서 가져온 정보를 반환
def get_stock_summary(itemcode):
    raw_resp = requests.get("https://api.finance.naver.com/service/itemSummary.naver?itemcode=" + itemcode)
    resp = raw_resp.json()
    return resp

# 실시간 인기 종목 알아보기
def get_trending_stocks():
    raw_resp = requests.get("https://m.stock.naver.com/api/mystock/group/-2")
    resp = raw_resp.json()
    stocks = resp["stocks"]
    return stocks

# 데이터를 조금 더 보기 쉬운 형태로 출력
def visualize_trending_stock(stocks):
    stocks_df = pd.DataFrame(stocks)
    stocks_df.to_html("tmp.html")

# summary = get_stock_summary('035720')
# print(summary)
trending_stocks = get_trending_stocks()
print(trending_stocks)
visualize_trending_stock(trending_stocks)
