import os

import FileEntity

SETTING_DIRECTORY = '/setting/'


class TextFileEditor:

    def __init__(self):
        self.f_working_directory = ''
        self.f_source = ''

    @property
    def working_directory(self) -> str:
        return self.f_working_directory

    @property
    def source(self) -> str:
        return self.f_source

    @property
    def target(self) -> str:
        if 0 == len(self.f_working_directory):
            return ''
        if 0 == len(self.f_source):
            return ''
        if 0 > self.f_source.rfind('.'):
            return ''
        if not self.f_source.startswith(self.f_working_directory):
            return ''
        return self.f_source[len(self.f_working_directory) - 1:self.f_source.rfind('.')]

    @property
    def action(self) -> str:
        if 0 > self.f_source.rfind('.'):
            return ''
        return self.f_source[self.f_source.rfind('.') + 1:]

    @property
    def target_directory_exists(self) -> bool:
        return os.path.isdir(self.target[:self.target.rfind('/')])

    @property
    def target_directory_to_list(self) -> list:
        p_list = self.target.split('/')
        return p_list[1:len(p_list) - 1]

    @working_directory.setter
    def working_directory(self, arg: str):
        self.f_working_directory = arg + SETTING_DIRECTORY

    @source.setter
    def source(self, arg: str):
        self.f_source = arg

    def make_target_directory(self) -> None:
        d_list = self.target_directory_to_list
        p = '/'
        for item in d_list:
            p += item + '/'
            if os.path.isdir(p):
                continue
            os.mkdir(p)
        return None

    def source_to_list(self) -> list:
        if not os.path.isfile(self.source):
            return []
        source_file = FileEntity.FileEntity()
        source_file.path = self.source
        source_file.read()
        return source_file.content

    def append(self) -> None:
        if not self.target_directory_exists:
            self.make_target_directory()
        target_file = FileEntity.FileEntity()
        target_file.path = self.target
        source_file = self.source_to_list()
        if 0 == len(source_file):
            return None
        if os.path.isfile(self.target):
            target_file.append(source_file)
        else:
            target_file.rewrite(source_file)
        return None

    def replace(self) -> None:
        if not os.path.isfile(self.target):
            return None
        target_file = FileEntity.FileEntity()
        target_file.path = self.target
        target_file.read()
        source_file = self.source_to_list()
        new_content = []
        for line in target_file.content:
            if source_file[0] == line:
                new_content.extend(source_file)
                break
            else:
                new_content.append(line)
        target_file.content = new_content
        target_file.write()
        return None

    def run(self) -> None:
        if 'append' == self.action:
            self.append()
        elif 'replace' == self.action:
            self.replace()
        return None


class Runner:

    def __init__(self):
        self.f_working_directory = os.path.dirname(__file__)
        self.SETTING_DIR = self.f_working_directory + SETTING_DIRECTORY
        self.f_target = []

    @property
    def target(self) -> list:
        return self.f_target

    def gather_targets(self) -> None:
        d = os.walk(self.SETTING_DIR)
        for c, d, f in d:
            if 0 < len(f):
                for item in f:
                    self.f_target.append(c + '/' + item)
        return None

    def run(self) -> None:
        self.gather_targets()
        e = TextFileEditor()
        e.working_directory = self.f_working_directory
        for item in self.target:
            e.source = item
            e.run()
        return None
