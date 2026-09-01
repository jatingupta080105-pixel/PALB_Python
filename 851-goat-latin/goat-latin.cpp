class Solution {
public:
    string toGoatLatin(string sentence) {
        stringstream ss(sentence);
        string word;
        string ans;
        int count = 1;
        while (ss >> word) {
            char c = tolower(word[0]);

            if (!(c == 'a' || c == 'e' || c == 'i' ||
                  c == 'o' || c == 'u')) {
                word = word.substr(1) + word[0];
            }
            word += "ma";
            word += string(count, 'a');

            if (!ans.empty())
                ans += " ";
            ans += word;
            count++;
        }
        return ans;
    }
};