import collections


class Solution:
    def canAttendMeetings(self, intervals):
        if len(intervals) <= 1:
            return True

        for index in range(len(intervals)):
            interval = intervals[index]
            intervals.remove(interval)
            intervals.insert(0, interval)
            if index != len(intervals):
                for rest_other_interval in intervals[1:]:
                    if interval[0] < rest_other_interval[0] < interval[1] or interval[0] < rest_other_interval[1] < interval[1] or interval[0]==rest_other_interval[0] or rest_other_interval[1]==interval[1]:
                        return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canAttendMeetings([[9, 10], [4, 9], [4, 17]]))