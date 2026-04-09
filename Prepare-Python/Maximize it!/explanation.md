# 🚀 The Problem Overview

The goal is to maximize the sum of squares from $K$ lists, subject to a modulo $M$.

$$S = (f(X_1) + f(X_2) + \dots + f(X_k)) \pmod M$$

Because the modulo operator is involved, simply picking the largest numbers doesn't work. For example, if $M = 10$, a sum of $9$ is better than a sum of $11$ ($11 \pmod{10} = 1$).

---

## 🧠 The Optimal Strategy: Dynamic Programming (DP)

Instead of exploring every possible combination (which grows exponentially), we use **Dynamic Programming**. We track only the *possible sums* at each step.

### Why this works

At any given list $i$, we don't need to know *which* specific numbers we picked from previous lists. We only need to know what **remainders modulo $M$** were possible. Since there are only $M$ possible remainders ($0$ to $M-1$), our "search space" stays small.

---

## 📝 Step-by-Step Walkthrough

**Constraints:** $M = 10$, $K = 3$ lists.

1. **Preprocessing:** Square every element and take it modulo $M$. Store them in a `set` to remove duplicates.
    * List 1: $\{2, 5\} \rightarrow \{4, 5\}$
    * List 2: $\{3, 7\} \rightarrow \{9\}$ (Both $3^2$ and $7^2$ mod 10 are 9)
    * List 3: $\{1, 4\} \rightarrow \{1, 6\}$

2. **The DP Table (Iterative Sets):**
    * **Start:** `possible_sums = {0}`
    * **After List 1:** Apply $\{4, 5\}$ to `{0}` $\rightarrow$ `{4, 5}`
    * **After List 2:** Apply $\{9\}$ to `{4, 5}`:
        * $(4 + 9) \pmod{10} = 3$
        * $(5 + 9) \pmod{10} = 4$
        * New set: `{3, 4}`
    * **After List 3:** Apply $\{1, 6\}$ to `{3, 4}`:
        * From 3: $(3+1)=4, (3+6)=9$
        * From 4: $(4+1)=5, (4+6)=0$
        * Final set: `{0, 4, 5, 9}`

3. **Result:** The maximum value in the final set is **9**.

---

## 💻 Python Implementation

This code uses the set-based DP approach. It is highly efficient because the size of `possible_sums` is capped at $M$.

```python
def solve():
    # K = number of lists, M = modulo
    k, m = map(int, input().split())
    
    # We start with a sum of 0 possible
    possible_sums = {0}
    
    for _ in range(k):
        # Read list, ignore first element (size), square others % M
        current_list = set(int(x)**2 % m for x in input().split()[1:])
        
        next_possible_sums = set()
        
        # Combine every existing sum with every new possible squared value
        for s in possible_sums:
            for val in current_list:
                next_possible_sums.add((s + val) % m)
        
        # Update the state for the next list
        possible_sums = next_possible_sums

    # The answer is the maximum remainder found
    print(max(possible_sums))

# solve()
```

---

## 📊 Complexity Comparison

| Feature | Backtracking / Brute Force | Dynamic Programming |
| :--- | :--- | :--- |
| **Logic** | Checks every single combination | Checks every possible remainder |
| **Complexity** | $O(N^K)$ (Exponential) | $O(K \times N \times M)$ (Pseudo-polynomial) |
| **Worst Case** | $7^7 = 823,543$ paths | $7 \times 7 \times 1000 = 49,000$ operations |
| **Efficiency** | Slows down as $K$ increases | Stays stable as long as $M$ is reasonable |

> **Note:** If $M$ is very small, DP is vastly superior. If $M$ is massive but $K$ is small, the `itertools.product` (brute force) method is actually faster in Python because it runs in highly optimized C-code.

Does this DP approach feel more manageable than the backtracking logic you were originally visualizing?
