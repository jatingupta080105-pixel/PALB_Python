class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int, int> freq;

        for (int x : arr1)
            freq[x]++;

        vector<int> ans;

        // Elements according to arr2
        for (int x : arr2) {
            while (freq[x] > 0) {
                ans.push_back(x);
                freq[x]--;
            }
        }

        // Remaining elements
        vector<int> remaining;

        for (auto it : freq) {
            while (it.second > 0) {
                remaining.push_back(it.first);
                it.second--;
            }
        }

        sort(remaining.begin(), remaining.end());

        for (int x : remaining)
            ans.push_back(x);

        return ans;
    }
};