# HW 5 - Binary Search Tree

import random
import matplotlib.pyplot as plt
from collections import Counter


class _Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a distinct key into the BST."""
        new_node = _Node(key)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if key <= current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:  # Keys are distinct, so key > current.key
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, key):
        """Return True if key exists, otherwise False."""
        found, _ = self.search_with_comparisons(key)
        return found

    def search_with_comparisons(self, key):
        """
        Return (found, comparisons).

        Each visited node counts as one key comparison. The count is
        meaningful for successful searches; it is also returned on failure.
        """
        current = self.root
        comparisons = 0

        while current is not None:
            comparisons += 1
            if key == current.key:
                return True, comparisons
            if key < current.key:
                current = current.left
            else:
                current = current.right

        return False, comparisons

    def inorder_traversal(self):
        """Return the keys in ascending order."""
        result = []
        stack = []
        current = self.root

        while current is not None or stack:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.key)
            current = current.right

        return result

    def height(self):
        """Return the maximum node depth; an empty tree has height -1."""
        if self.root is None:
            return -1

        max_depth = -1
        stack = [(self.root, 0)]

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))

        return max_depth

    def node_depths(self):
        """Return a dictionary mapping each key to its depth."""
        depths = {}
        if self.root is None:
            return depths

        stack = [(self.root, 0)]
        while stack:
            node, depth = stack.pop()
            depths[node.key] = depth

            if node.left is not None:
                stack.append((node.left, depth + 1))
            if node.right is not None:
                stack.append((node.right, depth + 1))

        return depths
    
    def __str__(self):
        if self.root is None:
            return "(empty tree)"

        lines = []

        def add_lines(node, prefix="", is_left=False):
            if node is None:
                return

            # Display the right subtree above this node.
            add_lines(node.right, prefix + ("│   " if is_left else "    "), False)

            branch = "└── " if is_left else "┌── "
            lines.append(prefix + branch + str(node.key))

            # Display the left subtree below this node.
            add_lines(node.left, prefix + ("    " if is_left else "│   "), True)

        # Draw the root without a branch symbol.
        def draw(node, prefix=""):
            if node.right is not None:
                draw(node.right, prefix + "    ")
            lines.append(prefix + str(node.key))
            if node.left is not None:
                draw(node.left, prefix + "    ")

        draw(self.root)
        return "\n".join(lines)

def random_stack(n, seed):
    """Return a list of 1 through N in random order (used as a stack)."""
    if n < 0:
        raise ValueError("n must be non-negative")

    rng = random.Random(seed)
    return rng.sample(range(1, n + 1), n)

def build_ascending_bst(n):
    if n < 1:
        raise ValueError("n must be at least 1")

    bst_in_order = BinarySearchTree()

    for i in range (1, n + 1):
        bst_in_order.insert(i)
    return bst_in_order

def build_random_bst(n, seed):
    if n < 1:
        raise ValueError("n must be at least 1")

    bst_random = BinarySearchTree()
    rdm_stack = random_stack(n, seed)
    for i in range(0, n):
        bst_random.insert(rdm_stack.pop())
    return bst_random

def build_balanced_bst(bst, lst):
    if not lst:
        return bst
    else:
        middle_node = len(lst) // 2
        bst.insert(lst[middle_node])
        left_list = lst[:middle_node]
        right_list = lst[middle_node + 1:]
        build_balanced_bst(bst, left_list)
        build_balanced_bst(bst, right_list)
    return bst

def insertion_order_experiments(n):
    if n < 1:
        raise ValueError("n must be at least 1")

    # Build the ascending tree
    ascending_bst = build_ascending_bst(n)

    # Build the 10 random trees with different seeds
    random_trees = []
    for i in range(12, 12 + 10):
        random_bst = build_random_bst(n, i)
        random_trees.append(random_bst)

    # Build the balanced tree
    balanced_bst = BinarySearchTree()
    lst = []
    for i in range(1, n + 1):
        lst.append(i)
    balanced_bst = build_balanced_bst(balanced_bst, lst)

    #####################################################
    #                                                   #
    #           Find the heights of each tree           #
    #                                                   #
    #####################################################
    # Ascending
    ascending_tree_height = ascending_bst.height()

    # 10 Random Trees
    random_tree_heights = []
    for i in range(0, 10):
        random_tree_heights.append(random_trees[i].height())
    random_avg_tree_height = sum(random_tree_heights) / len(random_trees)


    # Balanced
    balanced_tree_height = balanced_bst.height()

    #####################################################
    #                                                   #
    #    Find the average node depths of each tree      #
    #                                                   #
    #####################################################
    # Ascending tree
    ascending_dict_node_depth = ascending_bst.node_depths()
    ascending_avg_node_depth = sum(ascending_dict_node_depth.values()) / n

    # Random Trees
    random_tree_avg_node_depths = []
    random_avg_node_depth_dicts = []
    for i in range(0, 10):
        random_avg_node_depth_dicts.append(random_trees[i].node_depths())
        random_tree_avg_node_depths.append(0)
        for j in range(1, n + 1):
            random_tree_avg_node_depths[i] += random_avg_node_depth_dicts[i][j]

    for i in range(0, 10):
        random_tree_avg_node_depths[i] /= n

    random_trees_avg_node_depth = sum(random_tree_avg_node_depths) / len(random_tree_avg_node_depths)

    # Balanced Tree
    balanced_dict = balanced_bst.node_depths()
    balanced_avg_node_depth = sum(balanced_dict.values()) / n

    #####################################################
    #                                                   #
    #    Find the average comparisons of each tree      #
    #                                                   #
    #####################################################
    # Ascending tree
    ascending_comparisons = []
    for i in range(1, n + 1):
        ascending_comparisons.append(ascending_bst.search_with_comparisons(i)[1])
    ascending_avg_comparisons = sum(ascending_comparisons) / n

    # Random Trees
    random_tree_avg_comparisons = []

    for i in range(10):
        total_comparisons = 0

        for j in range(1, n + 1):
            total_comparisons += random_trees[i].search_with_comparisons(j)[1]

        random_tree_avg_comparisons.append(total_comparisons / n)

    # Average across the 10 random trees
    random_trees_avg_comparison = (
            sum(random_tree_avg_comparisons) / len(random_tree_avg_comparisons)
    )

    # Balanced Trees
    balanced_comparisons = []
    for i in range(1, n + 1):
        balanced_comparisons.append(balanced_bst.search_with_comparisons(i)[1])

    balanced_avg_comparisons = sum(balanced_comparisons) / n

    return [ascending_bst,
            random_trees,
            balanced_bst,
            ascending_tree_height,
            ascending_avg_node_depth,
            ascending_avg_comparisons,
            random_tree_heights,
            random_avg_tree_height,
            random_tree_avg_node_depths,
            random_trees_avg_node_depth,
            random_tree_avg_comparisons,
            random_trees_avg_comparison,
            balanced_tree_height,
            balanced_avg_node_depth,
            balanced_avg_comparisons]



# Part 2. Insertion-Order Experiments
returned_lists = []

for N in [100, 500, 1000, 2000]:
    returned_lists.append(insertion_order_experiments(N))


# PLOTS
n = [100, 500, 1000, 2000]
# BST Height Comparison
sorted_height = [returned_lists[0][3], returned_lists[1][3], returned_lists[2][3], returned_lists[3][3]]
random_height = [returned_lists[0][7], returned_lists[1][7], returned_lists[2][7], returned_lists[3][7]]
balanced_height = [returned_lists[0][12], returned_lists[1][12], returned_lists[2][12], returned_lists[3][12]]
plt.plot(n, sorted_height, marker='o', label='Sorted')
plt.plot(n, random_height, marker='s', label='Random')
plt.plot(n, balanced_height, marker='^', label='Balanced')
plt.xlabel('Number of Nodes (N)')
plt.ylabel('BST Height')
plt.title('BST Height Comparison')
plt.legend()
plt.grid(True)
plt.show()

# BST Comparisons Comparison
sorted_comparison = [returned_lists[0][5], returned_lists[1][5], returned_lists[2][5], returned_lists[3][5]]
random_comparison = [returned_lists[0][11], returned_lists[1][11], returned_lists[2][11], returned_lists[3][11]]
balanced_comparison = [returned_lists[0][14], returned_lists[1][14], returned_lists[2][14], returned_lists[3][14]]
plt.plot(n, sorted_height, marker='o', label='Sorted')
plt.plot(n, random_height, marker='s', label='Random')
plt.plot(n, balanced_height, marker='^', label='Balanced')
plt.xlabel('Number of Nodes (N)')
plt.ylabel('BST Comparisons')
plt.title('BST Comparisons Comparison')
plt.legend()
plt.grid(True)
plt.show()

# My trees for N = 1000 are returned_lists[2]
# My random see for returned_lists[2][5][0] is 12
# First I get my trees
ascend_bst = returned_lists[2][0]
random_bst = returned_lists[2][1][0]
balanced_bst = returned_lists[2][2]

# Then get the node depths
ascend_depths_dict = ascend_bst.node_depths()
random_depths_dict = random_bst.node_depths()
balanced_depths_dict = balanced_bst.node_depths()

# Then just get the depth of the nodes
ascend_depths = ascend_depths_dict.values()
random_depths = random_depths_dict.values()
balanced_depths = balanced_depths_dict.values()

# Then count how many of each depth there are
ascend_counts = dict(Counter(ascend_depths))
random_counts = dict(Counter(random_depths))
balanced_counts = dict(Counter(balanced_depths))

plt.bar(ascend_counts.keys(), ascend_counts.values())
plt.xlabel("Node Depth")
plt.ylabel("Counts")
plt.title('Ascending Tree')
plt.xticks(list(ascend_counts.keys()))
plt.ylim(0, 2)
plt.show()

plt.bar(random_counts.keys(), random_counts.values())
plt.xlabel("Node Depth")
plt.ylabel("Counts")
plt.title('Random Tree, seed = 12')
plt.xticks(list(random_counts.keys()))
plt.ylim(0, 550)
plt.show()

plt.bar(balanced_counts.keys(), balanced_counts.values())
plt.xlabel("Node Depth")
plt.ylabel("Counts")
plt.title('Balanced Tree')
plt.xticks(list(balanced_counts.keys()))
plt.ylim(0, 550)
plt.show()