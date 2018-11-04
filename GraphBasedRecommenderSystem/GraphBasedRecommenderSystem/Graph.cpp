#include "Graph.hpp"
#include "Util.hpp"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <unordered_set>
Graph::Graph()
{
}

void Graph::fromFile(std::string path, bool skipFirstLine)
{
    std::ifstream stream(path);
    string line;
    std::getline(stream, line);
    if (skipFirstLine)
    {
        std::getline(stream, line);
    }
    while (!stream.fail())
    {
        auto items = Util::split(line, '\t');
        string header = items.at(0);
        string link = items.at(1);
        headers.push_back(header);
        links.push_back(link);
        int index = headers.size() - 1;
        for (auto keyword : Util::split(items.at(2), ','))
        {
            bool found = keywordMap.find(keyword) != keywordMap.end();
            if (found)
            {
                keywordMap[keyword].push_back(index);
            }
            else
            {
                keywordMap.insert({keyword, vector<int>()});
                keywords.push_back(keyword);
            }
        }
        std::getline(stream, line);
    }
}

void Graph::loadConnections(std::string path, bool skipFirstLine)
{
    for (int i = 0, n = keywords.size(); i < n; i++)
    {
        keywordIndex.insert({keywords.at(i), i});
    }
    this->edges = vector<vector<Edge>>(keywords.size());
    std::ifstream stream(path);
    string line;
    std::getline(stream, line);
    if (skipFirstLine)
    {
        std::getline(stream, line);
    }
    while (!stream.fail())
    {
        auto items = Util::split(line, ',');
        auto word1 = items.at(0);
        auto word2 = items.at(1);
        auto count = std::stoi(items.at(2));
        // TO DO: check whether the keyword is loaded.
        int index1 = keywordIndex[word1];
        int index2 = keywordIndex[word2];
        edges[index1].push_back(Edge(index1, index2, count));
        edges[index2].push_back(Edge(index2, index1, count));
        std::getline(stream, line);
    }
}

void Graph::search(std::string keyword)
{
    using std::cout;
    using std::endl;
    class QueryResult
    {
    public:
        int node;
        int weight;
        vector<int> headers;
        vector<int> links;
        QueryResult(int node, int weight)
            : node{node}
            , weight{weight}
        {
        }
        QueryResult(int node, int weight, vector<int> headers,
                    vector<int> links)
            : node{node}
            , weight{weight}
            , headers{headers}
            , links{links}
        {
        }
    };

    bool found = keywordIndex.find(keyword) != keywordIndex.end();
    if (found)
    {
        auto queryNode = [this](const string& keyword,
                                int weight) -> QueryResult {
            QueryResult result(keywordIndex[keyword], weight);

            for (auto index : keywordMap[keyword])
            {
                result.headers.push_back(index);
                result.links.push_back(index);
            }
            return result;
        };
        vector<QueryResult> choices;
        const int INT_MAX = 2147483647;
        choices.push_back(queryNode(keyword, INT_MAX));
        for (Edge edge : edges[keywordIndex[keyword]])
        {
            choices.push_back(queryNode(keywords[edge.dest], edge.weight));
        }
        std::sort(
            choices.begin(), choices.end(),
            [](QueryResult& x, QueryResult& y) { return x.weight > y.weight; });
        std::unordered_set<int> resultSet;
        for (int i = 0, n = choices.size(); i < std::min(5, n); i++)
        {
            QueryResult& result = choices.at(i);
            for (int k = 0, m = result.headers.size(); k < std::min(5, m); k++)
            {
                if (resultSet.find(result.headers.at(k)) != resultSet.end())
                {
                    continue;
                }
                else
                {
                    resultSet.insert(result.headers.at(k));
                    if (result.node == keywordIndex[keyword])
                    {
                        cout << "0: ";
                    }
                    else
                    {
                        cout << "1: ";
                    }
                    cout << headers.at(result.headers.at(k)) << '\t';
                    cout << links.at(result.links.at(k)) << endl;
                }
            }
        }
    }
    else
    {
        cout << "keyword is not found!" << endl;
    }
}
