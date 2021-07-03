#include <iostream>
#define FOR(N, M) for (int n = 0; n < N; n++) for (int m = 0; m < M; m++)
using namespace std;

int N, M;
char mp[1000][1000];
bool vis[1000][1000];

bool isValid(int r, int c) {
    return r >= 0 && r < N && c >= 0 && c < M && !vis[r][c] and mp[r][c] != '#';
}

void dfs(int r, int c) {
    vis[r][c] = true;
    if (isValid(r+1, c)) dfs(r+1, c);
    if (isValid(r-1, c)) dfs(r-1, c);
    if (isValid(r, c+1)) dfs(r, c+1);
    if (isValid(r, c-1)) dfs(r, c-1);
}

int main() {
    cin >> N >> M;
    FOR(N, M) {
        cin >> mp[n][m];
    }
    int count = 0;
    FOR(N, M) {
        if (!vis[n][m] and mp[n][m] != '#') {
            count += 1;
            dfs(n, m);
        }
    }
    cout << count << "\n";
    return 0;
}