# eye-tracking-GoogleStreetView
eye tracking in case of exploring Google Street View using an eye tracker "Tobii Pro Nano" and visualization with video, panoramic images and, kernel density  
アイトラッカー（TobiiProNano）を用いた、Googleストリートビュー探索時のアイトラッキングと、動画、パノラマ画像、カーネル密度での視線の可視化
  

https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/3cb0390c-95c8-4b1b-94c0-fcb7b25ee61f  
  
<img width="1000" alt="panorama_sample" src="https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/46cdee2f-f64f-44d1-a5c6-24285e1162f5">  
<img width="1000" alt="kernel_sample" src="https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/6deddf63-0069-48a4-8371-c5e3b23ad340">  

## 【概要】
アイトラッカー（TobiiProNano）を用いた、Googleストリートビュー探索時のアイトラッキングデータを記録し、動画への可視化や、GoogleストリートビューのURL情報をもとに生成したパノラマ画像上で可視化するための、一連のデータ処理プログラム。  
<img width="500" alt="kernel_sample" src="https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/fae93d1e-251b-4065-8404-2af64e0bf55c"> 

## 【アイトラッカー Tobii Pro Nano】
`Tobii Pro Nano`：トビー社の小型軽量アイトラッカー。PC画面下部に設置することで、PC画面内の視線座標や瞳孔径をサンプリングレート60Hで記録することができる。


## 【視線データの記録　recorder.py】
Tobii Pro Nanoでアイトラッキングをするためには、専用の無料ソフトウェアである`Tobii Eye Tracker Manager`で、事前に位置関係の設定やサンプリングレートなどの設定や、被視線計測者の視線キャリブレーションを実施することが必要。  
本プログラムでは、`Tobii Eye Tracker Manager`での設定とキャリブレーション後に、`recorder.py`を実行することで、時刻と視線座標・瞳孔径を`output/gaze.csv`に出力することができる。  

出力データの形式は以下の通り。x,y座標はモニタの左上を原点として0〜1の間で記録され、瞳孔径はmm単位で記録されている。

|時刻|右目のx座標|右目のy座標|左目のx座標| 左目のy座標|右目の瞳孔径|左目の瞳孔径|右目瞳孔径データ有無|左目瞳孔径データ有無|
|:----|:----|:----|:----|:----|:----|:----|:----|:----|
|2021-05-14 10:14:30.012000|0.6005534529685974| 0.5111197829246521|0.6006736159324646| 0.5411497950553894|3.6480255127|3.5655670166|True|True|
|2021-05-14 10:14:30.012000|0.6005534529685974| 0.5111197829246521|0.6006736159324646| 0.5411497950553894|3.6480255127|3.5655670166|True|True|
|2021-05-14 10:14:30.028000|0.6024783849716187| 0.5084214210510254|0.6006250381469727| 0.5380455851554871|3.65855407715|3.58148193359|True|True|
|2021-05-14 10:14:30.028000|0.6024783849716187| 0.5084214210510254|0.6006250381469727| 0.5380455851554871|3.65855407715|3.58148193359|True|True|
|2021-05-14 10:14:30.045000|0.6006242036819458| 0.5084537267684937|0.5998525619506836| 0.537571132183075|3.65812683105|3.59248352051|True|True|
|2021-05-14 10:14:30.045000|0.6006242036819458| 0.5084537267684937|0.5998525619506836| 0.537571132183075|3.65812683105|3.59248352051|True|True|
|2021-05-14 10:14:30.061000|0.6033099293708801| 0.5138833522796631|0.6076745986938477| 0.5201295018196106|3.66387939453|3.59434509277|True|True|
|2021-05-14 10:14:30.061000|0.6033099293708801| 0.5138833522796631|0.6076745986938477| 0.5201295018196106|3.66387939453|3.59434509277|True|True|
|2021-05-14 10:14:30.078000|0.637449324131012| 0.5655802488327026|0.609611451625824| 0.5185182094573975|3.21092224121|3.52241516113|True|True|
|2021-05-14 10:14:30.078000|0.637449324131012| 0.5655802488327026|0.609611451625824| 0.5185182094573975|3.21092224121|3.52241516113|True|True|


## 【Googleストリートビューのカメラ情報の記録　get-url.ipynb】
Googleストリートビューの表示画面と視線データを紐付けて、パノラマ画像上で視線データを可視化するためには、Googleストリートビューで表示しているパノラマ画像のカメラ情報(方角、視野角、カメラアングルなど)を時刻とともに記録しておく必要がある。  
そして、その情報はURLに含まれているため、Googleストリートビュー探索時に（場所の移動や見回しによって）URLが変わるたびに、時刻とURLを記録しておくことで、時刻情報をもとに後からGoogleストリートビュー画像と視線データを紐付けることが出来る。
```
GoogleストリートビューのURLの例：　https://www.google.com/maps/@35.681537,139.766942,2a,75y,170h,90t...
```
この場合、緯度：`35.681537`　経度：`139.766942`　上下視野角：`75`　カメラ方位：`170`　仰角：`90`　となる。  

このURL情報の記録は、Google Chromeを操作することのできるモジュール`chromedriver`を用いて行う。
本プログラムでは、`get-url.ipynb`の各セルを順番に実行することで、まずは`recorder.py`を実行して視線データの記録を開始し、続けてchromedriverでブラウザのstreet viewを立ち上げることで、視線の記録と合わせてURLの記録を開始し、`output/url.csv`に出力することができる。  
なお、被験者はchromedriverの有無を気にせず、通常通りキーボード操作やマウス操作でGoogleストリートビュー上を探索することができる。

出力データは以下の通り。カメラ方位は北が0度、カメラ上下角度は天井が0度になっている。

|時刻|緯度|経度|視野角|カメラ方位|カメラ上下角度|paneID|URL|
|:----|:----|:----|:----|:----|:----|:----|:----|
|2021-05-14 10:14:30.061915|35.6818905|139.7677372|75|285.59|90|7Bo4nn9EfYkz-rdzbsKfvw|https://www.google.com/maps/@35.6818905,139.7677372,2a,75y,285.59h,90t/data=!3m6!1e1!3m4!1s7Bo4nn9EfYkz-rdzbsKfvw!2e0!7i13312!8i6656|
|2021-05-14 10:14:32.362105|35.6818973|139.7677009|75|285.59|90|DSSW3-Ba0_LXifmOIlqGbQ|https://www.google.com/maps/@35.6818973,139.7677009,2a,75y,285.59h,90t/data=!3m6!1e1!3m4!1sDSSW3-Ba0_LXifmOIlqGbQ!2e0!7i13312!8i6656|
|2021-05-14 10:14:33.664514|35.6819062|139.7676692|75|285.59|90|OzNk__GpWXGr-AZPTFrehQ|https://www.google.com/maps/@35.6819062,139.7676692,2a,75y,285.59h,90t/data=!3m6!1e1!3m4!1sOzNk__GpWXGr-AZPTFrehQ!2e0!7i13312!8i6656|
|2021-05-14 10:14:35.880201|35.6819173|139.7676336|75|285.59|90|8PXGZrEDzwsiMIW7YDyK_Q|https://www.google.com/maps/@35.6819173,139.7676336,2a,75y,285.59h,90t/data=!3m6!1e1!3m4!1s8PXGZrEDzwsiMIW7YDyK_Q!2e0!7i13312!8i6656|
|2021-05-14 10:14:40.065441|35.6819266|139.7675971|75|285.59|90|ZP0jpwMOMlI98rv61nNHSQ|https://www.google.com/maps/@35.6819266,139.7675971,2a,75y,285.59h,90t/data=!3m6!1e1!3m4!1sZP0jpwMOMlI98rv61nNHSQ!2e0!7i13312!8i6656|
|2021-05-14 10:14:42.846908|35.6819266|139.7675971|75|292.6|90|ZP0jpwMOMlI98rv61nNHSQ|https://www.google.com/maps/@35.6819266,139.7675971,2a,75y,292.6h,90t/data=!3m6!1e1!3m4!1sZP0jpwMOMlI98rv61nNHSQ!2e0!7i13312!8i6656|
|2021-05-14 10:14:43.711487|35.6819266|139.7675971|75|299.87|90|ZP0jpwMOMlI98rv61nNHSQ|https://www.google.com/maps/@35.6819266,139.7675971,2a,75y,299.87h,90t/data=!3m6!1e1!3m4!1sZP0jpwMOMlI98rv61nNHSQ!2e0!7i13312!8i6656|
|2021-05-14 10:14:44.893362|35.6819355|139.7675625|75|299.87|90|897Qk7Djww5VYSYoJleJew|https://www.google.com/maps/@35.6819355,139.7675625,2a,75y,299.87h,90t/data=!3m6!1e1!3m4!1s897Qk7Djww5VYSYoJleJew!2e0!7i13312!8i6656|
|2021-05-14 10:14:46.031282|35.6819355|139.7675625|75|318.8|90|897Qk7Djww5VYSYoJleJew|https://www.google.com/maps/@35.6819355,139.7675625,2a,75y,318.8h,90t/data=!3m6!1e1!3m4!1s897Qk7Djww5VYSYoJleJew!2e0!7i13312!8i6656|
|2021-05-14 10:14:48.930007|35.6819355|139.7675625|75|327.44|90|897Qk7Djww5VYSYoJleJew|https://www.google.com/maps/@35.6819355,139.7675625,2a,75y,327.44h,90t/data=!3m6!1e1!3m4!1s897Qk7Djww5VYSYoJleJew!2e0!7i13312!8i6656|

## 【動画での視線可視化　visualize_gaze_movement.ipynb】
Googleストリートビュー探索時に画面画録画をし、動画の開始時刻を記録しておくと、`visualize_gaze_movement.ipynb`を実行することで、後から時刻情報をもとに動画での視線の可視化をすることができる。
`output`フォルダに、`visualize_gaze_movement.ipynb`で可視化したサンプル動画として、元動画の`screen_record_sample.mp4`と可視化後の`gaze_movement_sample_readme.mp4`を格納している。

## 【パノラマ画像での視線可視化　generate-gaze-map.ipynb】
Googleストリートビュー探索時の視線を分析する上では、PC画面に表示される平面画像上の視線位置ではなく、360度のパノラマ画像上での見回しも含めた一連の視線を考える必要がある。
そこで、`get-url.ipynb`で取得したURLデータとrecorder.pyで取得した視線データを紐付け、URLカメラ情報をもとにパノラマ画像と視線データの座標変換を行うことで、同じ地点における見回しも含む一連の視線を一つのパノラマ画像上に可視化することができる。

以下にパノラマ画像での視線可視化の方法を図で示す。  

<img width="500" alt="generate_pano" src="https://github.com/sumomoyuri/eye-tracking-GoogleStreetView/assets/116475757/fc99b94a-0aa4-4d68-8a92-8adb0f58f4f4">  

`generate-gaze-map.ipynb`のセルを順番に実行することで、`URLデータと視線データの紐付け`→`GoogleストリートビューAPI画像の取得`→`座標変換によるパノラマ合成`→`パノラマ画像上での視線可視化`まで行える。

### APIを用いたGoogleストリートビュー画像の取得
googleのAPIで、緯度・経度、画像サイズ、カメラ方向、カメラ角度、水平視野角を指定することで、指定した向きのGoogleストリートビュー画像を取得することができる。
```
#指定したカメラ方向のgsv画像をAPIで取得する関数
def getAPIImg(pointid, latitude, longitude, heading, j):
    # streetviewのURLを作成して画像を取得
    g_url="https://maps.googleapis.com/maps/api/"
    g_url_sub=[]
    g_url_sub.append("streetview?location=" + str(latitude) + "," + str(longitude)) # 場所の指定
    g_url_sub.append("&size=" + str(size[0]) + "x" + str(size[1])) # 画像サイズ
    g_url_sub.append("&heading=" + str(heading)) # カメラの方位
    g_url_sub.append("&pitch=" + str(pitch)) # カメラ角度
    g_url_sub.append("&fov=" + str(fov)) # 水平視野角
    g_url_sub.append("&key=" + api_key) #api key
    for t in g_url_sub:
        g_url = g_url + t
    file =io.BytesIO(urlopen(g_url).read())
    img__ =Image.open(file)
    img_ = np.array(img__, dtype=np.uint8)
    img = cv2.cvtColor(img_, cv2.COLOR_RGB2BGR)
    return img
```

### Googleストリートビュー画像パノラマのパノラマ合成
位置地点における複数方向のGoogleストリートビュー画像を一枚のパノラマ画像として合成するためには、平面から球面への変換行列`K`と球面上での回転行列`R`が必要で、それらは以下の通り算出できる。
  
平面から球面への変換行列`K`：カメラのf値が決まれば決まる。このf値はopenCVのstitchingモジュールで算出した。
```
#Googleストリートビューのカメラパラメータ
focus = 200
#平面から球面への変換行列
K = np.array([[focus, 0, size[0]/2], [0, focus, size[1]/2], [0, 0, 1]], dtype=np.float32)
```
球面上での回転行列`R`：カメラ方位はURLから得られる
```
#thetaはカメラ方位(度)
#球面上での回転行列
sin = math.sin(math.radians((theta)))
cos = math.cos(math.radians((theta)))
R = np.array([[-cos, 0, -sin], [0, 1, 0], [sin, 0, -cos]], dtype=np.float32)
```
  
また、`K`と`R`を元に画像を合成するにあたっては、openCVの関数を使って`画像のマッピング`→`継ぎ目の算出`→`ブレンド処理`の手順で継ぎ目を綺麗に合成することができる。
```
#一地点におけるパノラマ画像を生成する関数
def genPanoImg(images, R_list):

    #images：一地点におけるGoogleストリートビュー画像のリスト
    #R_list：一地点におけるGoogleストリートビュー画像の回転行列のリスト

    #画像のマッピング----------------------------------------
    corners = [] #マッピング後の左上の点の座標のリスト
    masks_warped = [] #画像のWarp()実行結果のリスト
    images_warped = [] #マスクのWarp()実行結果のリスト
    sizes = [] #Warp画像サイズのリスト
    masks = [] #初期化したマスク格納用リスト
    warper = cv2.PyRotationWarper('spherical', scale)
    #マスクの初期化
    for i in range(0, len(images)):
        um = cv2.UMat(255 * np.ones((images[i].shape[0], images[i].shape[1]), np.uint8))
        masks.append(um)
    #全画像とそのマスクに対して warper.warp() を実行して、結果を images_warped と masks_warped それぞれに格納
    for idx in range(0, len(images)):
        corner, image_wp = warper.warp(images[idx], K, R_list[idx], cv2.INTER_LINEAR, cv2.BORDER_REFLECT)
        corners.append(corner)
        sizes.append((image_wp.shape[1], image_wp.shape[0]))
        images_warped.append(image_wp)
        p, mask_wp = warper.warp(masks[idx], K, R_list[idx], cv2.INTER_NEAREST, cv2.BORDER_CONSTANT)
        masks_warped.append(mask_wp.get())
        
    #継ぎ目の算出----------------------------------------
    images_warped_f = []
    for img in images_warped:
        imgf = img.astype(np.float32)
        images_warped_f.append(imgf)
    seam_finder = cv2.detail_GraphCutSeamFinder('COST_COLOR')
    seam_finder.find(images_warped_f, corners, masks_warped)

    #ブレンド処理--------------------------------------------
    blend_strength = 5
    blender = cv2.detail.Blender_createDefault(cv2.detail.Blender_NO)
    dst_sz = cv2.detail.resultRoi(corners=corners, sizes=sizes)
    blend_width = np.sqrt(dst_sz[2] * dst_sz[3]) * blend_strength / 100
    if blend_width < 1:
        blender = cv2.detail.Blender_createDefault(cv2.detail.Blender_NO)
    blender.prepare(dst_sz)
    for idx in range(0, len(images)):
        images_warped_s = images_warped[idx].astype(np.int16)
        blender.feed(cv2.UMat(images_warped_s), masks_warped[idx], corners[idx])

    # #最終結果の出力--------------------------------------------
    result, result_mask = blender.blend(result, result_mask) #ブレンドする。
    pano_img = cv2.normalize(src=result, dst=None, alpha=255., norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U) #正規化
    
    return pano_img
```

### 視線データの座標変換
回転行列Rの逆行列を用いて、以下のようにパノラマ上の極座標を求めることができる。
```
#注視点のパノラマ画像上の極座標を求める関数
def getPolarCoords(gaze_point):
    #gaze_pointリストの中身：[gaze_time, [x,y,pupil], id, 地点ID, urlID, 緯度経度, panoID, head]
    #r_kinv：回転行列Rの逆行列
    x = gaze_point[1][0] * size[0]
    y = gaze_point[1][1] * size[1]
    X = r_kinv[0, 0] * x + r_kinv[0, 1] * y + r_kinv[0, 2]
    Y = r_kinv[1, 0] * x + r_kinv[1, 1] * y + r_kinv[1, 2]
    Z = r_kinv[2, 0] * x + r_kinv[2, 1] * y + r_kinv[2, 2]
    u = math.atan2(X, Y) #極座標u
    w = Y / math.sqrt(X**2 + Y**2 + Z**2)
    v = (math.pi - math.acos(w)) #極座標v
    return [u, v]
```

### カーネル密度分布の描画
カーネル密度分布は、scipyのgaussian_kdeを用いて算出し、画像で可視化するために、0〜255で正規化している。
```
#カーネル密度を生成する関数
#gaze_list_pano：パノラマ上の視線データの極座標のリスト
def Karnel(img, gaze_list_pano):
    img_x = img.shape[1]
    img_y = img.shape[0]
    gaze_list = np.array(gaze_list_pano)#注視点リストをnumpy配列に変換
    value = gaze_list.T #転置してgaussian_kdeに渡せる形に変換
    kernel = gaussian_kde(value, bw_method=0.7) #bw_methodはバンド幅
    xx,yy = np.mgrid[0:img_x:1,0:img_y:1]
    meshdata = np.vstack([xx.ravel(),yy.ravel()])
    z = kernel.evaluate(meshdata)
    data = z.reshape(img_x, img_y).T #カーネル分布(合計=1)
    img_gray = np.uint8((min_max(data))*255) #標準化してグレースケールに変換
    return img_gray
```


