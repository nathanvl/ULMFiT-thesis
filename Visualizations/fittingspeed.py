import matplotlib.pyplot as plt

x1 = [i for i in range(1,21)]
x2 = [i for i in range(1,18)]

y1 = [0.315829
,0.326209
,0.335176
,0.342129
,0.347226
,0.352164
,0.356172
,0.36008
,0.363502
,0.366489
,0.370597
,0.374582
,0.378152
,0.382012
,0.385994
,0.388984
,0.391583
,0.393331
,0.394229
,0.394359]

y2 = [0.384827
,0.399044
,0.40215
,0.397402
,0.398084
,0.396688
,0.398618
,0.398037
,0.400091
,0.402013
,0.403987
,0.406205
,0.40945
,0.412725
,0.41503
,0.418768
,0.42177]


plt.plot(x1,y1,label='English LM fine-tuning on IMDb')
plt.plot(x2,y2,label='Dutch LM fine-tuning on 110kDBRD')

plt.xlabel(r'Epoch')
plt.ylabel(r'Accuracy')
plt.xticks(range(1,21))
plt.legend()
plt.show()
