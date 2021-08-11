##변수 선언
member = [0, 0, 0]
member[0] = {"NAME": "", "ID": "", "PASSWORD": "", "securePW": ""}
dayList = ['Mon', 'Tue', 'Wed', 'Tur', 'Fri', 'Sat', 'Sun']
movieList = ['Harry Potter', 'Gravity Fall', 'Iron Man', 'The Avengers']
ScreenTimeList = ['13:00', '15:00', '17:00', '19:00']
theaterNum = 1
sDay = ""
sMovie = ""
sTime = ""
seatChoice=""
seatChoiceList=[]
seatDic={}
adult=0
youth=0
child=0

#좌석배치도 딕셔너리
for i in range(0, 8):
    for k in range(0, 10):
        ss = chr(65 + i) + str(k + 1)
        seatDic[ss] = "O"

##함수
# part1 opening
def drawLineBold():
    print("==================================================")


def signUp():
    print("                    [회원가입]                      ")
    drawLineBold()
    name = input("이름              :")
    ID = input("ID                :")
    while True:
        PASSWORD = input("PASSWORD<8자 이상>:")
        if len(PASSWORD) < 8:
            print("8자 이상 비밀번호를 입력 하세요.")
            print()
        else:
            break

    member[0]["NAME"] = name
    member[0]["ID"] = ID
    member[0]["PASSWORD"] = PASSWORD
    PASSWORD = list(PASSWORD)
    for i in range(-1, -6, -1):
        PASSWORD[i] = "*"
    securePW = "".join(PASSWORD)
    member[0]["securePW"] = securePW


def Qeixt(user):
    if user.lower() != "yes":
        drawLineBold()
        print("                프로그램을 종료합니다.                ")
        quit()


def welcome():
    drawLineBold()
    print("              WELCOME TO CCV[SOHUI]               ")
    drawLineBold()
    print()
    print("CGV에 오신 것을 환영합니다.")
    print("영화예매를 하시겠습니까?[yes/no]")
    YorN = input(">>")

    Qeixt(YorN)

    print("영화예매는 로그인 후 이용 가능합니다.")
    print("회원가입 창으로 넘어갑니다.")

    signUp()

    print()
    print(member[0]["NAME"], "님 CGV[SOHUI]에 회원가입이 완료되었습니다.")

    print("ID                :", member[0]["ID"])
    print("PASSWORD          :", member[0]["securePW"])
    print()
    drawLineBold()
    print("회원가입 환영 영화 할인 쿠폰이 지급되었습니다!")
    print("[3000원 할인 쿠폰]")
    drawLineBold()
    print("영화 예매창으로 넘어갑니다.")
    print()


# part2 Ticketing

def ticketing():
    selectDay()
    selectMovie()
    selectTime()
    seatArrangement()
    pay()


def selectDay():
    print("\n예매 날짜를 선택해주세요.")

    for d in dayList:
        print(d, end=' ')
    print()

    while True:
        global sDay
        sDay = input(">>")

        if sDay in dayList:
            return
        else:
            print("요일을 다시 선택해주십시오.")


def selectMovie():
    print("\n" + sDay + "에 상영되는 영화입니다.")
    print("영화를 선택해주십시오.\n")
    for m in movieList:
        print(m)

    while True:
        global sMovie
        sMovie = input(">>")

        if sMovie in movieList:
            return
        else:
            print("영화를 다시 선택해주십시오.")


def selectTime():
    global theaterNum
    print("\n" + sDay + " " + sMovie + " 상영시간표 입니다. 상영시간을 선택해주십시오.\n")
    for t in ScreenTimeList:
        print(t + "___제" + str(theaterNum) + "상영관_[?/80]")  # 남은 자리 수 연결?
        theaterNum += 1

    while True:
        global sTime
        sTime = input(">>")

        if sTime in ScreenTimeList:
            return
        else:
            print("상영시간을 다시 선택해주십시오.")


def seatArray(key,value):
    for k in range(0,len(key),10):
        for i in range(0, int(len(key)/8)):
            print(key[i+k], end="  ")
        print()
        for i in range(0, int(len(value)/8)):
            print(value[i+k], end="   ")
        print()

def seatComp():
    global seatChoiceList
    global seatDic
    for i in range(len(seatChoiceList)):
        if seatDic[seatChoiceList[i]] == "O":
            seatDic[seatChoiceList[i]] = "X"

def seatArrangement():
    global seatChoice
    global seatChoiceList
    global seatDic
    global adult
    global youth
    global child

    print(sTime + " " + sMovie + " 좌석 배치도입니다.\nX는 예매가 완료된 좌석입니다.\n\n")

    print("---------------------------------------")
    print("                screen                 ")
    print("---------------------------------------")
    print(":입                                  출:")
    print(":구                                  구:\n")

    seatArray(list(seatDic.keys()), list(seatDic.values()))
    print()

    print("\n관람 인원을 입력해 주세요.\n[어른/청소년/아동]\n")
    adult = int(input("어른 :"))
    youth = int(input("청소년 :"))
    child = int(input("아동 :"))

    seatChoice = input("좌석 선택해주세요: ")
    seatChoiceList = seatChoice.split(" ")

    for i in range(0, len(seatChoiceList)):
        seatComp()

    print("\n좌석 선택이 완료되었습니다.\n선택하신 좌석은 [" + seatChoice + "]입니다.\n")

def pay():
    global adult
    global youth
    global child

    print("결제창으로 넘어갑니다.")
    print("---------------------------------------")

    # 영수증 수연 코드
    print("\n###수연 코드 부분###\n")
    # 영수증 부분 [결제 내역]
    print("   [결제 내역]")
    print("  ------------------------------------")

    # 서연 코드부분 어른, 청소년, 어린이
    print("\n###서연 코드 부분###\n")

    hap = adult * (int)(10000) + youth * (int)(8000) + child * (int)(5000)
    discount = 3000
    total = hap - discount

    print("   합산 금액: " + (str)(hap))
    print("   할인 금액: " + (str)(discount))
    print("  ------------------------------------")
    print("   총 결제 금액: " + (str)(total) + "\n")
    print("   성공적으로 결제가 완료되었습니다.\n   CGV를 이용해주셔서 감사합니다.")
    print(" -----------------------------------")
    print("=======================================")

# main코드
while True:
    welcome()
    ticketing()

