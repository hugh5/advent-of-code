
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.endValue = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, value):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endOfWord = True
        current.endValue = value

    def has(self, word, backwards=False):
        current = self.root
        i = backwards and -1 or 0
        for i in range(i, backwards and -len(word)-1 or len(word), backwards and -1 or 1):
            if word[i] not in current.children:
                return None
            current = current.children[word[i]]
            if current.endOfWord:
                return current.endValue
        return None

def part1():
    f = open("day1.input", "r")
    total = 0
    while True:
        line = f.readline()
        if not line:
            break

        start = 0
        while start < len(line) and not line[start].isdigit():
            start += 1

        end = len(line) - 1
        while end >= 0 and not line[end].isdigit():
            end -= 1
        total += int(line[start] + line[end])
    return total


def part2():
    words = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
             "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    trie = Trie()
    for word in words:
        trie.insert(word, words[word])

    backwards = Trie()
    for word in words:
        backwards.insert(word[::-1], words[word])

    f = open("day1.input", "r")
    total = 0
    while True:
        line = f.readline()
        if not line:
            break

        result = ""
        start = 0
        while start < len(line):
            if line[start].isdigit():
                result += line[start]
                break
            value = trie.has(line[start:])
            if value:
                result += value
                break
            start += 1

        end = len(line) - 1
        while end >= 0:
            if line[end].isdigit():
                result += line[end]
                break
            value = backwards.has(line[:end+1], True)
            if value:
                result += value
                break
            end -= 1
        print(f"{line[0:-1]} -> {result}")
        total += int(result)
    return total


if __name__ == "__main__":
    print(part2())
