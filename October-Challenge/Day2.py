"""
2038. Remove Colored Pieces if Both Neighbors are the Same Color

There are n pieces arranged in a line, and each piece is colored either by 'A' or by 'B'. You are given a string colors of length n where colors[i] is the color of the ith piece.

Alice and Bob are playing a game where they take alternating turns removing pieces from the line. In this game, Alice moves first.

Alice is only allowed to remove a piece colored 'A' if both its neighbors are also colored 'A'. She is not allowed to remove pieces that are colored 'B'.
Bob is only allowed to remove a piece colored 'B' if both its neighbors are also colored 'B'. He is not allowed to remove pieces that are colored 'A'.
Alice and Bob cannot remove pieces from the edge of the line.
If a player cannot make a move on their turn, that player loses and the other player wins.
Assuming Alice and Bob play optimally, return true if Alice wins, or return false if Bob wins.

 

Example 1:

Input: colors = "AAABABB"
Output: true
Explanation:
AAABABB -> AABABB
Alice moves first.
She removes the second 'A' from the left since that is the only 'A' whose neighbors are both 'A'.

Now it's Bob's turn.
Bob cannot make a move on his turn since there are no 'B's whose neighbors are both 'B'.
Thus, Alice wins, so return true.
Example 2:

Input: colors = "AA"
Output: false
Explanation:
Alice has her turn first.
There are only two 'A's and both are on the edge of the line, so she cannot move on her turn.
Thus, Bob wins, so return false.
Example 3:

Input: colors = "ABBBBBBBAAA"
Output: false
Explanation:
ABBBBBBBAAA -> ABBBBBBBAA
Alice moves first.
Her only option is to remove the second to last 'A' from the right.

ABBBBBBBAA -> ABBBBBBAA
Next is Bob's turn.
He has many options for which 'B' piece to remove. He can pick any.

On Alice's second turn, she has no more pieces that she can remove.
Thus, Bob wins, so return false.

"""
#Brute Force 
#Time Complexity --  O(n^2)
#Space Complexity -- O(n) due to stack space used by recursion

def helper(colors,chance):
    if len(colors) < 3:
        if chance == "Bob" : return True 
        else: return False 
    for i in range(1,len(colors)-1):
        if chance == "Alice":
            if colors[i] == "A" and colors[i-1] == "A" and colors[i+1] == "A":
                new_colors = colors[:i] + colors[i+1:]
                break 
        else:
            if colors[i] == "B" and colors[i-1] == "B" and colors[i+1] == "B":
                new_colors = colors[:i] + colors[i+1:]
                break 
    else:
        return (False if chance == "Alice" else True)
    nxt_chance = "Alice" if chance == "Bob" else "Bob"
    return helper(new_colors,nxt_chance)
def winnerOfGame(colors: str) -> bool:
    return helper(colors,"Alice")

#Optimised
#Time Complexity --  O(n)
#Space Complexity -- O(1)

def winnerOfGame(colors: str) -> bool:
    chance_count = {'A':0 , 'B':0}
    n = len(colors)
    if n < 3: return False 
    for i in range(n-2):
        if colors[i:i+3] == colors[i]*3:
            chance_count[colors[i]] += 1 
    return (False if chance_count['A'] <= chance_count['B'] else True) 