from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader


class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        # 从UI定义中动态 常见一个相应的窗口对象
        # 注意，里面的控件对象也成为了窗口对象的属性
        self.ui = QUiLoader().load("./ui/statis.ui")

        # 使用对象属性绑定事件
        self.ui.button.clicked.connect(self.handleCalc)

    def handleCalc(self):
        info = self.ui.textEdit.toPlainText()

        salary_above_20k = ''
        salary_below_20k = ''
        for line in info.splitlines():
            if not line.strip():
                continue
            parts = line.split(' ')

            parts = [p for p in parts if p]
            name, salary, age = parts
            if int(salary) >= 20000:
                salary_above_20k += name + '\n'
            else:
                salary_below_20k += name + '\n'

        QMessageBox.about(self.ui,
                          '统计结果',
                          f'''薪资20000 以上的有：\n{salary_above_20k}
                        \n薪资20000 以下的有：\n{salary_below_20k}'''
                          )


app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
