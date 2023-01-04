/*
Concept: BFS

먹이까지의 최단거리 계산 이후 가장 상단 왼쪽의 먹이를 골라 먹음
*/

#include<iostream>
#include<queue>

using namespace std;

queue<pair<int, int>> q;
queue<pair<int, int>> target_q;
int vst[21][21];
int tb[21][21];
int N;
int sz = 2;
int sz_cnt = 0;
pair<int, int> st;
int answer = 0;

int dx[] = {0, -1, 1, 0};
int dy[] = {-1, 0, 0, 1};

bool isTarget(int x, int y) {
    if(0 < tb[y][x] && tb[y][x] < sz) return true;
    else return false;
}

bool isValid(int x, int y) {
    if (x < 0 || y < 0 || N <= x || N <= y) return false;
    if (vst[y][x] == 1) return false;
    if (tb[y][x] > sz) return false;
    return true;
}

int main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    cin >> N;

    for(int i = 0; i < N; ++i) {
        for(int j = 0; j < N; ++j) {
            cin >> tb[i][j];
            if (tb[i][j] == 9) pair<int, int>(j, i).swap(st);
        }
    }

    int x = st.first;
    int y = st.second;
    int nextX, nextY;
    q.emplace(x, y);
    tb[y][x] = 0;
    
    // BFS
    int level = -1;
    while(q.size()) {
        int it = q.size();
        level += 1;
        target_q = queue<pair<int, int>>();
        for(int i = 0; i < it; ++i) {
            x = q.front().first;
            y = q.front().second;
            q.pop();

            if(isTarget(x, y)) target_q.emplace(x, y);

            for(int j = 0; j < 4; ++j) {
                nextX = x + dx[j];
                nextY = y + dy[j];

                if(isValid(nextX, nextY)) {
                    q.emplace(nextX, nextY);
                    vst[nextY][nextX] = 1;
                }
            }
        }
        
        // 가장 상단 왼쪽 먹이 찾음
        if(target_q.size() == 0) {
                continue;
            }
        else if(target_q.size() == 1) {
            nextX = target_q.front().first;
            nextY = target_q.front().second;
            target_q.pop();
        }
        else {
            nextX = target_q.front().first;
            nextY = target_q.front().second;
            target_q.pop();

            while(target_q.size()) {
                int tempX = target_q.front().first;
                int tempY = target_q.front().second;
                target_q.pop();

                if(tempY < nextY) {
                    nextX = tempX;
                    nextY = tempY;
                }
                if(tempY == nextY && tempX < nextX) {
                    nextX = tempX;
                    nextY = tempY;
                }
            }
        }
        
        tb[nextY][nextX] = 0;
        // 사이즈 check
        if (sz == ++sz_cnt) {
            sz++;
            sz_cnt = 0;
        }
        answer += level;
        level = -1;
        // queue와 visit table 초기화
        q = queue<pair<int, int>>();
        fill(&vst[0][0], &vst[20][20], 0);
        q.emplace(nextX, nextY);
        vst[nextY][nextX] = 1;
    }

    cout << answer << "\n";
    return 0;
}
