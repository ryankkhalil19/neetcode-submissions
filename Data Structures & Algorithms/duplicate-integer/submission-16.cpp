#include <unordered_set>
#include <vector>

class Solution {
public:
    bool hasDuplicate(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        seen.reserve(nums.size());
        
        for (auto val : nums) {
            if (!seen.insert(val).second) return true;
        }
        return false;
    }
};