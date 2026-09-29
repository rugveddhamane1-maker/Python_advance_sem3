def knapsack_bottom_up(values, weights, W):
    n = len(values)

    # DP table
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Find the selected items
    w = W
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    return dp[n][W], selected_items


# Example
values = [60, 100, 120]
weights = [10, 20, 30]
W = 50

max_value, selected_items = knapsack_bottom_up(values, weights, W)

print("Maximum Value:", max_value)
print("Selected Items:", selected_items)