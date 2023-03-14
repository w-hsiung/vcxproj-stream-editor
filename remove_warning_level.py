import vcxproj


@vcxproj.coroutine
def remove_warning_level(target):
    while True:
        action, params = yield
        if action == "start_elem" and params["name"] == "WarningLevel":
            action, params = yield
            assert action == "chars"
            action, params = yield
            assert action == "end_elem"
            assert params["name"] == "WarningLevel"
            continue
        target.send((action, params))


def main():
    vcxproj.filter_file("Ex1.vcxproj", remove_warning_level, "Ex1.new.vcxproj")
    return


if __name__ == "__main__":
    main()
