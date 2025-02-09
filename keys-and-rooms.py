from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        unlocked_rooms = set()
        N = len(rooms)

        def dfs(key):
            for new_key in rooms[key]:
                if new_key in unlocked_rooms:
                    continue

                unlocked_rooms.add(new_key)
                dfs(new_key)

        unlocked_rooms.add(0)
        dfs(0)

        return len(unlocked_rooms) == N


rooms = [[1], [2], [3], []]
rooms = [[1, 3], [3, 0, 1], [2], [0]]
print(Solution().canVisitAllRooms(rooms))
