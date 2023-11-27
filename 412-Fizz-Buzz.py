
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        results = []
        for i in range(1, n+1):
            result = ''
            if i % 3 == 0:
                result = 'Fizz'
            if i % 5 == 0:
                result += 'Buzz'
            if result == '':
                result = str(i)
            results.append(result)
        return results
    

if __name__ == '__main__':
    n = 15
    solution = Solution()
    print(solution.fizzBuzz(n))