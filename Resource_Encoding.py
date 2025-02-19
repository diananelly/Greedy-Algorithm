import heapq

class HuffmanNode:
    """represents a node in the Huffman tree"""

    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq  # frequency of the character
        self.char = char  # character (None for internal nodes)
        self.left = left  # left child
        self.right = right  # right child

    def __lt__(self, other):
        """defines priority queue (min-heap) comparison based on frequency"""
        return self.freq < other.freq


def huffman_coding(sensor_data):
    """
    constructs Huffman codes for given sensor data

    parameters:
    sensor_data (dict): dictionary with sensor types as keys and their frequencies as values

    returns:
    dict: Huffman codes for each sensor type
    """
    heap = [HuffmanNode(freq, char) for char, freq in sensor_data.items()]  # create a min-heap with leaf nodes
    heapq.heapify(heap)  # convert list to a priority queue

    while len(heap) > 1:
        left = heapq.heappop(heap)  # node with smallest frequency
        right = heapq.heappop(heap)  # second smallest frequency

        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)  # create a new internal node
        heapq.heappush(heap, merged)  # add merged node back to heap

    root = heap[0]  # root of the Huffman tree
    codes = {}

    def assign_codes(node, code):
        """recursive function to assign Huffman codes"""
        if node.char is not None:
            codes[node.char] = code  # assign code to leaf node
            return
        if node.left:
            assign_codes(node.left, code + '0')  # left branch is 0
        if node.right:
            assign_codes(node.right, code + '1')  # right branch is 1

    assign_codes(root, '')  # generate Huffman codes
    return codes


def calculate_encoded_size(sensor_data, codes):
    """
    estimates the total encoded size given the Huffman codes

    parameters:
    sensor_data (dict): dictionary with sensor types and their frequencies
    codes (dict): dictionary with sensor types and their Huffman codes

    returns:
    int: total encoded data size in bits
    """
    return sum(sensor_data[char] * len(codes[char]) for char in sensor_data)  # calculate total bits required


if __name__ == "__main__":
    num_sensors = int(input("Enter the number of sensor types: "))  # get number of sensor types
    sensor_data = {}

    for _ in range(num_sensors):
        sensor_type = input("Enter sensor type (single character or string): ")  # get sensor type
        frequency = int(input(f"Enter frequency for {sensor_type}: "))  # get frequency
        sensor_data[sensor_type] = frequency  # store in dictionary

    codes = huffman_coding(sensor_data)  # generate Huffman codes

    print("\nHuffman Codes:")
    for char in sorted(codes.keys()):
        print(f"Character: {char}, Code: {codes[char]}")  # display generated Huffman codes

    total_bits = calculate_encoded_size(sensor_data, codes)  # calculate encoded size
    print(f"\nEstimated Total Encoded Size: {total_bits} bits")  # display estimated size
