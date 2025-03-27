class Grouper:
    """操作相当于一个会议安排优化问题"""

    def __init__(self, students: list[list[str]]):
        self.students = students
        self.data = []  # 课程表
        self.students_list = set()  # 学生清单
        self.groups = []  # 记录选择的时间段
        self.unassigned_students = set()  # 未安排学生

    def get_results(self):
        # 基本数据处理，获取所有学生及其不可用时间
        self.data = [[set(j.split(",")) for j in i[1:]] for i in self.students] #str分割
        self.students_list = {item for sublist in self.data for slot in sublist for item in slot if item.strip()}
        self.unassigned_students = set(self.students_list)  # 初始化未安排学生列表

        while self.unassigned_students:
            best_time = None
            max_coverage = 0
            best_available_students = set()

            # 遍历所有时间段，找到覆盖最多未安排学生的时间段
            for time_slot_i in range(len(self.data)):
                for time_slot_j in range(len(self.data[time_slot_i])):

                    # 跳过 (2,1)班会，剩下几个空闲时间（md当时咋没看出来这么多空闲时间啊，哎）
                    if (time_slot_i, time_slot_j) in [(2, 1), (3, 1), (4, 0), (4, 4)]:
                        continue

                    unavailable_students = self.data[time_slot_i][time_slot_j]  # 该时间段不能参加的学生
                    available_students = self.unassigned_students - unavailable_students
                    coverage = len(available_students)

                    if coverage > max_coverage:
                        max_coverage = coverage
                        best_time = (time_slot_i, time_slot_j)
                        best_available_students = available_students

            if best_time:
                # 记录最佳时间段，移除已安排的学生
                self.groups.append(best_time)
                self.unassigned_students -= best_available_students
            else:
                # 如果无法再安排，可能有学生无法安排到会议
                break

        return self.groups
