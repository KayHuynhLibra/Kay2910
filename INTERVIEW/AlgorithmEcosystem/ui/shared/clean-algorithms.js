/**
 * Clean Algorithms Module
 * 
 * This module contains clean, well-documented versions of all algorithms
 * following clean code principles:
 * - Meaningful names
 * - Small functions
 * - Single responsibility
 * - Error handling
 * - Comprehensive documentation
 */

// ============================================================================
// VALIDATION UTILITIES
// ============================================================================

/**
 * Input validation utilities for algorithms
 */
class AlgorithmValidator {
    /**
     * Validates if input is a valid number array
     * @param {any} input - Input to validate
     * @returns {boolean} - True if valid number array
     */
    static isValidNumberArray(input) {
        return Array.isArray(input) && 
               input.length > 0 && 
               input.every(element => typeof element === 'number' && !isNaN(element));
    }

    /**
     * Validates if input is a valid sorted array
     * @param {any} input - Input to validate
     * @returns {boolean} - True if valid sorted array
     */
    static isValidSortedArray(input) {
        if (!this.isValidNumberArray(input)) {
            return false;
        }
        
        for (let i = 1; i < input.length; i++) {
            if (input[i] < input[i - 1]) {
                return false;
            }
        }
        return true;
    }

    /**
     * Validates if input is a valid target number
     * @param {any} input - Input to validate
     * @returns {boolean} - True if valid number
     */
    static isValidTargetNumber(input) {
        return typeof input === 'number' && !isNaN(input) && isFinite(input);
    }

    /**
     * Validates graph structure
     * @param {any} graph - Graph to validate
     * @returns {boolean} - True if valid graph
     */
    static isValidGraph(graph) {
        return graph && typeof graph === 'object' && !Array.isArray(graph);
    }
}

// ============================================================================
// ARRAY UTILITIES
// ============================================================================

/**
 * Common array operations
 */
class ArrayOperations {
    /**
     * Swaps two elements in an array
     * @param {any[]} array - Array containing elements
     * @param {number} index1 - First index
     * @param {number} index2 - Second index
     */
    static swapElements(array, index1, index2) {
        [array[index1], array[index2]] = [array[index2], array[index1]];
    }

    /**
     * Creates a copy of an array
     * @param {any[]} array - Array to copy
     * @returns {any[]} - New array copy
     */
    static createArrayCopy(array) {
        return [...array];
    }

    /**
     * Finds the minimum element in an array
     * @param {number[]} array - Array to search
     * @param {number} startIndex - Starting index
     * @param {number} endIndex - Ending index
     * @returns {number} - Index of minimum element
     */
    static findMinimumIndex(array, startIndex, endIndex) {
        let minimumIndex = startIndex;
        
        for (let currentIndex = startIndex + 1; currentIndex <= endIndex; currentIndex++) {
            if (array[currentIndex] < array[minimumIndex]) {
                minimumIndex = currentIndex;
            }
        }
        
        return minimumIndex;
    }
}

// ============================================================================
// CLEAN TWO SUM ALGORITHM
// ============================================================================

/**
 * Clean implementation of Two Sum algorithm
 */
class CleanTwoSum {
    /**
     * Finds two numbers in the array that add up to the target sum
     * 
     * @description
     * Uses a hash map to store complements. For each number, we check if its
     * complement (target - current) exists in the map. If found, we return
     * the indices of both numbers.
     * 
     * @complexity
     * - Time: O(n) - Single pass through the array
     * - Space: O(n) - Hash map storage
     * 
     * @param {number[]} numbers - Array of integers
     * @param {number} targetSum - Target sum to find
     * @returns {number[]} - Array containing indices of two numbers that sum to target
     * 
     * @throws {Error} - If input validation fails
     * 
     * @example
     * ```javascript
     * const result = CleanTwoSum.findTwoNumbersWithSum([2, 7, 11, 15], 9);
     * console.log(result); // [0, 1]
     * ```
     */
    static findTwoNumbersWithSum(numbers, targetSum) {
        // Validate inputs
        if (!AlgorithmValidator.isValidNumberArray(numbers)) {
            throw new Error('Input must be a valid number array');
        }
        
        if (!AlgorithmValidator.isValidTargetNumber(targetSum)) {
            throw new Error('Target sum must be a valid number');
        }

        const numberToIndexMap = new Map();
        
        for (let currentIndex = 0; currentIndex < numbers.length; currentIndex++) {
            const currentNumber = numbers[currentIndex];
            const complementNumber = targetSum - currentNumber;
            
            if (numberToIndexMap.has(complementNumber)) {
                const complementIndex = numberToIndexMap.get(complementNumber);
                return [complementIndex, currentIndex];
            }
            
            numberToIndexMap.set(currentNumber, currentIndex);
        }
        
        return [];
    }
}

// ============================================================================
// CLEAN BINARY SEARCH ALGORITHM
// ============================================================================

/**
 * Clean implementation of Binary Search algorithm
 */
class CleanBinarySearch {
    /**
     * Finds an element in a sorted array using binary search
     * 
     * @description
     * Binary search works by repeatedly dividing the search interval in half.
     * If the value of the search key is less than the item in the middle of
     * the interval, narrow the interval to the lower half. Otherwise, narrow
     * it to the upper half.
     * 
     * @complexity
     * - Time: O(log n) - Each iteration reduces search space by half
     * - Space: O(1) - Constant extra space
     * 
     * @param {number[]} sortedArray - Sorted array to search in
     * @param {number} targetValue - Value to find
     * @returns {number} - Index of target value, -1 if not found
     * 
     * @throws {Error} - If input validation fails
     * 
     * @example
     * ```javascript
     * const result = CleanBinarySearch.findElement([1, 3, 5, 7, 9], 5);
     * console.log(result); // 2
     * ```
     */
    static findElement(sortedArray, targetValue) {
        // Validate inputs
        if (!AlgorithmValidator.isValidSortedArray(sortedArray)) {
            throw new Error('Input must be a valid sorted array');
        }
        
        if (!AlgorithmValidator.isValidTargetNumber(targetValue)) {
            throw new Error('Target value must be a valid number');
        }

        return this.performBinarySearch(sortedArray, targetValue);
    }

    /**
     * Performs the actual binary search
     * @param {number[]} array - Sorted array
     * @param {number} target - Target value
     * @returns {number} - Index of target or -1
     */
    static performBinarySearch(array, target) {
        let leftBoundary = 0;
        let rightBoundary = array.length - 1;
        
        while (leftBoundary <= rightBoundary) {
            const middleIndex = this.calculateMiddleIndex(leftBoundary, rightBoundary);
            const middleValue = array[middleIndex];
            
            if (this.isTargetFound(middleValue, target)) {
                return middleIndex;
            }
            
            if (this.shouldSearchLeftHalf(middleValue, target)) {
                rightBoundary = middleIndex - 1;
            } else {
                leftBoundary = middleIndex + 1;
            }
        }
        
        return -1;
    }

    /**
     * Calculates the middle index between two boundaries
     * @param {number} left - Left boundary
     * @param {number} right - Right boundary
     * @returns {number} - Middle index
     */
    static calculateMiddleIndex(left, right) {
        return Math.floor((left + right) / 2);
    }

    /**
     * Checks if target value is found
     * @param {number} currentValue - Current value
     * @param {number} target - Target value
     * @returns {boolean} - True if found
     */
    static isTargetFound(currentValue, target) {
        return currentValue === target;
    }

    /**
     * Determines if search should continue in left half
     * @param {number} currentValue - Current value
     * @param {number} target - Target value
     * @returns {boolean} - True if should search left
     */
    static shouldSearchLeftHalf(currentValue, target) {
        return currentValue > target;
    }
}

// ============================================================================
// CLEAN BUBBLE SORT ALGORITHM
// ============================================================================

/**
 * Clean implementation of Bubble Sort algorithm
 */
class CleanBubbleSort {
    /**
     * Sorts an array using bubble sort algorithm
     * 
     * @description
     * Bubble sort repeatedly steps through the list, compares adjacent elements
     * and swaps them if they are in the wrong order. The pass through the list
     * is repeated until no swaps are needed.
     * 
     * @complexity
     * - Time: O(n²) - Worst and average case
     * - Space: O(1) - In-place sorting
     * - Stable: Yes - Maintains relative order of equal elements
     * 
     * @param {number[]} array - Array to sort
     * @returns {number[]} - Sorted array
     * 
     * @throws {Error} - If input validation fails
     * 
     * @example
     * ```javascript
     * const result = CleanBubbleSort.sort([64, 34, 25, 12, 22, 11, 90]);
     * console.log(result); // [11, 12, 22, 25, 34, 64, 90]
     * ```
     */
    static sort(array) {
        // Validate input
        if (!AlgorithmValidator.isValidNumberArray(array)) {
            throw new Error('Input must be a valid number array');
        }

        // Create a copy to avoid mutating original array
        const arrayCopy = ArrayOperations.createArrayCopy(array);
        const arrayLength = arrayCopy.length;
        
        // Perform bubble sort with optimization
        for (let passNumber = 0; passNumber < arrayLength - 1; passNumber++) {
            let hasSwapped = false;
            
            for (let currentIndex = 0; currentIndex < arrayLength - passNumber - 1; currentIndex++) {
                if (this.shouldSwapElements(arrayCopy[currentIndex], arrayCopy[currentIndex + 1])) {
                    ArrayOperations.swapElements(arrayCopy, currentIndex, currentIndex + 1);
                    hasSwapped = true;
                }
            }
            
            // Early exit if no swaps occurred (array is sorted)
            if (!hasSwapped) {
                break;
            }
        }
        
        return arrayCopy;
    }

    /**
     * Determines if two elements should be swapped
     * @param {number} firstElement - First element
     * @param {number} secondElement - Second element
     * @returns {boolean} - True if should swap
     */
    static shouldSwapElements(firstElement, secondElement) {
        return firstElement > secondElement;
    }
}

// ============================================================================
// CLEAN QUICK SORT ALGORITHM
// ============================================================================

/**
 * Clean implementation of Quick Sort algorithm
 */
class CleanQuickSort {
    /**
     * Sorts an array using quick sort algorithm
     * 
     * @description
     * Quick sort is a divide-and-conquer algorithm. It picks a pivot element
     * and partitions the array around the pivot. Elements smaller than pivot
     * go to the left, larger elements go to the right.
     * 
     * @complexity
     * - Time: O(n log n) average, O(n²) worst case
     * - Space: O(log n) - Stack space for recursion
     * - Stable: No - May change relative order of equal elements
     * 
     * @param {number[]} array - Array to sort
     * @returns {number[]} - Sorted array
     * 
     * @throws {Error} - If input validation fails
     * 
     * @example
     * ```javascript
     * const result = CleanQuickSort.sort([10, 7, 8, 9, 1, 5]);
     * console.log(result); // [1, 5, 7, 8, 9, 10]
     * ```
     */
    static sort(array) {
        // Validate input
        if (!AlgorithmValidator.isValidNumberArray(array)) {
            throw new Error('Input must be a valid number array');
        }

        // Create a copy to avoid mutating original array
        const arrayCopy = ArrayOperations.createArrayCopy(array);
        
        this.performQuickSort(arrayCopy, 0, arrayCopy.length - 1);
        
        return arrayCopy;
    }

    /**
     * Performs quick sort on a subarray
     * @param {number[]} array - Array to sort
     * @param {number} lowIndex - Lower boundary
     * @param {number} highIndex - Upper boundary
     */
    static performQuickSort(array, lowIndex, highIndex) {
        if (lowIndex < highIndex) {
            const pivotIndex = this.partitionArray(array, lowIndex, highIndex);
            
            // Recursively sort elements before and after pivot
            this.performQuickSort(array, lowIndex, pivotIndex - 1);
            this.performQuickSort(array, pivotIndex + 1, highIndex);
        }
    }

    /**
     * Partitions array around pivot element
     * @param {number[]} array - Array to partition
     * @param {number} lowIndex - Lower boundary
     * @param {number} highIndex - Upper boundary
     * @returns {number} - Pivot index after partitioning
     */
    static partitionArray(array, lowIndex, highIndex) {
        const pivotValue = array[highIndex];
        let smallerElementIndex = lowIndex - 1;
        
        for (let currentIndex = lowIndex; currentIndex < highIndex; currentIndex++) {
            if (array[currentIndex] <= pivotValue) {
                smallerElementIndex++;
                ArrayOperations.swapElements(array, smallerElementIndex, currentIndex);
            }
        }
        
        // Place pivot in correct position
        ArrayOperations.swapElements(array, smallerElementIndex + 1, highIndex);
        
        return smallerElementIndex + 1;
    }
}

// ============================================================================
// CLEAN MERGE SORT ALGORITHM
// ============================================================================

/**
 * Clean implementation of Merge Sort algorithm
 */
class CleanMergeSort {
    /**
     * Sorts an array using merge sort algorithm
     * 
     * @description
     * Merge sort is a divide-and-conquer algorithm that recursively breaks
     * down the array into smaller subarrays until each has only one element,
     * then merges them back together in sorted order.
     * 
     * @complexity
     * - Time: O(n log n) - Consistent performance
     * - Space: O(n) - Additional space for merging
     * - Stable: Yes - Maintains relative order of equal elements
     * 
     * @param {number[]} array - Array to sort
     * @returns {number[]} - Sorted array
     * 
     * @throws {Error} - If input validation fails
     * 
     * @example
     * ```javascript
     * const result = CleanMergeSort.sort([38, 27, 43, 3, 9, 82, 10]);
     * console.log(result); // [3, 9, 10, 27, 38, 43, 82]
     * ```
     */
    static sort(array) {
        // Validate input
        if (!AlgorithmValidator.isValidNumberArray(array)) {
            throw new Error('Input must be a valid number array');
        }

        // Base case: array with 0 or 1 element is already sorted
        if (array.length <= 1) {
            return ArrayOperations.createArrayCopy(array);
        }
        
        // Divide array into two halves
        const middleIndex = this.calculateMiddleIndex(array.length);
        const leftHalf = array.slice(0, middleIndex);
        const rightHalf = array.slice(middleIndex);
        
        // Recursively sort both halves
        const sortedLeftHalf = this.sort(leftHalf);
        const sortedRightHalf = this.sort(rightHalf);
        
        // Merge the sorted halves
        return this.mergeSortedArrays(sortedLeftHalf, sortedRightHalf);
    }

    /**
     * Calculates middle index for array division
     * @param {number} arrayLength - Length of array
     * @returns {number} - Middle index
     */
    static calculateMiddleIndex(arrayLength) {
        return Math.floor(arrayLength / 2);
    }

    /**
     * Merges two sorted arrays into one sorted array
     * @param {number[]} leftArray - Left sorted array
     * @param {number[]} rightArray - Right sorted array
     * @returns {number[]} - Merged sorted array
     */
    static mergeSortedArrays(leftArray, rightArray) {
        const mergedArray = [];
        let leftIndex = 0;
        let rightIndex = 0;
        
        // Compare elements from both arrays and merge in sorted order
        while (leftIndex < leftArray.length && rightIndex < rightArray.length) {
            if (leftArray[leftIndex] <= rightArray[rightIndex]) {
                mergedArray.push(leftArray[leftIndex]);
                leftIndex++;
            } else {
                mergedArray.push(rightArray[rightIndex]);
                rightIndex++;
            }
        }
        
        // Add remaining elements from left array
        while (leftIndex < leftArray.length) {
            mergedArray.push(leftArray[leftIndex]);
            leftIndex++;
        }
        
        // Add remaining elements from right array
        while (rightIndex < rightArray.length) {
            mergedArray.push(rightArray[rightIndex]);
            rightIndex++;
        }
        
        return mergedArray;
    }
}

// ============================================================================
// CLEAN GRAPH ALGORITHMS
// ============================================================================

/**
 * Clean implementation of Depth First Search
 */
class CleanDepthFirstSearch {
    /**
     * Performs depth first search on a graph
     * 
     * @description
     * DFS explores as far as possible along each branch before backtracking.
     * It uses a stack (or recursion) to keep track of vertices to visit.
     * 
     * @complexity
     * - Time: O(V + E) - V vertices, E edges
     * - Space: O(V) - Stack space
     * 
     * @param {Object} graph - Graph representation
     * @param {string|number} startNode - Starting node
     * @returns {Array} - DFS traversal order
     * 
     * @throws {Error} - If input validation fails
     */
    static traverse(graph, startNode) {
        // Validate inputs
        if (!AlgorithmValidator.isValidGraph(graph)) {
            throw new Error('Input must be a valid graph');
        }
        
        if (!startNode || !graph[startNode]) {
            throw new Error('Start node must exist in graph');
        }

        const visitedNodes = new Set();
        const traversalOrder = [];
        
        this.performDFS(graph, startNode, visitedNodes, traversalOrder);
        
        return traversalOrder;
    }

    /**
     * Performs the actual DFS traversal
     * @param {Object} graph - Graph representation
     * @param {string|number} currentNode - Current node
     * @param {Set} visitedNodes - Set of visited nodes
     * @param {Array} traversalOrder - Array to store traversal order
     */
    static performDFS(graph, currentNode, visitedNodes, traversalOrder) {
        // Mark current node as visited
        visitedNodes.add(currentNode);
        traversalOrder.push(currentNode);
        
        // Visit all unvisited neighbors
        const neighbors = graph[currentNode] || [];
        for (const neighbor of neighbors) {
            if (!visitedNodes.has(neighbor)) {
                this.performDFS(graph, neighbor, visitedNodes, traversalOrder);
            }
        }
    }
}

/**
 * Clean implementation of Breadth First Search
 */
class CleanBreadthFirstSearch {
    /**
     * Performs breadth first search on a graph
     * 
     * @description
     * BFS explores all vertices at the present depth before moving on to
     * vertices at the next depth level. It uses a queue to keep track of
     * vertices to visit.
     * 
     * @complexity
     * - Time: O(V + E) - V vertices, E edges
     * - Space: O(V) - Queue space
     * 
     * @param {Object} graph - Graph representation
     * @param {string|number} startNode - Starting node
     * @returns {Array} - BFS traversal order
     * 
     * @throws {Error} - If input validation fails
     */
    static traverse(graph, startNode) {
        // Validate inputs
        if (!AlgorithmValidator.isValidGraph(graph)) {
            throw new Error('Input must be a valid graph');
        }
        
        if (!startNode || !graph[startNode]) {
            throw new Error('Start node must exist in graph');
        }

        const visitedNodes = new Set();
        const traversalOrder = [];
        const nodeQueue = [startNode];
        
        visitedNodes.add(startNode);
        
        while (nodeQueue.length > 0) {
            const currentNode = nodeQueue.shift();
            traversalOrder.push(currentNode);
            
            // Add all unvisited neighbors to queue
            const neighbors = graph[currentNode] || [];
            for (const neighbor of neighbors) {
                if (!visitedNodes.has(neighbor)) {
                    visitedNodes.add(neighbor);
                    nodeQueue.push(neighbor);
                }
            }
        }
        
        return traversalOrder;
    }
}

// ============================================================================
// EXPORT MODULE
// ============================================================================

// Export all clean algorithm classes
window.CleanAlgorithms = {
    AlgorithmValidator,
    ArrayOperations,
    CleanTwoSum,
    CleanBinarySearch,
    CleanBubbleSort,
    CleanQuickSort,
    CleanMergeSort,
    CleanDepthFirstSearch,
    CleanBreadthFirstSearch
};

console.log('✅ Clean Algorithms Module loaded successfully!'); 