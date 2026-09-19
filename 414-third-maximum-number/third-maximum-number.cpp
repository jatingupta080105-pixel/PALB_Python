class Solution {
public:
    int thirdMax(vector<int>& nums) {

        long long v1 = LLONG_MIN;
        long long v2 = LLONG_MIN;
        long long v3 = LLONG_MIN;

        for (int i = 0; i < nums.size(); i++) {

            if (nums[i] == v1 || nums[i] == v2 || nums[i] == v3) {
                continue;
            }

            if (nums[i] > v1) {
                v3 = v2;
                v2 = v1;
                v1 = nums[i];
            }
            else if (nums[i] > v2) {
                v3 = v2;
                v2 = nums[i];
            }
            else if (nums[i] > v3) {
                v3 = nums[i];
            }
        }

        if (v3 == LLONG_MIN) {
            return v1;
        }

        return v3;
    }
};