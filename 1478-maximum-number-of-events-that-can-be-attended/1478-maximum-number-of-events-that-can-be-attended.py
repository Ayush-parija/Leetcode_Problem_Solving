from typing import List
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort the events by start day
        events.sort()
        event_index = 0
        total_events = len(events)
        min_heap = []
        day = 1
        attended = 0

        last_day = max(end for _, end in events)

        while day <= last_day:
            while event_index < total_events and events[event_index][0] == day:
                heapq.heappush(min_heap, events[event_index][1])
                event_index += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended += 1

            day += 1

        return attended
