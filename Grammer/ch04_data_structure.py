# 자료 구조

# list 
# 관련이 있는 여러 변수들을 묶어서 쓸수 있는 자료형

x = list((1,2,3,4,5))
x.append(1)

y = [1,2,3]
y.append(4)     # 데이터를 추가
y.append(5)
y.pop()         # list 가장 마지막 인덱스의 데이터를 제거
y[1] = 2        # 특정 인덱스의 데이터를 변경

print(x)
print(y)

# tuple
# list와 유사하지만 객체 내 데이터 수정이 불가능한 자료구조
# tuple은 코드 협업 시 누군가가 혹은 내가 임의로 인한 수정을 방지하기 위해
a = tuple((1,2,3,4))
# a = (1,2,3)
print(a)


# list vs tuple
# list : 초기 데이터의 값을 변경할 수 있다
# tuple : 데이터의 값을 변경 할 수 없다


# set
# 데이터가 순서대로 적재되지 않는다
# 어느 index에 데이터가 어떤건지 알수는 없지만
# 데이터 검색시 list에 비해 훨씬 더 빠른 결과를 반환한다. 
b = set(("seoul","incheon","jeju"))
b.add("busan")
print(b)
print('seoul' in b)

# dictionary
# key-value로 저장
# key 값을 이용하여 데이터를 로드
# 데이터가 순서대로 적재되지 않는다
# 데이터 검색 속도가 빠르지만 key에 대한 검색만 가능
c = dict(name = '광진', age = 30)

print(c)
print(c["name"])

# set vs dictionary
# set : key 데이터만 필요할 때
# dictionary : key - value 데이터로 저장이 필요할 때

