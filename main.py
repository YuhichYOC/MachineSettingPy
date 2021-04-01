import Runner

from Test import Setup, Clean

ROUTE_DIR = '/home/ubuntu/'


def run() -> None:
    r = Runner.Runner()
    r.gather_targets()
    r.run()
    return None


def test_setup() -> None:
    s = Setup.Setup()
    s.route_directory = ROUTE_DIR
    s.run()
    return None


def test_clean() -> None:
    c = Clean.Clean()
    c.route_directory = ROUTE_DIR
    c.run()
    return None


if __name__ == '__main__':
    run()
