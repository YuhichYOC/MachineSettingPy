import os


class Clean:

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

    def clean_file_01(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_01):
            return None
        os.remove(self.route_directory + self.TEST_DIR_01 + self.TEST_FILE_01)
        os.rmdir(self.route_directory + self.TEST_DIR_01)
        return None

    def clean_file_02(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_02):
            return None
        os.remove(self.route_directory + self.TEST_DIR_02 + self.TEST_FILE_02_A)
        os.remove(self.route_directory + self.TEST_DIR_02 + self.TEST_FILE_02_B)
        os.rmdir(self.route_directory + self.TEST_DIR_02)
        return None

    def clean_file_03(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_03):
            return None
        os.remove(self.route_directory + self.TEST_DIR_03 + self.TEST_FILE_03)
        os.rmdir(self.route_directory + self.TEST_DIR_03)
        return None

    def clean_file_04(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_04):
            return None
        os.remove(self.route_directory + self.TEST_DIR_04 + self.TEST_FILE_04_A)
        os.remove(self.route_directory + self.TEST_DIR_04 + self.TEST_FILE_04_B)
        os.rmdir(self.route_directory + self.TEST_DIR_04)
        return None

    def clean_file_05(self) -> None:
        if not os.path.isdir(self.route_directory + self.TEST_DIR_05):
            return None
        os.remove(self.route_directory + self.TEST_DIR_05 + self.TEST_FILE_05)
        os.rmdir(self.route_directory + self.TEST_DIR_05)
        return None

    def run(self) -> None:
        self.clean_file_05()
        self.clean_file_04()
        self.clean_file_03()
        self.clean_file_02()
        self.clean_file_01()
        return None
