def trap(height):
    left = 0
    right = len(height) - 1
    leftMax = 0
    rightMax = 0
    water = 0

    while left <= right:
        if height[left] < height[right]:
            if height[left] >= leftMax:
                leftMax = height[left]
            else:
                water += leftMax - height[left]
            left += 1
        else:
            if height[right] >= rightMax:
                rightMax = height[right]
            else:
                water += rightMax - height[right]
            right -= 1
    
    return water

# Test it
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))  # Output: 6

