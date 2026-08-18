def lcs_memo(X, Y, i, j, memo):

    # Base condition

    if i == 0 or j == 0:

        return 0

    # Check if already calculated

    if (i, j) in memo:

        return memo[(i, j)]

    # If characters match

    if X[i - 1] == Y[j - 1]:

        memo[(i, j)] = lcs_memo(X, Y, i - 1, j - 1, memo) + 1

    # If characters do not match

    else:

        memo[(i, j)] = max(

            lcs_memo(X, Y, i - 1, j, memo),

            lcs_memo(X, Y, i, j - 1, memo)

        )

    return memo[(i, j)]

def get_lcs_memo(X, Y):

    memo = {}

    length = lcs_memo(X, Y, len(X), len(Y), memo)

    # Reconstruct LCS

    i = len(X)

    j = len(Y)

    lcs_string = ""

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:

            lcs_string = X[i - 1] + lcs_string

            i -= 1

            j -= 1

        else:

            top = lcs_memo(X, Y, i - 1, j, memo)

            left = lcs_memo(X, Y, i, j - 1, memo)

            if top > left:

                i -= 1

            else:

                j -= 1

    return length, lcs_string