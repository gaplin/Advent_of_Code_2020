nums = list(map(lambda x: int(x) - 1, open('input2.txt').read()))

class Node:
    def __init__(self, value) -> None:
        self.value = value
    
nodes = []
for value in nums:
    nodes.append(Node(value))

n = len(nums)
for idx, node in enumerate(nodes):
    node.left = nodes[(idx - 1) % n]
    node.right = nodes[(idx + 1) % n]

def disconnect(node: Node, count: int) -> list:
    nodes_to_disconnect = []
    for _ in range(count):
        nodes_to_disconnect.append(node)
        node = node.right

    first_node = nodes_to_disconnect[0]
    last_node = nodes_to_disconnect[-1]

    left_neighbour = first_node.left
    right_neighbour = last_node.right

    left_neighbour.right = right_neighbour
    right_neighbour.left = left_neighbour

    first_node.left = None
    last_node.right = None

    return nodes_to_disconnect

def get_destination_cup(current_cup: Node, disconnected_cups: list, n: int) -> Node:
    usedValues = [x.value for x in disconnected_cups]
    label = (current_cup.value - 1) % n
    while label in usedValues:
        label = (label - 1) % n
    
    destination_cup = current_cup.right
    while destination_cup.value != label:
        destination_cup = destination_cup.right

    return destination_cup

def place_cups_clockwise(left_neighbour: Node, cups_to_place: list) -> None:
    right_neighbour = left_neighbour.right
    first_cup = cups_to_place[0]
    last_cup = cups_to_place[-1]

    left_neighbour.right = first_cup
    first_cup.left = left_neighbour

    right_neighbour.left = last_cup
    last_cup.right = right_neighbour

def make_a_move(current_cup: Node, n: int):
    clockwise_cup = current_cup.right
    disconnected_cups = disconnect(clockwise_cup, 3)
    destination_cup = get_destination_cup(current_cup, disconnected_cups, n)
    place_cups_clockwise(destination_cup, disconnected_cups)
    clockwise_cup = current_cup.right
    return clockwise_cup

def get_result(nodes: list, n: int) -> str:
    result = ''
    current_node = nodes[0]
    while current_node.value != 0:
        current_node = current_node.right

    current_node = current_node.right
    for _ in range(n - 1):
        result += str(current_node.value + 1)
        current_node = current_node.right
    return result

current_cup = nodes[0]

for _ in range(100):
    current_cup = make_a_move(current_cup, n)

result = get_result(nodes, n)

print(result)