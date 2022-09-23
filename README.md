概要

決められた感情付きのセリフを読み上げ、システムが感情を推定して、感情を上手く表現できていれば相手に攻撃、間違えていれば自分がダメージを受けるゲーム

#python == 3.7.8
#ライブラリに関してはrequirements.txtを参照

使い方

アプリケーションの実行

python tkinter_app.py

上記のコマンドで、guiが開きアプリケーションを実行できる


学習に関して

・学習はclolab上で行った。traningフォルダ内に学習コードがある。実行するにはcolab上でフォルダの位置を適切な場所に変える必要あり

training/audio_training_rav.ipynbは、ravdess datasetsを使用
・使用データセット(ravdess datasets)
https://www.kaggle.com/datasets/uwrfkaggler/ravdess-emotional-speech-audio

training/audio_training.ipynbは、声優統計コーパスを使用
http://voice-statistics.github.io/


感情推定に関して

感情推定を行っている関数はemotion_func_ravb.py、emotion_func.pyである。
emotion_func_ravb.pyは、ravdess datasetsを使用したモデルの関数
emotion_func.pyは、声優統計コーパスを使用したモデルの関数

modelフォルダ内に学習したモデルがある。
audio_emotion_v01.h5: 声優統計コーパスを使用したモデル
audio_emotion_rav_male_ver3.h5: ravdessの男性発話のみを用いたモデル
audio_emotion_rav_female.h5: ravdessの女性発話のみを用いたモデル
