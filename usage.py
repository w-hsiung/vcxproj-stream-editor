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


@vcxproj.coroutine
def change_build_settings(target):
    while True:
        action, params = yield
        if action == "start_elem" and params["name"] == "WarningLevel":
            target.send((action, params))
            action, params = yield
            assert action == "chars"
            print(params["content"])
            params["content"] = "Level4"
            target.send((action, params))
            action, params = yield
            assert action == "end_elem"
            assert params["name"] == "WarningLevel"
            target.send((action, params))
            continue
        target.send((action, params))


def main():
    #vcxproj.filter_file("Ex1.vcxproj", remove_warning_level, "Ex1.new.vcxproj")
    vcxproj.filter_file("Ex2.vcxproj", change_build_settings, "Ex2.new.vcxproj")
    return


if __name__ == "__main__":
    main()
