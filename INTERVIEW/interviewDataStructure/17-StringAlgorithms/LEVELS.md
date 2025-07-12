# STRING ALGORITHMS - 20 LEVELS TỪ CƠ BẢN ĐẾN NÂNG CAO

## 🎯 Tổng quan
20 level này được thiết kế để bạn học String Algorithms từ cơ bản đến nâng cao.

---

## 📚 **LEVEL 1: Hiểu cơ bản về String**
**Mục tiêu**: Hiểu khái niệm và thao tác cơ bản

### Bài toán: Reverse String
```python
def reverse_string(s):
    """
    Đảo ngược string
    """
    return s[::-1]

def reverse_string_inplace(s):
    """
    Đảo ngược string tại chỗ
    """
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
```

**Độ khó**: ⭐  
**Thời gian**: O(n)  
**Không gian**: O(1) cho in-place

---

## 📚 **LEVEL 2: String Matching**
**Mục tiêu**: Tìm pattern trong string

### Bài toán: String Matching
```python
def naive_string_matching(text, pattern):
    """
    Tìm pattern trong text với thuật toán naive
    """
    n, m = len(text), len(pattern)
    positions = []
    
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            positions.append(i)
    
    return positions
```

**Độ khó**: ⭐⭐  
**Thời gian**: O((n - m + 1) * m)  
**Không gian**: O(1)

---

## 📚 **LEVEL 3: KMP Algorithm**
**Mục tiêu**: Tìm pattern với KMP

### Bài toán: KMP Algorithm
```python
def kmp_search(text, pattern):
    """
    Tìm pattern với KMP algorithm
    """
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    lps = compute_lps(pattern)
    i = j = 0
    positions = []
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return positions
```

**Độ khó**: ⭐⭐⭐  
**Thời gian**: O(n + m)  
**Không gian**: O(m)

---

## 📚 **LEVEL 4: Boyer-Moore Algorithm**
**Mục tiêu**: Tìm pattern với Boyer-Moore

### Bài toán: Boyer-Moore Algorithm
```python
def boyer_moore_search(text, pattern):
    """
    Tìm pattern với Boyer-Moore algorithm
    """
    def build_bad_char_table(pattern):
        table = {}
        for i in range(len(pattern) - 1):
            table[pattern[i]] = len(pattern) - 1 - i
        return table
    
    bad_char = build_bad_char_table(pattern)
    n, m = len(text), len(pattern)
    positions = []
    
    i = m - 1
    while i < n:
        j = m - 1
        k = i
        
        while j >= 0 and text[k] == pattern[j]:
            j -= 1
            k -= 1
        
        if j == -1:
            positions.append(k + 1)
            i += m
        else:
            i += bad_char.get(text[i], m)
    
    return positions
```

**Độ khó**: ⭐⭐⭐⭐  
**Thời gian**: O(n/m) trong trường hợp tốt nhất  
**Không gian**: O(k) với k là số ký tự unique

---

## 📚 **LEVEL 5: Rabin-Karp Algorithm**
**Mục tiêu**: Tìm pattern với Rabin-Karp

### Bài toán: Rabin-Karp Algorithm
```python
def rabin_karp_search(text, pattern):
    """
    Tìm pattern với Rabin-Karp algorithm
    """
    def hash_string(s, base=256, mod=101):
        hash_val = 0
        for char in s:
            hash_val = (hash_val * base + ord(char)) % mod
        return hash_val
    
    n, m = len(text), len(pattern)
    if n < m:
        return []
    
    pattern_hash = hash_string(pattern)
    text_hash = hash_string(text[:m])
    positions = []
    
    # Power for rolling hash
    power = pow(256, m - 1, 101)
    
    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                positions.append(i)
        
        if i < n - m:
            text_hash = ((text_hash - ord(text[i]) * power) * 256 + ord(text[i + m])) % 101
    
    return positions
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(n + m) trung bình  
**Không gian**: O(1)

---

## 📚 **LEVEL 6: Longest Common Substring**
**Mục tiêu**: Tìm substring chung dài nhất

### Bài toán: Longest Common Substring
```python
def longest_common_substring(s1, s2):
    """
    Tìm substring chung dài nhất
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    end_pos = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_pos = i
    
    return s1[end_pos - max_length:end_pos]
```

**Độ khó**: ⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 7: Longest Palindromic Substring**
**Mục tiêu**: Tìm substring palindrome dài nhất

### Bài toán: Longest Palindromic Substring
```python
def longest_palindromic_substring(s):
    """
    Tìm substring palindrome dài nhất
    """
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    if len(s) < 2:
        return s
    
    longest = ""
    for i in range(len(s)):
        # Odd length palindrome
        palindrome1 = expand_around_center(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
        # Even length palindrome
        palindrome2 = expand_around_center(i, i + 1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
    
    return longest
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n²)  
**Không gian**: O(1)

---

## 📚 **LEVEL 8: Suffix Array**
**Mục tiêu**: Xây dựng suffix array

### Bài toán: Suffix Array
```python
def build_suffix_array(s):
    """
    Xây dựng suffix array
    """
    n = len(s)
    suffixes = [(s[i:], i) for i in range(n)]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

def search_in_suffix_array(text, pattern, suffix_array):
    """
    Tìm pattern trong suffix array
    """
    def binary_search(pattern):
        left, right = 0, len(suffix_array) - 1
        
        while left <= right:
            mid = (left + right) // 2
            suffix = text[suffix_array[mid]:]
            
            if suffix.startswith(pattern):
                return mid
            elif suffix < pattern:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    return binary_search(pattern)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n) cho build, O(m log n) cho search  
**Không gian**: O(n)

---

## 📚 **LEVEL 9: Trie Data Structure**
**Mục tiêu**: Xây dựng và sử dụng Trie

### Bài toán: Trie Implementation
```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m) cho insert/search  
**Không gian**: O(ALPHABET_SIZE * m * n)

---

## 📚 **LEVEL 10: Aho-Corasick Algorithm**
**Mục tiêu**: Tìm nhiều patterns với Aho-Corasick

### Bài toán: Aho-Corasick Algorithm
```python
class AhoCorasickNode:
    def __init__(self):
        self.children = {}
        self.fail = None
        self.output = []

def build_aho_corasick(patterns):
    """
    Xây dựng automaton cho Aho-Corasick
    """
    root = AhoCorasickNode()
    
    # Build trie
    for pattern in patterns:
        node = root
        for char in pattern:
            if char not in node.children:
                node.children[char] = AhoCorasickNode()
            node = node.children[char]
        node.output.append(pattern)
    
    # Build failure links
    queue = []
    for char, child in root.children.items():
        child.fail = root
        queue.append(child)
    
    while queue:
        current = queue.pop(0)
        for char, child in current.children.items():
            queue.append(child)
            fail = current.fail
            while fail and char not in fail.children:
                fail = fail.fail
            child.fail = fail.children[char] if fail else root
            child.output.extend(child.fail.output)
    
    return root

def search_aho_corasick(text, patterns):
    """
    Tìm patterns với Aho-Corasick
    """
    root = build_aho_corasick(patterns)
    results = []
    node = root
    
    for i, char in enumerate(text):
        while node and char not in node.children:
            node = node.fail
        node = node.children[char] if node else root
        
        for pattern in node.output:
            results.append((i - len(pattern) + 1, pattern))
    
    return results
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n + m + k) với k là tổng độ dài patterns  
**Không gian**: O(m)

---

## 📚 **LEVEL 11: Manacher's Algorithm**
**Mục tiêu**: Tìm tất cả palindromes với Manacher

### Bài toán: Manacher's Algorithm
```python
def manacher(s):
    """
    Tìm tất cả palindromes với Manacher's algorithm
    """
    # Transform string
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    
    center = right = 0
    for i in range(n):
        if i < right:
            p[i] = min(right - i, p[2 * center - i])
        
        # Expand palindrome
        left = i - (p[i] + 1)
        right_expand = i + (p[i] + 1)
        
        while left >= 0 and right_expand < n and t[left] == t[right_expand]:
            p[i] += 1
            left -= 1
            right_expand += 1
        
        if i + p[i] > right:
            center = i
            right = i + p[i]
    
    return p
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 12: Z Algorithm**
**Mục tiêu**: Tìm Z-array với Z algorithm

### Bài toán: Z Algorithm
```python
def z_algorithm(s):
    """
    Tính Z-array với Z algorithm
    """
    n = len(s)
    z = [0] * n
    left = right = 0
    
    for i in range(1, n):
        if i > right:
            left = right = i
            while right < n and s[right - left] == s[right]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < n and s[right - left] == s[right]:
                    right += 1
                z[i] = right - left
                right -= 1
    
    return z
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 13: Suffix Automaton**
**Mục tiêu**: Xây dựng suffix automaton

### Bài toán: Suffix Automaton
```python
class SuffixAutomatonNode:
    def __init__(self):
        self.next = {}
        self.link = -1
        self.len = 0

def build_suffix_automaton(s):
    """
    Xây dựng suffix automaton
    """
    sa = [SuffixAutomatonNode()]
    last = 0
    
    for char in s:
        current = len(sa)
        sa.append(SuffixAutomatonNode())
        sa[current].len = sa[last].len + 1
        
        p = last
        while p != -1 and char not in sa[p].next:
            sa[p].next[char] = current
            p = sa[p].link
        
        if p == -1:
            sa[current].link = 0
        else:
            q = sa[p].next[char]
            if sa[p].len + 1 == sa[q].len:
                sa[current].link = q
            else:
                clone = len(sa)
                sa.append(SuffixAutomatonNode())
                sa[clone].len = sa[p].len + 1
                sa[clone].next = sa[q].next.copy()
                sa[clone].link = sa[q].link
                
                while p != -1 and sa[p].next[char] == q:
                    sa[p].next[char] = clone
                    p = sa[p].link
                
                sa[q].link = clone
                sa[current].link = clone
        
        last = current
    
    return sa
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 14: Burrows-Wheeler Transform**
**Mục tiêu**: Thực hiện Burrows-Wheeler Transform

### Bài toán: Burrows-Wheeler Transform
```python
def burrows_wheeler_transform(s):
    """
    Thực hiện Burrows-Wheeler Transform
    """
    # Add sentinel
    s = s + '$'
    n = len(s)
    
    # Generate all rotations
    rotations = []
    for i in range(n):
        rotation = s[i:] + s[:i]
        rotations.append((rotation, i))
    
    # Sort rotations
    rotations.sort()
    
    # Extract last column and original position
    last_column = ''.join(rotation[0][-1] for rotation in rotations)
    original_pos = None
    for i, (rotation, pos) in enumerate(rotations):
        if pos == 0:
            original_pos = i
            break
    
    return last_column, original_pos

def inverse_burrows_wheeler_transform(last_column, original_pos):
    """
    Inverse Burrows-Wheeler Transform
    """
    n = len(last_column)
    
    # Create first column
    first_column = sorted(last_column)
    
    # Create mapping from first to last column
    first_to_last = {}
    last_to_first = {}
    
    # Count occurrences
    first_count = {}
    last_count = {}
    
    for i, char in enumerate(first_column):
        if char not in first_count:
            first_count[char] = 0
        first_count[char] += 1
        first_to_last[i] = (char, first_count[char])
    
    for i, char in enumerate(last_column):
        if char not in last_count:
            last_count[char] = 0
        last_count[char] += 1
        last_to_first[i] = (char, last_count[char])
    
    # Reconstruct
    result = []
    pos = original_pos
    
    for _ in range(n - 1):  # Exclude sentinel
        char, count = first_to_last[pos]
        result.append(char)
        
        # Find corresponding position in last column
        for i in range(n):
            if last_to_first[i] == (char, count):
                pos = i
                break
    
    return ''.join(reversed(result))
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n)  
**Không gian**: O(n)

---

## 📚 **LEVEL 15: Lempel-Ziv Compression**
**Mục tiêu**: Thực hiện Lempel-Ziv compression

### Bài toán: Lempel-Ziv Compression
```python
def lz77_compress(text, window_size=4096, look_ahead_size=16):
    """
    LZ77 compression
    """
    compressed = []
    i = 0
    
    while i < len(text):
        # Find longest match in sliding window
        start = max(0, i - window_size)
        window = text[start:i]
        
        longest_match = 0
        longest_offset = 0
        
        for offset in range(1, len(window) + 1):
            match_len = 0
            while (i + match_len < len(text) and 
                   match_len < look_ahead_size and
                   text[i + match_len] == window[-offset + match_len]):
                match_len += 1
            
            if match_len > longest_match:
                longest_match = match_len
                longest_offset = offset
        
        if longest_match > 2:
            compressed.append((longest_offset, longest_match, text[i + longest_match]))
            i += longest_match + 1
        else:
            compressed.append((0, 0, text[i]))
            i += 1
    
    return compressed

def lz77_decompress(compressed):
    """
    LZ77 decompression
    """
    result = []
    
    for offset, length, char in compressed:
        if length > 0:
            start = len(result) - offset
            for i in range(length):
                result.append(result[start + i])
        result.append(char)
    
    return ''.join(result)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n * window_size)  
**Không gian**: O(n)

---

## 📚 **LEVEL 16: Advanced String Matching**
**Mục tiêu**: Thuật toán string matching nâng cao

### Bài toán: Advanced String Matching
```python
def advanced_string_matching(text, patterns):
    """
    Thuật toán string matching nâng cao với nhiều patterns
    """
    def build_automaton(patterns):
        # Build Aho-Corasick automaton
        root = {'children': {}, 'fail': None, 'output': []}
        
        # Build trie
        for pattern in patterns:
            node = root
            for char in pattern:
                if char not in node['children']:
                    node['children'][char] = {'children': {}, 'fail': None, 'output': []}
                node = node['children'][char]
            node['output'].append(pattern)
        
        # Build failure links
        queue = []
        for char, child in root['children'].items():
            child['fail'] = root
            queue.append(child)
        
        while queue:
            current = queue.pop(0)
            for char, child in current['children'].items():
                queue.append(child)
                fail = current['fail']
                while fail and char not in fail['children']:
                    fail = fail['fail']
                child['fail'] = fail['children'][char] if fail else root
                child['output'].extend(child['fail']['output'])
        
        return root
    
    automaton = build_automaton(patterns)
    results = []
    node = automaton
    
    for i, char in enumerate(text):
        while node and char not in node['children']:
            node = node['fail']
        node = node['children'][char] if node else automaton
        
        for pattern in node['output']:
            results.append((i - len(pattern) + 1, pattern))
    
    return results
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n + m + k)  
**Không gian**: O(m)

---

## 📚 **LEVEL 17: String Similarity Algorithms**
**Mục tiêu**: Thuật toán tính độ tương tự string

### Bài toán: String Similarity
```python
def levenshtein_distance(s1, s2):
    """
    Tính khoảng cách Levenshtein
    """
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    return dp[m][n]

def jaro_winkler_similarity(s1, s2):
    """
    Tính độ tương tự Jaro-Winkler
    """
    def jaro_similarity(s1, s2):
        if len(s1) == 0 and len(s2) == 0:
            return 1.0
        if len(s1) == 0 or len(s2) == 0:
            return 0.0
        
        match_distance = (max(len(s1), len(s2)) // 2) - 1
        if match_distance < 0:
            match_distance = 0
        
        s1_matches = [False] * len(s1)
        s2_matches = [False] * len(s2)
        
        matches = 0
        transpositions = 0
        
        for i in range(len(s1)):
            start = max(0, i - match_distance)
            end = min(i + match_distance + 1, len(s2))
            
            for j in range(start, end):
                if s2_matches[j]:
                    continue
                if s1[i] != s2[j]:
                    continue
                s1_matches[i] = True
                s2_matches[j] = True
                matches += 1
                break
        
        if matches == 0:
            return 0.0
        
        k = 0
        for i in range(len(s1)):
            if not s1_matches[i]:
                continue
            while not s2_matches[k]:
                k += 1
            if s1[i] != s2[k]:
                transpositions += 1
            k += 1
        
        return (matches / len(s1) + matches / len(s2) + 
                (matches - transpositions / 2) / matches) / 3
    
    jaro = jaro_similarity(s1, s2)
    
    if jaro < 0.7:
        return jaro
    
    prefix = 0
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix += 1
        else:
            break
    
    return jaro + 0.1 * prefix * (1 - jaro)
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n) cho Levenshtein, O(m * n) cho Jaro-Winkler  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 18: Advanced Pattern Matching**
**Mục tiêu**: Pattern matching với regex và wildcards

### Bài toán: Advanced Pattern Matching
```python
def regex_matching(s, p):
    """
    Regex matching với . và *
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2]  # 0 occurrence
                if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i - 1][j]
    
    return dp[m][n]

def wildcard_matching(s, p):
    """
    Wildcard matching với ? và *
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    dp[0][0] = True
    
    # Handle patterns like *, **, etc.
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(m * n)  
**Không gian**: O(m * n)

---

## 📚 **LEVEL 19: String Compression Algorithms**
**Mục tiêu**: Thuật toán nén string nâng cao

### Bài toán: String Compression
```python
def run_length_encoding(s):
    """
    Run-length encoding
    """
    if not s:
        return ""
    
    result = []
    count = 1
    current = s[0]
    
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            result.append(f"{count}{current}")
            current = s[i]
            count = 1
    
    result.append(f"{count}{current}")
    return ''.join(result)

def huffman_encoding(s):
    """
    Huffman encoding
    """
    from collections import Counter
    import heapq
    
    # Count frequencies
    freq = Counter(s)
    
    # Build Huffman tree
    heap = [[freq[char], char] for char in freq]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        heapq.heappush(heap, [left[0] + right[0], [left, right]])
    
    # Build codes
    codes = {}
    
    def build_codes(node, code=""):
        if isinstance(node[1], str):
            codes[node[1]] = code
        else:
            build_codes(node[1][0], code + "0")
            build_codes(node[1][1], code + "1")
    
    if heap:
        build_codes(heap[0])
    
    # Encode
    encoded = ''.join(codes[char] for char in s)
    return encoded, codes
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n log n) cho Huffman  
**Không gian**: O(n)

---

## 📚 **LEVEL 20: Master Level - Complex String Applications**
**Mục tiêu**: Ứng dụng string trong bài toán phức tạp nhất

### Bài toán: Master String Algorithm
```python
def master_string_algorithm(text, patterns, constraints):
    """
    Thuật toán string master với nhiều ràng buộc phức tạp
    """
    def build_advanced_automaton(patterns):
        # Build multi-pattern automaton with constraints
        root = {
            'children': {},
            'fail': None,
            'output': [],
            'constraints': {}
        }
        
        for pattern in patterns:
            node = root
            for i, char in enumerate(pattern):
                if char not in node['children']:
                    node['children'][char] = {
                        'children': {},
                        'fail': None,
                        'output': [],
                        'constraints': {}
                    }
                node = node['children'][char]
                
                # Add position-specific constraints
                if i in constraints:
                    node['constraints'].update(constraints[i])
            
            node['output'].append(pattern)
        
        return root
    
    def check_constraints(node, position, context):
        # Check if current position satisfies all constraints
        for constraint_type, constraint_value in node['constraints'].items():
            if constraint_type == 'min_length' and len(context) < constraint_value:
                return False
            if constraint_type == 'max_length' and len(context) > constraint_value:
                return False
            if constraint_type == 'must_contain' and constraint_value not in context:
                return False
            if constraint_type == 'must_not_contain' and constraint_value in context:
                return False
        return True
    
    automaton = build_advanced_automaton(patterns)
    results = []
    node = automaton
    context = ""
    
    for i, char in enumerate(text):
        context += char
        
        while node and char not in node['children']:
            node = node['fail']
        node = node['children'][char] if node else automaton
        
        for pattern in node['output']:
            if check_constraints(node, i, context):
                results.append({
                    'position': i - len(pattern) + 1,
                    'pattern': pattern,
                    'context': context[-len(pattern):],
                    'constraints_satisfied': node['constraints']
                })
    
    return results
```

**Độ khó**: ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐  
**Thời gian**: O(n + m + k + c) với c là số constraints  
**Không gian**: O(m + c)

---

## 🎯 **Lộ trình học tập**

### **Giai đoạn 1 (Level 1-5)**: Nền tảng
- Hiểu khái niệm string algorithms
- Thành thạo basic string matching
- Làm quen với pattern cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Advanced string matching algorithms
- Data structures cho string
- Tối ưu hóa thuật toán

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Advanced string algorithms
- Compression algorithms
- Tối ưu hóa bộ nhớ

### **Giai đoạn 4 (Level 16-20)**: Master
- Complex applications
- Multiple constraints
- Edge cases phức tạp

## 💡 **Mẹo cho từng level**

- **Level 1-5**: Tập trung vào hiểu pattern cơ bản
- **Level 6-10**: Chú ý đến việc chọn thuật toán phù hợp
- **Level 11-15**: Hiểu sâu về string theory
- **Level 16-20**: Thực hành nhiều và phân tích các trường hợp đặc biệt

## 🔥 **Common Patterns**

### **String Matching Pattern**
```python
def string_matching(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i
    return -1
```

### **Trie Pattern**
```python
def build_trie(words):
    root = {}
    for word in words:
        node = root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True
    return root
```

### **DP for Strings Pattern**
```python
def dp_string(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
``` 