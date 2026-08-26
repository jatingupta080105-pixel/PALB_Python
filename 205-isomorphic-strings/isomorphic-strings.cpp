class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if (s.length() != t.length())
            return false;
        unordered_map<char, char> mpST;
        unordered_map<char, char> mpTS;

        for (int i = 0; i < s.length(); i++) {
            char a = s[i];
            char b = t[i];
            if (mpST.count(a) && mpST[a] != b)
                return false;
            if (mpTS.count(b) && mpTS[b] != a)
                return false;
            mpST[a] = b;
            mpTS[b] = a;
        }
        return true;
    }
};