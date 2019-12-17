#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define N (100001)
map<string, int> indices;
vector<int> tree[N];
int orbits[N];

vector<string> getInput(){
    ifstream inputFile;
    inputFile.open("input.txt");
    vector<string> output;
    if (inputFile.is_open()) {
        while (!inputFile.eof()) {
            string x;
            inputFile >> x;
            output.push_back(x);
        }
    }
    inputFile.close();
    return output;
}

void dfs(int node, int parent) {
    orbits[node] += orbits[parent]+1;
    for (auto next : tree[node]) {
        dfs(next, node);
    }
}

void buildTree(vector<string> input){
    int j = 0;
    for(int i=0; i<input.size(); i++){
        string info = input[i];
        int delim = info.find(')');
        string parent = info.substr(0, delim);
        string child = info.substr(delim+1, info.size());
        // map each string to an index for practical tree traversing
        if (indices.count(parent) == 0) {
            indices[parent] = j;
        }
        j++;
        if (indices.count(child) == 0) {
            indices[child] = j;
        }
        j++;
        int parentInd = indices[parent];
        int childInd = indices[child];
        tree[parentInd].push_back(childInd);
    }
}

int main() {
    vector<string> input = getInput();
    buildTree(input);
    int com = indices["COM"];
    // start from node orbiting the center of mass
    int start = tree[com][0];
    dfs(start, 0);
    int total = 0;
    for(int i=0; i<N; i++){
        total += orbits[i];
    }
    cout << total << '\n';
    return 0;
}