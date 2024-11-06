#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>
#include <cstring>

using namespace std;

const int INF = 200000;
vector<int> dijkstra(int start, int n, const vector<vector<pair<int, int>>>& adj) {
    vector<int> dist(n + 1, INF);  // distances initialized to INF
    dist[start] = 0;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int u = pq.top().second;
        int d = pq.top().first;
        pq.pop();

        if (d > dist[u]) continue;
   
        for (const auto& edge : adj[u]) {
            int v = edge.first;
            int weight = edge.second;
            
           
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
    
    return dist;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int s;  
    cin >> s;
    
    while (s--) {
        int n; 
        cin >> n;
        
        unordered_map<string, int> city_index; 
        vector<string> cities(n + 1); 
        vector<vector<pair<int, int>>> adj(n + 1);  
        
        int city_count = 1;
        
      
        for (int i = 1; i <= n; ++i) {
            string city_name;
            cin >> city_name;
            city_index[city_name] = city_count;
            cities[city_count] = city_name;
            int p;  
            cin >> p;
  
            for (int j = 0; j < p; ++j) {
                int nr, cost;
                cin >> nr >> cost;
                adj[city_count].push_back({nr, cost});
            }
            ++city_count;
        }
        
        int r; 
        cin >> r;
        for (int i = 0; i < r; ++i) {
            string city1, city2;
            cin >> city1 >> city2;
            int src = city_index[city1];
            int dest = city_index[city2];

            vector<int> dist = dijkstra(src, n, adj);
            cout << dist[dest] << '\n';
        }

        if (s > 0) {
            cout << '\n';
        }
    }
    
    return 0;
}


"""PYTHON"""

import heapq
import sys

INF = float('inf')

def dijkstra(n, graph, start):
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        dists, u = heapq.heappop(pq)

        if dists > dist[u]:
            continue

        for v, cost in graph[u]:
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
                heapq.heappush(pq, (dist[v], v))

    return dist

def solve():
    s = int(input())
    for _ in range(s):
        n = int(input())
        city_ind = {}
        graph = [[] for _ in range(n + 1)]

        for i in range(1, n + 1):
            city = input().strip()
            city_ind[city] = i
            p = int(input())
            for _ in range(p):
                nr, cost = map(int, input().split())
                graph[i].append((nr, cost))

        r = int(input())
        for _ in range(r):
            source, des = input().split()
            idx = city_ind[source]
            des_ind = city_ind[des]

            dist = dijkstra(n, graph, idx)
            result = dist[des_ind]
            if result == INF:
                print(-1)
            else:
                print(result)

        if __name__ == "__main__":
            print()
solve()