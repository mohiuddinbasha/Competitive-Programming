import java.util.*;
class Node{
	int value;
	ArrayList<Edge> edges;
	Node(int value){
		this.value = value;
		edges = new ArrayList<Edge>();
	}
} 

class Edge{
	int value;
	Node node_from;
	Node node_to;
	Edge(int value,Node node_from, Node node_to){
		this.value = value;
		this.node_from = node_from;
		this.node_to = node_to;
	}
}

public class Graph_Representation{
	ArrayList<Node> nodes;
	ArrayList<Edge> edges;
	Graph_Representation(){
		this.nodes = new ArrayList<Node>();
		this.edges = new ArrayList<Edge>();
	}

	public void insert_node(int value){
		Node new_node = new Node(value);
		this.nodes.add(new_node);
	}

	public void insert_edge(int val, int node_from_val, int node_to_val){
		Node from_found = null;
		Node to_found = null;
		for(int i = 0; i < this.nodes.size(); i++){
			if(node_from_val == nodes.get(i).value){
				from_found = nodes.get(i);
			}
			if(node_to_val == nodes.get(i).value){
				to_found = nodes.get(i);
			}
		}
		if(from_found == null){
			from_found = new Node(node_from_val);
			this.nodes.add(from_found);
		}
		if(to_found == null){
			to_found = new Node(node_to_val);
			this.nodes.add(to_found);
		}
		Edge new_edge = new Edge(val, from_found, to_found);
		from_found.edges.add(new_edge);
		to_found.edges.add(new_edge);
		this.edges.add(new_edge);

	}

	public ArrayList<ArrayList<Integer>> get_edge_list(){
		// """Don't return a list of edge objects!
        // Return a list of list that looks like this:
        // [Edge Value, From Node Value, To Node Value]"""
		ArrayList<ArrayList<Integer>> r = new ArrayList<ArrayList<Integer>>();
		for (int i = 0; i < edges.size(); i++) {
			Edge edge = edges.get(i);
			ArrayList<Integer> temp = new ArrayList<>();
			temp.add(edge.value);
			temp.add(edge.node_from.value);
			temp.add(edge.node_to.value);
			r.add(temp);
		}
        return r;
	}

	public ArrayList<ArrayList<Integer>> get_adjacency_list(){
		// """Don't return any Node or Edge objects!
        // You'll return a list of lists.
        // The indecies of the outer list represent
        // "from" nodes.
        // Each section in the list will store a list of To Node
		ArrayList<ArrayList<Integer>> r = new ArrayList<ArrayList<Integer>>();
		int max = -1;
		for (int i = 0; i < nodes.size(); i++) {
			if (nodes.get(i).value > max) {
				max = nodes.get(i).value;
			}
		}
		for (int i = 0; i <= max; i++) {
			r.add(new ArrayList<>());
		}
		for (int i = 0; i < nodes.size(); i++) {
			Node from = nodes.get(i);
			ArrayList<Integer> temp = new ArrayList<>();
			for (int j = 0; j < edges.size(); j++) {
				Edge edge = edges.get(j);
				if (edge.node_from == from) {
					temp.add(edge.node_to.value);
				}
			}
			r.set(from.value, temp);
		}
		return r;

	}

	public ArrayList<ArrayList<Integer>> get_adjacency_matrix(){
		// """Return a matrix, or 2D list.
        // Row numbers represent from nodes,
        // column numbers represent to nodes.
        // Store the edge values in each spot,
        // and a 0 if no edge exists."""
		
		ArrayList<ArrayList<Integer>> r = new ArrayList<ArrayList<Integer>>();
		int max = -1;
		for (int i = 0; i < nodes.size(); i++) {
			if (nodes.get(i).value > max) {
				max = nodes.get(i).value;
			}
		}
		for (int i = 0; i <= max; i++) {
			ArrayList<Integer> temp = new ArrayList<>();
			for (int j = 0; j <= max; j++) {
				temp.add(0);
			}
			r.add(temp);
		}
		for (int i = 0; i < edges.size(); i++) {
			Edge edge = edges.get(i);
			ArrayList<Integer> temp = r.get(edge.node_from.value);
			temp.set(edge.node_to.value, edge.value);
			r.set(edge.node_from.value, temp);
		}
		return r;
	}

	public static void main(String[] args) {
		Graph_Representation graph = new Graph_Representation();
		graph.insert_edge(100, 1, 2);
		graph.insert_edge(101, 1, 3);
		graph.insert_edge(102, 1, 4);
		graph.insert_edge(103, 3, 4);
		ArrayList<ArrayList<Integer>> r= graph.get_adjacency_matrix();
		System.out.println(r);
	}
}