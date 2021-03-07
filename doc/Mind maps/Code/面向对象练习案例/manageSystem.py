from student import  *

class StudentManage(object):
    def __init__(self):
        self.student_list=[]

    #程序入口
    def run(self):
        #1.加载学生数据
        self.load_student()

        while True:
            #2.显示功能菜单
            self.show_menu()

            #3.用户输入序号
            choice = int(input('请选择功能:'))

            #4.根据输入执行功能
            if choice == 1:
                #添加学员
                self.add_student()

            elif choice == 2:
                #删除学员
                self.remove_student()

            elif choice == 3:
                #修改学员信息
                self.modify()

            elif choice == 4:
                #查询学员信息
                self.search()

            elif choice == 5:
                #显示所有学员
                self.pr_all()

            elif choice == 6:
                #保存学员信息
                self.save_student()

            elif choice == 7:
                #退出系统
                break

    @staticmethod
    def show_menu():
        print('请选择以下功能：')
        print('-' * 10)
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')

    def add_student(self):
        name = input('输入学员名称:')
        gender = input('请输入学员性别:')
        tel = input('请输入电话号码:')
        student=Student(name,gender,tel)
        self.student_list.append(student)


    def remove_student(self):
        name=input('请输入学生姓名:')
        for i in self.student_list:
            if name == i.name:
                self.student_list.remove(i)
                break
            else:
                print('无该学生!')


    def modify(self):
        name=input('请输入学生姓名:')
        for i in self.student_list:
            if name ==  i.name:
                i.name = input('请输入新的学生姓名:')
                i.gender = input('请输入新的学生性别:')
                i.tel = input('请输入新的手机号码:')
                print(f'修改学生信息成功，{i.name},{i.gender},{i.tel}')
                break
        else:
            print('无该学生!')

    def search(self):
        name=input('请输入学生姓名:')
        for i in self.student_list:
            if name ==  i.name:
                print(f'姓名:{i.name},性别:{i.gender},手机号:{i.tel}')
                break
        else:
            print('无该学生!')



    def pr_all(self):
        for i in self.student_list:
            print(i)

    def save_student(self):
        #打开文件
        with open('student.data','w') as file:
            #写入文件
            new_list = [i.__dict__ for i in self.student_list]
            file.write(str(new_list))
        #关闭文件

    def load_student(self):
        try:
            file = open('student.data','r')
        except:
            file = open('student.data','w')
        else:
            data = file.read()
            new_list = eval(data)
            self.student_list=[Student(i['name'],i['gender'],i['tel']) for i in new_list]
        finally:
            file.close()