import heapq
from collections import defaultdict
from typing import Optional

###
# Here I used the template for this problem provided by udacity/nd256-data-structures-and-algorithms
###

# Huffman Tree Node
class HuffmanNode:
    """
    A class to represent a node in the Huffman Tree.

    Attributes:
    -----------
    char : Optional[str]
        The character stored in the node.
    freq : int
        The frequency of the character.
    left : Optional[HuffmanNode]
        The left child node.
    right : Optional[HuffmanNode]
        The right child node.
    """

    def __init__(self, char: Optional[str], freq: int) -> None:
        """
        Constructs all the necessary attributes for the HuffmanNode object.

        Parameters:
        -----------
        char : Optional[str]
            The character stored in the node.
        freq : int
            The frequency of the character.
        """
        self.char: Optional[str] = char
        self.freq: int = freq
        self.left: Optional[HuffmanNode] = None
        self.right: Optional[HuffmanNode] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        """
        Less-than comparison operator for HuffmanNode.

        Parameters:
        -----------
        other : HuffmanNode
            The other HuffmanNode to compare with.

        Returns:
        --------
        bool
            True if the frequency of this node is less than the other node, False otherwise.
        """
        return self.freq < other.freq

def calculate_frequencies(data: str) -> dict[str, int]:
    """
    Calculate the frequency of each character in the given data.

    Parameters:
    -----------
    data : str
        The input string for which frequencies are calculated.

    Returns:
    --------
    Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.
    """
    frequencies: dict[str, int] = {}

    for character in data:

        if character not in frequencies:
            frequencies[character] = 1
            continue
        
        frequencies[character] += 1

    return frequencies

def build_huffman_tree(frequency: dict[str, int]) -> HuffmanNode:
    """
    Build the Huffman Tree based on the character frequencies.

    Parameters:
    -----------
    frequency : Dict[str, int]
        A dictionary with characters as keys and their frequencies as values.

    Returns:
    --------
    HuffmanNode
        The root node of the constructed Huffman Tree.
    """
    if len(frequency) == 1:
        char = list(frequency.keys())[0]
        return HuffmanNode(char, frequency[char])

    priority_queue = []
    
    for key, number in frequency.items():
        heapq.heappush(priority_queue, HuffmanNode(key, number))

    while len(priority_queue) > 1:
        lowest_frequency_node_1: HuffmanNode = heapq.heappop(priority_queue)
        lowest_frequency_node_2: HuffmanNode = heapq.heappop(priority_queue)

        internal_node = HuffmanNode(None, lowest_frequency_node_1.freq + lowest_frequency_node_2.freq)
        internal_node.left = lowest_frequency_node_1
        internal_node.right = lowest_frequency_node_2
        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def generate_huffman_codes(node: Optional[HuffmanNode], code: str, huffman_codes: dict[str, str]) -> None:
    """
    Generate Huffman codes for each character by traversing the Huffman Tree.

    Parameters:
    -----------
    node : Optional[HuffmanNode]
        The current node in the Huffman Tree.
    code : str
        The current Huffman code being generated.
    huffman_codes : Dict[str, str]
        A dictionary to store the generated Huffman codes.
    """
    if node.char != None:
        huffman_codes[node.char] = code
        return
    
    if node.left:
        generate_huffman_codes(node.left, "0" if code == None else code + "0", huffman_codes)
    
    if node.right:
        generate_huffman_codes(node.right, "1" if code == None else code + "1", huffman_codes)

def huffman_encoding(data: str) -> tuple[str, Optional[HuffmanNode]]:
    """
    Encode the given data using Huffman coding.

    Parameters:
    -----------
    data : str
        The input string to be encoded.

    Returns:
    --------
    Tuple[str, Optional[HuffmanNode]]
        A tuple containing the encoded string and the root of the Huffman Tree.
    """
    if not data:
        return "", None

    frequency = calculate_frequencies(data)
    huffman_tree_root = build_huffman_tree(frequency)
    huffman_codes: dict[str, str] = {}

    if len(frequency) == 1:
        char = list(frequency.keys())[0]
        huffman_codes = {char: "0"}
    else:
        huffman_codes = {}
        generate_huffman_codes(huffman_tree_root, None, huffman_codes)

    encoded_data: str = ""

    for character in data:
        
        encoded_data += huffman_codes[character]

    return (encoded_data, huffman_tree_root)

def huffman_decoding(encoded_data: str, tree: Optional[HuffmanNode]) -> str:
    """
    Decode the given encoded data using the Huffman Tree.

    Parameters:
    -----------
    encoded_data : str
        The encoded string to be decoded.
    tree : Optional[HuffmanNode]
        The root of the Huffman Tree used for decoding.

    Returns:
    --------
    str
        The decoded string.
    """
    decoded_data = ""

    current_node = tree

    for digit in encoded_data:

        if digit == "0" and current_node.left:
            current_node = current_node.left


        if digit == "1" and current_node.right:
            current_node = current_node.right

        if current_node.char != None:
            decoded_data = decoded_data + current_node.char
            current_node = tree

    return decoded_data

# Main Function
if __name__ == "__main__":
    # Test Case 1: Standard test case
    print("\nTest Case 1: Standard sentence")
    sentence = "AAAAAAABBBCCCCCCCDDEEEEEE"
    print("Original: ", sentence)
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 2: Single character repetition
    print("\nTest Case 2: Single character repetition")
    sentence = "AAAAAAAAAAAA"
    print("Original: ", sentence)
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data


    # Test Case 3: Empty string and multiple characters
    print("\nTest Case 3: Empty string and multiple characters")
    sentence = ""
    print("Original: ", sentence)
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    sentence = "Hello, World!"
    print("\nOriginal: ", sentence)
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data

    # Test Case 4: Single character
    print("\nTest Case 4: Single character")
    sentence = "a"
    print("Original: ", sentence)
    encoded_data, tree = huffman_encoding(sentence)
    print("Encoded:", encoded_data)
    decoded_data = huffman_decoding(encoded_data, tree)
    print("Decoded:", decoded_data)
    assert sentence == decoded_data