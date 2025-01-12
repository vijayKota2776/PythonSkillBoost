def longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    longest_length = 0
    end_index_str1 = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_length:
                    longest_length = dp[i][j]
                    end_index_str1 = i - 1
            else:
                dp[i][j] = 0 
    longest_common_substr = str1[end_index_str1 - longest_length + 1:end_index_str1 + 1]
    
    return longest_common_substr
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
lcs = longest_common_substring(str1, str2)
print(f"The longest common substring is: {lcs}")
