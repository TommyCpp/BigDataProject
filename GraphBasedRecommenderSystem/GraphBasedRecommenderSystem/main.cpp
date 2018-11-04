#include "Graph.hpp"
#include "Util.hpp"
#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
    Graph graph;
    graph.fromFile("header_link_data.tsv", true);
    graph.loadConnections("word_network.csv", true);
    //    cout << "edge count = " << graph.edges.size() << endl;
    string line;
    cout << "query: ";
    cin >> line;
    while (!cin.fail())
    {
        if (line == "quit")
        {
            break;
        }
        else
        {
            system("clear");
            cout << "query: " << line << endl;
            graph.search(line);
            cout << "query: ";
            cin >> line;
        }
    }
    return 0;
}
