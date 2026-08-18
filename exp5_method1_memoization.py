# Experiment 5
# LCS using Top-Down Memoization

def lcs_memo(X, Y, i, j, memo):

    if i == 0 or j == 0:
        return 0

    if (i, j) in memo:
        return memo[(i, j)]

    if X[i - 1] == Y[j - 1]:
        memo[(i, j)] = lcs_memo(X, Y, i - 1, j - 1, memo) + 1
    else:
        memo[(i, j)] = max(
            lcs_memo(X, Y, i - 1, j, memo),
            lcs_memo(X, Y, i, j - 1, memo)
        )

    return memo[(i, j)]


def get_lcs_memo(X, Y):
    memo = {}

    length = lcs_memo(X, Y, len(X), len(Y), memo)

    i = len(X)
    j = len(Y)
    lcs_string = ""

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs_string = X[i - 1] + lcs_string
            i -= 1
            j -= 1

        elif lcs_memo(X, Y, i - 1, j, memo) > lcs_memo(X, Y, i, j - 1, memo):
            i -= 1

        else:
            j -= 1

    return length, lcs_string


# Example
X = "AGGTAB"
Y = "GXTXAYB"

length, sequence = get_lcs_memo(X, Y)

print("String 1:", X)
print("String 2:", Y)
print("Longest Common Subsequence:", sequence)
print("Length of LCS:", length)