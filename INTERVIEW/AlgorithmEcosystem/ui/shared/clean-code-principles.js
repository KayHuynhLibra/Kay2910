/**
 * Clean Code Principles Module
 * 
 * This module demonstrates clean code principles applied to algorithms
 * - Meaningful Names
 * - Small Functions
 * - Single Responsibility
 * - DRY (Don't Repeat Yourself)
 * - SOLID Principles
 * - Error Handling
 * - Documentation
 */

// ============================================================================
// 1. MEANINGFUL NAMES - Tên biến và hàm có ý nghĩa
// ============================================================================

/**
 * Clean Code Example: Two Sum with meaningful names
 * 
 * ❌ Bad: function ts(arr, t) { ... }
 * ✅ Good: function findTwoNumbersWithSum(numbers, targetSum) { ... }
 */
class TwoSumCleanCode {
    /**
     * Tìm hai số trong mảng có tổng bằng target
     * @param {number[]} numbers - Mảng số nguyên
     * @param {number} targetSum - Tổng cần tìm
     * @returns {number[]} - Mảng chứa chỉ số của hai số
     */
    static findTwoNumbersWithSum(numbers, targetSum) {
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
// 2. SMALL FUNCTIONS - Hàm nhỏ, một nhiệm vụ
// ============================================================================

/**
 * Clean Code Example: Binary Search with small, focused functions
 */
class BinarySearchCleanCode {
    /**
     * Tìm kiếm nhị phân trong mảng đã sắp xếp
     * @param {number[]} sortedArray - Mảng đã sắp xếp
     * @param {number} targetValue - Giá trị cần tìm
     * @returns {number} - Chỉ số của phần tử, -1 nếu không tìm thấy
     */
    static findElementInSortedArray(sortedArray, targetValue) {
        if (!this.isValidInput(sortedArray, targetValue)) {
            return -1;
        }
        
        return this.performBinarySearch(sortedArray, targetValue);
    }
    
    /**
     * Kiểm tra tính hợp lệ của input
     * @param {number[]} array - Mảng cần kiểm tra
     * @param {number} target - Giá trị cần tìm
     * @returns {boolean} - True nếu input hợp lệ
     */
    static isValidInput(array, target) {
        return Array.isArray(array) && 
               array.length > 0 && 
               typeof target === 'number';
    }
    
    /**
     * Thực hiện tìm kiếm nhị phân
     * @param {number[]} array - Mảng đã sắp xếp
     * @param {number} target - Giá trị cần tìm
     * @returns {number} - Chỉ số của phần tử
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
     * Tính chỉ số giữa
     * @param {number} left - Chỉ số trái
     * @param {number} right - Chỉ số phải
     * @returns {number} - Chỉ số giữa
     */
    static calculateMiddleIndex(left, right) {
        return Math.floor((left + right) / 2);
    }
    
    /**
     * Kiểm tra xem đã tìm thấy target chưa
     * @param {number} currentValue - Giá trị hiện tại
     * @param {number} target - Giá trị cần tìm
     * @returns {boolean} - True nếu tìm thấy
     */
    static isTargetFound(currentValue, target) {
        return currentValue === target;
    }
    
    /**
     * Quyết định tìm kiếm nửa trái hay phải
     * @param {number} currentValue - Giá trị hiện tại
     * @param {number} target - Giá trị cần tìm
     * @returns {boolean} - True nếu tìm nửa trái
     */
    static shouldSearchLeftHalf(currentValue, target) {
        return currentValue > target;
    }
}

// ============================================================================
// 3. SINGLE RESPONSIBILITY - Một lớp, một nhiệm vụ
// ============================================================================

/**
 * Clean Code Example: Sorting with separate responsibilities
 */
class ArrayValidator {
    /**
     * Kiểm tra tính hợp lệ của mảng
     * @param {any[]} array - Mảng cần kiểm tra
     * @returns {boolean} - True nếu hợp lệ
     */
    static isValidArray(array) {
        return Array.isArray(array) && array.length > 0;
    }
    
    /**
     * Kiểm tra mảng có phải số nguyên không
     * @param {any[]} array - Mảng cần kiểm tra
     * @returns {boolean} - True nếu là mảng số nguyên
     */
    static isIntegerArray(array) {
        return array.every(element => Number.isInteger(element));
    }
}

class ArraySorter {
    /**
     * Sắp xếp mảng số nguyên
     * @param {number[]} array - Mảng cần sắp xếp
     * @returns {number[]} - Mảng đã sắp xếp
     */
    static sortIntegerArray(array) {
        if (!ArrayValidator.isValidArray(array)) {
            throw new Error('Invalid array input');
        }
        
        if (!ArrayValidator.isIntegerArray(array)) {
            throw new Error('Array must contain only integers');
        }
        
        return [...array].sort((a, b) => a - b);
    }
}

// ============================================================================
// 4. DRY PRINCIPLE - Không lặp lại code
// ============================================================================

/**
 * Clean Code Example: Common utilities to avoid repetition
 */
class AlgorithmUtils {
    /**
     * Hoán đổi hai phần tử trong mảng
     * @param {any[]} array - Mảng chứa phần tử
     * @param {number} index1 - Chỉ số thứ nhất
     * @param {number} index2 - Chỉ số thứ hai
     */
    static swapElements(array, index1, index2) {
        [array[index1], array[index2]] = [array[index2], array[index1]];
    }
    
    /**
     * Tạo mảng số ngẫu nhiên
     * @param {number} size - Kích thước mảng
     * @param {number} min - Giá trị nhỏ nhất
     * @param {number} max - Giá trị lớn nhất
     * @returns {number[]} - Mảng số ngẫu nhiên
     */
    static generateRandomArray(size, min = 1, max = 100) {
        return Array.from({ length: size }, () => 
            Math.floor(Math.random() * (max - min + 1)) + min
        );
    }
    
    /**
     * Đo thời gian thực thi hàm
     * @param {Function} algorithmFunction - Hàm cần đo
     * @param {any[]} parameters - Tham số cho hàm
     * @returns {Object} - Kết quả và thời gian thực thi
     */
    static measureExecutionTime(algorithmFunction, ...parameters) {
        const startTime = performance.now();
        const result = algorithmFunction(...parameters);
        const endTime = performance.now();
        
        return {
            result,
            executionTime: endTime - startTime,
            executionTimeMs: (endTime - startTime).toFixed(4)
        };
    }
}

// ============================================================================
// 5. ERROR HANDLING - Xử lý lỗi tốt
// ============================================================================

/**
 * Custom Error Classes for better error handling
 */
class AlgorithmError extends Error {
    constructor(message, algorithmName, inputData) {
        super(message);
        this.name = 'AlgorithmError';
        this.algorithmName = algorithmName;
        this.inputData = inputData;
        this.timestamp = new Date().toISOString();
    }
}

class ValidationError extends AlgorithmError {
    constructor(message, inputData) {
        super(message, 'Validation', inputData);
        this.name = 'ValidationError';
    }
}

/**
 * Clean Code Example: Error handling in algorithms
 */
class SafeAlgorithmExecutor {
    /**
     * Thực thi thuật toán với xử lý lỗi an toàn
     * @param {Function} algorithm - Thuật toán cần thực thi
     * @param {string} algorithmName - Tên thuật toán
     * @param {any[]} parameters - Tham số
     * @returns {Object} - Kết quả hoặc lỗi
     */
    static executeSafely(algorithm, algorithmName, ...parameters) {
        try {
            // Validate input
            this.validateInput(parameters);
            
            // Execute algorithm
            const result = algorithm(...parameters);
            
            return {
                success: true,
                result,
                algorithmName,
                parameters
            };
            
        } catch (error) {
            return {
                success: false,
                error: error.message,
                algorithmName,
                parameters,
                timestamp: new Date().toISOString()
            };
        }
    }
    
    /**
     * Validate input parameters
     * @param {any[]} parameters - Tham số cần validate
     * @throws {ValidationError} - Nếu input không hợp lệ
     */
    static validateInput(parameters) {
        if (!Array.isArray(parameters)) {
            throw new ValidationError('Parameters must be an array', parameters);
        }
        
        if (parameters.length === 0) {
            throw new ValidationError('At least one parameter is required', parameters);
        }
    }
}

// ============================================================================
// 6. DOCUMENTATION - Tài liệu rõ ràng
// ============================================================================

/**
 * Clean Code Example: Well-documented algorithm
 * 
 * @example
 * ```javascript
 * const sorter = new BubbleSortCleanCode();
 * const result = sorter.sort([64, 34, 25, 12, 22, 11, 90]);
 * console.log(result); // [11, 12, 22, 25, 34, 64, 90]
 * ```
 */
class BubbleSortCleanCode {
    /**
     * Sắp xếp mảng bằng thuật toán Bubble Sort
     * 
     * @description
     * Bubble Sort là thuật toán sắp xếp đơn giản nhất.
     * Nó so sánh và hoán đổi các phần tử liền kề cho đến khi
     * mảng được sắp xếp hoàn toàn.
     * 
     * @complexity
     * - Time: O(n²) trong trường hợp xấu nhất
     * - Space: O(1) - In-place sorting
     * - Stable: Có - Giữ nguyên thứ tự các phần tử bằng nhau
     * 
     * @param {number[]} array - Mảng số nguyên cần sắp xếp
     * @returns {number[]} - Mảng đã được sắp xếp
     * 
     * @throws {ValidationError} - Nếu input không hợp lệ
     * 
     * @example
     * ```javascript
     * const sorter = new BubbleSortCleanCode();
     * const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
     * const sortedArray = sorter.sort(unsortedArray);
     * // sortedArray = [11, 12, 22, 25, 34, 64, 90]
     * ```
     */
    sort(array) {
        // Validate input
        if (!ArrayValidator.isValidArray(array)) {
            throw new ValidationError('Input must be a non-empty array', array);
        }
        
        if (!ArrayValidator.isIntegerArray(array)) {
            throw new ValidationError('Array must contain only integers', array);
        }
        
        // Create a copy to avoid mutating original array
        const arrayCopy = [...array];
        const arrayLength = arrayCopy.length;
        
        // Perform bubble sort
        for (let passNumber = 0; passNumber < arrayLength - 1; passNumber++) {
            let hasSwapped = false;
            
            for (let currentIndex = 0; currentIndex < arrayLength - passNumber - 1; currentIndex++) {
                if (this.shouldSwap(arrayCopy[currentIndex], arrayCopy[currentIndex + 1])) {
                    AlgorithmUtils.swapElements(arrayCopy, currentIndex, currentIndex + 1);
                    hasSwapped = true;
                }
            }
            
            // Early exit if no swaps occurred
            if (!hasSwapped) {
                break;
            }
        }
        
        return arrayCopy;
    }
    
    /**
     * Quyết định có nên hoán đổi hai phần tử không
     * @param {number} firstElement - Phần tử thứ nhất
     * @param {number} secondElement - Phần tử thứ hai
     * @returns {boolean} - True nếu cần hoán đổi
     */
    shouldSwap(firstElement, secondElement) {
        return firstElement > secondElement;
    }
}

// ============================================================================
// 7. SOLID PRINCIPLES - Nguyên tắc SOLID
// ============================================================================

/**
 * Clean Code Example: SOLID Principles
 */

// Single Responsibility Principle
class GraphNode {
    constructor(value) {
        this.value = value;
        this.neighbors = [];
    }
    
    addNeighbor(node) {
        this.neighbors.push(node);
    }
    
    getNeighbors() {
        return this.neighbors;
    }
}

// Open/Closed Principle
class GraphTraversal {
    constructor() {
        this.visited = new Set();
    }
    
    traverse(graph, startNode) {
        this.visited.clear();
        return this.performTraversal(graph, startNode);
    }
    
    performTraversal(graph, node) {
        // To be implemented by subclasses
        throw new Error('performTraversal must be implemented by subclass');
    }
}

class DepthFirstSearch extends GraphTraversal {
    performTraversal(graph, node) {
        if (!node || this.visited.has(node)) {
            return [];
        }
        
        this.visited.add(node);
        const result = [node.value];
        
        for (const neighbor of node.getNeighbors()) {
            result.push(...this.performTraversal(graph, neighbor));
        }
        
        return result;
    }
}

class BreadthFirstSearch extends GraphTraversal {
    performTraversal(graph, startNode) {
        const queue = [startNode];
        const result = [];
        
        while (queue.length > 0) {
            const currentNode = queue.shift();
            
            if (!this.visited.has(currentNode)) {
                this.visited.add(currentNode);
                result.push(currentNode.value);
                
                for (const neighbor of currentNode.getNeighbors()) {
                    queue.push(neighbor);
                }
            }
        }
        
        return result;
    }
}

// ============================================================================
// 8. TESTING UTILITIES - Tiện ích cho testing
// ============================================================================

/**
 * Clean Code Example: Testing utilities
 */
class AlgorithmTester {
    /**
     * Test algorithm với multiple test cases
     * @param {Function} algorithm - Thuật toán cần test
     * @param {Array} testCases - Các test case
     * @returns {Object} - Kết quả test
     */
    static runTests(algorithm, testCases) {
        const results = {
            total: testCases.length,
            passed: 0,
            failed: 0,
            details: []
        };
        
        for (const testCase of testCases) {
            const testResult = this.runSingleTest(algorithm, testCase);
            results.details.push(testResult);
            
            if (testResult.passed) {
                results.passed++;
            } else {
                results.failed++;
            }
        }
        
        return results;
    }
    
    /**
     * Chạy một test case
     * @param {Function} algorithm - Thuật toán
     * @param {Object} testCase - Test case
     * @returns {Object} - Kết quả test
     */
    static runSingleTest(algorithm, testCase) {
        const { input, expected, description } = testCase;
        
        try {
            const result = algorithm(...input);
            const passed = JSON.stringify(result) === JSON.stringify(expected);
            
            return {
                description,
                input,
                expected,
                actual: result,
                passed,
                error: null
            };
        } catch (error) {
            return {
                description,
                input,
                expected,
                actual: null,
                passed: false,
                error: error.message
            };
        }
    }
}

// ============================================================================
// EXPORT MODULE
// ============================================================================

// Export all clean code classes and utilities
window.CleanCodePrinciples = {
    TwoSumCleanCode,
    BinarySearchCleanCode,
    ArrayValidator,
    ArraySorter,
    AlgorithmUtils,
    SafeAlgorithmExecutor,
    BubbleSortCleanCode,
    GraphNode,
    GraphTraversal,
    DepthFirstSearch,
    BreadthFirstSearch,
    AlgorithmTester,
    AlgorithmError,
    ValidationError
};

console.log('✅ Clean Code Principles Module loaded successfully!'); 