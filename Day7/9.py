import random
def main(char_len = 4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    new_char = ""
    for a in range(char_len):
        index = random.randint(0,last_pos)
        new_char += all_chars[index]
    return new_char

def get_suffix(filename,has_dot=False):
    pos = filename.rfind('.')
    if 0<pos<len(filename)-1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ""
def get_max2(list):
    m1,m2 = (list[0],list[1]) if list[0]>list[1] else (list[1],list[0])
    for index in range(2,len(list)):
        if list[index]>m1:
            m2 = m1
            m1 = list[index]
        elif list[index]>m2:
            m2 = list[index]
    return m1,m2

def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    # 用bool索引的时候，True被认为1，false被认为0
    print(is_leap_year(year))
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date

#杨辉三角
def yanghui_triangle():
    num = int(input(("Number of rows:")))
    yh = [[]] * num
    # print(yh)
    # yh = []
    # for _ in range(num):
    #     yh.append([])
    # print(yh)
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
if __name__ == '__main__':
    yanghui_triangle()

