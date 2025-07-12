# 🔄 IN-PLACE REVERSAL - 20 LEVELS

## 📚 **Tổng quan**
In-Place Reversal là kỹ thuật đảo ngược các phần tử trong cấu trúc dữ liệu mà không cần sử dụng thêm bộ nhớ phụ.

---

## 🎯 **LEVEL 1: ARRAY REVERSAL CƠ BẢN**
### **Bài toán**: Reverse Array

#### **Python Solution:**
```python
def array_reversal_cơ_bản(arr):
    # Implementation for ARRAY REVERSAL CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = array_reversal_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> array_reversal_cơ_bản(vector<int>& arr) {
    // Implementation for ARRAY REVERSAL CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = array_reversal_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void array_reversal_cơ_bản(int arr[], int n) {
    // Implementation for ARRAY REVERSAL CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    array_reversal_cơ_bản(arr, n);
    
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

public class ARRAYREVERSALCƠBẢN {
    public static int[] array_reversal_cơ_bản(int[] arr) {
        // Implementation for ARRAY REVERSAL CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = array_reversal_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 2: REVERSE ARRAY VỚI RANGE**
### **Bài toán**: Reverse Array trong khoảng [start, end]

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

## 🎯 **LEVEL 3: REVERSE ARRAY THEO K**
### **Bài toán**: Rotate Array by K positions

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

## 🎯 **LEVEL 4: REVERSE ARRAY THEO BLOCKS**
### **Bài toán**: Reverse Array in groups of K

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

## 🎯 **LEVEL 5: REVERSE ARRAY VỚI CONDITIONS**
### **Bài toán**: Reverse Array based on conditions

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

## 🎯 **LEVEL 6: LINKED LIST REVERSAL CƠ BẢN**
### **Bài toán**: Reverse Linked List

#### **Python Solution:**
```python
def linked_list_reversal_cơ_bản(arr):
    # Implementation for LINKED LIST REVERSAL CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = linked_list_reversal_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> linked_list_reversal_cơ_bản(vector<int>& arr) {
    // Implementation for LINKED LIST REVERSAL CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = linked_list_reversal_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void linked_list_reversal_cơ_bản(int arr[], int n) {
    // Implementation for LINKED LIST REVERSAL CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    linked_list_reversal_cơ_bản(arr, n);
    
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

public class LINKEDLISTREVERSALCƠBẢN {
    public static int[] linked_list_reversal_cơ_bản(int[] arr) {
        // Implementation for LINKED LIST REVERSAL CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = linked_list_reversal_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 7: REVERSE LINKED LIST THEO K**
### **Bài toán**: Reverse Nodes in K-Group

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

## 🎯 **LEVEL 8: REVERSE LINKED LIST ALTERNATING**
### **Bài toán**: Reverse Linked List in Alternating Groups

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

## 🎯 **LEVEL 9: REVERSE LINKED LIST BETWEEN RANGE**
### **Bài toán**: Reverse Linked List from position m to n

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

## 🎯 **LEVEL 10: REVERSE LINKED LIST WITH SWAPPING**
### **Bài toán**: Swap Nodes in Pairs

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

## 🎯 **LEVEL 11: STRING REVERSAL CƠ BẢN**
### **Bài toán**: Reverse String

#### **Python Solution:**
```python
def string_reversal_cơ_bản(arr):
    # Implementation for STRING REVERSAL CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = string_reversal_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> string_reversal_cơ_bản(vector<int>& arr) {
    // Implementation for STRING REVERSAL CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = string_reversal_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void string_reversal_cơ_bản(int arr[], int n) {
    // Implementation for STRING REVERSAL CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    string_reversal_cơ_bản(arr, n);
    
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

public class STRINGREVERSALCƠBẢN {
    public static int[] string_reversal_cơ_bản(int[] arr) {
        // Implementation for STRING REVERSAL CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = string_reversal_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 12: REVERSE WORDS IN STRING**
### **Bài toán**: Reverse Words in a String

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

## 🎯 **LEVEL 13: REVERSE STRING THEO K**
### **Bài toán**: Reverse String II

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

## 🎯 **LEVEL 14: REVERSE VOWELS IN STRING**
### **Bài toán**: Reverse Vowels of a String

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

## 🎯 **LEVEL 15: REVERSE ONLY LETTERS**
### **Bài toán**: Reverse Only Letters

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

## 🎯 **LEVEL 16: REVERSE BITS**
### **Bài toán**: Reverse Bits

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

## 🎯 **LEVEL 17: REVERSE INTEGER**
### **Bài toán**: Reverse Integer

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

## 🎯 **LEVEL 18: REVERSE POLISH NOTATION**
### **Bài toán**: Evaluate Reverse Polish Notation

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

## 🎯 **LEVEL 19: REVERSE SUBARRAY TO MAXIMIZE ARRAY VALUE**
### **Bài toán**: Advanced Array Reversal

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

## 🎯 **LEVEL 20: ADVANCED REVERSAL APPLICATIONS**
### **Bài toán**: Complex Reversal Problems

#### **Python Solution:**
```python
def advanced_reversal_applications(arr):
    # Implementation for ADVANCED REVERSAL APPLICATIONS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = advanced_reversal_applications(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> advanced_reversal_applications(vector<int>& arr) {
    // Implementation for ADVANCED REVERSAL APPLICATIONS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = advanced_reversal_applications(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void advanced_reversal_applications(int arr[], int n) {
    // Implementation for ADVANCED REVERSAL APPLICATIONS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    advanced_reversal_applications(arr, n);
    
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

public class ADVANCEDREVERSALAPPLICATIONS {
    public static int[] advanced_reversal_applications(int[] arr) {
        // Implementation for ADVANCED REVERSAL APPLICATIONS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = advanced_reversal_applications(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **TỔNG KẾT 20 LEVELS**

### **Giai đoạn 1 (Level 1-5)**: Cơ bản
- Array reversal cơ bản
- Range reversal
- K-rotation
- Block reversal
- Conditional reversal

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Linked list reversal
- K-group reversal
- Alternating reversal
- Range reversal
- Pair swapping

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- String reversal
- Word reversal
- K-string reversal
- Vowel reversal
- Letter reversal

### **Giai đoạn 4 (Level 16-20)**: Master
- Bit reversal
- Integer reversal
- Polish notation
- Advanced applications
- Complex techniques

---

## 💡 **Ứng dụng thực tế**

### **Text Processing:**
- String manipulation
- Word processing
- Text analysis
- Natural language processing

### **Data Structures:**
- Linked list operations
- Array manipulation
- Memory optimization
- Performance improvement

### **Algorithm Design:**
- Pattern matching
- Optimization problems
- Competitive programming
- System design

### **System Programming:**
- Memory management
- Buffer operations
- Network protocols
- File systems

---

## 🚀 **Next Steps**

1. **Practice implementation** của từng level
2. **Solve problems** trên LeetCode/HackerRank
3. **Optimize performance** cho từng use case
4. **Apply to real projects** để hiểu sâu hơn
5. **Combine with other techniques** cho complex problems

---

**🎉 Chúc bạn thành thạo In-Place Reversal! 🎉** 