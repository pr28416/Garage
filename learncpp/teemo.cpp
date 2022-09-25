#include <iostream>
#include <vector>

using namespace std;

int findPoisonedDuration(vector<int>& timeSeries, int duration) {
    int total{0};
    for (int i = 0; i < timeSeries.size(); i++) {
        total += duration;
        if (i < timeSeries.size() - 1) {
            total -= max(0, timeSeries[i]+duration-timeSeries[i+1]);
        }
    }
    return total;
}
/*
1 3
4 6



1 3
2 4


*/