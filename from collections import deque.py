from collections import deque

# Вузол дерева
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

# Бінарне дерево магазинів
class ShopTree:
    def __init__(self):
        self.root = None

    # Додавання елемента в дерево
    def insert(self, name):
        new_node = Node(name)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        while True:
            if name < current.name:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break
            elif name > current.name:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break
            else:
                # Якщо такий магазин уже є
                print(f"Магазин '{name}' вже існує.")
                break

    # Пошук магазину
    def search(self, name):
        current = self.root
        while current:
            if name == current.name:
                return True
            elif name < current.name:
                current = current.left
            else:
                current = current.right
        return False

    # Видалення елемента
    def delete(self, name):
        self.root = self._delete_rec(self.root, name)

    def _delete_rec(self, node, name):
        if not node:
            return node

        if name < node.name:
            node.left = self._delete_rec(node.left, name)
        elif name > node.name:
            node.right = self._delete_rec(node.right, name)
        else:
            # Випадок 1: немає дітей
            if not node.left and not node.right:
                return None
            # Випадок 2: один нащадок
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            # Випадок 3: два нащадки
            min_node = self._min_value_node(node.right)
            node.name = min_node.name
            node.right = self._delete_rec(node.right, min_node.name)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Обхід дерева (in-order)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.name)
            self.inorder(node.right)

    def print_tree(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.print_tree(node.left)
        print(node.name)
        if node.right:
            self.print_tree(node.right)


# --- Демонстрація роботи ---
if __name__ == "__main__":
    tree = ShopTree()
    shops = ["Сільпо","АТБ", "Це Наше", "ВелМарт"]

    print("Додавання магазинів:")
    for s in shops:
        tree.insert(s)

    print("\nОбхід дерева (in-order):")
    tree.print_tree(tree.root)


    print("\nПошук 'Фора':", "знайдено" if tree.search("Фора") else "не знайдено")
    print("Пошук 'Копійка':", "знайдено" if tree.search("Копійка") else "не знайдено")

    print("\nВидалення 'Новус'...")
    tree.delete("Новус")
