import heapq


class HuffmanNode:
    """Represents a node in the Huffman tree."""

    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq  # Frequency of the character
        self.char = char  # Character (None for internal nodes)
        self.left = left  # Left child
        self.right = right  # Right child

    def __lt__(self, other):
        """Defines priority queue (min-heap) comparison based on frequency."""
        return self.freq < other.freq


def huffman_coding(sensor_data):
    """
    Constructs Huffman codes for given sensor data.

    Parameters:
    sensor_data (dict): Dictionary with sensor types as keys and their frequencies as values.

    Returns:
    dict: Huffman codes for each sensor type.
    """
    # Step 1: Create a priority queue (min-heap) with leaf nodes for each sensor type
    heap = [HuffmanNode(freq, char) for char, freq in sensor_data.items()]
    heapq.heapify(heap)

    # Step 2: Build the Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)  # Node with smallest frequency
        right = heapq.heappop(heap)  # Second smallest frequency

        # Create a new internal node with combined frequency
        merged = HuffmanNode(left.freq + right.freq, left=left, right=right)
        heapq.heappush(heap, merged)

    # Step 3: Traverse the Huffman tree to generate codes
    root = heap[0]
    codes = {}

    def assign_codes(node, code):
        """Recursive function to assign Huffman codes."""
        if node.char is not None:
            codes[node.char] = code  # Leaf node, assign the code
            return
        if node.left:
            assign_codes(node.left, code + '0')  # Left branch is 0
        if node.right:
            assign_codes(node.right, code + '1')  # Right branch is 1

    assign_codes(root, '')
    return codes


def calculate_encoded_size(sensor_data, codes):
    """
    Estimates the total encoded size given the Huffman codes.

    Parameters:
    sensor_data (dict): Dictionary with sensor types and their frequencies.
    codes (dict): Dictionary with sensor types and their Huffman codes.

    Returns:
    int: Total encoded data size in bits.
    """
    total_bits = sum(sensor_data[char] * len(codes[char]) for char in sensor_data)
    return total_bits


if __name__ == "__main__":
    # Step 1: User inputs sensor types and their frequencies
    num_sensors = int(input("Enter the number of sensor types: "))
    sensor_data = {}

    for _ in range(num_sensors):
        sensor_type = input("Enter sensor type (single character or string): ")
        frequency = int(input(f"Enter frequency for {sensor_type}: "))
        sensor_data[sensor_type] = frequency

    # Step 2: Generate Huffman codes
    codes = huffman_coding(sensor_data)

    # Step 3: Display Huffman codes
    print("\nHuffman Codes:")
    for char in sorted(codes.keys()):
        print(f"Character: {char}, Code: {codes[char]}")

    # Step 4: Estimate encoded size
    total_bits = calculate_encoded_size(sensor_data, codes)
    print(f"\nEstimated Total Encoded Size: {total_bits} bits")

