# bst.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================
class Student:
    def __init__(self, number, name):
        self.grade = number
        self.name = name

    def __lt__(self, kq):
        return self.grade < kq.grade

    def __gt__(self, kq):
        return self.grade > kq.grade

    def __eq__(self, kq):
        return self.grade == kq.grade

    def __ge__(self, kq):
        return self.grade >= kq.grade

    def __str__(self):
        if self.grade is not None:
            return str(self.name + "," + str(self.grade))
    '''
    def __repr__(self):
        if self.grade is not None:
            return str(self.name + "," + str(self.grade))
    '''



class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add(self, val):
        """
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """

        new_node = TreeNode(val)  # initialize a new link
        new_node.val = val

        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            # go through nodes, moving left or right depending on size.
            while current is not None:
                if val < current.val:
                    if current.left is None:
                        # if value is less than current node, and next node is empty, add it as leaf
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif val >= current.val:
                    if current.right is None:
                        # if value is greater than or equal to current node, and next node is empty, add it as a leaf
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def in_order_traversal(self, cur_node=None, visited=None) -> []:
        """
            Perform in-order traversal of the tree and return a list of visited nodes
            """
        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.in_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for in-order traversal:
        # visit left subtree, store current node value, visit right subtree
        self.in_order_traversal(cur_node.left, visited)
        visited.append(cur_node.val)
        self.in_order_traversal(cur_node.right, visited)
        return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """

        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.pre_order_traversal(self.root, visited)

        if cur_node is None:
            return visited

        # preorder, so append to list before traversing left and then right
        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left, visited)
        self.pre_order_traversal(cur_node.right, visited)
        return visited


    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """

        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.post_order_traversal(self.root, visited)

        if cur_node is None:
            return visited
        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        # postorder, so append after first traversing left and then right
        visited.append(cur_node.val)
        return visited

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """
        if self.root is None:
            return False
        else:
            current = self.root
            while current is not None:
                if current.val == kq:
                    # if value is found, return True
                    return True

                # if value isn't found, check to see if it's less than or greater than current value, and then move
                # left or right accordingly
                if kq < current.val:
                    current = current.left
                elif kq >= current.val:
                    current = current.right
        # if the value wasn't found, return False
        return False

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """
        if self.root is None:
            return None
        else:
            # select node passed to function, return it's the node pointed to in its .left
            current = node
            while current is not None:
                if current.left is None:
                    return current
                current = current.left

    def get_parent(self, kq):
        """
        Helper function - returns the parent node of a node passed to it.
        :param kq: Node whose parent to search for
        :return: Parent node of kq
        """
        if self.root is None:
            return None
        else:
            current = self.root
            while current is not None:
                if current.val == kq:
                    # if the value is found, return the parent node (the previous node)
                    return parent
                # if value wasn't found, check to see if it's less than or greater than current value, and then move
                # left or right accordingly, passing along  the current node as the parent node
                if kq < current.val:
                    parent = current
                    current = current.left
                elif kq >= current.val:
                    parent = current
                    current = current.right

    def get_inorder_successor(self, right_tree_root):
        """

        :param right_tree_root: the root node to be used to find the in order successor
        :return: the in order successor
        """
        current = right_tree_root
        if current is None:
            return None
        while current is not None:
            if current.left is None:
                # traverse left in the tree until the next value is None - return that node
                return current
            current = current.left

    def remove(self, kq):
        """
        Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """

        if self.root is None:
            pass
        elif self.root.val == kq:
            # call remove_first if the node being referred to is the root
            self.remove_first()
        else:
            current = self.root
            while current is not None:
                if current.left is not None:
                    if current.left.val == kq:
                        if current.left.left is None and current.left.right is None:
                            # if the node to be removed has no subnodes, set the current node's left value to refer
                            # to None
                            current.left = None
                            return True
                        # get the in order successor
                        successor = self.get_inorder_successor(current.left)
                        if successor is None:
                            # if the successor of the next left value is none, set the current values .left to none
                            current.left = None
                        else:
                            # set the successor's right value to refer to the current node's left subnode's right
                            # subnode
                            successor.right = current.left.right
                            # set the current node's left value to refer to the successor named above
                            current.left = successor
                        return True

                if current.right is not None:
                    if current.right.val == kq:
                        if current.right.left is None and current.right.right is None:
                            # if the node to be removed has no subnodes, set the current node's right value to refer
                            # to None
                            current.right = None
                            return True
                        # get the in order successor
                        successor = self.get_inorder_successor(current.right)
                        if successor is None:
                            # if the successor of the next right value is none, set the current values .right to none
                            current.right = None
                        else:
                            # set the successor's right value to refer to the current node's right subnode's right
                            # subnode
                            successor.right = current.right.right
                            current.right = successor
                            # set the current node's right value to refer to the successor named above
                        return True

                # if the node to be removed hasn't been found, continue to move through the tree accordingly
                if kq < current.val:
                    current = current.left
                elif kq >= current.val:
                    current = current.right
            return False


    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        if self.root is None:
            return None
        else:
            return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        if self.root is None:
            return False
        elif self.root.right is None and self.root.left is None:
            self.root = None
            return True
        elif self.root.right is None:
            # conditional for when there is no right subtree
            current = self.root
            parent = None
            while current is not None:
                if current.left is None:
                    # move through the left nodes of the tree, when the leftmost node is found set
                    # successor to refer to it
                    successor = current
                    break
                parent = current
                current = current.left
            if parent is not None:
                # if the parent node exists, set its left value to refer to the successor's right subnode
                parent.left = successor.right
            # set the successor's right to refer to None
            successor.right = None
            # set the successor's left value to refer to the original roots left subnode
            successor.left = self.root.left
            self.root = successor
            return True
        else:
            # normal path for removing the root node
            current = self.root
            # grab the in order successor
            successor = self.get_inorder_successor(current.right)
            # grab the parent of the in order successor
            successor_parent = self.get_parent(successor.val)

            if successor == self.root.right:
                # if the in order successor is the right subnode of the root, set the successor's left value to
                # refer to the root's left value
                successor.left = self.root.left
                self.root = successor
            else:
                # if normal in order successor, reassign values appropriately - make the successor's parent point left
                # to the successor's right subnode, give the successor the left and right subnodes of the original root,
                # and reassign the successor to the root position.
                successor_parent.left = successor.right
                successor.left = self.root.left
                successor.right = self.root.right
                self.root = successor