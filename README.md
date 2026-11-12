# LeetCode Solutions

![Total](https://img.shields.io/badge/solved-21-blue?style=for-the-badge)
![Easy](https://img.shields.io/badge/easy-19-00b8a3?style=for-the-badge)
![Medium](https://img.shields.io/badge/medium-2-ffc01e?style=for-the-badge)
![Hard](https://img.shields.io/badge/hard-0-ff375f?style=for-the-badge)
![Python](https://img.shields.io/badge/python-3-3776ab?style=for-the-badge&logo=python&logoColor=white)

A record of the LeetCode problems I have solved, written in Python. Every problem has its own folder
containing the accepted solution and a note file that records the approach, the complexity and the link
to the original problem.

## Summary

| Metric | Value |
|---|---|
| Problems solved | 21 |
| Easy / Medium / Hard | 19 / 2 / 0 |
| Solution files | 23 across 21 folders |
| Lines of code | 343 |
| Language | Python 3 |
| First solve | 2026-09-06 |
| Latest solve | 2026-11-11 |
| Active days | 6 |
| Topics covered | 12 |

## Progress by difficulty

Each bar is proportional to the total of 21 problems in the repository.

```text
Total   21  ████████████████████████  100.0%
Easy    19  ██████████████████████░░   90.5%
Medium   2  ██░░░░░░░░░░░░░░░░░░░░░░    9.5%
Hard     0  ░░░░░░░░░░░░░░░░░░░░░░░░    0.0%
```

## Repository layout

```text
Leetcodes/
|-- easy/
|   |-- 1-two-sum/
|   |   |-- notes.md          approach, complexity, problem link
|   |   `-- python_v1.py      accepted solution
|   |-- 1979-find-greatest-common-divisor-of-array/
|   |   |-- notes.md
|   |   |-- python3_v1.py     first attempt
|   |   `-- python3_v2.py     rewrite, kept alongside v1
|   `-- ...
|-- medium/
|   |-- 46-permutations/
|   `-- 50-powx-n/
`-- README.md
```

### Naming and structure

| Item | Rule |
|---|---|
| Difficulty folder | `easy/`, `medium/`, `hard/`. The folder carries the difficulty, so a problem is never duplicated. |
| Problem folder | `<number>-<title slug>`, taken from the LeetCode URL. |
| Solution file | `<language>_v<N>.py`. A rewrite increments the version instead of overwriting the earlier attempt. |
| Notes file | `notes.md`, holding the problem link, recorded complexity, the approach in plain words and any pitfalls. |

Every solution file opens with a four-line header recording the push time, the difficulty, and the runtime
and memory that LeetCode reported for that submission:

```python
# Pushed: 2026-10-06 16:34:39 UTC
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 21 MB
```

The tables in this README are built from those headers and from the folder layout, so the documented
figures and the repository contents stay in step.

## Topic coverage

| Topic | Problems | Problem numbers |
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

## Problem index

Ordered by problem number. Runtime and memory are the values reported by LeetCode for the accepted submission.

| # | Problem | Difficulty | Topics | Time | Space | Solved | Runtime | Memory |
|---:|---|---|---|---|---|---|---|---|
| 1 | [Two Sum](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1-two-sum) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Hash Table | O(n^2) | O(1) | 2026-09-09 | 5210 ms | 13.4 MB |
| 9 | [Palindrome Number](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/9-palindrome-number) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Math | O(log n) | O(1) | 2026-09-06 | 11 ms | 19.4 MB |
| 13 | [Roman to Integer](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/13-roman-to-integer) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Math | O(n) | O(1) | 2026-09-06 | 13 ms | 19.3 MB |
| 20 | [Valid Parentheses](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/20-valid-parentheses) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Stack | O(n) | O(n) | 2026-09-09 | 0 ms | 19.2 MB |
| 26 | [Remove Duplicates from Sorted Array](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/26-remove-duplicates-from-sorted-array) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Two Pointers | O(n) | O(1) | 2026-09-09 | 3 ms | 20.5 MB |
| 27 | [Remove Element](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/27-remove-element) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Two Pointers | O(n) | O(1) | 2026-10-05 | 0 ms | 19.1 MB |
| 28 | [Find the Index of the First Occurrence in a String](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/28-find-the-index-of-the-first-occurrence-in-a-string) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, String Matching, Two Pointers | O(n*m) | O(m) | 2026-09-09 | 0 ms | 19.2 MB |
| 46 | [Permutations](https://github.com/Godspirit4U/Leetcodes/tree/main/medium/46-permutations) | ![Medium](https://img.shields.io/badge/Medium-ffc01e?style=flat-square) | Backtracking, Recursion | O(n!) | O(n) | 2026-10-08 | 2 ms | 19.6 MB |
| 50 | [Pow(x, n)](https://github.com/Godspirit4U/Leetcodes/tree/main/medium/50-powx-n) | ![Medium](https://img.shields.io/badge/Medium-ffc01e?style=flat-square) | Math | O(1) | O(1) | 2026-09-09 | 3 ms | 19.5 MB |
| 58 | [Length of Last Word](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/58-length-of-last-word) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String | O(n) | O(n) | 2026-09-09 | 0 ms | 19.3 MB |
| 66 | [Plus One](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/66-plus-one) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Math | O(n) | O(n) | 2026-09-09 | 0 ms | 19.2 MB |
| 67 | [Add Binary](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/67-add-binary) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Math, Bit Manipulation | O(n) | O(n) | 2026-11-11 | 4 ms | 19.3 MB |
| 69 | [Sqrt(x)](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/69-sqrtx) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Math, Binary Search | O(sqrt(x)) | O(1) | 2026-09-09 | 1148 ms | 19.2 MB |
| 125 | [Valid Palindrome](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/125-valid-palindrome) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Two Pointers | O(n) | O(n) | 2026-09-09 | 3 ms | 19.7 MB |
| 136 | [Single Number](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/136-single-number) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Bit Manipulation | O(n) | O(1) | 2026-10-06 | 1 ms | 21 MB |
| 242 | [Valid Anagram](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/242-valid-anagram) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Hash Table, Sorting | O(n log n) | O(n) | 2026-09-09 | 15 ms | 20.5 MB |
| 290 | [Word Pattern](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/290-word-pattern) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Hash Table | O(n*k) | O(n) | 2026-09-09 | 0 ms | 19.2 MB |
| 884 | [Uncommon Words from Two Sentences](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/884-uncommon-words-from-two-sentences) ([v2](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/884-uncommon-words-from-two-sentences/python3_v2.py)) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Hash Table | O(n) | O(n) | 2026-09-09 | 0 ms | 19.1 MB |
| 1752 | [Check if Array Is Sorted and Rotated](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1752-check-if-array-is-sorted-and-rotated) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays | O(n) | O(1) | 2026-09-09 | 0 ms | 19.3 MB |
| 1859 | [Sorting the Sentence](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1859-sorting-the-sentence) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | String, Sorting | O(n log n) | O(n) | 2026-11-11 | 0 ms | 19.2 MB |
| 1979 | [Find Greatest Common Divisor of Array](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1979-find-greatest-common-divisor-of-array) ([v2](https://github.com/Godspirit4U/Leetcodes/tree/main/easy/1979-find-greatest-common-divisor-of-array/python3_v2.py)) | ![Easy](https://img.shields.io/badge/Easy-00b8a3?style=flat-square) | Arrays, Math | O(n) | O(1) | 2026-09-09 | 0 ms | 19.2 MB |

## Sessions

| Date | Problems solved | Problem numbers |
|---|---|---|
| 2026-09-06 | 2 | 9, 13 |
| 2026-09-09 | 14 | 1, 20, 26, 28, 50, 58, 66, 69, 125, 242, 290, 884, 1752, 1979 |
| 2026-10-05 | 1 | 27 |
| 2026-10-06 | 1 | 136 |
| 2026-10-08 | 1 | 46 |
| 2026-11-11 | 2 | 67, 1859 |

## Patterns

| Pattern | Problems | Problem numbers |
|---|---|---|
| Arrays and in-place writes | 4 | 26, 27, 66, 1752 |
| Hash map and counting | 4 | 1, 242, 290, 884 |
| Two pointers and string scanning | 3 | 13, 28, 125 |
| Stack | 1 | 20 |
| Math and number theory | 4 | 9, 50, 69, 1979 |
| Bit manipulation | 2 | 67, 136 |
| Backtracking and recursion | 1 | 46 |
| Sorting | 2 | 242, 1859 |

## Next targets

- Binary search: problem 69 is solved with a linear scan. Rewriting it as a search over the answer range
  would give the pattern a second example.
- Medium difficulty: two problems out of 21. Arrays and strings are well covered, the harder half is not.
- Hard difficulty: no problems yet.
- Notes: most note files still record `_not specified_` for complexity. These are being filled in as problems
  are revisited.

---

<sub>21 problems, 23 solution files, 343 lines of Python. Updated 2026-11-12.</sub>
