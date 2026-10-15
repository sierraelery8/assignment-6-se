
class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node.
        right (EmployeeNode): The right child node.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    '''

    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        # check if the tree has a team lead
        if self.root is None:
            print("Tree is empty. Add a team lead first.")
            return False

        # searching from the root
        if current_node is None:
            current_node = self.root

        # check if current employee is the manager
        if current_node.name == manager_name:

            if side == "left":
                if current_node.left is None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the LEFT of {manager_name}.")
                    return True
                else:
                    print(f"{manager_name} already has a LEFT subordinate.")
                    return False

            elif side == "right":
                if current_node.right is None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f"{employee_name} added to the RIGHT of {manager_name}.")
                    return True
                else:
                    print(f"{manager_name} already has a RIGHT subordinate.")
                    return False

            else:
                print("Invalid side. Enter left or right.")
                return False

        # search the left branch continuously (recursion)
        if current_node.left is not None:
            if self.insert(
                manager_name, employee_name, side, current_node.left
            ):
                return True

        # search the right branch continuously (recursion)
        if current_node.right is not None:
            if self.insert(
                manager_name, employee_name, side, current_node.right
            ):
                return True

        # report a missing manager at the root
        if current_node is self.root:
            print(f"Manager '{manager_name}' was not found.")

        return False

    def print_tree(self, node=None, level=0):
        # Start at the root when called for the first time.
        if node is None:
            if level == 0:
                node = self.root
            else:
                return

        # handle an empty tree
        if node is None:
            print("The company directory is empty.")
            return

        # print the employee with indentation
        indent = "    " * level
        print(f"{indent}- {node.name}")

        # print the left and right branches continuously (recursion)
        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)


# Test your code here


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input(
                "Should this employee be on the LEFT or RIGHT of the manager? "
            )
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳 Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break

        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    company_directory()
