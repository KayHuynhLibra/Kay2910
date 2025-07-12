# 🎯  - C IMPLEMENTATIONS

## 📚 **Tổng quan**
Tất cả các thuật toán trong nhóm  được implement bằng C.

---

## 🎯 **LEVEL 1**
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

---

## 🎯 **LEVEL 2**
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

---

## 🎯 **LEVEL 3**
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

---

## 🎯 **LEVEL 4**
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

---

## 🎯 **LEVEL 5**
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

---

## 🎯 **LEVEL 6**
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

---

## 🎯 **LEVEL 7**
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

---

## 🎯 **LEVEL 8**
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

---

## 🎯 **LEVEL 9**
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

---

## 🎯 **LEVEL 10**
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

---

## 🎯 **LEVEL 11**
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

---

## 🎯 **LEVEL 12**
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

---

## 🎯 **LEVEL 13**
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

---

## 🎯 **LEVEL 14**
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

---

## 🎯 **LEVEL 15**
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

---

## 🎯 **LEVEL 16**
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

---

## 🎯 **LEVEL 17**
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

---

## 🎯 **LEVEL 18**
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

---

## 🎯 **LEVEL 19**
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

---

## 🎯 **LEVEL 20**
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

---

