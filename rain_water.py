def calc_trapped_rain_water(heights):
    n = len(heights)
    left_max = [ i * 0 for i in range(n)]
    right_max = [ i * 0 for i in range(n) ]

    left_max[0] = heights[0]
    right_max[-1] = heights[-1]

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], heights[i])

    for i in range (2, n + 1):
        right_max[-1 * i] = max(right_max[(-1 * i) + 1], heights[-1 * i])

    trapped_water = 0

    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        trapped_water += water_level - heights[i]

    return trapped_water


def container_with_most_water(heights):
    n = len(heights)
    lp = 0
    rp = n - 1
    max_water = 0
    while lp < rp:
        width = rp - lp
        ht = min(heights[lp], heights[rp])
        water_stored = width * ht
        max_water = max(water_stored, max_water)

        if heights[lp] < heights[rp]:
            lp += 1
        else:
            rp -= 1

    return max_water


if __name__ == '__main__':
    heights = [4, 2, 0, 6, 3, 2, 5]

    print(calc_trapped_rain_water(heights))
    print(container_with_most_water(heights))