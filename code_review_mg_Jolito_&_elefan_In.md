### 

### **Annex C**

**Code Quality Assessment Worksheet**

**Section: \_\_\_\_\_\_Magnesium\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_	Score:\_\_\_\_\_\_\_\_\_\_\_\_**  
**C\# / Name:\_\_\_\_\_\_Jolito partner with Elefan\_\_\_\_\_\_	Date: August 26, 2026**

**Instructions:**

**The problem: Search for a Number in a Sorted List**

**For example: Both algorithms could search:**   
numbers \= \[5, 12, 18, 23, 31, 47, 56, 68, 74, 90\]  
target \= 47

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| def linear\_search(numbers, target):    *for* i *in* range(len(numbers)):        *if* numbers\[i\] \== target:            *return* i    *return* \-1   | def binary\_search(numbers, target):    low \= 0    high \= len(numbers) \- 1     *while* low \<= high:        middle \= (low \+ high) // 2         *if* numbers\[middle\] \== target:            *return* middle        *elif* numbers\[middle\] \< target:            low \= middle \+ 1        *else*:            high \= middle \- 1     *return* \-1   |

## 

## 

## 

## 

## **Questions with Checklists**

### **1\. Efficiency**

Which algorithm is faster when the list of numbers is very large? Why?

The Binary Search algorithm because instead of going through the list from the start, the binary search begins in the middle and seeks out the number from there.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list? | ~~How many elements might the algorithm need to check? Does the algorithm reduce the search area as it runs? Does the algorithm still work efficiently with a very large list?~~ |

**2\. Readability**

Which algorithm is easier to understand at first glance? What makes it clearer?

The Linear Search algorithm is the simpler one to understand due to it being a simple incrementing search function.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process?~~ | ~~How meaningful are the variable names? How simple is the logic? How concise is the code? How easy is it to follow the search process?~~ |

### 

### **3\. Maintainability**

If you had to modify the program, such as changing what happens when the target is found, which algorithm would be easier to update? Why?

The Linear Search algorithm as it only has one non-error output statement in *return i.* 

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating?~~ | ~~Is the structure straightforward? Would adding new steps break the code easily? Is there less chance of errors when updating?~~ |

### 

### **4\. Testability**

Which algorithm is easier to test with different inputs? Why?

The Linear Search algorithm is easier to test due to its process being simple and output predictable.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| ~~Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear?~~ | ~~Can you test with small lists easily? Does the algorithm have fewer conditions to check? Is the output predictable and clear?~~ |

### **5\. Reliability and Input Validation**

What should the algorithm check to avoid errors when receiving input from a user?

The algorithm should check for Index Errors in the lists and value errors for the contents and the target variables.

**Checklist to guide your answer:**

| Implementation 1 | Implementation 2 |
| ----- | ----- |
| Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Linear Search? | Does the algorithm check if the list is empty? Does it handle invalid inputs (like letters instead of numbers)? Does it avoid crashing when inputs are unusual? Does it check that the list is sorted before using Binary Search? |

### 

### **6\. Final Answer**

Based on your answers from 1 to 5, Which algorithm would you choose for this problem, and under what conditions would the other algorithm be more suitable? Summarize your answer.

My answers favor the Linear Search Algorithm because of its simplicity allowing for easy testability and code updating. The given list is also small allowing the function to clear the list incredibly fast.