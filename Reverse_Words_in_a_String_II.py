class Solution:
    def reverseWords(self, s):
        s = list(s)

        # Reverse the entire string
        s.reverse()

        # Reverse each word
        start = 0

        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                s[start:i] = reversed(s[start:i])
                start = i + 1

        return ''.join(s)
