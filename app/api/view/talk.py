from flask import request, jsonify
from flask.views import MethodView
from app.utills.NLP_trained_model import *

class Reply(MethodView):
    def post(self):
        input_sentence = ''
        while (1):
            try:
                # 得到用户终端的输入
                # input_sentence = input('> ')
                input_sentence = request.form.get("msg")
                # 是否退出
                #print(input_sentence)
                if input_sentence == 'q' or input_sentence == 'quit':
                    break
                # 句子归一化
                input_sentence = word_filter(jieba.cut(input_sentence) if word_wise else input_sentence)
                # 生成响应Evaluate sentence
                output_words = evaluate(encoder, decoder, searcher, voc, input_sentence)
                # 去掉EOS后面的内容
                words = []
                for word in output_words:
                    if word == 'EOS':
                        break
                    elif word != 'PAD':
                        words.append(word)
                # print('Bot:', ''.join(words))
                res = ''.join(words)
                # return json.dumps(res, ensure_ascii=False)
                return jsonify({'code': 200, 'reply': res})
            except KeyError:
                # print("Error: Encountered unknown word.")
                res = "我不知道呀，换个话题吧"
                # return json.dumps(res, ensure_ascii=False)
                return jsonify({'code': 201, 'reply': res})
