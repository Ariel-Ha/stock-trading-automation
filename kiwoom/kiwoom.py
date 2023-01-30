import os
import sys
from PyQt5.QAxContainer import * # QAxContainer파일의 클래스를 사용, 마이크로소프트사에서 제공하는 프로세스로 화면을 구성하는데 필요한 기능이 담겨있다.
from PyQt5.QtCore import * # QEventLoop()를 사용하기 위함
from config.errorCode import * # 에러 코드를 모아놓은 파일 임포트

# 키움 API 코드를 담당할 키움 클래스
class Kiwoom(QAxWidget):  # QAxWidet을 상속받아 사용한다. QAxWidet은 디자인 구성 컨트롤 및 재사용 기능을 갖고있다. setControl():설치된 API 모듈을 파이썬에 활용하는 함수, 키움Open API+가 .ocx형태로 저장되어 있으며, 함수가 .ocx확장자도 사용할 수 있게 해준다.

    def __init__(self):
        super().__init__()  # 상속된 QAxWidet의 __init__에 포함된 변수 및 함수들을 내려받아 사용하겠다./super().__init__() 은 QAxWidget.__init__()과 동일하다.
        print("Kiwoom() class start.")

        ##이벤트 루프를 실행하기 위한 변수 모음
        self.login_event_loop = QEventLoop()  # self.login_event_loop변수는 로그인을 요청하고 안전하게 완료될 때까지 기다리게 만들기 위한 event loop 변수/로그인 요청용 이벤트 루프

        # 초기 셋팅 함수들 바로 실행
        self.get_ocx_instance()  # get_ocx_instance()함수 실행 : ocx 방식을 파이썬에 사용할 수 있게 반환해 주는 함수 실행
        self.event_slots()  # event_slots()함수 실행
        self.signal_login_commConnect()  # 로그인 요청 함수 포함한 함수 실행
        self.get_account_info()  # 계좌번호 가져오기 함수 실행

    # 레지스트리에 저장된 API모듈 불러오기 함수
    def get_ocx_instance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1")  # 등록된 레지스트리(윈도우 운영체제에서 사용하기 위한 구성 정보들을 저장해 놓은 공간)

    # 슬롯 구역(self.login_slot()함수)을 이벤트와 연결해주는 함수
    def event_slots(self):  # 키움과 연결하기 위한 시그널/슬롯 모음, 이벤트를 모아 놓은 함수 (로그인 이벤트 등 다양한 이벤트), 이벤트를 모아서 관리하기 위함
        self.OnEventConnect.connect(self.login_slot)  # OnEventConnect()함수는 로그인 요청의 결과값을 받을 함수를 지정하는 이벤트/로그인을 요청하면 정상적으로 처리됐는지 슬롯 구역에서 확인

    # 로그인 요청 시그널 구역
    def signal_login_commConnect(self):
        self.dynamicCall("CommConnect()")  # 로그인 요청 시그널/dynamicCall() 키움 서버에 데이터 송수신 기능/CommConnect()함수는 로그인을 요청하는 시그널 함수
        self.login_event_loop.exec_()  # 이벤트 루프 실행 : 로그인 수행여부 결과 받을 때까지 대기 & 네트워크 연결 지속

    # 로그인 처리 결과를 받을 슬롯 구역
    def login_slot(self, err_code):  # OnEventConnect 이벤트 발생 결과인 로그인 성공여부를 login_slot으로 전달, 성공여부 변수를 err_code 변수 이름으로 받는다.
        print(errors(err_code)[1])
        self.login_event_loop.exit()  # 로그인 처리가 완료됐으면 이벤트 루프를 종료한다.

    # 계좌번호 가져오는 함수
    def get_account_info(self):  # 계좌번호는 결과값을 위해 대기하지 않아도 된다. 위치 관계X
        account_list = self.dynamicCall("GetLoginInfo(Qstring)", "ACCNO")  # 계좌번호 반환/GetLoginInfo(Qstring) 함수에 인자로 문자열을 지정하고, ACCNO를 가져오겠다고 지정해서 계좌 정보를 가져온다.
        account_num = account_list.split(';')[0]  # 반환받은 계좌번호들을 ;로 구분지어/첫 번째 계좌만 가져온다.
        self.account_num = account_num  # 가져온 계좌를 self.account_num 변수로 지정한다.
        print("계좌번호 : %s" % account_num)
