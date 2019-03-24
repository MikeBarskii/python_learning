# https://stepik.org/lesson/24462/step/7?unit=6768
def add_class_and_parents(class_name, *parent_classes):
    classes_and_parents[class_name] = []


number_of_classes = int(input())
classes_and_parents = dict()

for _ in range(number_of_classes):
    class_definition = input()
    class_definition_values = class_definition.split(":")
    if len(class_definition_values) == 1:
        add_class_and_parents(class_definition_values[0])
    else:
        add_class_and_parents(class_definition_values[0], class_definition_values[1].strip().split(' '))

print(classes_and_parents)
