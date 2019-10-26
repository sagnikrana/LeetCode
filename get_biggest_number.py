class Solution(object):
    def get_biggest_number(self, num):
        num_string = str(num)
        if "-" in num_string:
            max_num = -999999999
            for i in range(1,len(num_string) + 1):
                new_num = num_string[:i] + '5' + num_string[i:]
                new_num = int(new_num)
                if new_num > max_num:
                    max_num = new_num
        else:
            max_num = 0
            for i in range(len(num_string) + 1):
                new_num = num_string[:i] + '5' + num_string[i:]
                new_num = int(new_num)
                if new_num > max_num:
                    max_num = new_num
        return max_num


if __name__ == '__main__':
    result = Solution.get_biggest_number(Solution,"-45678")
    print(result)