#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tạo thêm 80 folder từ 21-100 tiếp nối 20 folder hiện tại
"""

import os

# Danh sách 80 thuật toán tiếp theo (21-100)
ALGORITHM_GROUPS_21_100 = {
    "21-ArrayManipulation": "ARRAY MANIPULATION",
    "22-MatrixOperations": "MATRIX OPERATIONS",
    "23-StackAlgorithms": "STACK ALGORITHMS",
    "24-QueueAlgorithms": "QUEUE ALGORITHMS",
    "25-DequeAlgorithms": "DEQUE ALGORITHMS",
    "26-HashTableAlgorithms": "HASH TABLE ALGORITHMS",
    "27-SetAlgorithms": "SET ALGORITHMS",
    "28-MapAlgorithms": "MAP ALGORITHMS",
    "29-PriorityQueueAlgorithms": "PRIORITY QUEUE ALGORITHMS",
    "30-HeapAlgorithms": "HEAP ALGORITHMS",
    "31-BinarySearchTree": "BINARY SEARCH TREE",
    "32-AVLTree": "AVL TREE",
    "33-RedBlackTree": "RED BLACK TREE",
    "34-BTree": "B-TREE",
    "35-TrieAlgorithms": "TRIE ALGORITHMS",
    "36-SuffixTree": "SUFFIX TREE",
    "37-SegmentTree": "SEGMENT TREE",
    "38-FenwickTree": "FENWICK TREE",
    "39-DisjointSet": "DISJOINT SET",
    "40-UnionFind": "UNION FIND",
    "41-BitManipulation": "BIT MANIPULATION",
    "42-BitwiseAlgorithms": "BITWISE ALGORITHMS",
    "43-MathAlgorithms": "MATH ALGORITHMS",
    "44-NumberTheory": "NUMBER THEORY",
    "45-Combinatorics": "COMBINATORICS",
    "46-Probability": "PROBABILITY",
    "47-Statistics": "STATISTICS",
    "48-Geometry": "GEOMETRY",
    "49-ComputationalGeometry": "COMPUTATIONAL GEOMETRY",
    "50-LinearAlgebra": "LINEAR ALGEBRA",
    "51-MatrixAlgorithms": "MATRIX ALGORITHMS",
    "52-GraphTheory": "GRAPH THEORY",
    "53-NetworkFlow": "NETWORK FLOW",
    "54-MatchingAlgorithms": "MATCHING ALGORITHMS",
    "55-Connectivity": "CONNECTIVITY",
    "56-Planarity": "PLANARITY",
    "57-Coloring": "COLORING",
    "58-Clique": "CLIQUE",
    "59-IndependentSet": "INDEPENDENT SET",
    "60-VertexCover": "VERTEX COVER",
    "61-EdgeCover": "EDGE COVER",
    "62-DominatingSet": "DOMINATING SET",
    "63-FeedbackVertexSet": "FEEDBACK VERTEX SET",
    "64-FeedbackEdgeSet": "FEEDBACK EDGE SET",
    "65-SteinerTree": "STEINER TREE",
    "66-TravelingSalesman": "TRAVELING SALESMAN",
    "67-VehicleRouting": "VEHICLE ROUTING",
    "68-FacilityLocation": "FACILITY LOCATION",
    "69-Scheduling": "SCHEDULING",
    "70-Assignment": "ASSIGNMENT",
    "71-Packing": "PACKING",
    "72-Covering": "COVERING",
    "73-Partitioning": "PARTITIONING",
    "74-Clustering": "CLUSTERING",
    "75-Classification": "CLASSIFICATION",
    "76-Regression": "REGRESSION",
    "77-Optimization": "OPTIMIZATION",
    "78-LinearProgramming": "LINEAR PROGRAMMING",
    "79-IntegerProgramming": "INTEGER PROGRAMMING",
    "80-NonlinearProgramming": "NONLINEAR PROGRAMMING",
    "81-ConvexOptimization": "CONVEX OPTIMIZATION",
    "82-NonConvexOptimization": "NON-CONVEX OPTIMIZATION",
    "83-Metaheuristics": "METAHEURISTICS",
    "84-GeneticAlgorithms": "GENETIC ALGORITHMS",
    "85-SimulatedAnnealing": "SIMULATED ANNEALING",
    "86-TabuSearch": "TABU SEARCH",
    "87-ParticleSwarm": "PARTICLE SWARM",
    "88-AntColony": "ANT COLONY",
    "89-BeeColony": "BEE COLONY",
    "90-FireflyAlgorithm": "FIREFLY ALGORITHM",
    "91-CuckooSearch": "CUCKOO SEARCH",
    "92-BatAlgorithm": "BAT ALGORITHM",
    "93-WolfAlgorithm": "WOLF ALGORITHM",
    "94-DragonflyAlgorithm": "DRAGONFLY ALGORITHM",
    "95-ButterflyAlgorithm": "BUTTERFLY ALGORITHM",
    "96-WhaleAlgorithm": "WHALE ALGORITHM",
    "97-MothAlgorithm": "MOTH ALGORITHM",
    "98-GrasshopperAlgorithm": "GRASSHOPPER ALGORITHM",
    "99-SalpAlgorithm": "SALP ALGORITHM",
    "100-HybridAlgorithms": "HYBRID ALGORITHMS"
}

def create_levels_template(group_name, group_title):
    """Tạo template cho LEVELS.md"""
    
    template = f"""# 🎯 {group_title} - 20 LEVELS

## 📚 **Tổng quan**
{group_title} là kỹ thuật quan trọng trong lập trình thi đấu và phỏng vấn.

---

## 🎯 **LEVEL 1: CƠ BẢN**
### **Bài toán**: Basic {group_title} Problem
```python
def basic_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 2: NÂNG CAO**
### **Bài toán**: Advanced {group_title} Problem
```python
def advanced_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 3: CHUYÊN SÂU**
### **Bài toán**: Expert {group_title} Problem
```python
def expert_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 4: MASTER**
### **Bài toán**: Master {group_title} Problem
```python
def master_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 5: EXPERT**
### **Bài toán**: Expert Level {group_title} Problem
```python
def expert_level_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 6: ADVANCED**
### **Bài toán**: Advanced Level {group_title} Problem
```python
def advanced_level_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 7: COMPLEX**
### **Bài toán**: Complex {group_title} Problem
```python
def complex_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 8: OPTIMIZED**
### **Bài toán**: Optimized {group_title} Problem
```python
def optimized_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 9: EFFICIENT**
### **Bài toán**: Efficient {group_title} Problem
```python
def efficient_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 10: PERFORMANT**
### **Bài toán**: Performant {group_title} Problem
```python
def performant_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 11: SCALABLE**
### **Bài toán**: Scalable {group_title} Problem
```python
def scalable_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 12: ROBUST**
### **Bài toán**: Robust {group_title} Problem
```python
def robust_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 13: FLEXIBLE**
### **Bài toán**: Flexible {group_title} Problem
```python
def flexible_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 14: ADAPTABLE**
### **Bài toán**: Adaptable {group_title} Problem
```python
def adaptable_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 15: INNOVATIVE**
### **Bài toán**: Innovative {group_title} Problem
```python
def innovative_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 16: CREATIVE**
### **Bài toán**: Creative {group_title} Problem
```python
def creative_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 17: INGENIOUS**
### **Bài toán**: Ingenious {group_title} Problem
```python
def ingenious_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 18: BRILLIANT**
### **Bài toán**: Brilliant {group_title} Problem
```python
def brilliant_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 19: EXCEPTIONAL**
### **Bài toán**: Exceptional {group_title} Problem
```python
def exceptional_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **LEVEL 20: MASTERPIECE**
### **Bài toán**: Masterpiece {group_title} Problem
```python
def masterpiece_{group_name.lower().replace('-', '_')}_solution():
    # Implementation here
    pass
```

---

## 🎯 **TỔNG KẾT 20 LEVELS**

### **Giai đoạn 1 (Level 1-5)**: Cơ bản
- Basic concepts
- Simple implementations
- Fundamental understanding

### **Giai đoạn 2 (Level 6-10)**: Nâng cao
- Advanced techniques
- Optimization strategies
- Performance improvement

### **Giai đoạn 3 (Level 11-15)**: Chuyên sâu
- Complex algorithms
- Multiple approaches
- Real-world applications

### **Giai đoạn 4 (Level 16-20)**: Master
- Expert-level problems
- Innovative solutions
- Competitive programming

---

## 💡 **Ứng dụng thực tế**

### **Software Development:**
- Algorithm optimization
- Performance tuning
- Code efficiency
- System design

### **Competitive Programming:**
- Problem solving
- Time optimization
- Memory management
- Advanced techniques

### **Interview Preparation:**
- Technical interviews
- Coding challenges
- System design
- Algorithm design

### **Real-world Applications:**
- Data processing
- System optimization
- Performance improvement
- Scalability

---

## 🚀 **Next Steps**

1. **Practice implementation** của từng level
2. **Solve problems** trên LeetCode/HackerRank
3. **Optimize performance** cho từng use case
4. **Apply to real projects** để hiểu sâu hơn
5. **Combine with other techniques** cho complex problems

---

**🎉 Chúc bạn thành thạo {group_title}! 🎉**
"""
    
    return template

def create_readme_template(group_name, group_title):
    """Tạo template cho README.md"""
    
    template = f"""# 🎯 {group_title}

## 📚 **Tổng quan**
{group_title} là kỹ thuật quan trọng trong lập trình thi đấu và phỏng vấn.

---

## 🎯 **20 LEVELS TỔNG QUAN**

### **Giai đoạn 1: Cơ bản (Level 1-5)**
- **Level 1**: Basic concepts
- **Level 2**: Simple implementations
- **Level 3**: Fundamental understanding
- **Level 4**: Core techniques
- **Level 5**: Basic applications

### **Giai đoạn 2: Nâng cao (Level 6-10)**
- **Level 6**: Advanced techniques
- **Level 7**: Optimization strategies
- **Level 8**: Performance improvement
- **Level 9**: Complex problems
- **Level 10**: Advanced applications

### **Giai đoạn 3: Chuyên sâu (Level 11-15)**
- **Level 11**: Expert techniques
- **Level 12**: Multiple approaches
- **Level 13**: Real-world applications
- **Level 14**: System design
- **Level 15**: Advanced algorithms

### **Giai đoạn 4: Master (Level 16-20)**
- **Level 16**: Master techniques
- **Level 17**: Competitive programming
- **Level 18**: Research-level problems
- **Level 19**: Innovation
- **Level 20**: Masterpiece solutions

---

## 🎯 **BÀI TOÁN TIÊU BIỂU**

### **Basic Problems:**
1. Fundamental concepts
2. Simple implementations
3. Core algorithms
4. Basic applications
5. Essential techniques

### **Advanced Problems:**
1. Complex algorithms
2. Optimization techniques
3. Performance tuning
4. Advanced applications
5. Expert solutions

### **Expert Problems:**
1. Research-level problems
2. Competitive programming
3. System design
4. Innovation
5. Masterpiece solutions

---

## 💡 **KỸ THUẬT NÂNG CAO**

### **Optimization:**
- Time complexity
- Space complexity
- Memory management
- Performance tuning

### **Advanced Techniques:**
- Multiple approaches
- Hybrid solutions
- Innovative algorithms
- Expert strategies

### **Real-world Applications:**
- System design
- Scalability
- Performance
- Efficiency

---

## 🚀 **LỘ TRÌNH HỌC TẬP**

### **Tuần 1-2: Cơ bản**
- Hiểu concepts cơ bản
- Implement đơn giản
- Practice fundamentals

### **Tuần 3-4: Nâng cao**
- Advanced techniques
- Optimization
- Complex problems

### **Tuần 5-6: Chuyên sâu**
- Expert techniques
- Real-world applications
- System design

### **Tuần 7-8: Master**
- Competitive programming
- Research problems
- Innovation

---

## 💻 **IMPLEMENTATION TIPS**

### **Basic Pattern:**
```python
def basic_pattern():
    # Basic implementation
    pass
```

### **Advanced Pattern:**
```python
def advanced_pattern():
    # Advanced implementation
    pass
```

### **Expert Pattern:**
```python
def expert_pattern():
    # Expert implementation
    pass
```

---

## 🎯 **INTERVIEW PREPARATION**

### **Common Questions:**
1. "Implement basic algorithm"
2. "Optimize for performance"
3. "Handle edge cases"
4. "Scale the solution"
5. "Design the system"

### **Advanced Questions:**
1. "Multiple approaches"
2. "Trade-offs analysis"
3. "Performance optimization"
4. "System design"
5. "Innovation"

---

## 📚 **RESOURCES**

### **Online Platforms:**
- LeetCode Problems
- HackerRank Challenges
- Codeforces Contests
- AtCoder Problems

### **Books:**
- "Introduction to Algorithms" (CLRS)
- "Competitive Programming" by Steven Halim
- "Cracking the Coding Interview"

### **Practice:**
- Daily coding challenges
- Mock interviews
- Peer programming
- Code reviews

---

**🎉 Chúc bạn thành thạo {group_title}! 🎉**
"""
    
    return template

def main():
    """Hàm chính tạo tất cả file"""
    
    base_dir = "interviewDataStructure"
    
    print("🚀 Bắt đầu tạo 80 folder thuật toán từ 21-100...")
    
    for group_name, group_title in ALGORITHM_GROUPS_21_100.items():
        group_dir = os.path.join(base_dir, group_name)
        
        # Tạo thư mục nếu chưa có
        if not os.path.exists(group_dir):
            os.makedirs(group_dir)
            print(f"✅ Tạo thư mục: {group_name}")
        
        # Tạo LEVELS.md
        levels_file = os.path.join(group_dir, "LEVELS.md")
        if not os.path.exists(levels_file):
            with open(levels_file, 'w', encoding='utf-8') as f:
                f.write(create_levels_template(group_name, group_title))
            print(f"✅ Tạo LEVELS.md: {group_name}")
        
        # Tạo README.md
        readme_file = os.path.join(group_dir, "README.md")
        if not os.path.exists(readme_file):
            with open(readme_file, 'w', encoding='utf-8') as f:
                f.write(create_readme_template(group_name, group_title))
            print(f"✅ Tạo README.md: {group_name}")
    
    print("\n🎉 Hoàn thành tạo 80 folder thuật toán!")
    print("📊 Tổng cộng: 100 nhóm thuật toán (20 + 80)")
    print("📁 Mỗi nhóm có: LEVELS.md (20 levels) + README.md")

if __name__ == "__main__":
    main() 