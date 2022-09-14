import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import random
import emotion_func_ravb

# label_decoder = {0:"angry", 1:"happy", 2:"normal"}

label_decoder = {0:'male_angry', 1:'male_happy', 2:'male_sad', 3:'male_surprise'}
# label_decoder = {0:'female_angry', 1:'female_happy', 2:'female_sad', 3:'female_surprise'}

# # 重複なし
# def rand_ints_nodup(a, b, k):
#   ns = []
#   while len(ns) < k:
#     n = random.randint(a, b)
#     if not n in ns:
#       ns.append(n)
#   return ns


happy_list = ["本当に良かった。僕も嬉しいです。",
              "ありがとうございます！\n これからもよろしくお願いします!",
              "say the word happy."
]

angry_list = ["なんなんだよまじで!",
              "ふざけんなよ、絶対許さないから!",
              "say the word angry."
]

sad_list = ["本当に、本当に申し訳ございませんでした...!",
              "なんでこんな事をしてしまったんだ...",
              "say the word sad."
]


surprise_list = ["え、本当に??、本当に??、まじで??",
              "そんな事があったんですか!?",
              "say the word surprise."
]

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(expand=1, fill=tk.BOTH)
        self.model = emotion_func_ravb.load_emotionModel()
       
        master.geometry("1350x700")
        master.title("上手に感情を表現して相手を倒せ!")

        self.create_widgets()

    # ウィジェットの生成と配置
    def create_widgets(self):

        self.rule = tk.Label(self, text="ルール",font=("",25))
        self.rule.place(x=20,y=20)
        self.rule = tk.Label(self, text="1. 録音は4秒。ボタンを押したらすぐ発話しよう",font=("",13))
        self.rule.place(x=20,y=100)
        self.rule = tk.Label(self, text="2. 感情が上手く表現出来ていたら相手に25ダメージ\n 間違えていたら自分が25ダメージ",font=("",13))
        self.rule.place(x=20,y=150)
        self.rule = tk.Label(self, text="3. 相手のライフが0になったらあなたの勝ち！ \n  自分が0になったらあなたの負け。",font=("",13))
        self.rule.place(x=20,y=200)
        self.enemy_hp = tk.Label(self, text="敵のhp：",font=("",20))
        self.enemy_hp.place(x=900,y=50)     
        self.enemy_num = tk.Label(self, borderwidth = 1, relief="raised", text=100, font=("",20))
        self.enemy_num.place(x=1060, y=40, width = 60, height=60)
        self.photo = tk.PhotoImage(file="enemy3.png",  master=root,  width=350, height=350)
        self.image_label = tk.Label(self, image = self.photo)
        self.image_label.place(x=500, y = 60, width=350, height=350)
        
        self.result = tk.Label(self, borderwidth = 1, relief="raised", text="スタートを押してセリフを言って!", font=("",20))
        self.result.place(x=320, y=380, width = 600, height=70)

        self.result_num = tk.Label(self, text="", font=("",14))
        self.result_num.place(x=330, y=340, width = 600, height=40)
        self.my_hp = tk.Label(self, text="自分のhp：",font=("",20))
        self.my_hp.place(x=40,y=500)
        self.my_num = tk.Label(self, borderwidth = 1, relief="raised", text=100, font=("",20))
        self.my_num.place(x=200, y=490, width = 60, height=60)
        self.record_button = tk.Button(self, text= "スタート",command=self.record, font=("",20))
        self.record_button.place(x= 300, y= 520, width = 120, height=60)

        self.reset_button = tk.Button(self, text= "リセット",command=self.reset, font=("",20))
        self.reset_button.place(x= 1000, y= 270, width = 100, height=50)

        self.radio_value = tk.IntVar(value = 1) 
        
        # ラジオボタンの作成
        self.radio0 = tk.Radiobutton(self.master, text = "angry:  ふざけんなよ、絶対許さないから!", font=("",13),
                                    command = self.radio_click, variable = self.radio_value, value = 0, anchor=tk.W, padx = 0)
        self.radio0.place(x=460, y= 480, width= 430, height=80)
        self.radio1 = tk.Radiobutton(self.master, text = "happy:  ありがとうございます！\nこれからもよろしくお願いします!", font=("",13),
                                    command = self.radio_click, variable = self.radio_value, value = 1, anchor=tk.W,padx = 0)
        self.radio1.place(x=850, y= 480, width= 430, height=80)
        self.radio2 = tk.Radiobutton(self.master, text = "sad:  本当に、本当に申し訳ございませんでした...!", font=("",13),
                                    command = self.radio_click, variable = self.radio_value, value = 2, anchor=tk.W, justify='left', padx = 0)
        self.radio2.place(x=460, y= 550, width= 430, height=80) 
        self.radio3 = tk.Radiobutton(self.master, text = "surprise:  え、本当に??,本当に??,まじで??", font=("",13),
                                    command = self.radio_click, variable = self.radio_value, value = 3, anchor=tk.W, justify='left',padx = 0)
        self.radio3.place(x=850, y= 550, width= 430, height=80)


        
    def radio_click(self):
        value = self.radio_value.get()
        print("click: " , value)
    
    def reset(self):
        self.result_num["text"] = ""
        self.enemy_num["text"] = 100
        self.my_num["text"] = 100
        self.result["text"] = "スタートを押してセリフを言って!"
        
        self.change_text()
    
    # def change_text(self):
    #     random_list = rand_ints_nodup(0,7,3)
    #     self.radio0["text"] = "明るく:" + text_list[random_list[0]]
    #     self.radio1["text"] = "怒って:" + text_list[random_list[1]]
    #     self.radio2["text"] = "普通に:" + text_list[random_list[2]]

    #録音する毎にテキストが変更される
    def change_text(self):
       
        self.radio0["text"] = "angry:  " + angry_list[random.randint(0, 2)]
        self.radio1["text"] = "happy:  " + happy_list[random.randint(0, 2)]
        self.radio2["text"] = "sad:  " + sad_list[random.randint(0, 2)]
        self.radio3["text"] = "surprise:  " + surprise_list[random.randint(0, 2)]
      
        
    
    def record(self):
        print("record")
        self.result["text"] = "録音中・・・"

        #選択した感情ラベル
        emotion_label = label_decoder[self.radio_value.get()]

        #推定された感情ラベル
        emotion_out = emotion_func_ravb.emotion_out(self.model)
        emotion = emotion_out[0]
        emotion_list = emotion_out[1]
        print(emotion)
        print(emotion_list)
        emotion_list_text = "推定結果  angry: {angry}  happy:  {happy}  sad:  {sad}  surprise:  {surprise}  (%)".format(angry = round(emotion_list[0] * 100), happy = round(emotion_list[1] * 100), sad = round(emotion_list[2] * 100), surprise = round(emotion_list[3] * 100))

        print(emotion_list_text)
        self.result_num["text"] = emotion_list_text

        #推定された感情が合っているかどうかで分岐
        if emotion_label == emotion:
            self.enemy_num["text"] = self.enemy_num["text"]-25
            if self.enemy_num["text"] == 0:
                self.result["text"] = "You win!!"
            else:
                self.result["text"] = "うまく表現出来てるよ!! その調子!"
        else:
            self.my_num["text"] = self.my_num["text"]-25
            if self.my_num["text"] == 0:
                self.result["text"] = "You lose!!"
            else:
                self.result["text"] = "まだまだ練習が足りないよ!"

        self.change_text()

if __name__ == "__main__":
    root = tk.Tk()
    Application(master=root)
    root.mainloop()