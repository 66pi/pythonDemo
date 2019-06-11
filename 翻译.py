#encoding=gbk
import requests
import json
from tkinter import Tk,Button,Entry,Label,Text,END

class YouDaoFanyi(object):
    def __init__(self):
        pass
    def crawl(self,word):
        url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        #ʹ��post��Ҫһ������
        data={'i': word,
              'from': 'AUTO',
              'to': 'AUTO',
              'smartresult': 'dict',
              'client': 'fanyideskweb',
              'doctype': 'json',
              'version': '2.1',
              'keyfrom': 'fanyi.web',
              'action': 'FY_BY_REALTIME',
              'typoResult': 'false'}
        #����Ҫpost�����ݣ����ֵ����ʽ��¼��data�ڡ�
        r = requests.post(url, data)
        #post��Ҫ��������������һ���Ǹղŵ����ӣ�һ����data�����ص���һ��Response����
        answer=json.loads(r.text)
        #������Լ�����printһ��r.text�����ݣ�Ȼ�����Ķ�����Ĵ��롣
        result = answer['translateResult'][0][0]['tgt']
        return result



class Application(object):
    def __init__(self):
        self.window = Tk()
        self.fanyi = YouDaoFanyi()


        self.window.title(u'�ҵķ���')
        #���ô��ڴ�С��λ��
        self.window.geometry('310x370+500+300')
        self.window.minsize(310,370)
        self.window.maxsize(310,370)
        #����һ���ı���
        #self.entry = Entry(self.window)
        #self.entry.place(x=10,y=10,width=200,height=25)
        #self.entry.bind("<Key-Return>",self.submit1)
        self.result_text1 = Text(self.window,background = 'azure')
        # ϲ��ʲô����ɫ������������Ŷ��������ɫ��ö����ԣ�http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
        self.result_text1.place(x = 10,y = 5,width = 285,height = 155)
        self.result_text1.bind("<Key-Return>",self.submit1)

        #����һ����ť
        #Ϊ��ť����¼�
        self.submit_btn = Button(self.window,text=u'����',command=self.submit)
        self.submit_btn.place(x=205,y=165,width=35,height=25)
        self.submit_btn2 = Button(self.window,text=u'���',command = self.clean)
        self.submit_btn2.place(x=250,y=165,width=35,height=25)

        #����������
        self.title_label = Label(self.window,text=u'������:')
        self.title_label.place(x=10,y=165)
        #������

        self.result_text = Text(self.window,background = 'light cyan')
        self.result_text.place(x = 10,y = 190,width = 285,height = 165)
        #�س�����
    def submit1(self,event):
        #��������ȡ�û������ֵ
        content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
        #�����ֵ���͸����������з���

        result = self.fanyi.crawl(content)
        #�������ʾ�ڴ����е��ı�����

        self.result_text.delete(0.0,END)
        self.result_text.insert(END,result)

        #print(content)

    def submit(self):
        #��������ȡ�û������ֵ
        content = self.result_text1.get(0.0,END).strip().replace("\n"," ")
        #�����ֵ���͸����������з���

        result = self.fanyi.crawl(content)
        #�������ʾ�ڴ����е��ı�����

        self.result_text.delete(0.0,END)
        self.result_text.insert(END,result)
        print(content)
    #����ı����е�����
    def clean(self):
        self.result_text1.delete(0.0,END)
        self.result_text.delete(0.0,END)

    def run(self):
        self.window.mainloop()


if __name__=="__main__":
    app = Application()
    app.run()