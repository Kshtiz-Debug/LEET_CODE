/*




Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.





*/



// now one way is like the brute force way 


class Solution {
    public int findKthPositive(int[] arr, int k) {
        int i=1;     // Is the element which will be used for traversing through every integer 
        int count =0;      // Is the count till k
        int index=0;   // keeps the count of elements traversed in the array 
        while(true){

            if(index<=arr.length-1 && arr[index]==i ){
                index++;
            }
            else{
                ++count;
            }



            if(count==k){
                return i;
            }
            i++;
        }
    }
}






// n the other way is to go like this 


