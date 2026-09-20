/*



Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.




*/



class Solution {
    public int trap(int[] height) {
       int leftmax=0;
       int rightmax=0;
       int l=0;
       int water=0;
       int r=height.length-1;


       for(int i=0;i<height.length-1;i++){
            if(height[l]>leftmax){
                leftmax=height[l];
            }
            if(height[r]>rightmax){
                rightmax=height[r];
            }
            if(leftmax>rightmax){
                
                water += rightmax - height[r];
                r=r-1;
            }
            else if(rightmax >= leftmax){
                
                water += leftmax - height[l]; 
                l=l+1;
            }
       }
       return water;
    }
}






/*






Okay so wht happens here is there r two pointers ... leftmax n rightmax 
we use both to get the maximum length n then calculate the water in bw the blocks 




*/
