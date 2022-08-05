import time
import psutil

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    
    return rss
    # print(f"[{message}] memory usage: {rss: 10.5f} MB")


def solution(s):
  answer = ""
  
  return answer


print()
use_before = memory_usage()
start_time = time.time()
########################################################
s = '2'
solution(s)
########################################################
end_time = time.time()
use_after = memory_usage()
print(f"[after_work] memory usage: {use_after-use_before: 10.5f} MB")
print('[running time]:',end_time-start_time)
print()