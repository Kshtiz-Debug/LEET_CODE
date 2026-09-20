/*




You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.




*/



class Solution {    
    public String largestOddNumber(String num) {
        int a = 0;
        int first = 0;

        for(int i = 0; i < num.length(); i++) {

            char z = num.charAt(num.length() - i - 1);
            int y = z - '0';

            if(y % 2 == 0 && first == 0) {
                continue;
            }
            else {
                first += 1;
                a = num.length() - i - 1;
                break;
            }
        }

        if(first == 0) {
            return "";
        }

        num = num.substring(0, a + 1);

        return num;
    }
}



/*


So wht is happening is 

We r tryna find the first odd digit from right n then storing its position ..... once tht is done then removing any leading zeroes so we get the 
biggest odd number 


*/




