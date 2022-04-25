from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


# 事件： 处理signal的函数叫做槽  slot
def handleCalc():
    # 获取文本控件内容
    info = textEdit.toPlainText()
    # print(info)
    # 薪资20000 以上 和 以下 的人员名单
    salary_above_20k = ''
    salary_below_20k = ''
    for line in info.splitlines():
        if not line.strip():
            continue
        parts = line.split(' ')
        # 去掉列表中的空字符串内容
        parts = [p for p in parts if p]
        name, salary, age = parts
        if int(salary) >= 20000:
            salary_above_20k += name + '\n'
        else:
            salary_below_20k += name + '\n'

    # 对话框
    QMessageBox.about(window,
                      '统计结果',
                      f'''薪资20000 以上的有：\n{salary_above_20k}
                \n薪资20000 以下的有：\n{salary_below_20k}'''
                      )


# QApplication 提供了整个图形界面程序的底层管理功能
app = QApplication([])

window = QMainWindow()
# 窗口的大小
window.resize(500, 400)
# 显示屏幕的位置
window.move(300, 310)
# 窗口的大小
window.setWindowTitle('薪资统计')

# 在主窗口的布局逻辑：指定父控件
textEdit = QPlainTextEdit(window)
# 占位符
textEdit.setPlaceholderText("请输入薪资表")
# 相对父空间的布局 左，上
textEdit.move(10, 25)
# 窗口大小
textEdit.resize(300, 350)

# button控件
button = QPushButton('统计', window)
button.move(380, 80)
# 绑定事件
button.clicked.connect(handleCalc)

# 展示界面
window.show()

# 事件进入循环
app.exec_()
