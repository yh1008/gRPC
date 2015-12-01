
#implement the method of Answer && Elaborate`
#make fun of politicians, lol

from random import randint
from grpc.beta import implementations
import re
import debate_pb2
import consultation_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Candidate(debate_pb2.BetaCandidateServicer):

        def Answer(self, request, context): 
                sentence = request.question.split()
                start_word = sentence[0].lower()
                match = re.search(r'what|why|how|who|when',start_word)
                if not match:
                        rand_num = randint (0,1)
                        if rand_num == 0:
                                ran_answer = "your 3 cent titanium tax goes too far"
                        else:
                                ran_answer = "your 3 cent titanium tax doesn't go too far enough"
                                #AnswerReply.answer
                        return debate_pb2.AnswerReply(answer=ran_answer)
                if match:
                        # if question is "what is your opinion on China", I change it to "what is my opinion on China"
                        answer_sub = []
                        for word in sentence:
                                word = word.lower()
                                if word == "you":
                                        word = "I"
                                elif word == "your":
                                        word = "my"
        
                                answer_sub.append(word + " ")
                        answer_string = ''.join(answer_sub)
                        
                        #makes an RPC call to external server CampainManager.Retort with request = "answer_string "
                        channel = implementations.insecure_channel('54.88.18.92', 50051)
                        stub = consultation_pb2.beta_create_CampaignManager_stub(channel)
                        try:
                                RetortReply = stub.Retort(consultation_pb2.RetortRequest(original_question=answer_string), request.timeout+10)
                                answer = 'You asked me ' + answer_string + 'but I want to say that ' + RetortReply.retort
                        #this service will reply something ridiculous, like "I am going to disprove CAP thoerem"
                        except grpc.framework.interfaces.face.face.ExpirationError:

                                answer = 'No comment.'
                        else:
                                answer = 'You asked me ' + answer_string + 'but I want to say that ' + RetortReply.retort

                        return debate_pb2.AnswerReply(answer=answer)
                        
        def Elaborate(self, request, context):
                #if topic = finance, blah_run = 3 2, method Elaborate will return
                # "blah_run blah_rub blah_run finance blah_run blah_run
                answer = []
                topic = request.topic
                num_blah = request.blah_run
                #num_blah is empty list
                if not num_blah:
                        answer_string = topic

                if num_blah:
                        for i in num_blah:
                                string = 'blah '*i + topic
                                for j in range(i):
                                        answer.append('blah ')
                                answer.append(topic)
                                answer.append(" ")
                        length = len(topic)
                        answer_string = ''.join(answer)
                        if len(num_blah) > 1:
                                answer_string= answer_string[:-( length+1)]

                return debate_pb2.ElaborateReply(answer=answer_string)
def serve():
        server = debate_pb2.beta_create_Candidate_server(Candidate())
        server.add_insecure_port('[::]:80000') #bind to any port that is higher than 20000
        server.start()
        try:
                while True:
                        time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
                server.stop()
       except KeyboardInterrupt:
                server.stop()

if __name__ == '__main__':
        serve()
