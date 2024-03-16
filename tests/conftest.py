from pytest import fixture


@fixture
def hello_world_str() -> str:
    return "Hello, World!"
