#include <proj1/hello.hpp>
#include <proj2/goodbye.hpp>

#include <iostream>

namespace proj3 {
    std::string hello_goodbye(const std::string& name) {
        return proj1::hello(name) + "\n" + proj2::goodbye(name);
    }
}

int main(const int argc, char const * const argv[]) {
    std::cout << hello_goodbye("Austin");
    return 0;
}
