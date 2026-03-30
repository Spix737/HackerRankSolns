import re

n = int(input())

for _ in range(n):
    line = input()

    # Using regex lookarounds to verify surrounding spaces without consuming them.
    #   (?<= ) : Positive lookbehind ensures a preceding space exists.
    #   (?= )  : Positive lookahead ensures a succeeding space exists.
    # This non-consuming approach prevents match failures on overlapping
    # patterns (e.g., consecutive symbols that share a space, like " && || ").
    modified_line = re.sub(
        r"(?<= )(&&|\|\|)(?= )",
        lambda match: "and" if match.group(0) == "&&" else "or",
        line,
    )

    print(modified_line)
