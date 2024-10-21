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

# Функція для знаходження найменшого значення в BST
def find_minimum(root):
    if root is None:
        return None  # Дерево порожнє

    current = root
    while current.left is not None:
        current = current.left

    return current.val

# Тестуємо функцію на прикладі
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert(root, key)

print(f"Найменше значення у дереві: {find_minimum(root)}")
