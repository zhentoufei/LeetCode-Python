def lcse(str1, str2):
    if str1 == None or str2 == None or str1 == '' or str2 == '':
        return None

    dp = getdp(str1, str2)
    print(dp)
    m = len(str1) - 1
    n = len(str2) - 1
    res = [['' for i in range(n)] for j in range(m)]
    index = dp[m][n] - 1

    while index > 0:
        if m > 0 and dp[m][n] == dp[m - 1][n]:
            m -= 1
        elif n > 0 and dp[m][n] == dp[m][n - 1]:
            n -= 1
        else:
            res[index] = str1[m]
            index -= 1
            m -= 1
            n -= 1
    ans = ''
    for row in res:
        ans += ''.join(row)
    print(ans)
    return ans


def getdp(str1, str2):

    dp = [[0 for i in range(len(str2))] for j in range(len(str1))]

    dp[0][0] = 1 if str1[0] == str2[0] else 0

    for i in range(1, len(str1)):
        dp[i][0] = max(dp[i - 1][0], 1 if str1[i] == str2[0] else 0)

    for j in range(1, len(str2)):
        dp[0][j] = max(dp[0][j - 1], 1 if str2[j] == str1[0] else 0)

    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if str1[i] == str2[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1

    return dp


str1 = "1A2C3D4B56"
str2 = "B1D23CA45B6A"
lcse(str1, str2)

