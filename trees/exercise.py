class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        # Currently not checking for duplicates
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, type):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        if type == "name":
            print(prefix + self.data["name"])

        if type == "designation":
            print(prefix + self.data["title"])

        if type == "both":
            print(prefix + self.data["name"] + " (" + self.data["title"] + ")")

        if self.children:
            for child in self.children:
                child.print_tree(type)


def build_product_tree():
    root = TreeNode({"name": "Nilupul", "title": "CEO"})

    cto = TreeNode({"name": "Chinmay", "title": "CTO"})

    hr_head = TreeNode({"name": "Gels", "title": "HR Head"})
    hr_head.add_child(TreeNode({"name": "Peter", "title": "Recruitment Manager"}))
    hr_head.add_child(TreeNode({"name": "Waqas", "title": "Policy Manager"}))

    inf_head = TreeNode({"name": "Vishwa", "title": "Infrastructure Head"})
    inf_head.add_child(TreeNode({"name": "Dhaval", "title": "Cloud Manager"}))
    inf_head.add_child(TreeNode({"name": "Abhijit", "title": "App Manager"}))

    app_head = TreeNode({"name": "Aamir", "title": "Application Head"})

    cto.add_child(inf_head)
    cto.add_child(app_head)

    root.add_child(cto)
    root.add_child(hr_head)

    return root


if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree("both")
    pass
