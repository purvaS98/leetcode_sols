class Solution {
    public boolean containsDuplicate(int[] nums) {
        Arrays.sort(nums);
        int j;
        for(int i=1; i<= nums.length -1; i++){
            j = i-1;
            if(nums[j] == nums[i]){
                return true;
            }
        }
        return false;
    }
}