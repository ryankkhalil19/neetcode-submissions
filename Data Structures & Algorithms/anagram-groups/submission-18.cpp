#include <vector>
#include <string>
#include <unordered_map>
#include <array>

class Solution {
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs) {
        // Use an array of size 26 as a frequency key
        std::unordered_map<std::string, std::vector<std::string>> anagramGroups;
        
        for (const std::string& s : strs) {
            std::array<int, 26> count = {0};
            for (char c : s) {
                count[c - 'a']++;
            }
            // Convert frequency array to a string key
            std::string key(reinterpret_cast<char*>(count.data()), sizeof(count));
            anagramGroups[key].push_back(s);
        }

        std::vector<std::vector<std::string>> result;
        result.reserve(anagramGroups.size());
        for (auto& entry : anagramGroups) {
            result.push_back(std::move(entry.second));
        }
        return result;
    }
};
