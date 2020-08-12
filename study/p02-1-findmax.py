# 최댓값 구하기
# 입력: 숫자가 n개 들어있는 리스트
# 출력: 숫자 n개 중 최댓값
# 시간복잡도: O(n)

def find_max(a):
  n = len(a)
  max_v = a[0]
  for i in range(1, n):
    if a[i] > max_v:
      max_v = a[i]
  return max_v

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max(v))