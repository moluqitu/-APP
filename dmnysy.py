import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("❥(^_-)")
root.geometry("500x400")  # 设置窗口大小

# 定义问题和选项的数据结构
questions = [
    {
        "question": "可爱的某某，美好的一天要开始了哦٩(๑^o^๑)۶！！！", #0
        "options": [tk.PhotoImage(file="2.png")]
    },
    {
        "question": "早上几点出发呀？（有本事你选10:00试试（手动狗头））",
        "options": ["8:00", "9:00", "10:00"]
    },
    {
        "question": "什么？你还真选10:00？给你一个重新选择的机会！（你还敢选10:00嘛）",
        "options": ["8:00", "9:00", "10:00"]
    },
    {
        "question": "什么？你还选10:00？看我把10:00这个选项删除了看你怎么选略略略",
        "options": ["8:00", "9:00"]
    },
    {
        "question": "8:00当然是有点早得嘞，怎么会有8:00这个选项呢",
        "options": ["9:00"]
    },
    {
        "question": "8:00当然是有点早得嘞，怎么会有8:00这个选项呢", #5
        "options": ["9:00", "10:00"]
    },
    {
        "question": "上午想去看千渡长江美术馆吗",
        "options": ["想", "特别想", "超级想"]
    },
    {
        "question": "为中午的带鱼选择一家饭店吧",
        "options": [tk.PhotoImage(file="3.png"), "大众点评第一名", "其实上面两个选项是同一家店啦"] #7
    },
    {
        "question": "下午想先唱歌还是想先看电影呢（温馨提示:电影时间(两个小时)有13:40,14:40,16:00,17:00）",
        "options": ["先看电影", "先唱歌"]
    },
    {
        "question": "下午看什么电影呢？",
        "options": ["没得选，只能选前任四哦"]
    },
    {
        "question": "晚上去哪吃饭然后干嘛呢？",
        "options": ["不知道，要不到时再说吧"] #10
    },
    {
        "question": "美好的一天结束了！！！(手动撒花 累der)",
        "options": [tk.PhotoImage(file="1.png")]
    },
    {
        "question": "什么？你还真选10:00？给你一个重新选择的机会！（你还敢选10:00嘛）",  #12
        "options": ["9:00", "10:00"]
    },
    {
        "question": "什么？你还选10:00？看我把10:00这个选项也删除了看你怎么选略略略",
        "options": ["9:00"]
    },
    # 添加更多问题和选项
]


# 答案列表
answers = []
a = []

# 创建问题和选项的Label
question_label = tk.Label(root, text=questions[len(answers)]["question"])
question_label.pack()

# 创建Radio按钮
selected_option = tk.StringVar()
selected_option.set(None)

def select_option(option):
    global flag, flag1
    option = str(option)

    if option != "pyimage1" and option != "pyimage6":
        print(option)
        print(type(option))

    if option == "pyimage1":
        root.geometry("500x100")  # 设置窗口大小
        question_label.config(text=questions[1]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[1]["options"])
        flag = 1
        flag1 = 1

    elif option == "10:00" and flag == 1 and flag1 == 1:
        question_label.config(text=questions[2]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[2]["options"])
        flag = flag + 1
        a.append(1)

    elif option == "10:00" and flag == 2 and flag1 == 1:
        question_label.config(text=questions[3]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[3]["options"])
        flag = flag + 1
        a.append(2)

    elif option == "10:00" and flag == 1 and flag1 == 0:
        question_label.config(text=questions[12]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[12]["options"])
        flag = flag + 1
        a.append(3)

    elif option == "10:00" and flag == 2 and flag1 == 0:
        question_label.config(text=questions[13]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[13]["options"])
        flag = flag + 1
        a.append(4)

    elif option == "8:00" and flag == 3:
        question_label.config(text=questions[4]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[4]["options"])
        a.append(5)

    elif option == "8:00" and flag == 1:
        question_label.config(text=questions[5]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[5]["options"])
        flag1 = 0
        a.append(6)

    elif option == "9:00":
        question_label.config(text=questions[6]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[6]["options"])

    elif option == "想" or option == "特别想" or option == "超级想":
        root.geometry("500x400")  # 设置窗口大小
        question_label.config(text=questions[7]["question"])
        selected_option.set(None)
        create_radio_buttonsimagegai(questions[7]["options"])

    elif option == "pyimage2" or option == "大众点评第一名" or option == "其实上面两个选项是同一家店啦":
        root.geometry("500x100")  # 设置窗口大小
        question_label.config(text=questions[8]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[8]["options"])

    elif option == "先看电影" or option == "先唱歌":
        answers.append(option)
        if option == "先看电影":
            answers.append("唱歌")
        else:
            answers.append("看电影")
        question_label.config(text=questions[9]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[9]["options"])

    elif option == "没得选，只能选前任四哦":
        question_label.config(text=questions[10]["question"])
        selected_option.set(None)
        create_radio_buttons(questions[10]["options"])

    elif option == "不知道，要不到时再说吧":
        root.geometry("500x400")  # 设置窗口大小
        question_label.config(text=questions[11]["question"])
        selected_option.set(None)
        create_radio_buttonsimage(questions[11]["options"])

    else:
        generate_word_button.pack()


# 创建Radio按钮
radio_buttons = []

def create_radio_buttons(options):
    for radio_button in radio_buttons:
        radio_button.destroy()

    radio_buttons.clear()

    for option in options:
        radio_button = tk.Radiobutton(root, text=option, variable=selected_option, value=option,
                                      command=lambda option=option: select_option(option))
        radio_buttons.append(radio_button)
        radio_button.pack()

def create_radio_buttonsimage(options):
    for radio_button in radio_buttons:
        radio_button.destroy()

    radio_buttons.clear()

    for option in options:
        radio_button = tk.Radiobutton(root, image=option, variable=selected_option, value=option,
                                      command=lambda option=option: select_option(option))
        radio_buttons.append(radio_button)
        radio_button.pack()

def create_radio_buttonsimagegai(options):
    global flaggai
    flaggai = 1

    for radio_button in radio_buttons:
        radio_button.destroy()

    radio_buttons.clear()

    for option in options:
        if flaggai == 1:
            radio_button = tk.Radiobutton(root, image=option, variable=selected_option, value=option,
                                          command=lambda option=option: select_option(option))
            radio_buttons.append(radio_button)
            radio_button.pack()
            flaggai = flaggai - 1
        elif flaggai == 0:
            radio_button = tk.Radiobutton(root, text=option, variable=selected_option, value=option,
                                          command=lambda option=option: select_option(option))
            radio_buttons.append(radio_button)
            radio_button.pack()

# 初始化第一个问题的单选按钮
create_radio_buttonsimage(questions[len(answers)]["options"])

def generate_word():
    root.geometry("500x120")  # 设置窗口大小
    longtext = f"""
    *美好的一天开始了(^o^)(消声烟花)
    早上9:00到八道门打车去千渡长江美术博物馆，到了约为9:30左右，参观两个小时左右(^o^)
    去菜园小馆吃带鱼，吃完大约2:00(^o^)
    下午{answers[0]}两个小时,然后去{answers[1]}两个小时(^o^)
    晚上干什么呢？相声？台球？吃提拉米苏？逛街？犹豫犹豫，待定吧(^o^)
    *美好的一天结束了，累der但是有意义(^o^)(手动撒花)
    """
    question_label.config(text=longtext)

generate_word_button = tk.Button(root, text="生成为某某准备的出行规划", command=generate_word)

root.mainloop()
