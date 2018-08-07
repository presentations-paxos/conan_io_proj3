from conans import ConanFile, CMake

class Proj3Conan(ConanFile):
    name = "proj3"
    # version = 0.0.1 

    license = "Public Domain"
    url = "http://gitlab:8080/demo/proj3"
    description = "Say Hello and Goodbye Executable"
    settings = "cppstd", "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    requires = "proj1/[>0.0.0-0,<0.0.1]@gitlab/develop", "proj2/[>0.0.0-0,<0.0.1]@gitlab/develop"

    def source(self):
        self.run("git clone http://gitlab:8080/demo/proj3.git")

    def configure(self):
        if self.settings.os == "Linux" and not self.settings.os.distro:
            raise ConanException("On Linux, 'distro' setting must be defined.")

        if self.settings.os == "Macos" and not self.settings.os.version:
            raise ConanException("On macOS, 'version' must be defined.")

        if self.settings.os == "Windows" and not self.settings.os.subsystem:
            raise ConanException("On Windows, 'subsystem' must be defined.")

    def build(self):
        cmake = CMake(self,generator="Ninja")
        cmake.configure(source_folder="proj3")
        cmake.build()

    def package(self):
        self.copy("proj3", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["proj3"]
