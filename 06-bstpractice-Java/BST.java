
class Node {
    public int value;
    public Node left, right;
    public Node(int value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

public class BST {
    public Node root;
    
    public BST(int value) {
        this.root = new Node(value);
    }

    public void insert(int value) {

    	insert(root, value);
    }

    private void insert(Node node, int value) {
        if (value < node.value) {
            if (node.left == null) {
                node.left = new Node(value);
                return;
            } else {
                insert(node.left, value);
            }
        } else {
            if (node.right == null) {
                node.right = new Node(value);
                return;
            } else {
                insert(node.right, value);
            }
        }
    }

    public boolean search(int value) {
        // Your code goes here
        if (root.value == value) {
            return true;
        }
        return search(root, value);
    }

    private boolean search(Node current, int value) {
    	// Your code goes here
    	if (current == null) {
            return false;
        } else if (current.value == value) {
            return true;
        } else {
            if (value < current.value) {
                return search(current.left, value);
            } else {
                return search(current.right, value);
            }
        }
    }

}