# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

A, B = 3, 7

def solution(A, B):
  result = 0
  binary = 0
  if(A > 0 and B > 0):
    result = A*B
    binary = bin(result)

  print(binary.count('1'))

if __name__ == "__main__":
  A, B = 3, 7
  solution(A, B)