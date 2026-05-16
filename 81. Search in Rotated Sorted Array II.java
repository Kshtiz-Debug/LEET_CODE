/*

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

*/


class Solution {
    public boolean search(int[] nums, int k) {
      int low=0;
      int high=nums.length-1;
      int side;
      while(low<=high){
        int mid=(low+high)/2;
        if(nums[mid]==k){
            return true;
        }

        if (nums[low]==nums[mid] && nums[mid]==nums[high]) {
            low++;
            high--;
            continue;
        }
        if(nums[mid]>=nums[low]){
            side=0;
        }
        else{
            side=1;
        }

        if(side==1){
            if(nums[mid]<k && nums[high]>=k){
                low=mid+1;
            }
            else if(nums[mid]<k && nums[high]<k){
                high=mid-1;
            }
            else if(nums[mid]>k){
                high=mid-1;
            }
        }
        else{
            if(nums[mid]>k && nums[low]<=k){
                high=mid-1;
            }
            else if(nums[mid]>k && nums[low]>k){
                low=mid+1;
            }
            else if(nums[mid]<k){
                low=mid+1;
            }
        }

      }
      return false;
    }
}
