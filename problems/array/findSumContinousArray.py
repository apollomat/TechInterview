static boolean findSum(final int[] array, final int k) {
    int start = 0;
    int sum = 0;
    for (int i = 0; i < array.length; i++) {
        sum += array[i];
        while (sum > k) {
            sum -= array[start];
            start++;
        }
        if (sum == k) {
            return true;
        }
    }
    return false;
}


# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result
def subArraySum(arr, n, sum):

    # Pick a starting
    # point
    for i in range(n):
        curr_sum = arr[i]

        # try all subarrays
        # starting with 'i'
        j = i+1
        while j <= n:

            if curr_sum == sum:
                print ("Sum found between")
                print("indexes %d and %d"%( i, j-1))

                return 1

            if curr_sum > sum or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print ("No subarray found")
    return 0
