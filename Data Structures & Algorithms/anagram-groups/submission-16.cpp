#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <ranges>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        
        std::unordered_map<std::string, std::vector<std::string>> anagramGroups;

        for (const std::string& s : strs) {
            std::string key = s;
            std::ranges::sort(key);
            anagramGroups[key].push_back(s);
        }

        std::vector<std::vector<std::string>> result;
        result.reserve(anagramGroups.size());
        for (auto& entry : anagramGroups
                            | std::views::values) {
            result.push_back(std::move(entry));
        }

        return result;
    }
};