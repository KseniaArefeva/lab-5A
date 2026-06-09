from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# ОСНОВНАЯ ЗАДАЧА
def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        preorder(root.left, result)
        preorder(root.right, result)
    return result

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result

def postorder(root, result=None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.value)
    return result

def level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
    return result

#ВАРИАТИВНАЯ ЧАСТЬ
def is_mirror(left_subtree, right_subtree):
    if not left_subtree and not right_subtree:
        return True
      
    if not left_subtree or not right_subtree:
        return False
   
    return (left_subtree.value == right_subtree.value) and \
           is_mirror(left_subtree.left, right_subtree.right) and \
           is_mirror(left_subtree.right, right_subtree.left)

def is_symmetric(root):
    if not root:
        return True
    return is_mirror(root.left, root.right)


def build_symmetric_tree():
    # Создаёт симметричное дерево:
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    return root

def build_asymmetric_tree():
    # Создаёт НЕсимметричное дерево
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(3) 
    return root

def build_mirror_symmetric_tree():
    # Зеркально-симметричное дерево (значения зеркальны):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    return root

def build_sample_tree():
    # Обычное дерево для демонстрации обходов:
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root

def print_tree_structure(title, root):
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    
    print("\n--- Обходы дерева (основная задача) ---")
    print(f"Прямой обход (preorder):     {preorder(root)}")
    print(f"Симметричный обход (inorder): {inorder(root)}")
    print(f"Обратный обход (postorder):   {postorder(root)}")
    
    levels = level_order(root)
    print(f"Обход в ширину (BFS):")
    for i, level in enumerate(levels, 1):
        print(f"  Уровень {i}: {level}")
    
    print("\n--- Вариативная часть №2 ---")
    sym_result = is_symmetric(root)
    print(f"Дерево симметрично относительно корня? {'ДА' if sym_result else 'НЕТ'}")

def main():
    # Тест
    
    # 1. Обычное дерево
    tree1 = build_sample_tree()
    print_tree_structure("ДЕРЕВО 1 (обычное, несимметричное)", tree1)
    
    # 2. Симметричное дерево 
    tree2 = build_symmetric_tree()
    print_tree_structure("ДЕРЕВО 2 (симметричное по структуре и значениям)", tree2)
    
    # 3. Несимметричное дерево
    tree3 = build_asymmetric_tree()
    print_tree_structure("ДЕРЕВО 3 (несимметричное, нарушена зеркальность)", tree3)
    
    # 4. Зеркально-симметричное дерево
    tree4 = build_mirror_symmetric_tree()
    print_tree_structure("ДЕРЕВО 4 (зеркально-симметричное)", tree4)
    
    # 5. Пустое дерево
    print(f"\n{'='*60}")
    print("ДЕРЕВО 5 (пустое)")
    print(f"{'='*60}")
    print("Пустое дерево симметрично? ДА (по определению)")
    print(f"Прямой обход: {preorder(None)}")
    print(f"Обход в ширину: {level_order(None)}")
    print(f"Проверка симметричности: {is_symmetric(None)}")

if __name__ == "__main__":
    main()
