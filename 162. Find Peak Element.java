/*

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.


*/




// now to achieve O(logn) time complexity we have to use binary search basics to get the effective output instead of brute force


class Solution {
    public int findPeakElement(int[] nums) {
        int high=nums.length-1;
        int low=0;
        while(low<high){
            int mid=low+(high-low)/2;
            if(nums[mid]<nums[mid+1]){
                low=mid+1;
            }
            else{
                high=mid;
            }
        }
        return low;
    }
}
