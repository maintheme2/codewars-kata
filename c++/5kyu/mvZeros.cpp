#include <iostream>
#include <vector>
#include <algorithm>

std::vector<int> move_zeroes(const std::vector<int>& input) {
    std::vector<int>& result = const_cast<std::vector<int>&>(input);
    size_t zerosCounter = std::count(result.begin(), result.end(), 0);
    result.erase(remove(result.begin(), result.end(), 0), result.end());
    for (int i = 0; i < zerosCounter; i++) {
        result.push_back(0);
    }
    return result;
}

int main() {
    move_zeroes({1, 0, 1, 2, 0, 1, 3});
}