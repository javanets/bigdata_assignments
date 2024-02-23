import os
import sys
import shutil
from dataclasses import dataclass


@dataclass
class Test:
    name: str
    path: str


class TestEnv:
    def __init__(self, script_file_name, solution_file_name):
        self.script_file_name = script_file_name
        self.solution_file_name = solution_file_name
        
        self.solution_dir = os.path.abspath(os.getcwd())
        self.script_dir = os.path.dirname(os.path.abspath(self.script_file_name))

        solution_file_found = False
        for _, _, filenames in os.walk(self.solution_dir):
            for filename in filenames:
                if filename == self.solution_file_name:
                    solution_file_found = True

        if not solution_file_found:
            raise ValueError(f"File {self.solution_file_name} doesn't exist in folder {self.solution_dir}")
        
        self.solution_path = os.path.join(self.solution_dir, solution_file_name)

        solution_dir_parts = self.solution_dir.split("/")
        self.module_name = solution_dir_parts[-2]
        self.problem_name = solution_dir_parts[-1]

        self.tests_dir = os.path.join(self.script_dir, "__testdata__", self.module_name, self.problem_name)
        if not os.path.exists(self.tests_dir):
            raise ValueError(f"Path {self.tests_dir} doesn't exist")

        test_names = sorted(os.listdir(os.path.join(self.tests_dir, "tests")))
        self.tests = [Test(name, os.path.join(self.tests_dir, "tests", name)) for name in test_names]
