from conans import ConanFile, CMake
import os

class Proj3Conan(ConanFile):
    name = os.environ['PROJ3_NAME']
    version = os.environ['PROJ3_VER']

    license = "Public Domain"
    url = "http://gitlab:8080/demo/proj3"
    description = "Say Hello and Goodbye Executable"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    requires = "proj1/[>0.0.0-0,<0.0.1]@gitlab/develop", "proj2/[>0.0.0-0,<0.0.1]@gitlab/develop"

    def source(self):
        self.run("git clone http://gitlab:8080/demo/proj3.git")

    def build(self):
        cmake = CMake(self,generator="Ninja")
        cmake.configure(source_folder="proj3")
        cmake.build()

    def package(self):
        self.copy("proj3", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["proj3"]
