import os

import FileEntity


class Runner:

    def __init__(self):
        self.SETTING_DIR = os.path.dirname(__file__) + '/setting/'
        self.f_target = []

    @property
    def target(self) -> list:
        return self.f_target

    def gather_targets(self) -> None:
        d = os.walk(self.SETTING_DIR)
        s = len(self.SETTING_DIR) - 1
        for c, d, f in d:
            if 0 < len(f):
                for item in f:
                    if 2 > item.rfind('.'):
                        continue
                    self.f_target.append([
                        c[s:] + '/' + item[:item.rfind('.')],
                        c + '/' + item,
                        item[item.rfind('.') + 1:],
                    ])
        return None

    def append(self, i: int) -> None:
        append_file = FileEntity.FileEntity()
        append_file.path = self.target[i][1]
        append_file.read()
        target_file = FileEntity.FileEntity()
        target_file.path = self.target[i][0]
        target_file.append(append_file.content)
        return None

    def replace(self, i: int) -> None:
        replace_file = FileEntity.FileEntity()
        replace_file.path = self.target[i][1]
        replace_file.read()
        target_file = FileEntity.FileEntity()
        target_file.path = self.target[i][0]
        target_file.read()
        new_content = []
        for line in target_file.content:
            if replace_file.content[0] == line:
                new_content.extend(replace_file.content)
                break
            else:
                new_content.append(line)
        target_file.content = new_content
        target_file.write()
        return None

    def run(self) -> None:
        count = len(self.target)
        for i in range(count):
            if 'append' == self.target[i][2]:
                self.append(i)
            elif 'replace' == self.target[i][2]:
                self.replace(i)
        return None
