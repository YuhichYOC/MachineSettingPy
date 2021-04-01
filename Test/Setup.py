import os

import FileEntity


class Setup:

    def __init__(self):
        self.f_route_directory = ''
        self.TEST_DIR_01 = 'test01/'
        self.TEST_DIR_02 = 'test01/test02/'
        self.TEST_DIR_03 = 'test03/'
        self.TEST_DIR_04 = 'test03/test04/'
        self.TEST_DIR_05 = 'test03/test04/test05/'
        self.TEST_FILE_01 = 'file01'
        self.TEST_FILE_02_A = 'file02_a'
        self.TEST_FILE_02_B = 'file02_b'
        self.TEST_FILE_03 = 'file03'
        self.TEST_FILE_04_A = 'file04_a'
        self.TEST_FILE_04_B = 'file04_b'
        self.TEST_FILE_05 = 'file05'

    @property
    def route_directory(self) -> str:
        return self.f_route_directory

    @route_directory.setter
    def route_directory(self, arg: str):
        self.f_route_directory = arg

    def write_file_01(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_01):
            os.mkdir(self.route_directory + self.TEST_DIR_01)
        fe = FileEntity.FileEntity()
        fe.path = self.route_directory + self.TEST_DIR_01 + self.TEST_FILE_01
        fe.rewrite([
            'abc',
            'def',
            'ghi',
            'jkl',
        ])
        return None

    def write_file_02_a(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_02):
            os.mkdir(self.route_directory + self.TEST_DIR_02)
        fe = FileEntity.FileEntity()
        fe.path = self.route_directory + self.TEST_DIR_02 + self.TEST_FILE_02_A
        fe.rewrite([
            'mno',
            'pqr',
            'stu',
            'vwx',
            'yz1',
        ])
        return None

    def write_file_02_b(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_02):
            os.mkdir(self.route_directory + self.TEST_DIR_02)
        fe = FileEntity.FileEntity()
        fe.path = self.route_directory + self.TEST_DIR_02 + self.TEST_FILE_02_B
        fe.rewrite([
            '234',
            '567',
            '890',
            'abc',
        ])
        return None

    def write_file_03(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_03):
            os.mkdir(self.route_directory + self.TEST_DIR_03)
        fe = FileEntity.FileEntity()
        fe.path = self.route_directory + self.TEST_DIR_03 + self.TEST_FILE_03
        fe.rewrite([
            'def',
            'ghi',
            'jkl',
            'mno',
        ])
        return None

    def write_file_04_a(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_04):
            os.mkdir(self.route_directory + self.TEST_DIR_04)
        fe = FileEntity.FileEntity()
        fe.path = self.route_directory + self.TEST_DIR_04 + self.TEST_FILE_04_A
        fe.rewrite([
            'pqr',
            'stu',
            'vwx',
            'yz1',
            '234',
        ])
        return None

    def write_file_04_b(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_04):
            os.mkdir(self.route_directory + self.TEST_DIR_04)
        fe = FileEntity.FileEntity()
        fe.path = self.route_directory + self.TEST_DIR_04 + self.TEST_FILE_04_B
        fe.rewrite([
            '567',
            '890',
            'abc',
            'def',
        ])
        return None

    def write_file_05(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_05):
            os.mkdir(self.route_directory + self.TEST_DIR_05)
        fe = FileEntity.FileEntity()
        fe.path = self.route_directory + self.TEST_DIR_05 + self.TEST_FILE_05
        fe.rewrite([
            'ghi',
            'jkl',
            'mno',
            'pqr',
        ])
        return None

    def run(self) -> None:
        self.write_file_01()
        self.write_file_02_a()
        self.write_file_02_b()
        self.write_file_03()
        self.write_file_04_a()
        self.write_file_04_b()
        self.write_file_05()
        return None
