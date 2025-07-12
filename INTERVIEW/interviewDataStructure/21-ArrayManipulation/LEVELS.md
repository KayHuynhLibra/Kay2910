# 🎯 ARRAY MANIPULATION - 20 LEVELS

## 📚 **Tổng quan**
Array Manipulation là kỹ thuật thao tác và biến đổi mảng một cách hiệu quả, bao gồm các phép toán cơ bản đến nâng cao.

---

## 🎯 **LEVEL 1: REVERSE ARRAY**
### **Bài toán**: Đảo ngược mảng

#### **Python Solution:**
```python
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
print("Original:", arr)
reverse_array(arr)
print("Reversed:", arr)  # [5, 4, 3, 2, 1]
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void reverse_array(int arr[], int n) {
    int left = 0, right = n - 1;
    while (left < right) {
        int temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    reverse_array(arr, n);
    
    printf("Reversed: ");
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

public class ReverseArray {
    public static void reverseArray(int[] arr) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        System.out.println("Original: " + Arrays.toString(arr));
        
        reverseArray(arr);
        
        System.out.println("Reversed: " + Arrays.toString(arr));
    }
}
```

---

---

## 🎯 **LEVEL 2: ROTATE ARRAY**
### **Bài toán**: Xoay mảng theo K vị trí

#### **Python Solution:**
```python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    
    # Reverse entire array
    arr.reverse()
    # Reverse first k elements
    arr[:k] = arr[:k][::-1]
    # Reverse remaining elements
    arr[k:] = arr[k:][::-1]
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original:", arr)
result = rotate_array(arr.copy(), k)
print(f"Rotated by {k}:", result)  # [5, 6, 7, 1, 2, 3, 4]
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void reverse(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void rotate_array(int arr[], int n, int k) {
    k = k % n;
    
    // Reverse entire array
    reverse(arr, 0, n - 1);
    // Reverse first k elements
    reverse(arr, 0, k - 1);
    // Reverse remaining elements
    reverse(arr, k, n - 1);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;
    
    printf("Original: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    rotate_array(arr, n, k);
    
    printf("Rotated by %d: ", k);
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

public class RotateArray {
    public static void rotateArray(int[] arr, int k) {
        int n = arr.length;
        k = k % n;
        
        // Reverse entire array
        reverse(arr, 0, n - 1);
        // Reverse first k elements
        reverse(arr, 0, k - 1);
        // Reverse remaining elements
        reverse(arr, k, n - 1);
    }
    
    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;
        
        System.out.println("Original: " + Arrays.toString(arr));
        
        rotateArray(arr, k);
        
        System.out.println("Rotated by " + k + ": " + Arrays.toString(arr));
    }
}
```

---

---

## 🎯 **LEVEL 3: SHIFT ARRAY**
### **Bài toán**: Dịch mảng trái/phải

#### **Python Solution:**
```python
def shift_array(arr):
    # Implementation for SHIFT ARRAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = shift_array(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void shift_array(int arr[], int n) {
    // Implementation for SHIFT ARRAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    shift_array(arr, n);
    
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

public class SHIFTARRAY {
    public static int[] shift_array(int[] arr) {
        // Implementation for SHIFT ARRAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = shift_array(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 4: FIND MAX/MIN**
### **Bài toán**: Tìm phần tử lớn nhất/nhỏ nhất

#### **Python Solution:**
```python
def find_max/min(arr):
    # Implementation for FIND MAX/MIN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = find_max/min(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void find_max/min(int arr[], int n) {
    // Implementation for FIND MAX/MIN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    find_max/min(arr, n);
    
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

public class FINDMAX/MIN {
    public static int[] find_max/min(int[] arr) {
        // Implementation for FIND MAX/MIN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = find_max/min(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 5: REMOVE DUPLICATES**
### **Bài toán**: Loại bỏ phần tử trùng lặp

#### **Python Solution:**
```python
def remove_duplicates(arr):
    # Implementation for REMOVE DUPLICATES
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = remove_duplicates(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void remove_duplicates(int arr[], int n) {
    // Implementation for REMOVE DUPLICATES
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    remove_duplicates(arr, n);
    
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

public class REMOVEDUPLICATES {
    public static int[] remove_duplicates(int[] arr) {
        // Implementation for REMOVE DUPLICATES
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = remove_duplicates(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 6: MERGE SORTED ARRAYS**
### **Bài toán**: Gộp hai mảng đã sắp xếp

#### **Python Solution:**
```python
def merge_sorted_arrays(arr):
    # Implementation for MERGE SORTED ARRAYS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = merge_sorted_arrays(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void merge_sorted_arrays(int arr[], int n) {
    // Implementation for MERGE SORTED ARRAYS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    merge_sorted_arrays(arr, n);
    
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

public class MERGESORTEDARRAYS {
    public static int[] merge_sorted_arrays(int[] arr) {
        // Implementation for MERGE SORTED ARRAYS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = merge_sorted_arrays(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 7: INTERSECT ARRAYS**
### **Bài toán**: Tìm giao của hai mảng

#### **Python Solution:**
```python
def intersect_arrays(arr):
    # Implementation for INTERSECT ARRAYS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = intersect_arrays(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void intersect_arrays(int arr[], int n) {
    // Implementation for INTERSECT ARRAYS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    intersect_arrays(arr, n);
    
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

public class INTERSECTARRAYS {
    public static int[] intersect_arrays(int[] arr) {
        // Implementation for INTERSECT ARRAYS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = intersect_arrays(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 8: UNION ARRAYS**
### **Bài toán**: Tìm hợp của hai mảng

#### **Python Solution:**
```python
def union_arrays(arr):
    # Implementation for UNION ARRAYS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = union_arrays(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void union_arrays(int arr[], int n) {
    // Implementation for UNION ARRAYS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    union_arrays(arr, n);
    
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

public class UNIONARRAYS {
    public static int[] union_arrays(int[] arr) {
        // Implementation for UNION ARRAYS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = union_arrays(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 9: SPLIT ARRAY**
### **Bài toán**: Chia mảng theo điều kiện

#### **Python Solution:**
```python
def split_array(arr):
    # Implementation for SPLIT ARRAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = split_array(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void split_array(int arr[], int n) {
    // Implementation for SPLIT ARRAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    split_array(arr, n);
    
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

public class SPLITARRAY {
    public static int[] split_array(int[] arr) {
        // Implementation for SPLIT ARRAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = split_array(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 10: FLATTEN ARRAY**
### **Bài toán**: Làm phẳng mảng đa chiều

#### **Python Solution:**
```python
def flatten_array(arr):
    # Implementation for FLATTEN ARRAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = flatten_array(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void flatten_array(int arr[], int n) {
    // Implementation for FLATTEN ARRAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    flatten_array(arr, n);
    
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

public class FLATTENARRAY {
    public static int[] flatten_array(int[] arr) {
        // Implementation for FLATTEN ARRAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = flatten_array(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 11: ROTATE MATRIX**
### **Bài toán**: Xoay ma trận 90 độ

#### **Python Solution:**
```python
def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    
    # Reverse entire array
    arr.reverse()
    # Reverse first k elements
    arr[:k] = arr[:k][::-1]
    # Reverse remaining elements
    arr[k:] = arr[k:][::-1]
    
    return arr

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original:", arr)
result = rotate_array(arr.copy(), k)
print(f"Rotated by {k}:", result)  # [5, 6, 7, 1, 2, 3, 4]
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void reverse(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

void rotate_array(int arr[], int n, int k) {
    k = k % n;
    
    // Reverse entire array
    reverse(arr, 0, n - 1);
    // Reverse first k elements
    reverse(arr, 0, k - 1);
    // Reverse remaining elements
    reverse(arr, k, n - 1);
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;
    
    printf("Original: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    
    rotate_array(arr, n, k);
    
    printf("Rotated by %d: ", k);
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

public class RotateArray {
    public static void rotateArray(int[] arr, int k) {
        int n = arr.length;
        k = k % n;
        
        // Reverse entire array
        reverse(arr, 0, n - 1);
        // Reverse first k elements
        reverse(arr, 0, k - 1);
        // Reverse remaining elements
        reverse(arr, k, n - 1);
    }
    
    private static void reverse(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7};
        int k = 3;
        
        System.out.println("Original: " + Arrays.toString(arr));
        
        rotateArray(arr, k);
        
        System.out.println("Rotated by " + k + ": " + Arrays.toString(arr));
    }
}
```

---

---

## 🎯 **LEVEL 12: SPIRAL TRAVERSAL**
### **Bài toán**: Duyệt ma trận theo hình xoắn ốc

#### **Python Solution:**
```python
def spiral_traversal(arr):
    # Implementation for SPIRAL TRAVERSAL
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = spiral_traversal(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void spiral_traversal(int arr[], int n) {
    // Implementation for SPIRAL TRAVERSAL
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    spiral_traversal(arr, n);
    
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

public class SPIRALTRAVERSAL {
    public static int[] spiral_traversal(int[] arr) {
        // Implementation for SPIRAL TRAVERSAL
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = spiral_traversal(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 13: DIAGONAL TRAVERSAL**
### **Bài toán**: Duyệt ma trận theo đường chéo

#### **Python Solution:**
```python
def diagonal_traversal(arr):
    # Implementation for DIAGONAL TRAVERSAL
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = diagonal_traversal(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void diagonal_traversal(int arr[], int n) {
    // Implementation for DIAGONAL TRAVERSAL
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    diagonal_traversal(arr, n);
    
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

public class DIAGONALTRAVERSAL {
    public static int[] diagonal_traversal(int[] arr) {
        // Implementation for DIAGONAL TRAVERSAL
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = diagonal_traversal(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 14: ARRAY PARTITIONING**
### **Bài toán**: Phân vùng mảng theo điều kiện

#### **Python Solution:**
```python
def array_partitioning(arr):
    # Implementation for ARRAY PARTITIONING
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_partitioning(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void array_partitioning(int arr[], int n) {
    // Implementation for ARRAY PARTITIONING
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_partitioning(arr, n);
    
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

public class ARRAYPARTITIONING {
    public static int[] array_partitioning(int[] arr) {
        // Implementation for ARRAY PARTITIONING
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_partitioning(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 15: ARRAY COMPRESSION**
### **Bài toán**: Nén mảng

#### **Python Solution:**
```python
def array_compression(arr):
    # Implementation for ARRAY COMPRESSION
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_compression(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void array_compression(int arr[], int n) {
    // Implementation for ARRAY COMPRESSION
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_compression(arr, n);
    
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

public class ARRAYCOMPRESSION {
    public static int[] array_compression(int[] arr) {
        // Implementation for ARRAY COMPRESSION
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_compression(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 16: ARRAY DIFFERENCE**
### **Bài toán**: Tìm hiệu của hai mảng

#### **Python Solution:**
```python
def array_difference(arr):
    # Implementation for ARRAY DIFFERENCE
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_difference(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void array_difference(int arr[], int n) {
    // Implementation for ARRAY DIFFERENCE
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_difference(arr, n);
    
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

public class ARRAYDIFFERENCE {
    public static int[] array_difference(int[] arr) {
        // Implementation for ARRAY DIFFERENCE
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_difference(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 17: ARRAY PERMUTATION**
### **Bài toán**: Tạo hoán vị của mảng

#### **Python Solution:**
```python
def array_permutation(arr):
    # Implementation for ARRAY PERMUTATION
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_permutation(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void array_permutation(int arr[], int n) {
    // Implementation for ARRAY PERMUTATION
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_permutation(arr, n);
    
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

public class ARRAYPERMUTATION {
    public static int[] array_permutation(int[] arr) {
        // Implementation for ARRAY PERMUTATION
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_permutation(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 18: ARRAY COMBINATIONS**
### **Bài toán**: Tạo tổ hợp của mảng

#### **Python Solution:**
```python
def array_combinations(arr):
    # Implementation for ARRAY COMBINATIONS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_combinations(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void array_combinations(int arr[], int n) {
    // Implementation for ARRAY COMBINATIONS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_combinations(arr, n);
    
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

public class ARRAYCOMBINATIONS {
    public static int[] array_combinations(int[] arr) {
        // Implementation for ARRAY COMBINATIONS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_combinations(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 19: ARRAY VALIDATION**
### **Bài toán**: Kiểm tra tính hợp lệ của mảng

#### **Python Solution:**
```python
def array_validation(arr):
    # Implementation for ARRAY VALIDATION
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_validation(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void array_validation(int arr[], int n) {
    // Implementation for ARRAY VALIDATION
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_validation(arr, n);
    
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

public class ARRAYVALIDATION {
    public static int[] array_validation(int[] arr) {
        // Implementation for ARRAY VALIDATION
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_validation(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 20: ARRAY OPTIMIZATION**
### **Bài toán**: Tối ưu hóa thao tác mảng

#### **Python Solution:**
```python
def array_optimization(arr):
    # Implementation for ARRAY OPTIMIZATION
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_optimization(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
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

#### **C Solution:**
```c
#include <stdio.h>

void array_optimization(int arr[], int n) {
    // Implementation for ARRAY OPTIMIZATION
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_optimization(arr, n);
    
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

public class ARRAYOPTIMIZATION {
    public static int[] array_optimization(int[] arr) {
        // Implementation for ARRAY OPTIMIZATION
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_optimization(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **TỔNG KẾT 20 LEVELS**

### **Giai đoạn 1 (Level 1-5)**: Cơ bản
- Reverse, rotate, shift arrays
- Find max/min elements
- Remove duplicates

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Merge, intersect, union arrays
- Split arrays by conditions
- Flatten nested arrays

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Matrix operations (rotate, spiral, diagonal)
- Array partitioning
- Array compression

### **Giai đoạn 4 (Level 16-20)**: Master
- Set operations (difference, symmetric difference)
- Permutations and combinations
- Array validation and optimization

---

## 💡 **Ứng dụng thực tế**

### **Data Processing:**
- Image processing
- Signal processing
- Data transformation
- Array manipulation

### **Algorithm Design:**
- Sorting algorithms
- Search algorithms
- Dynamic programming
- Graph algorithms

### **System Design:**
- Database operations
- Cache management
- Memory optimization
- Performance tuning

### **Competitive Programming:**
- Array problems
- Matrix problems
- Optimization problems
- Advanced algorithms

---

## 🚀 **Next Steps**

1. **Practice implementation** của từng level
2. **Solve problems** trên LeetCode/HackerRank
3. **Optimize performance** cho từng use case
4. **Apply to real projects** để hiểu sâu hơn
5. **Combine with other techniques** cho complex problems

---

**🎉 Chúc bạn thành thạo Array Manipulation! 🎉**
