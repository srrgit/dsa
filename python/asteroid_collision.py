# 735. Asteroid Collision (Medium)
#
# Each asteroid moves right (positive value) or left (negative value) at the
# same speed; abs(value) is its size. When two collide, the smaller
# explodes; if equal, both explode. Return the state of the asteroids after
# all collisions resolve.
#
# Approach: a stack models "asteroids still flying right, waiting to
# possibly collide." Push positives freely. For a negative (left-moving)
# asteroid, keep popping smaller positives off the top (they explode); if it
# hits an equal one, both vanish; if it hits a bigger one, the incoming one
# explodes and nothing changes. Only push the negative if it survives.
# Time: O(n) amortized. Space: O(n).

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []
        for a in asteroids:
            alive = True
            while alive and a < 0 and stack and stack[-1] > 0:
                top = stack[-1]
                if top < -a:
                    stack.pop()
                elif top == -a:
                    stack.pop()
                    alive = False
                else:
                    alive = False
            if alive:
                stack.append(a)
        return stack


if __name__ == "__main__":
    sol = Solution()
    print(sol.asteroidCollision([5, 10, -5]))        # [5, 10]
    print(sol.asteroidCollision([8, -8]))             # []
    print(sol.asteroidCollision([10, 2, -5]))         # [10]
    print(sol.asteroidCollision([-2, -1, 1, 2]))      # [-2, -1, 1, 2]
