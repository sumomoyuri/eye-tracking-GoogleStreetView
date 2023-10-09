# eye-tracking-GoogleStreetView
eye tracking in case of exploring Google Street View using an eye tracker "Tobii Pro Nano" and visualization with video, panoramic images and, kernel density  
アイトラッカー（TobiiProNano）を用いた、Googleストリートビュー探索時のアイトラッキングと、動画、パノラマ画像、カーネル密度での視線の可視化

https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/292617ec-e618-4d14-9bd0-8d9df8085b4c

![51](https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/25785f09-49c4-47d4-a38d-035868db1b46)

![511](https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/e76266ff-a455-4630-84b8-8c8f4cf06dbe)

## 【概要】
アイトラッカー（TobiiProNano）を用いた、Googleストリートビュー探索時のアイトラッキングデータを記録し、動画への可視化や、GoogleストリートビューのURL情報をもとに生成したパオラマ画像上で可視化するための、一連のデータ処理プログラム。

## 【アイトラッカー Tobii Pro Nano】
`Tobii Pro Nano`：トビー社の小型軽量アイトラッカー。PC画面下部に設置することで、PC画面内の視線座標や瞳孔径をサンプリングレート60Hで記録することができる。
![download](https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/01742d70-3b0b-47d9-88a3-de633e7ede91)

### 【視線データの記録】
Tobii Pro Nanoでアイトラッキングをするためには、専用の無料ソフトウェアである`Tobii Eye Tracker Manager`で、事前に位置関係の設定やサンプリングレートなどの設定や、被視線計測者の視線キャリブレーションを実施することが必要。  
本プログラムでは、`Tobii Eye Tracker Manager`での設定とキャリブレーション後に、`recorder.py`を実行することで、時刻と視線座標・瞳孔径を`output/gaze.csv`に出力することができる。  

### 【Googleストリートビューのカメラ情報の記録】
Googleストリートビューの表示画面と視線データを紐付けて、パノラマ画像上で視線データを可視化するためには、Googleストリートビューで表示しているパノラマ画像のカメラ情報(方角、視野角、カメラアングルなど)を時刻とともに記録しておく必要がある。  
そして、その情報はURLに含まれているため、Googleストリートビュー探索時に（場所の移動や見回しによって）URLが変わるたびに、時刻とURLを記録しておくことで、時刻情報をもとに後からGoogleストリートビュー画像と視線データを紐付けることが出来る。
```
GoogleストリートビューのURLの例：　https://www.google.com/maps/@35.681537,139.766942,2a,75y,170h,90t...
```
この場合、緯度：`35.681537`　経度：`139.766942`　上下視野角：`75`　カメラ方位：`170`　仰角：`90 `　となる。  

このURL情報の記録は、Google Chromeを操作することのできるモジュール`chromedriver`を用いて行う。
本プログラムでは、`get-url.ipynb`の各セルを順番に実行することで、まずは`recorder.py`を実行して視線データの記録を開始し、続けてchromedriverでブラウザのstreet viewを立ち上げることで、視線の記録と合わせてURLの記録を開始することができる。  
なお、被験者はchromedriverの有無を気にせず、通常通りキーボード操作やマウス操作でGoogleストリートビュー上を探索することができる。

