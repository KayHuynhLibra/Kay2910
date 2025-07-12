# 🎯  - C++ IMPLEMENTATIONS

## 📚 **Tổng quan**
Tất cả các thuật toán trong nhóm  được implement bằng C++.

---

## 🎯 **LEVEL 1**
```cpp
#include <iostream>
#include <vector>
using namespace std;

void reverse_array(vector<int>& arr) {
    int left = 0, right = arr.size() - 1;
    while (left < right) {
        swap(arr[left], arr[right]);
        left++;
        right--;
    }
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    cout << "Original: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    
    reverse_array(arr);
    
    cout << "Reversed: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 2**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void rotate_array(vector<int>& arr, int k) {
    int n = arr.size();
    k = k % n;
    
    // Reverse entire array
    reverse(arr.begin(), arr.end());
    // Reverse first k elements
    reverse(arr.begin(), arr.begin() + k);
    // Reverse remaining elements
    reverse(arr.begin() + k, arr.end());
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    
    cout << "Original: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    
    rotate_array(arr, k);
    
    cout << "Rotated by " << k << ": ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 3**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> shift_array(vector<int>& arr) {
    // Implementation for SHIFT ARRAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = shift_array(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 4**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> find_max/min(vector<int>& arr) {
    // Implementation for FIND MAX/MIN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = find_max/min(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 5**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> remove_duplicates(vector<int>& arr) {
    // Implementation for REMOVE DUPLICATES
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = remove_duplicates(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 6**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> merge_sorted_arrays(vector<int>& arr) {
    // Implementation for MERGE SORTED ARRAYS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = merge_sorted_arrays(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 7**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> intersect_arrays(vector<int>& arr) {
    // Implementation for INTERSECT ARRAYS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = intersect_arrays(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 8**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> union_arrays(vector<int>& arr) {
    // Implementation for UNION ARRAYS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = union_arrays(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 9**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> split_array(vector<int>& arr) {
    // Implementation for SPLIT ARRAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = split_array(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 10**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> flatten_array(vector<int>& arr) {
    // Implementation for FLATTEN ARRAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = flatten_array(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 11**
```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void rotate_array(vector<int>& arr, int k) {
    int n = arr.size();
    k = k % n;
    
    // Reverse entire array
    reverse(arr.begin(), arr.end());
    // Reverse first k elements
    reverse(arr.begin(), arr.begin() + k);
    // Reverse remaining elements
    reverse(arr.begin() + k, arr.end());
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;
    
    cout << "Original: ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    
    rotate_array(arr, k);
    
    cout << "Rotated by " << k << ": ";
    for (int num : arr) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 12**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> spiral_traversal(vector<int>& arr) {
    // Implementation for SPIRAL TRAVERSAL
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = spiral_traversal(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 13**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> diagonal_traversal(vector<int>& arr) {
    // Implementation for DIAGONAL TRAVERSAL
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = diagonal_traversal(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 14**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_partitioning(vector<int>& arr) {
    // Implementation for ARRAY PARTITIONING
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_partitioning(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 15**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_compression(vector<int>& arr) {
    // Implementation for ARRAY COMPRESSION
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_compression(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 16**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_difference(vector<int>& arr) {
    // Implementation for ARRAY DIFFERENCE
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_difference(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 17**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_permutation(vector<int>& arr) {
    // Implementation for ARRAY PERMUTATION
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_permutation(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 18**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_combinations(vector<int>& arr) {
    // Implementation for ARRAY COMBINATIONS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_combinations(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 19**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_validation(vector<int>& arr) {
    // Implementation for ARRAY VALIDATION
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_validation(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

## 🎯 **LEVEL 20**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_optimization(vector<int>& arr) {
    // Implementation for ARRAY OPTIMIZATION
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_optimization(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}

```

---

