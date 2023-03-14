import vcxproj


@vcxproj.coroutine
def print_project_guid():
    while True:
        action, params = yield
        if action == "start_elem" and params["name"] == "ProjectGuid":
            action, params = yield
            assert action == "chars"
            print("Project GUID is ", params["content"])


def main():
    vcxproj.check_file("Ex1.vcxproj", print_project_guid)
    return


if __name__ == "__main__":
    main()
