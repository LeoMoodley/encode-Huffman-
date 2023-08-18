import queue

MAX_SIZE = 100

chars_binary = {}


class HufftManNodeTree:
    def __init__(self, character, frequency):
        # Stores character
        self.data = character

        self.freq = frequency

        self.left = None

        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class isSame:
    def __call__(self, a, b):
        return a.freq > b.freq


def buildTrees(priorityQueue):
    while priorityQueue.qsize() != 1:
        left = priorityQueue.get()

        right = priorityQueue.get()

        node = HufftManNodeTree('$', left.freq + right.freq)
        node.left = left
        node.right = right

        priorityQueue.put(node)

    return priorityQueue.get()
def outputCodes(root, arr, top):
    if root.left:
        arr[top] = 0
        outputCodes(root.left, arr, top + 1)

    if root.right:
        arr[top] = 1
        outputCodes(root.right, arr, top + 1)

    with open("codes.txt", "a") as f:
        if not root.left and not root.right:
            chars_binary.setdefault(root.data, "")
            f.write(str(root.data) + ' ')
            for i in range(top):
                chars_binary[root.data] += str(1 - arr[i])
                f.write(str(1 - arr[i]))
            f.write('\n')


def HuffmanCodes(data, freq, size):
    priorityQueue = queue.PriorityQueue()

    for i in range(size):
        newNode = HufftManNodeTree(data[i], freq[i])
        priorityQueue.put(newNode)

    root = buildTrees(priorityQueue)

    arr = [0] * MAX_SIZE
    top = 0
    outputCodes(root, arr, top)


def find_Chars(text):
    unique_characters = set()

    for char in text:
        unique_characters.add(char)

    look_for_characters = sorted(list(unique_characters))

    return look_for_characters


if __name__ == '__main__':
    characters_main = []

    frequency_main = []

    char_count = {}

    with open('test1.txt', 'r') as file:
        text = file.read()

    look_for_characters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + \
                          [str(i) for i in range(10)] + [',', '.', ' ']

    set1 = set(look_for_characters)
    set2 = set(characters_main)

    result_set = set1.union(set2)

    text = text.strip().replace('\n', '')
    text = text.strip().replace('\r', '')
    text = text.strip().replace('\t', '')
    text = text.strip().replace("\t", "").strip().replace("\n", "").strip().replace("\r", "").strip().replace("\f",
                                                                                                              "").strip().replace(
        "\v", "")
    text = text.replace("\\", "")
    text = text.lower()

    for element in text:
        if element not in look_for_characters:
            text = text.replace(f"{element}", " ")

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            characters_main.append(char)
            char_count[char] = 1

    for element in look_for_characters:

        if element not in characters_main and element not in char_count:
            characters_main.append(element)
            frequency_main.append(char_count.setdefault(element, 0))

    characters_main = sorted(list(characters_main))

    for char in characters_main:
        frequency_main.append(char_count.setdefault(char, 0))

    frequency_main = frequency_main[1:]

    add_file = ""
    for i in range(len(frequency_main)):
        add_file += f"{characters_main[i]}:{frequency_main[i]}\n"
    new_size = len(characters_main)
    HuffmanCodes(characters_main, frequency_main, new_size)

    with open("frequency.txt", "w") as file:
        file.write(add_file.strip())

    input_file = 'test1.txt'
    output_file = 'compressed.bin'

    with open(input_file, 'r') as file:
        input_text = file.read()

    output_text = ''

    input_text = input_text.lower()
    for char in input_text:
        if char in chars_binary:
            output_text += chars_binary[char]
        else:
            output_text += char

    with open(output_file, 'w') as file:
        file.write(output_text)