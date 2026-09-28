class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::map<std::array<int, 26>, std::vector<std::string>> charCountMap;

        for (const auto& str: strs) {
            std::array<int, 26> count{};

            for (const auto& c: str) {
                ++count[c - 'a'];
            }

            charCountMap[count].push_back(str);
        }
        std::vector<std::vector<std::string>> result;
        result.reserve(charCountMap.size());
        for (auto& [key, group] : charCountMap) {
            result.push_back(std::move(group));
        }
        return result;
    }
};