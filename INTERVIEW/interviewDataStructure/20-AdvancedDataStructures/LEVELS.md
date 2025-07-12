# 🏗️ ADVANCED DATA STRUCTURES - 20 LEVELS

## 📚 **Tổng quan**
Advanced Data Structures là các cấu trúc dữ liệu phức tạp được sử dụng để giải quyết các bài toán nâng cao trong lập trình thi đấu và phỏng vấn.

---

## 🎯 **LEVEL 1: TRIE CƠ BẢN**
### **Bài toán**: Implement Trie (Prefix Tree)

#### **Python Solution:**
```python
def trie_cơ_bản(arr):
    # Implementation for TRIE CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = trie_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> trie_cơ_bản(vector<int>& arr) {
    // Implementation for TRIE CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = trie_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void trie_cơ_bản(int arr[], int n) {
    // Implementation for TRIE CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    trie_cơ_bản(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class TRIECƠBẢN {
    public static int[] trie_cơ_bản(int[] arr) {
        // Implementation for TRIE CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = trie_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 2: TRIE VỚI COUNT**
### **Bài toán**: Trie với đếm số từ có prefix

#### **Python Solution:**
```python
def trie_với_count(arr):
    # Implementation for TRIE VỚI COUNT
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = trie_với_count(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> trie_với_count(vector<int>& arr) {
    // Implementation for TRIE VỚI COUNT
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = trie_với_count(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void trie_với_count(int arr[], int n) {
    // Implementation for TRIE VỚI COUNT
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    trie_với_count(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class TRIEVỚICOUNT {
    public static int[] trie_với_count(int[] arr) {
        // Implementation for TRIE VỚI COUNT
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = trie_với_count(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 3: TRIE VỚI WILDCARD**
### **Bài toán**: Word Search II với wildcard

#### **Python Solution:**
```python
def trie_với_wildcard(arr):
    # Implementation for TRIE VỚI WILDCARD
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = trie_với_wildcard(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> trie_với_wildcard(vector<int>& arr) {
    // Implementation for TRIE VỚI WILDCARD
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = trie_với_wildcard(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void trie_với_wildcard(int arr[], int n) {
    // Implementation for TRIE VỚI WILDCARD
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    trie_với_wildcard(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class TRIEVỚIWILDCARD {
    public static int[] trie_với_wildcard(int[] arr) {
        // Implementation for TRIE VỚI WILDCARD
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = trie_với_wildcard(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 4: SEGMENT TREE CƠ BẢN**
### **Bài toán**: Range Sum Query - Mutable

#### **Python Solution:**
```python
def segment_tree_cơ_bản(arr):
    # Implementation for SEGMENT TREE CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = segment_tree_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> segment_tree_cơ_bản(vector<int>& arr) {
    // Implementation for SEGMENT TREE CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = segment_tree_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void segment_tree_cơ_bản(int arr[], int n) {
    // Implementation for SEGMENT TREE CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    segment_tree_cơ_bản(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class SEGMENTTREECƠBẢN {
    public static int[] segment_tree_cơ_bản(int[] arr) {
        // Implementation for SEGMENT TREE CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = segment_tree_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 5: SEGMENT TREE VỚI MIN/MAX**
### **Bài toán**: Range Minimum Query

#### **Python Solution:**
```python
def segment_tree_với_min/max(arr):
    # Implementation for SEGMENT TREE VỚI MIN/MAX
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = segment_tree_với_min/max(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> segment_tree_với_min/max(vector<int>& arr) {
    // Implementation for SEGMENT TREE VỚI MIN/MAX
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = segment_tree_với_min/max(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void segment_tree_với_min/max(int arr[], int n) {
    // Implementation for SEGMENT TREE VỚI MIN/MAX
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    segment_tree_với_min/max(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class SEGMENTTREEVỚIMIN/MAX {
    public static int[] segment_tree_với_min/max(int[] arr) {
        // Implementation for SEGMENT TREE VỚI MIN/MAX
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = segment_tree_với_min/max(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 6: FENWICK TREE CƠ BẢN**
### **Bài toán**: Binary Indexed Tree cho prefix sum

#### **Python Solution:**
```python
def fenwick_tree_cơ_bản(arr):
    # Implementation for FENWICK TREE CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = fenwick_tree_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> fenwick_tree_cơ_bản(vector<int>& arr) {
    // Implementation for FENWICK TREE CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = fenwick_tree_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void fenwick_tree_cơ_bản(int arr[], int n) {
    // Implementation for FENWICK TREE CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    fenwick_tree_cơ_bản(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class FENWICKTREECƠBẢN {
    public static int[] fenwick_tree_cơ_bản(int[] arr) {
        // Implementation for FENWICK TREE CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = fenwick_tree_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 7: FENWICK TREE VỚI RANGE UPDATE**
### **Bài toán**: Range Update và Point Query

#### **Python Solution:**
```python
def fenwick_tree_với_range_update(arr):
    # Implementation for FENWICK TREE VỚI RANGE UPDATE
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = fenwick_tree_với_range_update(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> fenwick_tree_với_range_update(vector<int>& arr) {
    // Implementation for FENWICK TREE VỚI RANGE UPDATE
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = fenwick_tree_với_range_update(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void fenwick_tree_với_range_update(int arr[], int n) {
    // Implementation for FENWICK TREE VỚI RANGE UPDATE
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    fenwick_tree_với_range_update(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class FENWICKTREEVỚIRANGEUPDATE {
    public static int[] fenwick_tree_với_range_update(int[] arr) {
        // Implementation for FENWICK TREE VỚI RANGE UPDATE
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = fenwick_tree_với_range_update(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 8: DISJOINT SET CƠ BẢN**
### **Bài toán**: Union Find với path compression

#### **Python Solution:**
```python
def disjoint_set_cơ_bản(arr):
    # Implementation for DISJOINT SET CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = disjoint_set_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> disjoint_set_cơ_bản(vector<int>& arr) {
    // Implementation for DISJOINT SET CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = disjoint_set_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void disjoint_set_cơ_bản(int arr[], int n) {
    // Implementation for DISJOINT SET CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    disjoint_set_cơ_bản(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class DISJOINTSETCƠBẢN {
    public static int[] disjoint_set_cơ_bản(int[] arr) {
        // Implementation for DISJOINT SET CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = disjoint_set_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 9: DISJOINT SET VỚI SIZE**
### **Bài toán**: Union Find với tracking size

#### **Python Solution:**
```python
def disjoint_set_với_size(arr):
    # Implementation for DISJOINT SET VỚI SIZE
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = disjoint_set_với_size(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> disjoint_set_với_size(vector<int>& arr) {
    // Implementation for DISJOINT SET VỚI SIZE
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = disjoint_set_với_size(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void disjoint_set_với_size(int arr[], int n) {
    // Implementation for DISJOINT SET VỚI SIZE
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    disjoint_set_với_size(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class DISJOINTSETVỚISIZE {
    public static int[] disjoint_set_với_size(int[] arr) {
        // Implementation for DISJOINT SET VỚI SIZE
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = disjoint_set_với_size(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 10: SEGMENT TREE VỚI LAZY PROPAGATION**
### **Bài toán**: Range Update và Range Query

#### **Python Solution:**
```python
def segment_tree_với_lazy_propagation(arr):
    # Implementation for SEGMENT TREE VỚI LAZY PROPAGATION
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = segment_tree_với_lazy_propagation(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> segment_tree_với_lazy_propagation(vector<int>& arr) {
    // Implementation for SEGMENT TREE VỚI LAZY PROPAGATION
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = segment_tree_với_lazy_propagation(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void segment_tree_với_lazy_propagation(int arr[], int n) {
    // Implementation for SEGMENT TREE VỚI LAZY PROPAGATION
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    segment_tree_với_lazy_propagation(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class SEGMENTTREEVỚILAZYPROPAGATION {
    public static int[] segment_tree_với_lazy_propagation(int[] arr) {
        // Implementation for SEGMENT TREE VỚI LAZY PROPAGATION
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = segment_tree_với_lazy_propagation(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 11: TRIE VỚI XOR**
### **Bài toán**: Maximum XOR of Two Numbers in an Array

#### **Python Solution:**
```python
def trie_với_xor(arr):
    # Implementation for TRIE VỚI XOR
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = trie_với_xor(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> trie_với_xor(vector<int>& arr) {
    // Implementation for TRIE VỚI XOR
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = trie_với_xor(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void trie_với_xor(int arr[], int n) {
    // Implementation for TRIE VỚI XOR
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    trie_với_xor(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class TRIEVỚIXOR {
    public static int[] trie_với_xor(int[] arr) {
        // Implementation for TRIE VỚI XOR
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = trie_với_xor(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 12: SEGMENT TREE VỚI GCD**
### **Bài toán**: Range GCD Query

#### **Python Solution:**
```python
def segment_tree_với_gcd(arr):
    # Implementation for SEGMENT TREE VỚI GCD
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = segment_tree_với_gcd(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> segment_tree_với_gcd(vector<int>& arr) {
    // Implementation for SEGMENT TREE VỚI GCD
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = segment_tree_với_gcd(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void segment_tree_với_gcd(int arr[], int n) {
    // Implementation for SEGMENT TREE VỚI GCD
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    segment_tree_với_gcd(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class SEGMENTTREEVỚIGCD {
    public static int[] segment_tree_với_gcd(int[] arr) {
        // Implementation for SEGMENT TREE VỚI GCD
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = segment_tree_với_gcd(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 13: FENWICK TREE VỚI 2D**
### **Bài toán**: 2D Binary Indexed Tree

#### **Python Solution:**
```python
def fenwick_tree_với_2d(arr):
    # Implementation for FENWICK TREE VỚI 2D
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = fenwick_tree_với_2d(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> fenwick_tree_với_2d(vector<int>& arr) {
    // Implementation for FENWICK TREE VỚI 2D
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = fenwick_tree_với_2d(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void fenwick_tree_với_2d(int arr[], int n) {
    // Implementation for FENWICK TREE VỚI 2D
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    fenwick_tree_với_2d(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class FENWICKTREEVỚI2D {
    public static int[] fenwick_tree_với_2d(int[] arr) {
        // Implementation for FENWICK TREE VỚI 2D
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = fenwick_tree_với_2d(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 14: DISJOINT SET VỚI ROLLBACK**
### **Bài toán**: Union Find với khả năng rollback

#### **Python Solution:**
```python
def disjoint_set_với_rollback(arr):
    # Implementation for DISJOINT SET VỚI ROLLBACK
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = disjoint_set_với_rollback(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> disjoint_set_với_rollback(vector<int>& arr) {
    // Implementation for DISJOINT SET VỚI ROLLBACK
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = disjoint_set_với_rollback(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void disjoint_set_với_rollback(int arr[], int n) {
    // Implementation for DISJOINT SET VỚI ROLLBACK
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    disjoint_set_với_rollback(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class DISJOINTSETVỚIROLLBACK {
    public static int[] disjoint_set_với_rollback(int[] arr) {
        // Implementation for DISJOINT SET VỚI ROLLBACK
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = disjoint_set_với_rollback(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 15: SEGMENT TREE VỚI PERSISTENT**
### **Bài toán**: Persistent Segment Tree

#### **Python Solution:**
```python
def segment_tree_với_persistent(arr):
    # Implementation for SEGMENT TREE VỚI PERSISTENT
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = segment_tree_với_persistent(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> segment_tree_với_persistent(vector<int>& arr) {
    // Implementation for SEGMENT TREE VỚI PERSISTENT
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = segment_tree_với_persistent(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void segment_tree_với_persistent(int arr[], int n) {
    // Implementation for SEGMENT TREE VỚI PERSISTENT
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    segment_tree_với_persistent(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class SEGMENTTREEVỚIPERSISTENT {
    public static int[] segment_tree_với_persistent(int[] arr) {
        // Implementation for SEGMENT TREE VỚI PERSISTENT
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = segment_tree_với_persistent(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 16: TRIE VỚI COMPRESSED**
### **Bài toán**: Compressed Trie (Radix Tree)

#### **Python Solution:**
```python
def trie_với_compressed(arr):
    # Implementation for TRIE VỚI COMPRESSED
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = trie_với_compressed(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> trie_với_compressed(vector<int>& arr) {
    // Implementation for TRIE VỚI COMPRESSED
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = trie_với_compressed(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void trie_với_compressed(int arr[], int n) {
    // Implementation for TRIE VỚI COMPRESSED
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    trie_với_compressed(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class TRIEVỚICOMPRESSED {
    public static int[] trie_với_compressed(int[] arr) {
        // Implementation for TRIE VỚI COMPRESSED
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = trie_với_compressed(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 17: SEGMENT TREE VỚI MERGE SORT**
### **Bài toán**: Merge Sort Tree cho range queries

#### **Python Solution:**
```python
def segment_tree_với_merge_sort(arr):
    # Implementation for SEGMENT TREE VỚI MERGE SORT
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = segment_tree_với_merge_sort(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> segment_tree_với_merge_sort(vector<int>& arr) {
    // Implementation for SEGMENT TREE VỚI MERGE SORT
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = segment_tree_với_merge_sort(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void segment_tree_với_merge_sort(int arr[], int n) {
    // Implementation for SEGMENT TREE VỚI MERGE SORT
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    segment_tree_với_merge_sort(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class SEGMENTTREEVỚIMERGESORT {
    public static int[] segment_tree_với_merge_sort(int[] arr) {
        // Implementation for SEGMENT TREE VỚI MERGE SORT
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = segment_tree_với_merge_sort(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 18: FENWICK TREE VỚI RANGE MIN/MAX**
### **Bài toán**: Range Minimum/Maximum với Fenwick Tree

#### **Python Solution:**
```python
def fenwick_tree_với_range_min/max(arr):
    # Implementation for FENWICK TREE VỚI RANGE MIN/MAX
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = fenwick_tree_với_range_min/max(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> fenwick_tree_với_range_min/max(vector<int>& arr) {
    // Implementation for FENWICK TREE VỚI RANGE MIN/MAX
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = fenwick_tree_với_range_min/max(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void fenwick_tree_với_range_min/max(int arr[], int n) {
    // Implementation for FENWICK TREE VỚI RANGE MIN/MAX
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    fenwick_tree_với_range_min/max(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class FENWICKTREEVỚIRANGEMIN/MAX {
    public static int[] fenwick_tree_với_range_min/max(int[] arr) {
        // Implementation for FENWICK TREE VỚI RANGE MIN/MAX
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = fenwick_tree_với_range_min/max(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 19: DISJOINT SET VỚI WEIGHTED**
### **Bài toán**: Weighted Union Find

#### **Python Solution:**
```python
def disjoint_set_với_weighted(arr):
    # Implementation for DISJOINT SET VỚI WEIGHTED
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = disjoint_set_với_weighted(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> disjoint_set_với_weighted(vector<int>& arr) {
    // Implementation for DISJOINT SET VỚI WEIGHTED
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = disjoint_set_với_weighted(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void disjoint_set_với_weighted(int arr[], int n) {
    // Implementation for DISJOINT SET VỚI WEIGHTED
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    disjoint_set_với_weighted(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class DISJOINTSETVỚIWEIGHTED {
    public static int[] disjoint_set_với_weighted(int[] arr) {
        // Implementation for DISJOINT SET VỚI WEIGHTED
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = disjoint_set_với_weighted(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 20: ADVANCED HYBRID STRUCTURES**
### **Bài toán**: Combination của nhiều cấu trúc dữ liệu

#### **Python Solution:**
```python
def advanced_hybrid_structures(arr):
    # Implementation for ADVANCED HYBRID STRUCTURES
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = advanced_hybrid_structures(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> advanced_hybrid_structures(vector<int>& arr) {
    // Implementation for ADVANCED HYBRID STRUCTURES
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = advanced_hybrid_structures(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void advanced_hybrid_structures(int arr[], int n) {
    // Implementation for ADVANCED HYBRID STRUCTURES
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    advanced_hybrid_structures(arr, n);
    
    printf("Result: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

#### **Java Solution:**
```java
import java.util.Arrays;

public class ADVANCEDHYBRIDSTRUCTURES {
    public static int[] advanced_hybrid_structures(int[] arr) {
        // Implementation for ADVANCED HYBRID STRUCTURES
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = advanced_hybrid_structures(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **TỔNG KẾT 20 LEVELS**

### **Giai đoạn 1 (Level 1-5)**: Cơ bản
- Trie cơ bản và nâng cao
- Segment Tree cơ bản
- Fenwick Tree cơ bản
- Disjoint Set cơ bản

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Lazy propagation
- Range operations
- Size tracking
- Advanced queries

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- XOR operations
- GCD queries
- 2D structures
- Persistent structures

### **Giai đoạn 4 (Level 16-20)**: Master
- Compressed structures
- Merge sort trees
- Weighted operations
- Hybrid combinations

---

## 💡 **Ứng dụng thực tế**

### **Trie:**
- Autocomplete systems
- Spell checkers
- IP routing tables
- DNA sequence analysis

### **Segment Tree:**
- Range queries in databases
- Image processing
- Geographic information systems
- Financial data analysis

### **Fenwick Tree:**
- Cumulative frequency counting
- Inversion counting
- Range sum queries
- Dynamic programming optimization

### **Disjoint Set:**
- Network connectivity
- Image segmentation
- Kruskal's algorithm
- Cycle detection in graphs

---

## 🚀 **Next Steps**

1. **Practice implementation** của từng cấu trúc
2. **Solve problems** trên LeetCode/HackerRank
3. **Optimize performance** cho từng use case
4. **Combine structures** cho complex problems
5. **Apply to real projects** để hiểu sâu hơn

---

**🎉 Chúc bạn thành thạo Advanced Data Structures! 🎉** 