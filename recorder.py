# -*- coding: utf-8 -*-
# 視線計測記録用プログラム（Ver:2022/03/08）
# 注：Tobii Eye Tracker Managerで事前に視線のキャリブレーションが必要。

import tobii_research as tr
import sys
import datetime
import csv

# 出力ファイル
f = open('output/output.csv', 'a')
writer = csv.writer(f)

# アイトラッカーの存在確認
eyetrackers = tr.find_all_eyetrackers()
if len(eyetrackers) >= 1 :
    eyetracker = eyetrackers[0]
else:
    print("Error: Not Found EyeTracker")
    sys.exit()

# アイトラッカー情報の表示
my_eyetracker = eyetrackers[0]
print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

# CallBack関数
def MyCallBack(gaze_data):
    tt = datetime.datetime.now() #時刻
    left_point = gaze_data.left_eye.gaze_point.position_on_display_area #左目の座標
    right_point = gaze_data.right_eye.gaze_point.position_on_display_area #右目の座標
    left_pupil = gaze_data.left_eye.pupil.diameter #左目の瞳孔径
    right_pupil = gaze_data.right_eye.pupil.diameter #右目の瞳孔径
    left_pupil_validity = gaze_data.left_eye.pupil.validity #左目の瞳孔径が取得できていればtrue
    right_pupil_validity = gaze_data.right_eye.pupil.validity #左目の瞳孔径が取得できていればtrue
    
    writer.writerow([tt,left_point[0],left_point[1],right_point[0], right_point[y],left_pupil,right_pupil,left_pupil_validity,right_pupil_validity])

# CallBack関数の登録
eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, MyCallBack, as_dictionary=False)

# プログラムの終了
while(True):
    # if Key is "ESC"
    if key == 27:
        # CallBack関数の解除
        eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, MyCallBack)
        f.close()
        sys.exit()
