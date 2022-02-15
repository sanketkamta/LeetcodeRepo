class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy = INT_MAX;
        int res = 0;
        for (int p:prices){
            buy = min(p, buy);
            res = max((p-buy), res);
        }
        return res;
    }
};