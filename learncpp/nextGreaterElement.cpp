#include <iostream>
#include <vector>
#include <map>

using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    map<int, int> nexts;
    nexts[nums2[nums2.size()-1]] = -1;
    int curMax = -1;
    for (int i = nums2.size()-2; i >= 0; i--) {
        if (nums2[i] < nums2[i+1]) {
            curMax = nums2[i+1];
        }
        nexts[i] = curMax;
    }
    vector<int> queries(nums1.size(), 0);
    for (int i = 0; i < queries.size(); i++) {
        queries[i] = nexts[nums1[i]];
    }
    return queries;
}