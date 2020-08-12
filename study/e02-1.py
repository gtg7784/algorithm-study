# 최솟값 구하기
# 입력: 숫자가 n개 들어있는 리스트
# 출력: 숫자 n개 중 최솟값
# 시간복잡도: O(n)

def find_min(a):
  min_v = a[0]
  for i in a:
    if min_v > i:
      min_v = i
  return min_v

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_min(v))