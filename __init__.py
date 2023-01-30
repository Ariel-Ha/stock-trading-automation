# ___init__.py는 프로그램 실행 용도

# init.py를 실행하면 Main()클래스 생성, Main클래스에는 Kiwoom()클래스가 인스턴스화 되어 있어서 Kiwoom()클래스도 실행
from kiwoom.kiwoom import *  # 키움 파일의 내용을 가져와 사용하겠다.
import sys  # 스크립트 종료, 파이썬 변수 함수를 다루는 기능
from PyQt5.QtWidgets import *  # PyQt5라이브러리에서 QtWidggets 파일의 클래스를 사용하겠다.

sys.path.append("C:/Users/La vie est belle/PycharmProjects/stock-trading-automation/")

class Main():  # 프로그램을 실행시킬 메인 클래스

    def __init__(self):  # 클래스 동작 시 설정해야 할 기본 데이터 구성/Main 객체 생성 시 __init__함수에서, 임포트한 키움 클래스의 객체 생성
        print("Main() start")
        self.app = QApplication(sys.argv)  # QApplication클래스는 프로그램을 앱, 홈페이지처럼 실행할 수 있도록 그래픽적 요소를 제어, 동시성 처리/QApplication 인스턴스화 후, 실행하려는 파일 이름이 들어있는 sys.argv 전달->PyQt5는 실행할 파일을 인지 후 동시성 처리 지원
        self.kiwoom = Kiwoom()  # 키움 클래스 객체화
        self.app.exec_()  # 이벤트 루프 실행/QApplication 클래스의 exec_()함수를 실행해 프로그램이 종료되지 않고 동시성 처리를 지원하도록


if __name__ == "__main__":  # Main() 클래스가 실행용 파일이라는 것을 명시하기 위한 실행 조건문
    Main()
