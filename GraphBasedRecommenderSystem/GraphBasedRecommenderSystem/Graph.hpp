#ifndef GRAPH_HPP
#define GRAPH_HPP
#include <string>
#include <unordered_map>
#include <vector>
using std::string;
using std::unordered_map;
using std::vector;

class Edge
{
public:
    int src;
    int dest;
    int weight;
    Edge(int src, int dest, int weight)
        : src{src}
        , dest{dest}
        , weight{weight}
    {
    }
};

class Graph
{
public:
    vector<vector<Edge>> edges;
    vector<string> keywords;
    unordered_map<string, int> keywordIndex;
    unordered_map<string, vector<int>> keywordMap;
    vector<string> links;
    vector<string> headers;
    Graph();
    void fromFile(string path, bool skipFirstLine);
    void loadConnections(string path, bool skipFirstLine);
    void search(string keyword);
};

#endif // GRAPH_HPP
