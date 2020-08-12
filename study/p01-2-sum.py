# 1부터 n까지 연속한 숫자의 합을 구하는 알고리즘 2
# 입력: n
# 출력: 1부터 n까지의 숫자를 더한 값
# 시간복잡도: O(1)

def sum_n(n):
  return n * (n+1) // 2

print(sum_n(10))
print(sum_n(100))