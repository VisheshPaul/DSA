class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {

        Arrays.sort(nums);

        int[] ans = new int[queries.length];

        // Prefix sum
        for(int i = 1; i < nums.length; i++){
            nums[i] += nums[i - 1];
        }

        // Binary search for every query
        for(int i = 0; i < queries.length; i++){

            int left = 0;
            int right = nums.length - 1;

            while(left <= right){

                int mid = left + (right - left) / 2;

                if(nums[mid] <= queries[i]){
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }

            ans[i] = left;
        }

        return ans;
    }
}