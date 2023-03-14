import vcxproj


@vcxproj.coroutine
def print_elements():
    while True:
        action, params = yield
        if action == "start_elem" and params["name"] == "ItemDefinitionGroup":
            tup = params["attrs"]
            print(params["name"], tup["Condition"])
            continue
        if action == "start_elem" and params["name"] == "OutDir":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "IntDir":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "TypeLibraryName":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "PrecompiledHeaderOutputFile":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "AssemblerListingLocation":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "ObjectFileName":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "ProgramDataBaseFileName":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "OutputFile":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue
        if action == "start_elem" and params["name"] == "ProgramDatabaseFile":
            name = params["name"]
            action, params = yield
            print(name, params["content"])
            continue


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
    print("*****************************")
    vcxproj.check_file("Ex1.vcxproj", print_elements)
    return


if __name__ == "__main__":
    main()
