regex_integer_in_range = r"^[1-9]\d{5}$"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.

import re

P = input()

print(
    bool(re.match(regex_integer_in_range, P))
    and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2
)


# removed these when running - they'd bug it out even with the correct response.
# Range: Starts with 1-9, followed by exactly 5 digits (100,000 to 999,999)

# Alternating Repetitive Pair: Find a digit (\d), skip one digit (\d),
# and see if the first digit appears again (\1).
# We use a lookahead (?=...) so that it finds overlapping pairs like 12121.
