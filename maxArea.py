def maxArea(arr: list) -> float:
    l = 0
    r = len(arr) - 1
    max_area_l = 0
    max_area_r = 0
    max_area = 0
    while l < r:
        shorter_height = min(arr[l], arr[r])
        distance = r - l
        area = shorter_height * distance
        if area > max_area:
            max_area = area
            max_area_l = l 
            max_area_r = r
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return max_area, max_area_l, max_area_r

