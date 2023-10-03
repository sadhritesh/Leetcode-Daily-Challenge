"""
557. Reverse Words in a String III

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"

Time Complexity is O(n * k)
Space Complexity is O(n).
"""
def reverseWords(self, s: str) -> str:
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)
 