def is_palindrome(num):
  assert num >= 0
  # get big digit
  b = 1
  while num / b >= 10:
    b = b * 10
  while num > 0:
    fd = num / b
    ld = num % 10
    print("fd: {}, ld: {}, b: {}, num: {}".format(fd, ld, b, num))
    if fd != ld:
      return False
    num = (num % b) / 10 
    b = b / 100
  return True



