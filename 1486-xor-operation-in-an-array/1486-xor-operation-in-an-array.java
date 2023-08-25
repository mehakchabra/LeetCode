class Solution {
    public int xorOperation(int n, int start) {
        int nums[] = new int[n];
        for(int i = 0; i < n; i++){
            nums[i] = i * 2 + start;
        }
        int sum = nums[0];
        for(int i = 1; i < n; i++)
             sum ^= nums[i];
        return sum;
    }
}