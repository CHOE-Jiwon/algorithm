##############################################
# 작성일: 2022-07-06
# 문제 링크: https://www.acmicpc.net/problem/9093
##############################################

class MyClass():
    
    def reverse_word(self, word):
        return word[::-1]
    
    def reverse_sentence(self, sentence):

        result = list()

        for word in sentence.split():
            result.append(self.reverse_word(word))
        
        return ' '.join(result)

if __name__ == "__main__":

    myClass = MyClass()

    input_cnt = int(input().strip())

    loop_cnt = 0
    result_list = list()

    while loop_cnt < input_cnt:
        input_sentence = input().strip()
        result_list.append(myClass.reverse_sentence(input_sentence))

        loop_cnt += 1
    
    for result in result_list:
        print(result)