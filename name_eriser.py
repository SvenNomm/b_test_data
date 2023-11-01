# this function alters file name by erising reference to particular human name
import re


def name_eriser(name):
    print(name)
    names = re.split(r'\s|-', name)
    regex = r"\b[A-Z]\w*"
    matches = []
    matches.append(re.findall(regex, name))
    print(matches)
    print(names)
    new_name = ""
    #new_name = str(new_name)
    for elt in names:
        if elt not in matches[0]:
            if len(new_name) > 0:
                new_name=new_name + '-'

            new_name=new_name + str(elt)

    #new_name.append('.json')
    #print('.'.join(map(str, new_name)))

    print(new_name)
    #print("That's all folks")
    return new_name

