# LeetCode Solutions

![Total](https://img.shields.io/badge/solved-21-blue?style=for-the-badge)
![Easy](https://img.shields.io/badge/easy-19-00b8a3?style=for-the-badge)
![Medium](https://img.shields.io/badge/medium-2-ffc01e?style=for-the-badge)
![Hard](https://img.shields.io/badge/hard-0-ff375f?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3-3776ab?style=for-the-badge&logo=python&logoColor=white)

Every problem I have solved on [LeetCode](https://leetcode.com), kept as a working notebook rather than a dump of code.
Each problem gets its own folder holding the accepted solution, a short set of notes, and — where I rewrote it —
a second version alongside the first. The point is to be able to come back to any problem months later and
recover *why* the solution works, not just what it was.

---

## At a glance

| | |
|---|---|
| Problems solved | **21** |
| Easy / Medium / Hard | 19 / 2 / 0 |
| Solution files | 23 across 21 folders |
| Lines of code | 343 |
| Primary language | Python 3 |
| First solve | 2026-09-06 |
| Most recent solve | 2026-11-11 |
| Days with at least one solve | 6 |
| Topics touched | 12 |

## Progress by difficulty

```
Easy    19  ████████████████████████  100%
Medium   2  ███░░░░░░░░░░░░░░░░░░░░░   11%
Hard     0  ░░░░░░░░░░░░░░░░░░░░░░░░    0%
```

The bars are scaled against Easy, not against a target, so the shape shows where the work has actually gone.
Hard is untouched and Medium has 2 entries — closing that gap is the next stretch.

## Repository structure

```text
Leetcodes/
├── easy/
│   ├── 1-two-sum/
│   │   ├── notes.md          # approach, complexity, link
│   │   └── python_v1.py      # accepted solution
│   ├── 1979-find-greatest-common-divisor-of-array/
│   │   ├── notes.md
│   │   ├── python3_v1.py     # first attempt
│   │   └── python3_v2.py     # rewrite, kept for comparison
│   └── …
├── medium/
│   ├── 46-permutations/
│   └── 50-powx-n/
└── README.md
```

### Conventions

- **Folder name** — `<problem number>-<title slug>`, matching the LeetCode URL exactly.
- **Difficulty folder** — `easy/`, `medium/`, `hard/`. The folder is the difficulty, so the same problem never
  appears twice.
- **File name** — `<language>_v<N>.py`. A rewrite bumps `N` instead of overwriting the earlier attempt; both
  versions stay so the change in thinking is visible.
- **Notes** — `notes.md` per problem: the problem link, recorded time and space complexity, the approach in
  plain words, and any gotchas I hit.
- **Solution header** — every file opens with a four-line block recording when it was pushed, the difficulty,
  and the runtime and memory LeetCode reported for that submission:

```python
# Pushed: 2026-10-06 16:34:39 UTC
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 21 MB
```

That block is what makes this repo queryable — the tables below are generated from it, so the numbers in the
README and the numbers in the code can never drift apart.

## Topic coverage

| Topic | Problems | Where |
|---|---|---|
| String | 10 | [13](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/13-roman-to-integer), [20](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/20-valid-parentheses), [28](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/28-find-the-index-of-the-first-occurrence-in-a-string), [58](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/58-length-of-last-word), [67](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/67-add-binary), [125](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/125-valid-palindrome), [242](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/242-valid-anagram), [290](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/290-word-pattern), [884](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/884-uncommon-words-from-two-sentences), [1859](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1859-sorting-the-sentence) |
| Arrays | 7 | [1](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1-two-sum), [26](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/26-remove-duplicates-from-sorted-array), [27](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/27-remove-element), [66](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/66-plus-one), [136](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/136-single-number), [1752](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1752-check-if-array-is-sorted-and-rotated), [1979](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1979-find-greatest-common-divisor-of-array) |
| Math | 7 | [9](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/9-palindrome-number), [13](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/13-roman-to-integer), [50](https://github.com/Godspirit4U/Leetcodes/tree/main/medium/50-powx-n), [66](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/66-plus-one), [67](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/67-add-binary), [69](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/69-sqrtx), [1979](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1979-find-greatest-common-divisor-of-array) |
| Hash Table | 4 | [1](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1-two-sum), [242](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/242-valid-anagram), [290](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/290-word-pattern), [884](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/884-uncommon-words-from-two-sentences) |
| Two Pointers | 4 | [26](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/26-remove-duplicates-from-sorted-array), [27](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/27-remove-element), [28](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/28-find-the-index-of-the-first-occurrence-in-a-string), [125](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/125-valid-palindrome) |
| Bit Manipulation | 2 | [67](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/67-add-binary), [136](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/136-single-number) |
| Sorting | 2 | [242](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/242-valid-anagram), [1859](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1859-sorting-the-sentence) |
| Backtracking | 1 | [46](https://github.com/Godspirit4U/Leetcodes/tree/main/medium/46-permutations) |
| Binary Search | 1 | [69](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/69-sqrtx) |
| Recursion | 1 | [46](https://github.com/Godspirit4U/Leetcodes/tree/main/medium/46-permutations) |
| Stack | 1 | [20](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/20-valid-parentheses) |
| String Matching | 1 | [28](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/28-find-the-index-of-the-first-occurrence-in-a-string) |

`Backtracking`, `Binary Search`, `Recursion`, `Stack`, `String Matching` appear only once so far — those are the tags with a single data point behind them,
which is exactly where a second problem is worth more than a tenth array problem.

## Problem index

Sorted by problem number. `Runtime` and `Memory` are what LeetCode reported for the accepted submission.

| # | Problem | Difficulty | Topics | Time | Space | Solved | Runtime | Memory |
|---:|---|---|---|---|---|---|---|---|
| 1 | [Two Sum](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1-two-sum) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Hash Table | O(n²) | O(1) | 2026-09-09 | 5210 ms | 13.4 MB |
| 9 | [Palindrome Number](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/9-palindrome-number) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Math | O(log n) | O(1) | 2026-09-06 | 11 ms | 19.4 MB |
| 13 | [Roman to Integer](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/13-roman-to-integer) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Math | O(n) | O(1) | 2026-09-06 | 13 ms | 19.3 MB |
| 20 | [Valid Parentheses](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/20-valid-parentheses) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Stack | O(n) | O(n) | 2026-09-09 | 0 ms | 19.2 MB |
| 26 | [Remove Duplicates from Sorted Array](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/26-remove-duplicates-from-sorted-array) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Two Pointers | O(n) | O(1) | 2026-09-09 | 3 ms | 20.5 MB |
| 27 | [Remove Element](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/27-remove-element) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Two Pointers | O(n) | O(1) | 2026-10-05 | 0 ms | 19.1 MB |
| 28 | [Find the Index of the First Occurrence in a String](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/28-find-the-index-of-the-first-occurrence-in-a-string) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, String Matching, Two Pointers | O(n·m) | O(m) | 2026-09-09 | 0 ms | 19.2 MB |
| 46 | [Permutations](https://github.com/Godspirit4U/Leetcodes/tree/main/medium/46-permutations) | ![Medium](https://img.shields.io/badge/Medium-ffc01e?style=flat-square) | Backtracking, Recursion | O(n!) | O(n) | 2026-10-08 | 2 ms | 19.6 MB |
| 50 | [Pow(x, n)](https://github.com/Godspirit4U/Leetcodes/tree/main/medium/50-powx-n) | ![Medium](https://img.shields.io/badge/Medium-ffc01e?style=flat-square) | Math | O(1) | O(1) | 2026-09-09 | 3 ms | 19.5 MB |
| 58 | [Length of Last Word](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/58-length-of-last-word) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String | O(n) | O(n) | 2026-09-09 | 0 ms | 19.3 MB |
| 66 | [Plus One](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/66-plus-one) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Math | O(n) | O(n) | 2026-09-09 | 0 ms | 19.2 MB |
| 67 | [Add Binary](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/67-add-binary) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Math, Bit Manipulation | O(n) | O(n) | 2026-11-11 | 4 ms | 19.3 MB |
| 69 | [Sqrt(x)](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/69-sqrtx) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Math, Binary Search | O(√x) | O(1) | 2026-09-09 | 1148 ms | 19.2 MB |
| 125 | [Valid Palindrome](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/125-valid-palindrome) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Two Pointers | O(n) | O(n) | 2026-09-09 | 3 ms | 19.7 MB |
| 136 | [Single Number](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/136-single-number) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Bit Manipulation | O(n) | O(1) | 2026-10-06 | 1 ms | 21 MB |
| 242 | [Valid Anagram](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/242-valid-anagram) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Hash Table, Sorting | O(n log n) | O(n) | 2026-09-09 | 15 ms | 20.5 MB |
| 290 | [Word Pattern](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/290-word-pattern) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Hash Table | O(n·k) | O(n) | 2026-09-09 | 0 ms | 19.2 MB |
| 884 | [Uncommon Words from Two Sentences](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/884-uncommon-words-from-two-sentences) — [v2](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/884-uncommon-words-from-two-sentences/python3_v2.py) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Hash Table | O(n) | O(n) | 2026-09-09 | 0 ms | 19.1 MB |
| 1752 | [Check if Array Is Sorted and Rotated](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1752-check-if-array-is-sorted-and-rotated) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays | O(n) | O(1) | 2026-09-09 | 0 ms | 19.3 MB |
| 1859 | [Sorting the Sentence](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1859-sorting-the-sentence) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Sorting | O(n log n) | O(n) | 2026-11-11 | 0 ms | 19.2 MB |
| 1979 | [Find Greatest Common Divisor of Array](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1979-find-greatest-common-divisor-of-array) — [v2](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1979-find-greatest-common-divisor-of-array/python3_v2.py) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Math | O(n) | O(1) | 2026-09-09 | 0 ms | 19.2 MB |

## Timeline

| Date | Solved | Problems |
|---|---|---|
| 2026-09-06 | 2 | 9. Palindrome Number, 13. Roman to Integer |
| 2026-09-09 | 14 | 1. Two Sum, 20. Valid Parentheses, 26. Remove Duplicates from Sorted Array, 28. Find the Index of the First Occurrence in a String, 50. Pow(x, n), 58. Length of Last Word, 66. Plus One, 69. Sqrt(x), 125. Valid Palindrome, 242. Valid Anagram, 290. Word Pattern, 884. Uncommon Words from Two Sentences, 1752. Check if Array Is Sorted and Rotated, 1979. Find Greatest Common Divisor of Array |
| 2026-10-05 | 1 | 27. Remove Element |
| 2026-10-06 | 1 | 136. Single Number |
| 2026-10-08 | 1 | 46. Permutations |
| 2026-11-11 | 2 | 67. Add Binary, 1859. Sorting the Sentence |

6 sessions across 21 problems. The bulk of it landed on 2026-09-09, when 14 problems went up in one sitting — a sweep through the array-and-string basics rather than a set of unrelated one-offs.

## What is in here, by pattern

| Pattern | Count | Problems |
|---|---|---|
| Arrays & in-place writes | 4 | 26. Remove Duplicates from Sorted Array, 27. Remove Element, 66. Plus One, 1752. Check if Array Is Sorted and Rotated |
| Hash map / counting | 4 | 1. Two Sum, 242. Valid Anagram, 290. Word Pattern, 884. Uncommon Words from Two Sentences |
| Two pointers & string scanning | 3 | 13. Roman to Integer, 28. Find the Index of the First Occurrence in a String, 125. Valid Palindrome |
| Stack | 1 | 20. Valid Parentheses |
| Math & number theory | 4 | 9. Palindrome Number, 50. Pow(x, n), 69. Sqrt(x), 1979. Find Greatest Common Divisor of Array |
| Bit manipulation | 2 | 67. Add Binary, 136. Single Number |
| Backtracking & recursion | 1 | 46. Permutations |
| Sorting as the trick | 2 | 242. Valid Anagram, 1859. Sorting the Sentence |

Read as a whole, the repo is heavy on the two shapes that pay off first — linear scans with an index pointer,
and a dictionary standing in for a nested loop. The gaps are equally visible: no trees, no graphs, no dynamic
programming, one backtracking problem, and binary search attempted exactly once.

## Where this goes next

- **Binary search** — `69. Sqrt(x)` was solved by a linear scan. Redoing it with a search over the answer
  range would give the pattern a proper second data point.
- **Mediums** — two out of twenty-one. The array and string floor is solid; the ceiling has not been tested.
- **Hard** — untouched. Not worth starting until Medium feels routine.
- **Backfill the notes** — most `notes.md` files still read `_not specified_` for complexity. Filling those in
  as problems get revisited costs a minute each and makes the repo genuinely useful later.

---

<sub>Generated from the repository itself — 21 problems, 23 solution files, 343 lines of Python. Last updated 2026-11-12.</sub>
