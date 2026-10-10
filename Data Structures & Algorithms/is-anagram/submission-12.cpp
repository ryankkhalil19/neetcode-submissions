#include <array>
#include <string_view>

class Solution {
    public:
    bool isAnagram(std::string& s, std::string& t) {
        std::array<uint8_t, 26> sCount{};
        std::array<uint8_t, 26> tCount{};

        for (char c : s) {
            ++sCount[c - 'a'];
        }

        for (char c : t) {
            ++tCount[c - 'a'];
        }

        return sCount == tCount;
    }
};