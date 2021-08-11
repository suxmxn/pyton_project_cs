time = "15:00"
movieName = "Harry Potter"

def seatArray(s):
    for i in range(0,10):
        print(s[i], end="  ")
    print()

def seatReserve(li):
    for i in range(0,10):
        print(li[i], end="   ")

def seatComp(ss):
    if ss == "A1" or ss == "A2" or ss == "A3" or ss == "A4" or ss == "A5" or ss == "A6" or ss == "A7" or ss == "A8" or ss == "A9" or ss == "A10":
        seat[0][ss] = "X"
    elif ss == "B1" or ss == "B2" or ss == "B3" or ss == "B4" or ss == "B5" or ss == "B6" or ss == "B7" or ss == "B8" or ss == "B9" or ss == "B10":
        seat[1][ss] = "X"
    elif ss == "C1" or ss == "C2" or ss == "C3" or ss == "C4" or ss == "C5" or ss == "C6" or ss == "C7" or ss == "C8" or ss == "C9" or ss == "C10":
        seat[2][ss] = "X"
    elif ss == "D1" or ss == "D2" or ss == "D3" or ss == "D4" or ss == "D5" or ss == "D6" or ss == "D7" or ss == "D8" or ss == "D9" or ss == "D10":
        seat[3][ss] = "X"
    elif ss == "E1" or ss == "E2" or ss == "E3" or ss == "E4" or ss == "E5" or ss == "E6" or ss == "E7" or ss == "E8" or ss == "E9" or ss == "E10":
        seat[4][ss] = "X"
    elif ss == "F1" or ss == "F2" or ss == "F3" or ss == "F4" or ss == "F5" or ss == "F6" or ss == "F7" or ss == "F8" or ss == "F9" or ss == "F10":
        seat[5][ss] = "X"
    elif ss == "G1" or ss == "G2" or ss == "G3" or ss == "G4" or ss == "G5" or ss == "G6" or ss == "G7" or ss == "G8" or ss == "G9" or ss == "G10":
        seat[6][ss] = "X"
    elif ss == "H1" or ss == "H2" or ss == "H3" or ss == "H4" or ss == "H5" or ss == "H6" or ss == "H7" or ss == "H8" or ss == "H9" or ss == "H10":
        seat[7][ss] = "X"




print(time +" " + movieName + " 좌석 배치도입니다.\nX는 예매가 완료된 좌석입니다.\n\n")

print("---------------------------------------")
print("                screen                 ")
print("---------------------------------------")
print(":입                                  출:")
print(":구                                  구:\n")

seat=[]
seat.append({"A1":"O", "A2":"X", "A3":"X", "A4":"X", "A5":"X", "A6":"X", "A7":"X", "A8":"X", "A9":"X", "A10":"X"})
seat.append({"B1":"X", "B2":"X", "B3":"X", "B4":"X", "B5":"X", "B6":"X", "B7":"X", "B8":"X", "B9":"X", "B10":"X"})
seat.append({"C1":"X", "C2":"X", "C3":"X", "C4":"X", "C5":"X", "C6":"X", "C7":"O", "C8":"O", "C9":"O", "C10":"O"})
seat.append({"D1":"O", "D2":"X", "D3":"X", "D4":"X", "D5":"O", "D6":"X", "D7":"O", "D8":"X", "D9":"X", "D10":"X"})
seat.append({"E1":"O", "E2":"X", "E3":"O", "E4":"X", "E5":"O", "E6":"O", "E7":"X", "E8":"X", "E9":"O", "E10":"O"})
seat.append({"F1":"X", "F2":"X", "F3":"X", "F4":"O", "F5":"X", "F6":"X", "F7":"O", "F8":"O", "F9":"O", "F10":"O"})
seat.append({"G1":"X", "G2":"O", "G3":"X", "G4":"O", "G5":"X", "G6":"O", "G7":"O", "G8":"X", "G9":"X", "G10":"O"})
seat.append({"H1":"X", "H2":"X", "H3":"O", "H4":"X", "H5":"O", "H6":"X", "H7":"O", "H8":"X", "H9":"O", "H10":"O"})


for i in range(0,8):
    seatArray(list(seat[i].keys()))
    seatReserve(list(seat[i].values()))
    print()



print("\n관람 인원을 입력해 주세요.\n[어른/청소년/아동]\n")
adult=int(input("어른 :"))
youth=int(input("청소년 :"))
child=int(input("아동 :"))

seatChoice = input("좌석 선택해주세요: ")
seatChoiceList = seatChoice.split(" ")

for i in range(0, len(seatChoiceList)):
    seatComp(seatChoiceList[i])


for i in range(0,8):
    seatArray(list(seat[i].keys()))
    seatReserve(list(seat[i].values()))
    print()


print("\n좌석 선택이 완료되었습니다.\n선택하신 좌석은 ["+seatChoice+"]입니다.\n")
print("결제창으로 넘어갑니다.")
print("---------------------------------------")

#영수증 수연 코드
print("\n###수연 코드 부분###\n")
#영수증 부분 [결제 내역]
print("   [결제 내역]")
print("  ------------------------------------")

#서연 코드부분 어른, 청소년, 어린이
print("\n###서연 코드 부분###\n")

hap = adult*(int)(10000) + youth*(int)(8000) + child*(int)(5000)
discount = 3000
total = hap - discount

print("   합산 금액: "+(str)(hap))
print("   할인 금액: "+(str)(discount))
print("  ------------------------------------")
print("   총 결제 금액: "+(str)(total)+"\n")
print("   성공적으로 결제가 완료되었습니다.\n   CGV를 이용해주셔서 감사합니다.")
print(" -----------------------------------")
print("=======================================")