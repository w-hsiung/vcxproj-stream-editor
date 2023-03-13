import vcxproj


@vcxproj.coroutine
def print_project_guid():
    while True:
        action, params = yield
        print(action, params)
        if action == "start_elem" and params["name"] == "ProjectGuid":
            action, params = yield
            assert action == "chars"
            print("Project GUID is ", params["content"])


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
    vcxproj.check_file("Ex1.vcxproj", print_project_guid)
    vcxproj.filter_file("Ex1.vcxproj", remove_warning_level, "Ex1.stripped.vcxproj")
    return


if __name__ == "__main__":
    main()
