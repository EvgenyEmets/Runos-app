from conans import ConanFile, tools

class L2LearningSwitchConan(ConanFile):
    name = "RunosApp"
    version = "0.1"
    settings = None
    description = "L3 RUNOS App"
    url = "None"
    license = "None"
    author = "None"
    topics = None

    def package(self):
        self.copy("*")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
