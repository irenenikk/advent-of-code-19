#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

#define N (100001)
map<string, int> indices;
map<int, string> ind2name;
vector<int> tree[N];

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

void dfs(int node, int parent, int fromStart) {
    if (ind2name[node] == "SAN") {
        // -2 because the first and last orbits are not taken into account 
        cout << fromStart-2 << "\n";
    }
    for (auto next : tree[node]) {
        if (next == parent) continue;
        dfs(next, node, fromStart+1);
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
            ind2name[j] = parent;
        }
        j++;
        if (indices.count(child) == 0) {
            indices[child] = j;
            ind2name[j] = child;
        }
        j++;
        int parentInd = indices[parent];
        int childInd = indices[child];
        tree[parentInd].push_back(childInd);
        tree[childInd].push_back(parentInd);
    }
}

int main() {
    vector<string> input = getInput();
    buildTree(input);
    int start = indices["YOU"];
    dfs(start, 0,  0);
    return 0;
}