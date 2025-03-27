import time
import file_reader as ftl
from grouper import Grouper

if __name__ == "__main__":
    start_time = time.time()
    fileDo = ftl.FileReader(input("读取文件路径（直接拖入文件即可）："))

    grouper = Grouper(fileDo.dataframe_to_list())

    result = grouper.get_results()

    for i in result:
        print(f"{i}:{fileDo.dataframe_to_list()[i[0]][i[1]+1]}")

    end_time = time.time()
    print(f"运行用时：{end_time - start_time:.6f}s")


