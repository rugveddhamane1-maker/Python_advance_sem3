def knapsack_top_down(weights, values, capacity):
    n = len(weights)
    memo = {}

    def solve(i, remaining):
        # Base case
        if i == n or remaining == 0:
            return 0

        # Return cached result
        if (i, remaining) in memo:
            return memo[(i, remaining)]

        # Skip current item
        not_take = solve(i + 1, remaining)

        # Take current item if possible
        take = 0
        if weights[i] <= remaining:
            take = values[i] + solve(i + 1, remaining - weights[i])

        # Store maximum value
        memo[(i, remaining)] = max(take, not_take)

        return memo[(i, remaining)]

    # Get maximum value
    max_value = solve(0, capacity)

    # Find selected items
    selected_items = []
    i = 0
    remaining = capacity

    while i < n:
        not_take = solve(i + 1, remaining)

        take = -1
        if weights[i] <= remaining:
            take = values[i] + solve(i + 1, remaining - weights[i])

        if take > not_take:
            selected_items.append(i + 1)
            remaining -= weights[i]

        i += 1

    return max_value, selected_items


# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected_items = knapsack_top_down(
    weights, values, capacity
)

print("Maximum Value:", max_value)
print("Selected Items:", selected_items)