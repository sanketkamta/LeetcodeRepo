class Solution {
public:
    int maxArea(vector<int>& height) {
        int max = 0;
        int i = 0;
        int j = height.size() - 1;
        while(i < j){
            if(height[i] < height[j]){
                if (max < ((j - i) * (height[i])))
                    max = ((j - i) * (height[i]));
                i++;
            }
            else{
                if (max < ((j - i) * (height[j])))
                    max = ((j - i) * (height[j]));
                j--;
            }
        }
        return max;
    }
};