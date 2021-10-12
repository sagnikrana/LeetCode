import collections


class Solution:
    def canAttendMeetings(self, intervals):
        if len(intervals) <= 1:
            return True

        for index, interval in enumerate(intervals):
            # interval = intervals[index]
            # intervals.remove(interval)
            # intervals.insert(0, interval)
            if index != len(intervals)-1:
                for rest_other_interval in intervals[index+1:]:
                    if self.checkOverlap(interval, rest_other_interval):
                        return False
                    interval, rest_other_interval = rest_other_interval, interval
                    if self.checkOverlap(interval, rest_other_interval):
                        return False
        return True

    def checkOverlap(self, interval, rest_other_interval):
        if interval[0] < rest_other_interval[0] < interval[1] or interval[0] < rest_other_interval[1] < \
                interval[1] or interval[0] == rest_other_interval[0] or rest_other_interval[1] == interval[
            1]:
            # print(interval[0] < rest_other_interval[0] < interval[1])
            # print(interval[0] < rest_other_interval[1] < interval[1])
            # print(interval[0] == rest_other_interval[0])
            # print(rest_other_interval[1] == interval[1])
            return True



if __name__ == '__main__':
    sol = Solution()
    print(sol.canAttendMeetings([[15,16],[10,15],[16,25]]))
