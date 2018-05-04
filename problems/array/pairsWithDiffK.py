# Find all pairs with difference k
FIND ALL PAIRS WITH DIFFERENCE K
Method 5 (Use Sorting)
* Sort the array arr
* Take two pointers, l and r, both pointing to 1st element
* Take the difference arr[r] – arr[l]
    * If value diff is K, increment count and move both pointers to next element
    * if value diff > k, move l to next element
    * if value diff < k, move r to next element
* return count
1 2 3 4 5. k == 4
