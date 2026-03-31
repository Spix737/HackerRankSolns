# Combinatorial String Counting or Implicit Substring Enumeration.


def minion_game(string: str) -> None:
    """
    Determines the winner of the Minion Game.
    Stuart scores for substrings starting with consonants; Kevin for vowels.
    Optimized to O(N) time and O(1) space by calculating substring counts mathematically.
    """
    # Use a set for O(1) constant-time lookups
    vowels = set("AEIOU")

    stuart_score, kevin_score = 0, 0
    length = len(string)

    for i, char in enumerate(string):
        # The number of valid substrings starting at index 'i' is exactly (length - i)
        if char in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    # Output results
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
