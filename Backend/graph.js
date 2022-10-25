
class Node {
    constructor(value) {
        this.value = value;
        this.adjacents = [];
    }

    addAdjacent(node) {
        this.adjacents.push(node);
    }

    removeAdjacent(node) {
        const index = this.adjacents.indexOf(node);
        if (index > -1) {
            this.adjacents.splice(index, 1);
            return node;
        }
    }

    getAdjacents() {
        return this.adjacents;
    }

    isAdjacent(node) {
        return this.adjacents.indexOf(node) > -1;
    }

    getValue() {
        return this.value;
    }
}

class Graph {
    constructor(edgeDirection = Graph.DIRECTED) {
        this.nodes = new Map();
        this.edgeDirection = edgeDirection;
    }

    addEdge(source, destination) {
        const sourceNode = this.addVertex(source);
        const destinationNode = this.addVertex(destination);

        source.addAdjacent(destinationNode);

        if (this.edgeDirection === Graph.UNDIRECTED) {
            destinationNode.addAdjacent(sourceNode);
        }

        return [sourceNode, destinationNode];
    }

    addVertex(value) {
        if(this.nodes.has(value)) {
            return this.nodes.get(value);
        } else {
            const vertex = new Node(value);
            this.nodes.set(value, vertex);
            return vertex;
        }
    }

    removeVertex(value) {
        const current = this.nodes.get(value);
        if(current) {
            for(const node of this.nodes.values()) {
                node.removeAdjacent(current);
            }
        }
        return this.nodes.delete(value)
    }

    removeEdge(source, destination) {
        const sourceNode = this.nodes.get(source);
        const destinationNode = this.nodes.get(destination);

        if(sourceNode && destinationNode) {
            sourceNode.removeAdjacent(destinationNode);

            if(this.edgeDirection === Graph.UNDIRECTED) {
                destinationNode.removeAdjacent(sourceNode)
            }
        }

        return [sourceNode, destinationNode];
    }

    *depthFirstTraversal(start) {
        const visited = new Map();
        const visitList = new Queue();

        visitList.add(first);

        while(!visitList.isEmpty()) {
            const node = visitList.remove();
            if(node && !visited.has(node)) {
                yield node;
                visited.set(node);
                node.getAdjacents().forEach(adj => visitList.add(adj));
            }
        }
    }

    dijkstra(node) {
        const visited = new Map();
        const distances = new Map();
        const previous = new Map();

        for(const vertex of this.nodes.values()) {
            distances.set(vertex, Number.POSITIVE_INFINITY);
            previous.set(vertex, null);
        }

        distances.set(node, 0);

        const queue = new PriorityQueue();
        queue.add(node, 0);

        while(!queue.isEmpty()) {
            const current = queue.remove();
            visited.set(current, true);

            for(const neighbor of current.getAdjacents()) {
                const alt = distances.get(current) + current.getValue().distanceTo(neighbor.getValue());
                if(alt < distances.get(neighbor)) {
                    distances.set(neighbor, alt);
                    previous.set(neighbor, current);
                    queue.add(neighbor, alt);
                }
            }
        }

        return {
            distances,
            previous
        }
    }

}



Graph.UNDIRECTED = Symbol('undirected graph');
Graph.DIRECTED = Symbol('directed graph');