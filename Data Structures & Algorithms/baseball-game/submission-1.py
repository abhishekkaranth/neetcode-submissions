class Solution:
    def isinteger(self, char):
        try:
            int(char)
            return True
        except ValueError as e:
            return False

    def calPoints(self, operations: List[str]) -> int:
        arr = []
        len_arr = 0
        for char in operations:
            print(char, arr, len_arr)
            if self.isinteger(char):
                arr.append(int(char))
                len_arr += 1
            elif char == '+':
                arr.append(arr[len_arr-1] + arr[len_arr-2])
                len_arr += 1
            elif char == 'D':
                arr.append(arr[len_arr-1]*2)
                len_arr += 1
            elif char == 'C':
                arr.pop()
                len_arr -= 1
        
        return sum(arr)