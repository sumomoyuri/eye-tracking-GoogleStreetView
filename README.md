# eye-tracking-GoogleStreetView
eye tracking in case of exploring Google Street View using an eye tracker "Tobii Pro Nano" and visualization with video, panoramic images and, kernel density  
アイトラッカー（TobiiProNano）を用いた、Googleストリートビュー探索時のアイトラッキングと、動画、パノラマ画像、カーネル密度での視線の可視化

## 【概要】
アイトラッカー（TobiiProNano）を用いた、Googleストリートビュー探索時のアイトラッキングデータを記録し、動画への可視化や、GoogleストリートビューのURL情報をもとに生成したパオラマ画像上で可視化するための、一連のデータ処理プログラム。

## 【アイトラッカー Tobii Pro Nano】
`Tobii Pro Nano`：トビー社の小型軽量アイトラッカー。PC画面下部に設置することで、PC画面内の視線座標や瞳孔径をサンプリングレート60Hで記録することができる。

### 【視線データの記録　recorder.py】
Tobii Pro Nanoでアイトラッキングをするためには、専用の無料ソフトウェアである`Tobii Eye Tracker Manager`で、事前に位置関係の設定やサンプリングレートなどの設定や、被視線計測者の視線キャリブレーションを実施することが必要。  
本プログラムでは、`Tobii Eye Tracker Manager`での設定とキャリブレーション後に、`recorder.py`を実行することで、時刻と視線座標・瞳孔径を`output/gaze.csv`に出力することができる。  

