class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i - 1] == 1:
                continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1] == 1:
                continue
            flowerbed[i] = 1
            count += 1
            if count == n:
                return True
        return False
