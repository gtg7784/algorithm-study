# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 1
# 입력: n
# 출력: 1부터 n까지의 숫자를 더한 값
# 시간복잡도: O(n)

def sum_n(n):
  s = 0
  for i in range(1, n+1):
    s += i
  return s

print(sum_n(10))
print(sum_n(100))