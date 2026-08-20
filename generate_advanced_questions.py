import json
import random
import os

def gen_subsets():
    n = random.randint(4, 7)
    arr = random.sample(range(1, 20), n)
    arr.sort()
    inp = f"{n}\n" + " ".join(map(str, arr))
    
    ans = [[]]
    for x in arr:
        ans += [curr + [x] for curr in ans]
    
    ans.sort(key=lambda x: (len(x), x))
    out_str = "\n".join(" ".join(map(str, sub)) if sub else "EMPTY" for sub in ans)
    
    desc = "Given an integer array of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Print them sorted by length, then lexicographically. Empty subset is printed as 'EMPTY'.\n\n**Input Format**\nFirst line: N\nSecond line: N integers\n\n**Output Format**\nSubsets, one per line."
    return "Subsets", desc, inp, out_str

def gen_permutations():
    n = random.randint(3, 5)
    arr = list(range(1, n+1))
    random.shuffle(arr)
    inp = f"{n}\n" + " ".join(map(str, arr))
    
    import itertools
    perms = list(itertools.permutations(sorted(arr)))
    out_str = "\n".join(" ".join(map(str, p)) for p in perms)
    
    desc = "Given an array of distinct integers, return all the possible permutations. Print them in lexicographical order.\n\n**Input Format**\nFirst line: N\nSecond line: N integers\n\n**Output Format**\nPermutations, one per line."
    return "Permutations", desc, inp, out_str

def gen_combination_sum():
    n = random.randint(3, 5)
    arr = random.sample(range(2, 10), n)
    arr.sort()
    target = random.randint(10, 15)
    inp = f"{n}\n" + " ".join(map(str, arr)) + f"\n{target}"
    
    res = []
    def dfs(idx, path, total):
        if total == target:
            res.append(path)
            return
        if total > target:
            return
        for i in range(idx, len(arr)):
            dfs(i, path + [arr[i]], total + arr[i])
    dfs(0, [], 0)
    
    out_str = "\n".join(" ".join(map(str, r)) for r in res) if res else "NONE"
    
    desc = "Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. The same number may be chosen unlimited number of times.\n\n**Input Format**\nFirst line: N\nSecond line: N integers\nThird line: Target\n\n**Output Format**\nCombinations sorted lexicographically, one per line."
    return "Combination Sum", desc, inp, out_str

def gen_min_path_sum():
    m, n = random.randint(3, 5), random.randint(3, 5)
    grid = [[random.randint(1, 10) for _ in range(n)] for _ in range(m)]
    inp = f"{m} {n}\n" + "\n".join(" ".join(map(str, row)) for row in grid)
    
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for i in range(1, m): dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n): dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            
    desc = "Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path. You can only move down or right.\n\n**Input Format**\nFirst line: m n\nNext m lines: n integers each\n\n**Output Format**\nMinimum sum integer."
    return "Minimum Path Sum", desc, inp, str(dp[-1][-1])

def gen_coin_change():
    n = random.randint(3, 5)
    coins = random.sample([1, 2, 5, 10, 20], n)
    target = random.randint(20, 50)
    inp = f"{n}\n" + " ".join(map(str, coins)) + f"\n{target}"
    
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for c in coins:
        for i in range(c, target + 1):
            dp[i] = min(dp[i], dp[i - c] + 1)
            
    ans = dp[target] if dp[target] != float('inf') else -1
    desc = "You are given an integer array coins representing coins of different denominations and an integer amount. Return the fewest number of coins that you need to make up that amount.\n\n**Input Format**\nFirst line: N\nSecond line: N integers\nThird line: Amount\n\n**Output Format**\nMinimum coins, or -1 if not possible."
    return "Coin Change", desc, inp, str(ans)

def gen_lis():
    n = random.randint(8, 12)
    arr = [random.randint(1, 20) for _ in range(n)]
    inp = f"{n}\n" + " ".join(map(str, arr))
    
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    desc = "Given an integer array nums, return the length of the longest strictly increasing subsequence.\n\n**Input Format**\nFirst line: N\nSecond line: N integers\n\n**Output Format**\nInteger length."
    return "Longest Increasing Subsequence", desc, inp, str(max(dp))

def gen_number_islands():
    m, n = random.randint(4, 6), random.randint(4, 6)
    grid = [[random.choice(['0', '1']) for _ in range(n)] for _ in range(m)]
    inp = f"{m} {n}\n" + "\n".join(" ".join(row) for row in grid)
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
                
    desc = "Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.\n\n**Input Format**\nFirst line: m n\nNext m lines: n space-separated '0's and '1's\n\n**Output Format**\nInteger count."
    return "Number of Islands", desc, inp, str(count)

def gen_flood_fill():
    m, n = random.randint(4, 6), random.randint(4, 6)
    grid = [[random.randint(1, 3) for _ in range(n)] for _ in range(m)]
    sr, sc = random.randint(0, m-1), random.randint(0, n-1)
    new_color = random.randint(4, 6)
    inp = f"{m} {n}\n" + "\n".join(" ".join(map(str, row)) for row in grid) + f"\n{sr} {sc} {new_color}"
    
    start_color = grid[sr][sc]
    def dfs(r, c):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != start_color or grid[r][c] == new_color:
            return
        grid[r][c] = new_color
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
        
    dfs(sr, sc)
    out_str = "\n".join(" ".join(map(str, row)) for row in grid)
    desc = "Perform a flood fill on the image starting from the pixel (sr, sc) with newColor.\n\n**Input Format**\nFirst line: m n\nNext m lines: n integers\nLast line: sr sc newColor\n\n**Output Format**\nThe modified grid."
    return "Flood Fill", desc, inp, out_str

def gen_max_area_island():
    m, n = random.randint(5, 7), random.randint(5, 7)
    grid = [[random.choice([0, 1]) for _ in range(n)] for _ in range(m)]
    inp = f"{m} {n}\n" + "\n".join(" ".join(map(str, row)) for row in grid)
    
    def dfs(r, c):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)
        
    max_area = max([dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1] + [0])
    
    desc = "Find the maximum area of an island in a given 2D array.\n\n**Input Format**\nFirst line: m n\nNext m lines: n integers (0 or 1)\n\n**Output Format**\nInteger area."
    return "Max Area of Island", desc, inp, str(max_area)

def gen_top_k_frequent():
    n = random.randint(10, 15)
    arr = [random.randint(1, 5) for _ in range(n)]
    k = random.randint(1, 3)
    inp = f"{n}\n" + " ".join(map(str, arr)) + f"\n{k}"
    
    from collections import Counter
    counts = Counter(arr)
    ans = [x[0] for x in counts.most_common(k)]
    ans.sort()
    
    desc = "Given an integer array nums and an integer k, return the k most frequent elements. Sort the output array.\n\n**Input Format**\nFirst line: N\nSecond line: N integers\nThird line: k\n\n**Output Format**\nSpace-separated k elements in ascending order."
    return "Top K Frequent Elements", desc, inp, " ".join(map(str, ans))

def gen_sort_chars_freq():
    s = "".join(random.choices("aabbbccdddeeefff", k=15))
    inp = s
    from collections import Counter
    counts = Counter(s)
    ans = "".join(char * count for char, count in counts.most_common())
    
    desc = "Given a string s, sort it in decreasing order based on the frequency of the characters.\n\n**Input Format**\nSingle string S.\n\n**Output Format**\nSorted string."
    return "Sort Characters By Frequency", desc, inp, ans

def gen_kth_largest():
    n = random.randint(8, 12)
    arr = [random.randint(1, 50) for _ in range(n)]
    k = random.randint(1, 5)
    inp = f"{n}\n" + " ".join(map(str, arr)) + f"\n{k}"
    
    ans = sorted(arr, reverse=True)[k-1]
    
    desc = "Given an integer array nums and an integer k, return the kth largest element in the array.\n\n**Input Format**\nFirst line: N\nSecond line: N integers\nThird line: k\n\n**Output Format**\nSingle integer."
    return "Kth Largest Element", desc, inp, str(ans)

def gen_lru_cache():
    capacity = random.randint(2, 3)
    ops = random.randint(6, 10)
    
    inp_lines = [str(capacity), str(ops)]
    ans = []
    cache = {}
    order = []
    
    for _ in range(ops):
        if random.choice(["PUT", "GET"]) == "PUT":
            k = random.randint(1, 5)
            v = random.randint(10, 99)
            inp_lines.append(f"PUT {k} {v}")
            if k in cache:
                order.remove(k)
            elif len(cache) >= capacity:
                del cache[order.pop(0)]
            cache[k] = v
            order.append(k)
        else:
            k = random.randint(1, 5)
            inp_lines.append(f"GET {k}")
            if k in cache:
                order.remove(k)
                order.append(k)
                ans.append(str(cache[k]))
            else:
                ans.append("-1")
                
    desc = "Simulate an LRU Cache. Implement PUT key value and GET key. Print the result of every GET query.\n\n**Input Format**\nFirst line: Capacity\nSecond line: Number of Operations Q\nNext Q lines: 'PUT key value' or 'GET key'\n\n**Output Format**\nOne line for each GET operation result."
    return "LRU Cache Simulation", desc, "\n".join(inp_lines), "\n".join(ans)

def gen_cpu_fcfs():
    n = random.randint(3, 5)
    processes = []
    for i in range(n):
        processes.append({
            "pid": i+1,
            "arr": random.randint(0, 5),
            "burst": random.randint(2, 8)
        })
    processes.sort(key=lambda x: x["arr"])
    
    inp = f"{n}\n" + "\n".join(f"{p['arr']} {p['burst']}" for p in processes)
    
    time = 0
    total_waiting = 0
    for p in processes:
        if time < p["arr"]:
            time = p["arr"]
        wait = time - p["arr"]
        total_waiting += wait
        time += p["burst"]
        
    avg_wait = total_waiting / n
    ans = f"{avg_wait:.2f}"
    
    desc = "Simulate FCFS CPU Scheduling. Given arrival times and burst times of N processes, calculate the average waiting time (rounded to 2 decimal places).\n\n**Input Format**\nFirst line: N\nNext N lines: arrival_time burst_time\n\n**Output Format**\nFloat representing average waiting time."
    return "FCFS CPU Scheduling", desc, inp, ans

def gen_page_replacement():
    frames = random.randint(3, 4)
    ref_len = random.randint(10, 15)
    ref = [random.randint(0, 5) for _ in range(ref_len)]
    
    inp = f"{frames}\n{ref_len}\n" + " ".join(map(str, ref))
    
    faults = 0
    memory = []
    for page in ref:
        if page not in memory:
            faults += 1
            if len(memory) >= frames:
                memory.pop(0)
            memory.append(page)
            
    desc = "Simulate FIFO Page Replacement Algorithm. Given number of frames and a reference string, count total page faults.\n\n**Input Format**\nFirst line: Number of Frames\nSecond line: N (Length of reference string)\nThird line: N integers\n\n**Output Format**\nTotal page faults."
    return "FIFO Page Replacement", desc, inp, str(faults)


GENERATORS = [
    gen_subsets, gen_permutations, gen_combination_sum, gen_min_path_sum,
    gen_coin_change, gen_lis, gen_number_islands, gen_flood_fill,
    gen_max_area_island, gen_top_k_frequent, gen_sort_chars_freq, gen_kth_largest,
    gen_lru_cache, gen_cpu_fcfs, gen_page_replacement
]

weeks_data = {}
# Weeks 1-9, and 11
week_numbers = list(range(1, 11))

for week in week_numbers:
    week_qs = []
    for gen in GENERATORS:
        test_cases = []
        for i in range(3):
            title, desc, inp, ans = gen()
            test_cases.append({
                "in": inp,
                "out": ans,
                "is_sample": (i == 0)
            })
            
        week_qs.append({
            "title": f"Adv: {title} (W{week})",
            "desc": desc,
            "diff": "medium",
            "test_cases": test_cases
        })
    weeks_data[str(week)] = week_qs

os.makedirs("data", exist_ok=True)

# Build canonical format
canonical = {
    "category": "advanced_placement_training",
    "modules": []
}

# Weeks 1-9, and 10
week_numbers = list(range(1, 11))

for week in week_numbers:
    week_qs = []
    for gen in GENERATORS:
        # We need 3 test cases with distinct (input, expected) pairs
        test_cases = []
        attempts = 0
        while len(test_cases) < 3 and attempts < 20:
            title, desc, inp, ans = gen()
            if not inp.strip() and not ans.strip():
                attempts += 1
                continue
            pair = (inp, ans)
            if any(pair == (tc["input"], tc["expected_output"]) for tc in test_cases):
                attempts += 1
                continue
            test_cases.append({
                "input": inp,
                "expected_output": ans,
                "is_sample": len(test_cases) == 0
            })
            attempts += 1
        # Fallback if we couldn't get 3 distinct (unlikely)
        if len(test_cases) < 3:
            while len(test_cases) < 3:
                title, desc, inp, ans = gen()
                test_cases.append({
                    "input": inp,
                    "expected_output": ans,
                    "is_sample": len(test_cases) == 0
                })
            
        week_qs.append({
            "question_id": f"ADV-W{week:02d}-Q{len(week_qs)+1:02d}",
            "title": f"Adv: {title} (W{week})",
            "topic": (
                "Revision of Programming Fundamentals, Complexity Analysis" if week == 1 else
                "Sliding Window, Prefix Sum, String manipulation problems" if week == 2 else
                "Sudoku, Maze, N-Queens, Divide & Conquer" if week == 3 else
                "Reverse linked list, Stack using arrays, Queue implementation" if week == 4 else
                "Tree traversals, BST operations" if week == 5 else
                "DFS/BFS Traversals, Priority Queues" if week == 6 else
                "Hash Maps, Frequency counting, Collision handling" if week == 7 else
                "Merge Sort, Quick Sort, DP basics, Knapsack" if week == 8 else
                "Classes, Objects, Inheritance, Polymorphism, LLD" if week == 9 else
                "Process vs Thread, CPU Scheduling, Synchronization, Deadlocks"
            ),
            "level": week,
            "level_range": "Easy" if week <= 3 else "Medium" if week <= 7 else "Hard",
            "difficulty": "medium",
            "description": desc,
            "starter_code": "#include <stdio.h>\n\nint main(void)\n{\n    /* Read from stdin. Do not print prompts unless required. */\n    return 0;\n}",
            "time_limit": 2.0,
            "memory_limit_kb": 128000,
            "max_score": 1,
            "is_active": True,
            "is_mandatory": True,
            "allow_multiple_languages": True,
            "test_cases": test_cases
        })
    canonical["modules"].append({
        "module": (
            "Week 1: Complexity Analysis" if week == 1 else
            "Week 2: Arrays and Strings" if week == 2 else
            "Week 3: Recursion & Backtracking" if week == 3 else
            "Week 4: Linked Lists & Stacks" if week == 4 else
            "Week 5: Trees and BST" if week == 5 else
            "Week 6: Graphs and Heaps" if week == 6 else
            "Week 7: Hashing and Searching" if week == 7 else
            "Week 8: Sorting, Greedy & DP" if week == 8 else
            "Week 9: OOP & Design Patterns" if week == 9 else
            "Week 10: OS Fundamentals"
        ),
        "module_order": week,
        "questions": week_qs
    })

with open("data/advanced_placement_training_questions.json", "w") as f:
    json.dump(canonical, f, indent=2)

print("Generated Advanced Placement Training Data!")
