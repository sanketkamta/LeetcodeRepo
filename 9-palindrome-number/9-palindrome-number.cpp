class Solution {
public:
    bool isPalindrome(int x) {
        string inp = to_string(x);
        int i = 0;
        int j = inp.length() - 1;
        while(i<j){
            if(inp[i] != inp[j])
                return false;
            i++;
            j--;
        }
        return true;
    };
};