# import heapq

# list = [1,3,5,7,9,2,4,6,8,0]
# h = []
# for i in list:
#   heapq.heappush(h, i)
#   print(h)

# import heapq

# def heapsort(iterable):
#   h = []
#   result = []
#   # 모든 원소를 차례대로 힙에 삽입
#   for value in iterable:
#     heapq.heappush(h, value)
#   # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#   for _ in range(len(h)):
#     # 순서와 관계없이 heappop()은 heap에서 가장 작은 원소를 반환한다.
#     result.append(heapq.heappop(h))
#   return result

# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)

import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
    print(h)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

