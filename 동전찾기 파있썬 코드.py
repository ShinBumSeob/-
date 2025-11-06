Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def find_fake_coin(coins):
...     """
...     coins: list of 9 integers (동전의 무게). 정상 동전은 같고, 가짜는 더 가벼움 (중복 없음).
...     return: 가짜 동전의 인덱스 (0~8)
...     """
...     # Step 1: 3개씩 3그룹으로 나눈다
...     group1 = coins[:3]
...     group2 = coins[3:6]
...     group3 = coins[6:]
...     
...     sum1 = sum(group1)
...     sum2 = sum(group2)
... 
...     # 비교1: group1 vs group2
...     if sum1 == sum2:
...         # 가짜는 group3에 있다.
...         fake_group = group3
...         start_index = 6
...     elif sum1 < sum2:
...         # group1에 가짜
...         fake_group = group1
...         start_index = 0
...     else:
...         # group2에 가짜
...         fake_group = group2
...         start_index = 3
... 
...     # 비교2: 그룹 내 동전 2개 비교
...     if fake_group[0] == fake_group[1]:
...         # 둘 다 정상이면 3번째가 가짜
...         return start_index + 2
...     elif fake_group[0] < fake_group[1]:
...         return start_index
...     else:
...         return start_index + 1
... 
# 사용 예시
coins = [10, 10, 9, 10, 10, 10, 10, 10, 10]  # 2번째(인덱스 2)가 가짜(무게 9)
