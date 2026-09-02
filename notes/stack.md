# Stacks — Notes

---

## 1. Valid Parentheses

**The problem in one line:** Check if brackets open and close correctly and in the right order.

**What we learned:**
Whenever a problem is about "nesting" or "the last thing opened must be the first thing closed," that's a stack, immediately. Push every opening bracket. When you hit a closing bracket, check: does it match what's on top of the stack? If yes, pop it (that pair is resolved). If no — either wrong type, or nothing to match — the string is invalid.

The elegant part: all three ways a string can be invalid (mismatched pair, an unexpected closer, or an unclosed opener) all collapse into one final check: **is the stack empty at the end?**

**Pseudocode:**
```
create an empty stack
map of closing bracket -> matching opening bracket

for each character in the string:
    if it's a closing bracket AND the top of the stack matches it:
        pop the stack
    else:
        push the character onto the stack

return True if the stack is empty at the end, else False
```

**Complexity:** O(n) time, O(n) space

---

## 2. Min Stack

**The problem in one line:** Build a stack that can also tell you the minimum value in O(1).

**What we learned:**
The naive way to get the min would be to scan the whole stack every time (O(n)) — too slow. Instead, keep a **second stack that runs in parallel**, where each position stores "what was the minimum so far, up to this point in the stack." Every push updates both stacks together; every pop removes from both together.

The trick that makes this work: when you pop a value, you're also automatically popping the minimum that was true *while that value was on top*. Since both stacks move in lockstep, the second stack always "reverts" to the correct previous minimum with zero extra work.

**Pseudocode:**
```
maintain two stacks: "stack" (real values) and "minStack" (running min)

push(val):
    push val onto "stack"
    new_min = val if minStack is empty else min(val, minStack top)
    push new_min onto "minStack"

pop():
    pop from both stacks

top():
    return top of "stack"

getMin():
    return top of "minStack"
```

**Complexity:** O(1) time for every operation, O(n) space (two parallel stacks)
**Big idea to keep:** this "shadow stack that tracks a running aggregate" trick generalizes beyond min — you could track max, running sum, etc. the same way.

---

## 3. Evaluate Reverse Polish Notation

**The problem in one line:** Evaluate a math expression written in postfix (operators come after their operands).

**What we learned:**
RPN is specifically designed to be evaluated with a stack: push numbers as you see them. When you hit an operator, pop the two most recent numbers, apply the operator, and push the result back. No need to worry about parentheses or operator precedence at all — that's the whole point of this notation.

The one thing to be careful about: for `-` and `/`, **order matters**. The two numbers you pop come off in reverse order from how they were pushed, so you have to pop into `num2` (top/most recent) then `num1` (older), and compute `num1 - num2`, not the other way around.

**Pseudocode:**
```
create an empty stack
for each token:
    if token is a number:
        push it onto the stack
    else (it's an operator):
        num2 = pop from stack   # most recently pushed
        num1 = pop from stack   # pushed before that
        result = apply the operator to (num1, num2)
        push result back onto the stack
return the last remaining value on the stack
```

**Complexity:** O(n) time, O(n) space
**Watch out for:** division must truncate toward zero, not floor. In Python, `int(a / b)` does this correctly; `a // b` does NOT (it floors, which gives the wrong answer for negative results).

---

## 4. Daily Temperatures

**The problem in one line:** For each day, how many days until a warmer temperature shows up?

**What we learned:**
Brute force compares every day to every future day (O(n²)). The better way: walk through the days once, and keep a stack of "days that are still waiting to find a warmer day" — specifically, keep it in **decreasing temperature order**. When a new day's temperature is warmer than what's on top of the stack, that resolves the waiting day(s): pop them and record how many days it took (`current_index - waiting_index`). Keep popping as long as the new temperature keeps beating the stack's top.

This is called a **monotonic stack**, because the stack always maintains a consistent order (here: decreasing) — anything that would break that order gets resolved and removed immediately.

**Pseudocode:**
```
create an empty stack (holds indices, not temperatures)
result = array of 0s, same length as temperatures

for each index i, temperature in temperatures:
    while stack is not empty AND temperature at top of stack < current temperature:
        idx = pop from stack
        result[idx] = i - idx
    push i onto the stack

return result
```

**Complexity:** O(n) time (each index is pushed once and popped at most once — the total work across the whole run is bounded, even though single steps can pop multiple items — this is called **amortized** O(n)), O(n) space.
**Why store indices, not values:** you need the *distance* between days, so you need to know *where* something was, not just what its value was.

---

## 5. Car Fleet

**The problem in one line:** Cars driving toward the same destination merge into fleets if a slower car ahead blocks a faster car behind it. Count the fleets.

**What we learned:**
Sort cars by starting position, from closest-to-target to farthest. For each car (going front to back), calculate how long it would take to reach the destination *if driving alone*. Compare that to the time of the fleet directly ahead of it:
- If this car's time is ≤ the time of the fleet ahead, it will catch up and merge into that fleet before reaching the destination — so it does NOT form a new fleet.
- If its time is greater (it's slower), it can never catch up — it forms its own new fleet, and that fleet now "leads" for everything still behind it.

You only ever need to compare against the **most recent unmerged fleet's time** — you don't need to look further back, because that fleet's pace is already set by its leading (slowest) car.

**Pseudocode:**
```
pair up each car's (position, speed) and sort by position, closest-to-target first

fleets = 0
last_fleet_time = nothing yet

for each car (position, speed) in that order:
    time_to_target = (target - position) / speed
    if time_to_target > last_fleet_time:
        fleets += 1
        last_fleet_time = time_to_target
    # otherwise, this car merges into the fleet ahead — do nothing

return fleets
```

**Complexity:** O(n log n) — the sort dominates; this is actually optimal for this problem.
**Good thing to notice:** this problem *looks* like it needs a real stack, but in practice you only ever need to remember the most recent fleet's time — a single variable does the job, no actual stack data structure required. Good habit: check whether a "stack" solution is really using stack behavior (push/pop from both ends of history) or just tracking the latest value.

---

## 6. Largest Rectangle in Histogram

**The problem in one line:** Given bar heights, find the largest rectangular area that fits among them.

**What we learned:**
For any single bar, its maximum possible rectangle is bounded by the **nearest shorter bar** on its left and on its right — you can't extend the rectangle past a bar that's too short. Brute force checks this for every bar by scanning outward both directions (O(n²)).

The optimization: walk through the bars once, keeping a stack of indices in **increasing height order**. When a new bar is shorter than the one on top of the stack, that means the top bar just found its "nearest shorter bar on the right" — the current index. Pop it, and its "nearest shorter bar on the left" is now whatever is left on top of the stack after popping. Compute its area using those two boundaries. Keep popping as long as the new bar keeps being shorter than the stack's top.

One extra trick: at the very end, some bars might be left in the stack because nothing ever "beat" them. To resolve those too, add an imaginary bar of height `-1` (or `0`) at the very end — since it's shorter than everything real, it forces the stack to fully empty out and resolve every remaining bar.

**Pseudocode:**
```
create an empty stack (holds indices)
add a sentinel value smaller than any real height at the end of the array (conceptually)

for each index i, height in heights (including the sentinel):
    while stack is not empty AND height < height at top of stack:
        idx = pop from stack
        right_boundary = i
        left_boundary = whatever is now on top of stack, or -1 if empty
        width = right_boundary - left_boundary - 1
        area = width * height[idx]
        update max area if this is bigger
    push i onto the stack

return max area found
```

**Complexity:** O(n) time (same amortized reasoning as Daily Temperatures — every index pushed/popped once), O(n) space.
**Relationship to Daily Temperatures:** same skeleton, just flipped (increasing stack instead of decreasing) and resolving an *area* (using both a left and right boundary) instead of a *distance*. Worth remembering as "Daily Temperatures' harder cousin" rather than a totally separate trick.

---

## The Big Picture: What This Whole Section Teaches

- **Basic stack** = "last in, first out" — perfect for nesting, matching pairs, and undo-style problems (Valid Parentheses).
- **Shadow/auxiliary stack** = keep a second stack in lockstep with the first to track a running aggregate (min, max, etc.) in O(1) (Min Stack).
- **Stack as an expression evaluator** = when notation removes the need for precedence rules (like RPN), a stack evaluates it directly, no parsing needed (Evaluate RPN).
- **Monotonic stack (decreasing)** = "find the next element that beats this one" type problems — resolve pending answers the moment something disproves them (Daily Temperatures).
- **Monotonic stack (increasing)** = similar idea, but used to find boundaries on both sides at once, often for area/width calculations (Largest Rectangle in Histogram).
- **Not everything that "feels stacky" needs a real stack** — sometimes tracking just the most recent value is enough (Car Fleet).
- **Amortized O(n)** — monotonic stack problems often have a `while` loop inside a `for` loop that looks like O(n²), but since each element is pushed and popped at most once *across the whole run*, the true total cost is O(n).
- **Sentinel values** — adding a fake smallest/largest element at the boundary is a clean, standard way to force cleanup of anything left unresolved at the end of a monotonic stack pass.

**The one sentence to say out loud in every interview:**
"This has a nesting/ordering structure, or I need to find the 'next bigger/smaller' thing efficiently — that's a stack, and if I need it to stay ordered as I go, that's a monotonic stack."
