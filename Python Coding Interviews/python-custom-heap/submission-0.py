import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    final = []

    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)

    while heap:
        pair = heapq.heappop(heap)
        original_num = pair[1]
        final.append(original_num)


    return final


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
