# https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/editorial/?envType=daily-question&envId=2025-01-30


class Solution:
    # Main function to calculate the maximum number of groups for the entire graph
    def magnificentSets(self, n, edges):
        adj_list = [[] for _ in range(n)]
        parent = [-1] * n
        depth = [0] * n

        # Build the adjacency list and apply Union-Find for each edge
        for edge in edges:
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)
            self._union(edge[0] - 1, edge[1] - 1, parent, depth)

        num_of_groups_for_component = {}

        # For each node, calculate the maximum number of groups for its component
        for node in range(n):
            number_of_groups = self._get_number_of_groups(adj_list, node, n)
            if number_of_groups == -1:
                return -1  # If invalid split, return -1
            root_node = self._find(node, parent)
            num_of_groups_for_component[root_node] = max(
                num_of_groups_for_component.get(root_node, 0), number_of_groups
            )

        # Calculate the total number of groups across all components
        total_number_of_groups = sum(num_of_groups_for_component.values())
        return total_number_of_groups

    # Function to calculate the number of groups for a given component starting from srcNode
    def _get_number_of_groups(self, adj_list, src_node, n):
        nodes_queue = deque()
        layer_seen = [-1] * n
        nodes_queue.append(src_node)
        layer_seen[src_node] = 0
        deepest_layer = 0

        # Perform BFS to calculate the number of layers (groups)
        while nodes_queue:
            num_of_nodes_in_layer = len(nodes_queue)
            for _ in range(num_of_nodes_in_layer):
                current_node = nodes_queue.popleft()
                for neighbor in adj_list[current_node]:
                    # If neighbor hasn't been visited, assign it to the next layer
                    if layer_seen[neighbor] == -1:
                        layer_seen[neighbor] = deepest_layer + 1
                        nodes_queue.append(neighbor)
                    else:
                        # If the neighbor is already in the same layer, return -1 (invalid partition)
                        if layer_seen[neighbor] == deepest_layer:
                            return -1
            deepest_layer += 1
        return deepest_layer

    # Find the root of the given node in the Union-Find structure
    def _find(self, node, parent):
        while parent[node] != -1:
            node = parent[node]
        return node

    # Union operation to merge two sets
    def _union(self, node1, node2, parent, depth):
        node1 = self._find(node1, parent)
        node2 = self._find(node2, parent)

        # If both nodes already belong to the same set, no action needed
        if node1 == node2:
            return

        # Union by rank (depth) to keep the tree balanced
        if depth[node1] < depth[node2]:
            node1, node2 = node2, node1
        parent[node2] = node1

        # If the depths are equal, increment the depth of the new root
        if depth[node1] == depth[node2]:
            depth[node1] += 1


class Solution:

    # Main function to calculate the maximum number of magnificent sets
    def magnificentSets(self, n, edges):
        # Create adjacency list for the graph
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            # Transition to 0-index
            adj_list[edge[0] - 1].append(edge[1] - 1)
            adj_list[edge[1] - 1].append(edge[0] - 1)

        # Initialize color array to -1
        colors = [-1] * n

        # Check if the graph is bipartite
        for node in range(n):
            if colors[node] != -1:
                continue
            # Start coloring from uncolored nodes
            colors[node] = 0
            if not self._is_bipartite(adj_list, node, colors):
                return -1

        # Calculate the longest shortest path for each node
        distances = [
            self._get_longest_shortest_path(adj_list, node, n) for node in range(n)
        ]

        # Calculate the total maximum number of groups across all components
        max_number_of_groups = 0
        visited = [False] * n
        for node in range(n):
            if visited[node]:
                continue
            # Add the number of groups for this component to the total
            max_number_of_groups += self._get_number_of_groups_for_component(
                adj_list, node, distances, visited
            )

        return max_number_of_groups

    # Checks if the graph is bipartite starting from the given node
    def _is_bipartite(self, adj_list, node, colors):
        for neighbor in adj_list[node]:
            # If a neighbor has the same color as the current node, the graph is not bipartite
            if colors[neighbor] == colors[node]:
                return False
            # If the neighbor is already colored, skip it
            if colors[neighbor] != -1:
                continue
            # Assign the opposite color to the neighbor
            colors[neighbor] = (colors[node] + 1) % 2
            # Recursively check bipartiteness for the neighbor; return false if it fails
            if not self._is_bipartite(adj_list, neighbor, colors):
                return False
        # If all neighbors are properly colored, return true
        return True

    # Computes the longest shortest path (height) in the graph starting from the source node
    def _get_longest_shortest_path(self, adj_list, src_node, n):
        # Initialize a queue for BFS and a visited array
        nodes_queue = deque([src_node])
        visited = [False] * n
        visited[src_node] = True
        distance = 0

        # Perform BFS layer by layer
        while nodes_queue:
            # Process all nodes in the current layer
            for _ in range(len(nodes_queue)):
                current_node = nodes_queue.popleft()
                # Visit all unvisited neighbors of the current node
                for neighbor in adj_list[current_node]:
                    if visited[neighbor]:
                        continue
                    visited[neighbor] = True
                    nodes_queue.append(neighbor)
            # Increment the distance for each layer
            distance += 1

        # Return the total distance (longest shortest path)
        return distance

    # Calculates the maximum number of groups for a connected component
    def _get_number_of_groups_for_component(self, adj_list, node, distances, visited):
        # Start with the distance of the current node as the maximum
        max_number_of_groups = distances[node]
        visited[node] = True

        # Recursively calculate the maximum for all unvisited neighbors
        for neighbor in adj_list[node]:
            if visited[neighbor]:
                continue
            max_number_of_groups = max(
                max_number_of_groups,
                self._get_number_of_groups_for_component(
                    adj_list, neighbor, distances, visited
                ),
            )
        return max_number_of_groups
