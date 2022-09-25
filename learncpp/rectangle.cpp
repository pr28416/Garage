#include <iostream>
#include <vector>
#include <cmath>

class Solution {
public:
    std::vector<int> constructRectangle(int area) {
        std::vector<int> v(2, 0);
        for (int sq = (int)sqrt(area); sq > 0; sq--) {
            if (area % sq == 0) {
                v[0] = area / sq;
                v[1] = sq;
                break;
            }
        }
        return v;
    }
};

int main(int argc, char* argv[]) {
    std::cout << argv[1] - '0' << "\n";
    return 0;
}