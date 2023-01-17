//정답코드
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

queue<int> q;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    for(int i=0; i<speeds.size(); i++){
        q.push((99-progresses[i])/speeds[i]+1);
    }
    
    int max = q.front();
    int count = 1;
    
    while(!q.empty()){
        q.pop();
        
        if(max >= q.front()){
            count += 1;
        }
        else{
            answer.push_back(count);
            max = q.front();
            count = 1;
        }
    }
    
    answer.push_back(count-1);
    
    return answer;
}
