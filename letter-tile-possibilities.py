class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        sequences = set()
        used = [False] * len(tiles)

        self._generate_sequences(tiles, "", used, sequences)

        return len(sequences) - 1

    def _generate_sequences(
        self, tiles: str, current: str, used: list, sequences: set
    ) -> None:
        sequences.add(current)

        for pos, char in enumerate(tiles):
            if not used[pos]:
                used[pos] = True
                self._generate_sequences(tiles, current + char, used, sequences)
                used[pos] = False


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        char_count = [0] * 26
        for char in tiles:
            char_count[ord(char) - ord("A")] += 1

        return self._find_sequences(char_count)

    def _find_sequences(self, char_count: list) -> int:
        total = 0

        for pos in range(26):
            if char_count[pos] == 0:
                continue

            total += 1
            char_count[pos] -= 1
            total += self._find_sequences(char_count)
            char_count[pos] += 1

        return total


tiles = "AAB"
print(Solution().numTilePossibilities(tiles))
