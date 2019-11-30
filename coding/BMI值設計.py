# BMI
print('BMI值計算：【 體重(kg) / 身高(m)的平方 】') #title
print('＊＊＊請注意！體重請填公斤(kg)＊＊＊') #subtitle weight

weight = input('請填體重(kg)： ') #輸入體重
weight = float(weight)

print('＊＊＊請注意！身高請填公分(cm)＊＊＊') #subtitle height

height = input('請填身高(cm)： ') #輸入身高
height = float(height)
h = height ** 2 / 100 ** 2

BMI = float #BMI值
BMI = weight / h
print('您的BMI為：【', BMI, '】')

if BMI < 18.5: #代入BMI值判斷體重過輕或過重
	print('您的體重"過輕"囉！')
elif BMI >= 35:
	print('"重度"肥胖！請及早諮詢醫生：控八控控⋯⋯⋯⋯')
elif BMI >=24 or BMI <27:
	print('"過重"囉！請多攝取蔬果以策健康。')
elif BMI >=27 or BMI <30:
	print('"輕度"肥胖！請注意您的心血管以及肝腎問題。')
elif BMI >=30 or BMI <35:
	print('"中度"肥胖！您已入三十大關，請放下邪惡的食物展望健康的未來。')

print('＊＊＊請注意腰圍：男性小於90cm ; 女性小於80cm 才等於"正常"喔！＊＊＊')