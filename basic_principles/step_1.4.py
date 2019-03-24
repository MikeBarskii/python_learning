# https://stepik.org/lesson/24460/step/9?unit=6766
def add_arg_to_namespace(namespace, arg):
    args[namespace][0].add(arg)


def create_new_namespace(namespace, parent_namespace="global"):
    args[parent_namespace][1].add(namespace)
    args[namespace] = (set(), set())


def find_parent_namespace(namespace):
    for key, value in args.items():
        if namespace in value[1]:
            return key


def find_var_in_namespaces(namespase, var):
    if var in args[namespase][0]:
        return namespase
    elif namespase == "global":
        return None
    else:
        parent_namespace = find_parent_namespace(namespase)
        return find_var_in_namespaces(parent_namespace, var)


number_of_commands = int(input())

args = dict()
args['global'] = (set(), set())

for _ in range(number_of_commands):
    command, namesp, arg = input().split()

    if command == "add":
        add_arg_to_namespace(namesp, arg)
    elif command == "create":
        create_new_namespace(namesp, arg)
    elif command == "get":
        if namesp not in args.keys():
            print("Namespace " + namesp + " is not exist!")
            continue
        namespace_of_arg = find_var_in_namespaces(namesp, arg)
        print(namespace_of_arg)
