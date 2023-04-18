from os import close
import datetime
from tkinter import *
from tkinter import filedialog
import random
from tkinter import messagebox as msg

from tkinter.constants import LEFT, RIGHT, CENTER, BOTTOM, TOP
import tkinter.messagebox

aaaa = 0
id_data_base = [1]
pw_data_base = [1]

wd = [
    "개미", "호랑이", "사자", "코뿔소", "강아지", "장미", "고양이", "코딩", "귀찮아", "문자열",
    "미국", "아버지", "기철이", "기영이", "나무", "이웃집 토토로", 
    "겨울왕국", "대전", "서울", "무서운", "글쓰기", "영어", "제비", "까마귀", "까치", "구피",
    "교수님", "과제", "학생", "라따뚜이", "수학", "국어", "폭풍우 치는 밤에", "로봇의 별",
    "치킨", "카래", "커피", "스무디", "요거트", "시리얼", "갈비찜", "라면", "김치찌개"
]

# 화면전환
def toggle():
    global frame1,frame2
    if (frame1.winfo_ismapped()):
        frame3.pack_forget()
        frame4.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame1.pack_forget()
        frame2.pack(expand = "yes")

    else:
        frame2.pack_forget()
        frame3.pack_forget()
        frame4.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame1.pack(expand = "yes") 
        entry_new_id.delete(0,len(entry_new_id.get()))
        entry_new_pw.delete(0,len(entry_new_pw.get()))
        entry_pw.config(show='' )
        entry_id.insert(0,'ID를 입력해 주세요')
        entry_pw.insert(0,'PW를 입력해 주세요')

def toggle1_1():
    global frame1,frame2
    if (frame2.winfo_ismapped()):
        frame6.pack_forget()
        frame5.pack_forget()
        frame3.pack_forget()
        frame4.pack_forget()
        frame2.pack_forget()
        frame1.pack(expand = "yes")
        entry_new_id.delete(0,len(entry_new_id.get()))
        entry_new_pw.delete(0,len(entry_new_pw.get()))
        entry_pw.config(show='' )
        entry_id.insert(0,'ID를 입력해 주세요')
        entry_pw.insert(0,'PW를 입력해 주세요')

    else:
        frame1.pack_forget()
        frame3.pack_forget()
        frame4.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame2.pack(expand = "yes") 
       
def toggle2():
    global frame3,frame4
    if (frame3.winfo_ismapped()):
        frame3.pack_forget()
        frame1.pack_forget()
        frame2.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame4.pack(expand = "yes")

        
    else:
        frame4.pack_forget()
        frame1.pack_forget()
        frame2.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame3.pack(expand = "yes") 
        word_list()

def toggle3():
    global frame3,frame4
    if (frame4.winfo_ismapped()):
        frame3.pack_forget()
        frame1.pack_forget()
        frame2.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        frame3.pack(expand = "yes")

        
    else:
        frame3.pack_forget()
        frame1.pack_forget()
        frame2.pack_forget()
        frame5.pack_forget()
        frame6.pack_forget()
        entry_id.delete(0,len(entry_id.get()))
        entry_pw.delete(0,len(entry_pw.get()))
        entry_new_pw.config(show='' )
        entry_new_id.insert(0,'사용할 ID를 입력해 주세요')
        entry_new_pw.insert(0,'사용할 PW를 입력해 주세요')
        frame4.pack(expand = "yes") 

def toggle4():
    global frame5,frame6
    if (frame5.winfo_ismapped()):
        frame5.pack_forget()
        frame4.pack_forget()
        frame3.pack_forget()
        frame1.pack_forget()
        frame2.pack_forget()
        frame6.pack(expand = "yes")

        
    else:
        frame6.pack_forget()
        frame3.pack_forget()
        frame4.pack_forget()
        frame1.pack_forget()
        frame2.pack_forget()
        frame5.pack(expand = "yes")

# 메시지 박스
def login_massagebox():
    response = tkinter.messagebox.askyesno("회원이 아닙니다.","회원가입을 하시겠습니까?")
    if response == 1:
        print('yes')
        toggle3()
    else:
        print('no')
        

def game_massagebox():
    response = tkinter.messagebox.askyesno("게임이 끝났습니다",str((et - st).seconds)+"초 걸리셨습니다. 게임을 다시 하시려면 yes, 아니면 no를 눌러주세요" )
    if response == 1:
        print('yes')
        quit()
        if stage_number == 10 :
            one_stage()
        elif stage_number == 15:
            two_stage()
        elif stage_number == 20:
            three_stage()
        elif four_stage == 25:
            four_stage()
        elif stage_number == 30:
            five_stage()
        elif stage_number == 35:
            six_stage()
        print(stage_number)
            
    else:
        print('no')
        quit()

# 회원 정보 확인
def surch():
    global a,b,pos2,pos1
    pw = entry_pw.get()
    id = entry_id.get()

    a = 0
    b = 0
    pos1 = -1
    pos2 = -1
    if int(id) in id_data_base:
        pos1==1
        print('id 사용자 확인')
        if int(pw) in pw_data_base:
            if id_data_base.index(int(id))==pw_data_base.index(int(pw)):
                pos2==1
                print('pw 사용자 확인')
                print('인증 성공')
                toggle()
                entry_id.delete(0,len(entry_id.get()))
                entry_pw.delete(0,len(entry_pw.get()))
            else:
                print('id와 pw가 맞지 않습니다')
                login_massagebox()
        else:
            print('pw 사용자가 아닙니다')
            login_massagebox()

                  
    
    else:
        print("id 또는 pw 틀림")
        login_massagebox()
        print(pos1,pos2)
   

# 회원가입
def new_member():
    ni = entry_new_id.get()
    np = entry_new_pw.get()
    id_data_base.append(int(ni))
    pw_data_base.append(int(np))
    print(id_data_base)
    print(pw_data_base)
    toggle()

# 순위 정렬
def word_list():
    global aa
    if aaaa == 0:
        aa = wd
        print(aa)
        for i in range(0,len(aa)):
            minIndex = findMin(i,len(aa)-1)
            aa[i],aa[minIndex] = aa[minIndex],aa[i]
            print('단어 : ',aa[i], end = '\n')
            txt = str(aa[i])
            text.insert("1.0", txt)

        
    else : 
        aa = b
        print(aa)
        for i in range(0,len(aa)-1):
            minIndex = findMin(i,len(aa)-1)
            aa[i],aa[minIndex] = aa[minIndex],aa[i]
            print('단어 : ',aa[i], end = '\n')
            txt = str(aa[i])
            text.insert("1.0", txt)

      
# entry 문자 지우기
def clear1(event):
    if entry_id.get() == 'ID를 입력해 주세요':
        entry_id.delete(0,len(entry_id.get()))
def clear2(event):
    if entry_pw.get() == 'PW를 입력해 주세요':
        entry_pw.delete(0,len(entry_pw.get()))
        entry_pw.config(show="*")
def clear3(event):
    if entry_new_id.get() == '사용할 ID를 입력해 주세요':
        entry_new_id.delete(0,len(entry_new_id.get()))
def clear4(event):
    if entry_new_pw.get() == '사용할 PW를 입력해 주세요':
        entry_new_pw.delete(0,len(entry_new_pw.get()))
        entry_new_pw.config(show="*")
# canvas 창닫기
def quit():
    canvas.destroy()
    toggle4()

# 정렬 알고리즘
def findMin(start,end):
    min = wd[start]
    index = start
    for i in range(start+1,end+1):
        if min < wd[i]:
            min = wd[i]
            index = i
    return index

# 게임화면
def start_game_btn(stage_number):
    # 전역변수 선언
    global bk, point, kill, aa, canvas,entry3,ch,st, et
    point = 0
    if aaaa == 0:
        aa = wd
        print(aaaa)
        
    else : 
        aa = b
        print(aaaa)
    st = datetime.datetime.now()
    # 캔버스 생성
    canvas = tkinter.Canvas(root, width = 800, height = 600,bg = "black")
    canvas.pack()

    # 2개의 frame 초기화
    frame5.pack_forget()
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack_forget()
    frame1.pack_forget()
    
    # 글자 입력창
    entry3 = tkinter.Entry(canvas,width=25,font = ("맑은고딕", 16))
    entry3.place(x=270, y=550)
    ch = entry3.get()
    #canvas.update()

    dle = tkinter.Button(canvas,text = "back", font = ("맑은고딕", 16), command = quit)
    dle.place(x = 700, y = 550)
    canvas.update()

    # 글자 장애물
    b1 = 0 
    a1 = 0
    i = 0
    while True :
        while a1 ==i: 
            a1+=1
            # 단어를 랜덤으로 선택
            kill = random.choice(aa)
            # 출현 위치 랜덤으로 선택
            pl_x = random.randint(100,570)
            pl_y = random.randint(50,500)
            # 글자 표시
            label3 = tkinter.Label(canvas, text = kill, font = ("맑은 고딕",20))
            label3.place(x = pl_x, y = pl_y)
            print(kill) # 글자가 랜덤으로 잘나오는지 확인용
        # 점수 표시
            label2 = tkinter.Label(canvas, text = "점수 : "+str(point), font = ("맑은고딕", 25))
            label2.place(x = 10, y = 550)  
            canvas.update()

    
        while b1==i :
        # 입력한 글자와 글자가 같으면 글자는 사라지고 점수는 올라감
            ch = entry3.get()
            if ch == kill : # 입력한 단어가 같은지 비교
                b1 +=1
                point+=1 # 점수 상승
             
                print(1,ch) # 비교가 작동하는지  확인용
            
                label2 = tkinter.Label(canvas, text = "점수 : "+str(point), font = ("맑은고딕", 25))
                label2.place(x = 10, y = 550) 
                label3.destroy()
                #entry3.insert(0,'')
                print("삭제")
                entry3.delete(0,len(entry3.get()))
               
        

            canvas.update()
        i +=1

        if i == stage_number :
            et = datetime.datetime.now()
            game_massagebox()
            break

# 글자 입력창에 있는 주소를 전송
def input_txt_dtn():
    global aaaa, txt,f,b
    
    txt = entry_get_fille.get()
    if len(txt) == 0:
        aaaa = 0
    else :
        aaaa = 1
        in_file = open(str(txt), 'r', encoding = 'utf-8')
        f = in_file.readline()
        b = f.split(',')
        print(b)
        in_file . close
    text.delete('1.0', END)
    word_list()


def one_stage():
    global stage_number
    stage_number = 10
    print(stage_number)
    start_game_btn(stage_number)

def two_stage():
    global stage_number
    stage_number = 15
    print(stage_number)
    start_game_btn(stage_number)

def three_stage():
    global stage_number
    stage_number = 20
    print(stage_number)
    start_game_btn(stage_number)

def four_stage():
    global stage_number
    stage_number = 25
    print(stage_number)
    start_game_btn(stage_number)

def five_stage():
    global stage_number
    stage_number = 30
    print(stage_number)
    start_game_btn(stage_number)

def six_stage():
    global stage_number
    stage_number = 35
    print(stage_number)
    start_game_btn(stage_number)

root = tkinter.Tk()
root.title("한글 타자 게임")
root.resizable(False, False)
root.geometry("800x600")

"""--------------------     frame 1     -----------------------"""
# 로그인 페이지
frame1 = tkinter.Frame(root)
frame1.pack(anchor = "center", expand = "yes")

entry_id = tkinter.Entry(frame1, width=25,font = ("맑은고딕", 16))
entry_id.insert(0,'ID를 입력해 주세요')
entry_id.bind("<Button-1>",clear1)
entry_id.pack()

entry_pw = tkinter.Entry(frame1, width=25,font = ("맑은고딕", 16))
entry_pw.insert(0,'PW를 입력해 주세요')
entry_pw.bind("<Button-1>",clear2)
entry_pw.pack()

log = tkinter.Button(frame1,text = "LOGIN", font = ("맑은고딕", 30), command = surch)
log.place(x = 440, y = 280)
log.pack()

add_button = tkinter.Button(frame1,text = "회원가입", font = ("맑은고딕", 30), command = toggle3)
add_button.pack()

"""-------------------------------     frame 2     ---------------------------------------"""

frame2 = tkinter.Frame(root)

classic = tkinter.Button(frame2,text = "classic", font = ("맑은고딕", 30), command = toggle4)
classic.pack(side= LEFT)


"""time_attack = tkinter.Button(frame2,text = "time attack", font = ("맑은고딕", 30), command = toggle5)
time_attack.pack(side= LEFT)"""

option = tkinter.Button(frame2,text = "option", font = ("맑은고딕", 30), command = toggle2)
option.pack(side= LEFT)

logout = tkinter.Button(frame2,text = "logout", font = ("맑은고딕", 30), command = toggle1_1)
logout.pack(side= LEFT)


"""----------------------------     frame 3     ---------------------------------------"""
frame3 = tkinter.Frame(root)

label6 = tkinter.Label(frame3, text = '현재 사용 단어', font = ("맑은 고딕",20))
label6.pack()

text = tkinter.Text(frame3,width=40, height = 5, font = ("맑은고딕", 16))
text.pack()

# 단어파일 입력
entry_get_fille = tkinter.Entry(frame3,width=25,font = ("맑은고딕", 16))
entry_get_fille.pack()

tx = tkinter.Button(frame3,text = "단어 업로드", font = ("맑은고딕",30), command = input_txt_dtn)
tx.pack()
# 메인 화면으로 이동
bk = tkinter.Button(frame3,text = "back", font = ("맑은고딕", 30), command = toggle1_1)
bk.pack()


"""----------------------------      frame 4       ---------------------------------------"""
# 회원가입 페이지
frame4 = tkinter.Frame(root)
entry_new_id = tkinter.Entry(frame4, width=25,font = ("맑은고딕", 16))
entry_new_id.bind("<Button-1>",clear3)
entry_new_id.pack()

entry_new_pw = tkinter.Entry(frame4, width=25,font = ("맑은고딕", 16))
entry_new_pw.bind("<Button-1>",clear4)
entry_new_pw.pack()

new_input = tkinter.Button(frame4,text = "등록", font = ("맑은고딕", 30), command = new_member)
new_input.pack()

back = tkinter.Button(frame4,text = "back", font = ("맑은고딕", 30), command = toggle)
back.pack()

"""----------------------------      frame 5      ---------------------------------------"""
frame5 = tkinter.Frame(root)

new_input = tkinter.Button(frame5,text = "1 stage", font = ("맑은고딕", 30), command = one_stage)
new_input.pack()

new_input = tkinter.Button(frame5,text = "2 stage", font = ("맑은고딕", 30), command = two_stage)
new_input.pack()

new_input = tkinter.Button(frame5,text = "3 stage", font = ("맑은고딕", 30), command = three_stage)
new_input.pack()

new_input = tkinter.Button(frame5,text = "4 stage", font = ("맑은고딕", 30), command = four_stage)
new_input.pack()

new_input = tkinter.Button(frame5,text = "5 stage", font = ("맑은고딕", 30), command = five_stage)
new_input.pack()

new_input = tkinter.Button(frame5,text = "6 stage", font = ("맑은고딕", 30), command = six_stage)
new_input.pack()

new_input = tkinter.Button(frame5,text = "back", font = ("맑은고딕", 30), command = toggle1_1)
new_input.pack()

"""----------------------------      frame 6      ---------------------------------------"""
frame6 = tkinter.Frame(root)


root.mainloop()
