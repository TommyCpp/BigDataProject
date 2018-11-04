#include "Util.hpp"

std::vector<std::string> Util::split(std::string& text, char separator)
{
    std::vector<std::string> result;
    int last = 0;
    for (int i = 0, n = text.size(); i < n; i++)
    {
        if (text[i] == separator)
        {
            if (i - last > 0)
            {
                auto s = text.substr(last, i - last);
                result.push_back(s);
            }
            last = i + 1;
        }
    }
    if (last != static_cast<int>(text.size()))
    {
        result.push_back(text.substr(last, text.size()));
    }
    return result;
}
