import java.util.prefs.NodeChangeListener;

class Node {
	public int value;
	public Node left, right;
	public Node(int value) {
		this.value = value;
		this.left = null;
		this.right = null;
	}
}

public class BinaryTree {
	public Node root;
	
	public BinaryTree(int value) {
        root = new Node(value);
	}

	public boolean search(int value) {
		// Your code goes here
		return search_Node(root, value);
	}

	private boolean search_Node(Node node, int value) {
		// Your code goes here
		if (node == null) {
			return false;
		} else if (node.value == value) {
			return true;
		} else {
			boolean left = search_Node(node.left, value);
			boolean right = search_Node(node.right, value);
			if (left || right) {
				return true;
			} else {
				return false;
			}
		}
	}
}