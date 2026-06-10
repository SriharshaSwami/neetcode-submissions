class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1
        res = []
        apnaX = - 1
        #Searching the insert position of the x value in arr
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            elif arr[mid] > x:
                right = mid - 1
            else:
                apnaX = mid
                break
        if apnaX >= 0:
            mid = apnaX
        else:
            mid = left
        #Finding k closest using sliding window(2 pointer)
        left = mid - 1
        right = mid
        while k :
            if left < 0 and right:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            elif(abs(arr[left] - x) <= abs(arr[right] - x)):
                res.append(arr[left])
                left -=1 
            elif(abs(arr[left] - x) > abs(arr[right] - x)):
                res.append(arr[right])
                right += 1
            k -= 1

        return sorted(res)      