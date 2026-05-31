import sys
import random
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QMessageBox
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt,QTimer

class SnakeGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Snake game')
        self.setFixedSize(400,440)
        self.setStyleSheet("background-color:#0A0A0A;color:white")

        self.GRID_SIZE=20
        self.CELL_SIZE=20

        self.timer=QTimer()
        self.timer.timeout.connect(self.game_loop)

        self.score_label=QLabel('SCORE: 0',self)
        self.score_label.setFont(QFont('Courier New',14,QFont.Bold))
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("color:#00FF00;padding:5px")

        layout=QVBoxLayout()
        layout.addWidget(self.score_label)
        layout.addSpacing(400)
        self.setLayout(layout)

        self.reset_game()

    def reset_game(self):
        self.snake=[(10,10),(10,11),(10,12)]
        self.direction=Qt.Key_Up
        self.score=0
        self.score_label.setText(f'SCORE: {self.score}')
        self.spawn_food()
        self.game_over=False
        self.timer.start(150)

    def spawn_food(self):
        while True:
            self.food=(random.randint(0,self.GRID_SIZE-1),random.randint(0,self.GRID_SIZE-1))
            if self.food not in self.snake:
                break

    def paintEvent(self,event):
        painter=QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        painter.setPen(QColor('#333333'))
        painter.drawRect(0,40,400,400)

        painter.setBrush(QColor('#FF0055'))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.food[0]*self.CELL_SIZE,40+self.food[1]*self.CELL_SIZE,self.CELL_SIZE-2,self.CELL_SIZE-2)

        for index,segment in enumerate(self.snake):
            if index==0:
                painter.setBrush(QColor('#00FF66'))
            else:
                painter.setBrush(QColor('#00AA44'))
            painter.drawRect(segment[0]*self.CELL_SIZE,40+segment[1]*self.CELL_SIZE,self.CELL_SIZE-2,self.CELL_SIZE-2)

    def keyPressEvent(self,event):
        key=event.key()

        if key==Qt.Key_Left and self.direction!=Qt.Key_Right:
            self.direction=key
        elif key==Qt.Key_Right and self.direction!=Qt.Key_Left:
            self.direction=key
        elif key==Qt.Key_Up and self.direction!=Qt.Key_Down:
            self.direction=key
        elif key==Qt.Key_Down and self.direction!=Qt.Key_Up:
            self.direction=key

    def game_loop(self):
        if self.game_over:
            return

        head_x,head_y=self.snake[0]

        if self.direction==Qt.Key_Left:
            head_x-=1
        elif self.direction==Qt.Key_Right:
            head_x+=1
        elif self.direction==Qt.Key_Up:
            head_y-=1
        elif self.direction==Qt.Key_Down:
            head_y+=1

        new_head=(head_x,head_y)

        if(head_x<0 or head_x>=self.GRID_SIZE or head_y<0 or head_y>=self.GRID_SIZE or new_head in self.snake):
            self.game_over=True
            self.timer.stop()
            QMessageBox.information(self,'Game Over',f'Game Over! Your score:{self.score}')
            self.reset_game()
            return

        self.snake.insert(0,new_head)

        if new_head==self.food:
            self.score+=10
            self.score_label.setText(f'SCORE:{self.score}')
            self.spawn_food()
        else:
            self.snake.pop()

        self.update()

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=SnakeGame()
    ex.show()
    sys.exit(app.exec_())