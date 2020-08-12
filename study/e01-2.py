# 1부터 n까지 연속한 숫자의 제곱의 합을 구하는 알고리즘 2
# n(n+1)(2n+1)/6
# 입력: n
# 출력: 1부터 n까지의 제곱을 더한 값
# 시간복잡도: O(1)

def sum_sqaured_n(n):
  return n * (n + 1) * (2 * n + 1) / 6

print(sum_sqaured_n(10))