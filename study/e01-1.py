# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 알고리즘 1
# for 반복문을 사용하세요
# 입력: n
# 출력: 1부터 n까지의 제곱을 더한 값
# 시간복잡도: O(n)

def sum_sqaured_n(n):
  s = 0
  for i in range(1, n+1):
    s += i * i
  
  return s

print(sum_sqaured_n(10))