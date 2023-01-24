class MergerSort:
    def __init__(self, numbers_to_sort):
        self.numbers = numbers_to_sort

    def sort(self):
        numbers = len(self.numbers)
        if numbers == 1:
            return self.numbers

        left = MergerSort(self.numbers[: numbers // 2]).sort()
        right = MergerSort(self.numbers[numbers // 2:]).sort()

        return self._merge_and_sort(left, right)

    def _merge_and_sort(self, left, right):
        # Base case: if one of the lists is empty, return the other
        if not left:
            return right
        if not right:
            return left

        if left[0] < right[0]:
            return [left[0]] + self._merge_and_sort(left[1:], right)
        return [right[0]] + self._merge_and_sort(left, right[1:])


if __name__ == "__main__":

    list_to_sort = [7, 5, 9, 2, 6, 8]
    print(MergerSort(list_to_sort).sort())
