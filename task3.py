class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Вставка нового вузла в дерево
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Функція для знаходження суми всіх значень у дереві
def sum_tree(root):
    if root is None:
        return 0
    return root.val + sum_tree(root.left) + sum_tree(root.right)

# Тестуємо функцію на прикладі
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert(root, key)

print(f"Сума всіх значень у дереві: {sum_tree(root)}")
