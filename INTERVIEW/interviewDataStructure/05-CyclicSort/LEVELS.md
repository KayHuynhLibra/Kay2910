# 🔄 CYCLIC SORT - 20 LEVELS

## 📚 **Tổng quan**
Cyclic Sort là kỹ thuật sắp xếp mảng với O(n) time complexity khi các phần tử nằm trong range [1, n] hoặc [0, n-1].

---

## 🎯 **LEVEL 1: CYCLIC SORT CƠ BẢN**
### **Bài toán**: Cyclic Sort cho mảng [1, n]

#### **Python Solution:**
```python
def cyclic_sort_cơ_bản(arr):
    # Implementation for CYCLIC SORT CƠ BẢN
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = cyclic_sort_cơ_bản(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> cyclic_sort_cơ_bản(vector<int>& arr) {
    // Implementation for CYCLIC SORT CƠ BẢN
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = cyclic_sort_cơ_bản(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void cyclic_sort_cơ_bản(int arr[], int n) {
    // Implementation for CYCLIC SORT CƠ BẢN
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cyclic_sort_cơ_bản(arr, n);
    
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

public class CYCLICSORTCƠBẢN {
    public static int[] cyclic_sort_cơ_bản(int[] arr) {
        // Implementation for CYCLIC SORT CƠ BẢN
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = cyclic_sort_cơ_bản(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 2: CYCLIC SORT VỚI RANGE [0, N-1]**
### **Bài toán**: Cyclic Sort cho mảng [0, n-1]

#### **Python Solution:**
```python
def cyclic_sort_với_range_[0,_n-1](arr):
    # Implementation for CYCLIC SORT VỚI RANGE [0, N-1]
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = cyclic_sort_với_range_[0,_n-1](arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> cyclic_sort_với_range_[0,_n-1](vector<int>& arr) {
    // Implementation for CYCLIC SORT VỚI RANGE [0, N-1]
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = cyclic_sort_với_range_[0,_n-1](arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void cyclic_sort_với_range_[0,_n-1](int arr[], int n) {
    // Implementation for CYCLIC SORT VỚI RANGE [0, N-1]
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    cyclic_sort_với_range_[0,_n-1](arr, n);
    
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

public class CYCLICSORTVỚIRANGE[0,N-1] {
    public static int[] cyclic_sort_với_range_[0,_n-1](int[] arr) {
        // Implementation for CYCLIC SORT VỚI RANGE [0, N-1]
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = cyclic_sort_với_range_[0,_n-1](arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 3: TÌM SỐ BỊ THIẾU**
### **Bài toán**: Find Missing Number

#### **Python Solution:**
```python
def tìm_số_bị_thiếu(arr):
    # Implementation for TÌM SỐ BỊ THIẾU
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_số_bị_thiếu(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_số_bị_thiếu(vector<int>& arr) {
    // Implementation for TÌM SỐ BỊ THIẾU
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_số_bị_thiếu(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_số_bị_thiếu(int arr[], int n) {
    // Implementation for TÌM SỐ BỊ THIẾU
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_số_bị_thiếu(arr, n);
    
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

public class TÌMSỐBỊTHIẾU {
    public static int[] tìm_số_bị_thiếu(int[] arr) {
        // Implementation for TÌM SỐ BỊ THIẾU
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_số_bị_thiếu(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 4: TÌM TẤT CẢ SỐ BỊ THIẾU**
### **Bài toán**: Find All Missing Numbers

#### **Python Solution:**
```python
def tìm_tất_cả_số_bị_thiếu(arr):
    # Implementation for TÌM TẤT CẢ SỐ BỊ THIẾU
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_tất_cả_số_bị_thiếu(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_tất_cả_số_bị_thiếu(vector<int>& arr) {
    // Implementation for TÌM TẤT CẢ SỐ BỊ THIẾU
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_tất_cả_số_bị_thiếu(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_tất_cả_số_bị_thiếu(int arr[], int n) {
    // Implementation for TÌM TẤT CẢ SỐ BỊ THIẾU
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_tất_cả_số_bị_thiếu(arr, n);
    
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

public class TÌMTẤTCẢSỐBỊTHIẾU {
    public static int[] tìm_tất_cả_số_bị_thiếu(int[] arr) {
        // Implementation for TÌM TẤT CẢ SỐ BỊ THIẾU
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_tất_cả_số_bị_thiếu(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 5: TÌM SỐ TRÙNG LẶP**
### **Bài toán**: Find Duplicate Number

#### **Python Solution:**
```python
def tìm_số_trùng_lặp(arr):
    # Implementation for TÌM SỐ TRÙNG LẶP
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_số_trùng_lặp(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_số_trùng_lặp(vector<int>& arr) {
    // Implementation for TÌM SỐ TRÙNG LẶP
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_số_trùng_lặp(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_số_trùng_lặp(int arr[], int n) {
    // Implementation for TÌM SỐ TRÙNG LẶP
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_số_trùng_lặp(arr, n);
    
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

public class TÌMSỐTRÙNGLẶP {
    public static int[] tìm_số_trùng_lặp(int[] arr) {
        // Implementation for TÌM SỐ TRÙNG LẶP
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_số_trùng_lặp(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 6: TÌM TẤT CẢ SỐ TRÙNG LẶP**
### **Bài toán**: Find All Duplicates

#### **Python Solution:**
```python
def tìm_tất_cả_số_trùng_lặp(arr):
    # Implementation for TÌM TẤT CẢ SỐ TRÙNG LẶP
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_tất_cả_số_trùng_lặp(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_tất_cả_số_trùng_lặp(vector<int>& arr) {
    // Implementation for TÌM TẤT CẢ SỐ TRÙNG LẶP
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_tất_cả_số_trùng_lặp(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_tất_cả_số_trùng_lặp(int arr[], int n) {
    // Implementation for TÌM TẤT CẢ SỐ TRÙNG LẶP
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_tất_cả_số_trùng_lặp(arr, n);
    
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

public class TÌMTẤTCẢSỐTRÙNGLẶP {
    public static int[] tìm_tất_cả_số_trùng_lặp(int[] arr) {
        // Implementation for TÌM TẤT CẢ SỐ TRÙNG LẶP
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_tất_cả_số_trùng_lặp(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 7: TÌM SỐ BỊ THIẾU VÀ TRÙNG LẶP**
### **Bài toán**: Set Mismatch

#### **Python Solution:**
```python
def tìm_số_bị_thiếu_và_trùng_lặp(arr):
    # Implementation for TÌM SỐ BỊ THIẾU VÀ TRÙNG LẶP
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_số_bị_thiếu_và_trùng_lặp(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_số_bị_thiếu_và_trùng_lặp(vector<int>& arr) {
    // Implementation for TÌM SỐ BỊ THIẾU VÀ TRÙNG LẶP
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_số_bị_thiếu_và_trùng_lặp(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_số_bị_thiếu_và_trùng_lặp(int arr[], int n) {
    // Implementation for TÌM SỐ BỊ THIẾU VÀ TRÙNG LẶP
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_số_bị_thiếu_và_trùng_lặp(arr, n);
    
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

public class TÌMSỐBỊTHIẾUVÀTRÙNGLẶP {
    public static int[] tìm_số_bị_thiếu_và_trùng_lặp(int[] arr) {
        // Implementation for TÌM SỐ BỊ THIẾU VÀ TRÙNG LẶP
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_số_bị_thiếu_và_trùng_lặp(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 8: TÌM PHẦN TỬ ĐẦU TIÊN BỊ THIẾU**
### **Bài toán**: First Missing Positive

#### **Python Solution:**
```python
def tìm_phần_tử_đầu_tiên_bị_thiếu(arr):
    # Implementation for TÌM PHẦN TỬ ĐẦU TIÊN BỊ THIẾU
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_phần_tử_đầu_tiên_bị_thiếu(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_phần_tử_đầu_tiên_bị_thiếu(vector<int>& arr) {
    // Implementation for TÌM PHẦN TỬ ĐẦU TIÊN BỊ THIẾU
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_phần_tử_đầu_tiên_bị_thiếu(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_phần_tử_đầu_tiên_bị_thiếu(int arr[], int n) {
    // Implementation for TÌM PHẦN TỬ ĐẦU TIÊN BỊ THIẾU
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_phần_tử_đầu_tiên_bị_thiếu(arr, n);
    
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

public class TÌMPHẦNTỬĐẦUTIÊNBỊTHIẾU {
    public static int[] tìm_phần_tử_đầu_tiên_bị_thiếu(int[] arr) {
        // Implementation for TÌM PHẦN TỬ ĐẦU TIÊN BỊ THIẾU
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_phần_tử_đầu_tiên_bị_thiếu(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 9: TÌM K PHẦN TỬ NHỎ NHẤT**
### **Bài toán**: Kth Missing Positive Number

#### **Python Solution:**
```python
def tìm_k_phần_tử_nhỏ_nhất(arr):
    # Implementation for TÌM K PHẦN TỬ NHỎ NHẤT
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_k_phần_tử_nhỏ_nhất(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_k_phần_tử_nhỏ_nhất(vector<int>& arr) {
    // Implementation for TÌM K PHẦN TỬ NHỎ NHẤT
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_k_phần_tử_nhỏ_nhất(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_k_phần_tử_nhỏ_nhất(int arr[], int n) {
    // Implementation for TÌM K PHẦN TỬ NHỎ NHẤT
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_k_phần_tử_nhỏ_nhất(arr, n);
    
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

public class TÌMKPHẦNTỬNHỎNHẤT {
    public static int[] tìm_k_phần_tử_nhỏ_nhất(int[] arr) {
        // Implementation for TÌM K PHẦN TỬ NHỎ NHẤT
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_k_phần_tử_nhỏ_nhất(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 10: TÌM PHẦN TỬ TRONG MẢNG XOAY**
### **Bài toán**: Find Element in Rotated Sorted Array

#### **Python Solution:**
```python
def tìm_phần_tử_trong_mảng_xoay(arr):
    # Implementation for TÌM PHẦN TỬ TRONG MẢNG XOAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_phần_tử_trong_mảng_xoay(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_phần_tử_trong_mảng_xoay(vector<int>& arr) {
    // Implementation for TÌM PHẦN TỬ TRONG MẢNG XOAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_phần_tử_trong_mảng_xoay(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_phần_tử_trong_mảng_xoay(int arr[], int n) {
    // Implementation for TÌM PHẦN TỬ TRONG MẢNG XOAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_phần_tử_trong_mảng_xoay(arr, n);
    
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

public class TÌMPHẦNTỬTRONGMẢNGXOAY {
    public static int[] tìm_phần_tử_trong_mảng_xoay(int[] arr) {
        // Implementation for TÌM PHẦN TỬ TRONG MẢNG XOAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_phần_tử_trong_mảng_xoay(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 11: TÌM MINIMUM TRONG MẢNG XOAY**
### **Bài toán**: Find Minimum in Rotated Sorted Array

#### **Python Solution:**
```python
def tìm_minimum_trong_mảng_xoay(arr):
    # Implementation for TÌM MINIMUM TRONG MẢNG XOAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_minimum_trong_mảng_xoay(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_minimum_trong_mảng_xoay(vector<int>& arr) {
    // Implementation for TÌM MINIMUM TRONG MẢNG XOAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_minimum_trong_mảng_xoay(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_minimum_trong_mảng_xoay(int arr[], int n) {
    // Implementation for TÌM MINIMUM TRONG MẢNG XOAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_minimum_trong_mảng_xoay(arr, n);
    
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

public class TÌMMINIMUMTRONGMẢNGXOAY {
    public static int[] tìm_minimum_trong_mảng_xoay(int[] arr) {
        // Implementation for TÌM MINIMUM TRONG MẢNG XOAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_minimum_trong_mảng_xoay(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 12: TÌM PEAK ELEMENT**
### **Bài toán**: Find Peak Element

#### **Python Solution:**
```python
def tìm_peak_element(arr):
    # Implementation for TÌM PEAK ELEMENT
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_peak_element(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_peak_element(vector<int>& arr) {
    // Implementation for TÌM PEAK ELEMENT
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_peak_element(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_peak_element(int arr[], int n) {
    // Implementation for TÌM PEAK ELEMENT
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_peak_element(arr, n);
    
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

public class TÌMPEAKELEMENT {
    public static int[] tìm_peak_element(int[] arr) {
        // Implementation for TÌM PEAK ELEMENT
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_peak_element(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 13: TÌM ELEMENT TRONG 2D ARRAY**
### **Bài toán**: Search in 2D Matrix

#### **Python Solution:**
```python
def tìm_element_trong_2d_array(arr):
    # Implementation for TÌM ELEMENT TRONG 2D ARRAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_element_trong_2d_array(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_element_trong_2d_array(vector<int>& arr) {
    // Implementation for TÌM ELEMENT TRONG 2D ARRAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_element_trong_2d_array(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_element_trong_2d_array(int arr[], int n) {
    // Implementation for TÌM ELEMENT TRONG 2D ARRAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_element_trong_2d_array(arr, n);
    
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

public class TÌMELEMENTTRONG2DARRAY {
    public static int[] tìm_element_trong_2d_array(int[] arr) {
        // Implementation for TÌM ELEMENT TRONG 2D ARRAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_element_trong_2d_array(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 14: TÌM RANGE TRONG SORTED ARRAY**
### **Bài toán**: Find First and Last Position

#### **Python Solution:**
```python
def tìm_range_trong_sorted_array(arr):
    # Implementation for TÌM RANGE TRONG SORTED ARRAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_range_trong_sorted_array(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_range_trong_sorted_array(vector<int>& arr) {
    // Implementation for TÌM RANGE TRONG SORTED ARRAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_range_trong_sorted_array(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_range_trong_sorted_array(int arr[], int n) {
    // Implementation for TÌM RANGE TRONG SORTED ARRAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_range_trong_sorted_array(arr, n);
    
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

public class TÌMRANGETRONGSORTEDARRAY {
    public static int[] tìm_range_trong_sorted_array(int[] arr) {
        // Implementation for TÌM RANGE TRONG SORTED ARRAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_range_trong_sorted_array(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 15: TÌM KTH ELEMENT TRONG 2 SORTED ARRAYS**
### **Bài toán**: Median of Two Sorted Arrays

#### **Python Solution:**
```python
def tìm_kth_element_trong_2_sorted_arrays(arr):
    # Implementation for TÌM KTH ELEMENT TRONG 2 SORTED ARRAYS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_kth_element_trong_2_sorted_arrays(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_kth_element_trong_2_sorted_arrays(vector<int>& arr) {
    // Implementation for TÌM KTH ELEMENT TRONG 2 SORTED ARRAYS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_kth_element_trong_2_sorted_arrays(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_kth_element_trong_2_sorted_arrays(int arr[], int n) {
    // Implementation for TÌM KTH ELEMENT TRONG 2 SORTED ARRAYS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_kth_element_trong_2_sorted_arrays(arr, n);
    
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

public class TÌMKTHELEMENTTRONG2SORTEDARRAYS {
    public static int[] tìm_kth_element_trong_2_sorted_arrays(int[] arr) {
        // Implementation for TÌM KTH ELEMENT TRONG 2 SORTED ARRAYS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_kth_element_trong_2_sorted_arrays(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 16: TÌM ELEMENT TRONG INFINITE ARRAY**
### **Bài toán**: Search in Infinite Sorted Array

#### **Python Solution:**
```python
def tìm_element_trong_infinite_array(arr):
    # Implementation for TÌM ELEMENT TRONG INFINITE ARRAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_element_trong_infinite_array(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_element_trong_infinite_array(vector<int>& arr) {
    // Implementation for TÌM ELEMENT TRONG INFINITE ARRAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_element_trong_infinite_array(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_element_trong_infinite_array(int arr[], int n) {
    // Implementation for TÌM ELEMENT TRONG INFINITE ARRAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_element_trong_infinite_array(arr, n);
    
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

public class TÌMELEMENTTRONGINFINITEARRAY {
    public static int[] tìm_element_trong_infinite_array(int[] arr) {
        // Implementation for TÌM ELEMENT TRONG INFINITE ARRAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_element_trong_infinite_array(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 17: TÌM ELEMENT TRONG BITONIC ARRAY**
### **Bài toán**: Search in Bitonic Array

#### **Python Solution:**
```python
def tìm_element_trong_bitonic_array(arr):
    # Implementation for TÌM ELEMENT TRONG BITONIC ARRAY
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_element_trong_bitonic_array(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_element_trong_bitonic_array(vector<int>& arr) {
    // Implementation for TÌM ELEMENT TRONG BITONIC ARRAY
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_element_trong_bitonic_array(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_element_trong_bitonic_array(int arr[], int n) {
    // Implementation for TÌM ELEMENT TRONG BITONIC ARRAY
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_element_trong_bitonic_array(arr, n);
    
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

public class TÌMELEMENTTRONGBITONICARRAY {
    public static int[] tìm_element_trong_bitonic_array(int[] arr) {
        // Implementation for TÌM ELEMENT TRONG BITONIC ARRAY
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_element_trong_bitonic_array(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 18: TÌM ELEMENT TRONG ARRAY VỚI DUPLICATES**
### **Bài toán**: Search in Rotated Array with Duplicates

#### **Python Solution:**
```python
def tìm_element_trong_array_với_duplicates(arr):
    # Implementation for TÌM ELEMENT TRONG ARRAY VỚI DUPLICATES
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_element_trong_array_với_duplicates(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_element_trong_array_với_duplicates(vector<int>& arr) {
    // Implementation for TÌM ELEMENT TRONG ARRAY VỚI DUPLICATES
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_element_trong_array_với_duplicates(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_element_trong_array_với_duplicates(int arr[], int n) {
    // Implementation for TÌM ELEMENT TRONG ARRAY VỚI DUPLICATES
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_element_trong_array_với_duplicates(arr, n);
    
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

public class TÌMELEMENTTRONGARRAYVỚIDUPLICATES {
    public static int[] tìm_element_trong_array_với_duplicates(int[] arr) {
        // Implementation for TÌM ELEMENT TRONG ARRAY VỚI DUPLICATES
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_element_trong_array_với_duplicates(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 19: TÌM ELEMENT TRONG ARRAY VỚI ABSENT ELEMENTS**
### **Bài toán**: Search in Array with Absent Elements

#### **Python Solution:**
```python
def tìm_element_trong_array_với_absent_elements(arr):
    # Implementation for TÌM ELEMENT TRONG ARRAY VỚI ABSENT ELEMENTS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = tìm_element_trong_array_với_absent_elements(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> tìm_element_trong_array_với_absent_elements(vector<int>& arr) {
    // Implementation for TÌM ELEMENT TRONG ARRAY VỚI ABSENT ELEMENTS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = tìm_element_trong_array_với_absent_elements(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void tìm_element_trong_array_với_absent_elements(int arr[], int n) {
    // Implementation for TÌM ELEMENT TRONG ARRAY VỚI ABSENT ELEMENTS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    tìm_element_trong_array_với_absent_elements(arr, n);
    
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

public class TÌMELEMENTTRONGARRAYVỚIABSENTELEMENTS {
    public static int[] tìm_element_trong_array_với_absent_elements(int[] arr) {
        // Implementation for TÌM ELEMENT TRONG ARRAY VỚI ABSENT ELEMENTS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = tìm_element_trong_array_với_absent_elements(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **LEVEL 20: ADVANCED CYCLIC SORT APPLICATIONS**
### **Bài toán**: Complex Array Manipulation

#### **Python Solution:**
```python
def advanced_cyclic_sort_applications(arr):
    # Implementation for ADVANCED CYCLIC SORT APPLICATIONS
    n = len(arr)
    # Add your logic here
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
result = advanced_cyclic_sort_applications(arr)
print(f"Result: {result}")
```

#### **C++ Solution:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> advanced_cyclic_sort_applications(vector<int>& arr) {
    // Implementation for ADVANCED CYCLIC SORT APPLICATIONS
    int n = arr.size();
    // Add your logic here
    return arr;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<int> result = advanced_cyclic_sort_applications(arr);
    
    cout << "Result: ";
    for (int num : result) cout << num << " ";
    cout << endl;
    return 0;
}
```

#### **C Solution:**
```c
#include <stdio.h>

void advanced_cyclic_sort_applications(int arr[], int n) {
    // Implementation for ADVANCED CYCLIC SORT APPLICATIONS
    // Add your logic here
}

int main() {
    int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    advanced_cyclic_sort_applications(arr, n);
    
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

public class ADVANCEDCYCLICSORTAPPLICATIONS {
    public static int[] advanced_cyclic_sort_applications(int[] arr) {
        // Implementation for ADVANCED CYCLIC SORT APPLICATIONS
        int n = arr.length;
        // Add your logic here
        return arr;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int[] result = advanced_cyclic_sort_applications(arr);
        
        System.out.println("Result: " + Arrays.toString(result));
    }
}
```

---

---

## 🎯 **TỔNG KẾT 20 LEVELS**

### **Giai đoạn 1 (Level 1-5)**: Cơ bản
- Cyclic sort cơ bản
- Missing numbers
- Duplicate numbers
- Basic array manipulation

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Multiple missing/duplicates
- First missing positive
- Kth missing positive
- Rotated array search

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Peak finding
- 2D array search
- Range search
- Median of arrays

### **Giai đoạn 4 (Level 16-20)**: Master
- Infinite array search
- Bitonic array search
- Duplicate handling
- Advanced applications

---

## 💡 **Ứng dụng thực tế**

### **Database Systems:**
- Index management
- Record sorting
- Duplicate detection

### **File Systems:**
- File organization
- Directory sorting
- Duplicate file detection

### **Memory Management:**
- Memory allocation
- Garbage collection
- Memory compaction

### **Network Routing:**
- Packet sorting
- Route optimization
- Load balancing

---

## 🚀 **Next Steps**

1. **Practice implementation** của từng level
2. **Solve problems** trên LeetCode/HackerRank
3. **Optimize performance** cho từng use case
4. **Apply to real projects** để hiểu sâu hơn
5. **Combine with other techniques** cho complex problems

---

**🎉 Chúc bạn thành thạo Cyclic Sort! 🎉** 