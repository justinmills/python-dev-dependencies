import dev_dependencies as devdeps


def test_version_is_set() -> None:
    print(f"Package version is {devdeps.VERSION} / {devdeps.__version__}")
    assert devdeps.VERSION is not None
    assert devdeps.__version__ is not None


# We can't really test the unset case since it's all global state. Once the
# module is imported, the value is set and the code won't be executed again.
