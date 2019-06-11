#encoding=gbk
import requests, json

url = 'http://ictclas.nlpir.org/nlpir/index6/getWord2Vec.do'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
word = input('请输入词汇：')
params = {
	'content': word
}
res = requests.post(url=url, params=params, headers=headers)
data_word = res.text
dic_word = json.loads(data_word)
print('跟' + word + '相关的还有：')
f=0
for i in dic_word['w2vlist']:
    f += 1
    words = i.split(',')
    print('(' + str(f) + ')' + words[0] + '，其相关度为' + words[1])  # 打印数据






