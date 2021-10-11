import collections


class Solution:

    def __init__(self):
        self.counter = 0

    def canPlaceFlowers(self, flowerbed, n):
        if len(flowerbed) == 1:
            if 0 in flowerbed and n <= 1:
                return True
            else:
                return False

        if len(flowerbed) == 2:
            if 1 in flowerbed or n > 1:
                return False
            else:
                return True

        if len(flowerbed) >= 3:
            if 0 not in flowerbed:
                return False
            first_available = flowerbed.index(0)
            if first_available == 0:
                if flowerbed[first_available + 1] in [0,2]:
                    flowerbed[first_available] = 1
                    flowerbed[first_available + 1] = 2
                    self.counter += 1
                    if self.counter == n:
                        return True
                    else:
                        self.canPlaceFlowers(flowerbed, n)

            # print(first_available)
            elif flowerbed[first_available - 1] in [0, 2] and flowerbed[first_available + 1] in [0, 2] and first_available > 0:
                flowerbed[first_available - 1] = 2
                flowerbed[first_available + 1] = 2
                flowerbed[first_available] = 1
                print(flowerbed)
                self.counter += 1
                if self.counter == n:
                    return True
                else:
                    self.canPlaceFlowers(flowerbed, n)
            elif flowerbed[first_available - 1] == 1 or flowerbed[first_available + 1] == 1:
                flowerbed[first_available] = 2
                self.canPlaceFlowers(flowerbed, n)

        if self.counter == n:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPlaceFlowers(flowerbed=[0, 0, 1, 0, 1], n=1))