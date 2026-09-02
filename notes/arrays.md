# Arrays & Hashing — Notes

---

## 1. Contains Duplicate

**The problem in one line:** Does any number show up twice?

**What we learned:**
The naive way is to compare every number to every other number — slow (O(n²)). The trick is: instead of comparing things to each other, just *remember* what you've already seen. A hash set lets you ask "have I seen this before?" instantly (O(1)), so one single pass through the array is enough.

This is the most basic version of a pattern you'll see again and again: **"seen-before" hashing.**

**Pseudocode:**
```
create an empty set called "seen"
for each number in the array:
    if the number is already in "seen":
        return True (duplicate found)
    otherwise, add the number to "seen"
return False (no duplicates)
```

**Complexity:** O(n) time, O(n) space

---

## 2. Valid Anagram

**The problem in one line:** Do two strings have exactly the same letters, same amounts?

**What we learned:**
Sorting both strings and comparing them works, but sorting costs O(n log n). A faster way: count how many times each letter appears in each string, then compare the counts. If the counts match exactly, they're anagrams. This is the same "hash" idea as before, but now we're counting instead of just checking existence — this is called **frequency counting**.

**Pseudocode:**
```
if the two strings have different lengths:
    return False

count how many times each letter appears in string 1 -> count1
count how many times each letter appears in string 2 -> count2

return True if count1 equals count2, else False
```

**Complexity:** O(n) time, O(1) space (since there's a fixed alphabet)
**Bonus:** Python's `Counter(s) == Counter(t)` does this in one line.

---

## 3. Two Sum

**The problem in one line:** Find two numbers in the array that add up to a target.

**What we learned:**
Brute force checks every pair (O(n²)). The smarter way: as you walk through the array, ask yourself "what number would I need to reach the target from here?" (that's `target - current_number`). Then check: have I already seen that number? If yes, you found your pair. If no, remember the current number (and its index) for later.

This is the same "seen-before" idea from problem 1, but now we're storing *where* we saw it (a map, not just a set), and we're looking for a "complement" instead of a duplicate.

**Pseudocode:**
```
create an empty map called "seen" (number -> index)
for each index, number in the array:
    needed = target - number
    if needed is already in "seen":
        return [index of needed, current index]
    otherwise, remember: seen[number] = current index
```

**Complexity:** O(n) time, O(n) space
**Why order matters:** always check for the complement BEFORE adding the current number — this stops a number from accidentally pairing with itself.

---

## 4. Group Anagrams

**The problem in one line:** Group all strings that are anagrams of each other.

**What we learned:**
Two strings are anagrams if they become identical once sorted, or if they have the exact same letter counts. So: pick one of those two things (sorted string, or a "fingerprint" of letter counts) as a **key**, and put every string into a bucket (map) based on that key. All anagrams naturally land in the same bucket.

**Pseudocode:**
```
create an empty map called "groups"
for each string in the list:
    key = sorted version of the string   (or: a count of each letter a-z)
    add the string to groups[key]
return all the groups (values of the map)
```

**Complexity:**
- Using sorted string as key: O(n · m log m)
- Using letter-count fingerprint as key: O(n · m) — better in theory
**Real talk:** for short strings, the "better" version can be slower in practice because building a 26-length array for every string has its own overhead. Good to know both, and to explain the trade-off out loud.

---

## 5. Top K Frequent Elements

**The problem in one line:** Find the k numbers that appear most often.

**What we learned:**
Sorting by frequency works but costs O(n log n). Since frequency can never be higher than the array's length, we can skip sorting entirely: make a list of "buckets," where bucket index = frequency, and each bucket holds the numbers with that frequency. Then just read the buckets from highest frequency down until you have k numbers. This is called **bucket sort** — you use the value you're sorting BY as an array index instead of comparing things.

**Pseudocode:**
```
count how many times each number appears -> count map

create buckets: a list of empty lists, one for each possible frequency (0 to n)
for each number and its frequency:
    put the number into buckets[frequency]

result = []
go through buckets from highest frequency to lowest:
    add numbers to result until you have k of them
return result
```

**Complexity:** O(n) time, O(n) space

---

## 6. Encode and Decode Strings

**The problem in one line:** Turn a list of strings into one string (and back), safely.

**What we learned:**
The obvious idea is to join strings with a separator character (like a comma). The problem: what if a string itself contains that exact separator? Everything breaks. Since ANY character could show up inside the strings, we can't safely reserve any character as a separator.

The fix: instead of a separator, write the LENGTH of each string before it. The decoder reads the length first, then knows exactly how many characters to grab next — no searching for special characters needed, so it doesn't matter what's inside the string.

**Pseudocode:**
```
ENCODE:
result = ""
for each string s:
    result += length of s, then a marker character, then s itself
return result

DECODE:
result = []
i = 0
while i < length of the encoded string:
    read digits until you hit the marker -> that's the length
    read exactly that many characters after the marker -> that's the next string
    move i forward past that string
return result
```

**Complexity:** O(total characters), both directions
**Real-world version of this idea:** this is basically how network protocols like TCP frame their messages.

---

## 7. Product of Array Except Self

**The problem in one line:** For each position, multiply everything EXCEPT that position — without using division.

**What we learned:**
You can't just divide the total product by each number (division is banned, and it breaks with zeros anyway). Instead: for each position, the answer is "everything to the LEFT multiplied together" times "everything to the RIGHT multiplied together."

So do it in two passes: first pass, walk left to right, keeping a running product of everything before the current position. Second pass, walk right to left, keeping a running product of everything after — and multiply it into what you already have.

**Pseudocode:**
```
result = array of 1s, same length as nums

running_left = 1
walk left to right:
    result[i] = running_left
    running_left *= nums[i]

running_right = 1
walk right to left:
    result[i] *= running_right
    running_right *= nums[i]

return result
```

**Complexity:** O(n) time, O(1) extra space (not counting the output array)

---

## 8. Valid Sudoku

**The problem in one line:** Check that no row, column, or 3x3 box has a repeated digit.

**What we learned:**
Instead of scanning rows, then columns, then boxes separately (three full passes), do it all in ONE pass: for every cell, check if its value already exists in that row's set, that column's set, or that box's set. If yes, it's invalid. Otherwise, add it to all three sets and move on.

The trick for identifying which 3x3 box a cell belongs to: `(row // 3, col // 3)` always gives you a unique box id for any cell. Worth memorizing — this is the standard way to divide a grid into fixed-size blocks.

**Pseudocode:**
```
create empty sets for each row, each column, each box
for each cell (row, col) in the board:
    if the cell is empty, skip it
    value = the digit in that cell
    box_id = (row divided by 3, col divided by 3)
    if value is already in rows[row] or cols[col] or boxes[box_id]:
        return False
    add value to rows[row], cols[col], boxes[box_id]
return True
```

**Complexity:** O(1) for a fixed 9x9 board (O(n²) if you imagine a general n×n board)

---

## 9. Longest Consecutive Sequence

**The problem in one line:** Find the longest run of consecutive numbers (order doesn't matter in the original array), in O(n) — no sorting allowed.

**What we learned:**
Sorting would make this easy but costs O(n log n), which is too slow. Instead: put everything in a set for instant lookups. Then, only START counting a sequence from a number that is a TRUE starting point — meaning `number - 1` is NOT in the set. If it's not a true start, skip it; some other number will pick up the count from its own true start.

From each true start, keep checking `number + 1`, `number + 2`, etc. as long as they're in the set, counting how long the streak goes.

The clever part: even though this looks like a loop inside a loop, each number only ever gets "walked over" once across the whole algorithm (because you skip non-starts), so the total work stays O(n) — this is called **amortized** O(n).

**Pseudocode:**
```
put all numbers into a set
longest = 0
for each number in the set:
    if (number - 1) is NOT in the set:      # this means it's a true start
        length = 1
        keep checking number+1, number+2, ... while they're in the set
        increase length each time
        update longest if this length is bigger
return longest
```

**Complexity:** O(n) time, O(n) space

---

## The Big Picture: What This Whole Section Teaches

If you remember nothing else, remember this:

- **Hash set** = "have I seen this exact thing before?" (yes/no)
- **Hash map** = "have I seen this, and what do I need to remember about it?" (index, count, group, etc.)
- **Fixed-size array instead of a map** = when your "alphabet" is small and known (26 letters, ASCII), an array can be faster than a map.
- **Bucket sort** = when you're sorting by something that's bounded by n (like frequency), skip real sorting — use the value as an array index instead.
- **Prefix/suffix passes** = "everything before me" + "everything after me," combined in two simple passes instead of recomputing from scratch each time.
- **Length-prefixing** = when no character is safe to use as a separator, encode the LENGTH instead of relying on a special character.
- **Amortized O(n)** = sometimes a loop inside a loop still adds up to O(n) total, because most iterations get skipped or each element is only truly processed once overall. Don't assume "nested loop = O(n²)" without checking this.

**The one sentence to say out loud in every interview:**
"Here's the brute force and its complexity — now here's the trade-off (usually space-for-time) that gets us to the optimal solution."
