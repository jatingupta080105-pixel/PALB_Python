class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();

        vector<bool> present(n + 1, false);

        for (int x : nums)
            present[x] = true;

        vector<int> ans;

        for (int i = 1; i <= n; i++) {
            if (!present[i])
                ans.push_back(i);
        }

        return ans;
    }
};