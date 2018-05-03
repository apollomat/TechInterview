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
