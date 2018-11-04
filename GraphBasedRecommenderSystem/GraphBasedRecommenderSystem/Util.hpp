#ifndef UTIL_HPP
#define UTIL_HPP
#include <string>
#include <vector>
class Util
{
public:
    static std::vector<std::string> split(std::string& text, char separator);
};

#endif // UTIL_HPP
