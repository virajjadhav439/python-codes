# PRN: 2024082681
def lego_stack(blocks):
    left = 0
    right = len(blocks) - 1
    last = float('inf')  # Start with very large value

    while left <= right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1

        if current > last:
            return "Impossible"

        last = current

    return "Possible"


# Example
blocks = [5, 4, 2, 1, 4, 5]
print(lego_stack(blocks))