#include <iostream>
#include <vector>
#include <queue>
#include <omp.h>

using namespace std;

void BFS(const vector<vector<int>>& adj, int V, int start) {
    vector<bool> visited(V, false);
    queue<int> q;
    visited[start] = true;
    q.push(start);

    while (!q.empty()) {
        int u;
        #pragma omp parallel
        {
            #pragma omp single nowait
            {
                u = q.front();
                q.pop();
            }

            #pragma omp for
            for (int i = 0; i < adj[u].size(); ++i) {
                int v = adj[u][i];
                #pragma omp critical
                {
                    if (!visited[v]) {
                        visited[v] = true;
                        #pragma omp single nowait
                        {
                            q.push(v);
                        }
                    }
                }
            }
        }
        cout << u << " ";
    }
    cout << endl;
}

void DFS(const vector<vector<int>>& adj, int V, int u, vector<bool>& visited) {
    visited[u] = true;
    cout << u << " ";

    #pragma omp parallel for
    for (int i = 0; i < adj[u].size(); ++i) {
        int v = adj[u][i];
        if (!visited[v]) {
            #pragma omp critical
            {
                DFS(adj, V, v, visited);
            }
        }
    }
}

int main() {
    int V;
    cout << "Enter the number of vertices: ";
    cin >> V;

    vector<vector<int>> adj(V);

    int edgeCount;
    cout << "Enter the number of edges: ";
    cin >> edgeCount;

    cout << "Enter the edges (in format 'source destination'): \n";
    for (int i = 0; i < edgeCount; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u); // If the graph is undirected
    }

    int startVertex;
    cout << "Enter the starting vertex for traversal: ";
    cin >> startVertex;

    cout << "BFS traversal starting from node " << startVertex << ": ";
    BFS(adj, V, startVertex);
    cout << endl;

    cout << "DFS traversal starting from node " << startVertex << ": ";
    vector<bool> visited(V, false);
    DFS(adj, V, startVertex, visited);
    cout << endl;

    return 0;
}
