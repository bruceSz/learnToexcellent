ingredients = 'spam eggs apple'
line = '-'*10
def iter_elements(getter,action):
    for element in getter():
        action(element)
        print(line)


def rev_elements(getter,action):
    for element in getter()[::-1]:
        action(element)
        print(line)


def get_list():
    return ingredients.split()
def get_lists():
    return [list(x) for x in ingredients.split()]

def print_item(item):
    print(item)
def reverse_item(item):
    print(item[::-1])


def make_template(skeleton,getter,action):
    def template():
        skeleton(getter,action)
    return template

templates = [make_template(s,g,a)
             for g in (get_list,get_lists)
             for a in (print_item,reverse_item)
             for s in (iter_elements,rev_elements)]

for template in templates:
    template()
    
