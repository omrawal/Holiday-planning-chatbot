# Author Om Rawal
# 01/04/2021 09:22


class Chatbot(object):
    def __init__(self):
        self.flow = None
        self.isInitial = True
        self.source1 = None
        self.dest1 = None
        self.date1 = None
        self.dest2 = None
        self.date2 = None
        self.duration2 = None
        self.source3 = None
        self.dest3 = None
        self.date3 = None
        self.duration3 = None

    def set_flow(self, query):
        query = query.lower()

        if('book' in query):

            if('flight' in query):
                self.flow = 1

            elif('hotel' in query):
                self.flow = 2

            elif('cab' in query):
                self.flow = 3

    def query(self, user_query):
        if(self.isInitial):

            self.set_flow(user_query)
            self.isInitial = False
            return 'Which city are you going to?'

        else:

            if(self.flow == 1):  # for flight

                if(self.dest1 == None):
                    self.dest1 = user_query
                    return "Which city are you leaving from?"

                elif(self.source1 == None):
                    self.source1 = user_query
                    return "What is the travel date?"

                elif(self.date1 == None):
                    self.date1 = user_query
                    return "Thanks. Your Flight details will be shared soon!"

            elif(self.flow == 2):  # for hotel

                if(self.dest2 == None):
                    self.dest2 = user_query
                    return "What is the travel date?"

                elif(self.date2 == None):
                    self.date2 = user_query
                    return "What is the travel duration?"

                elif(self.duration2 == None):
                    self.duration2 = user_query
                    return "Thanks. Your Hotel details will be shared soon!"

            elif(self.flow == 3):  # for cab
                if(self.dest3 == None):
                    self.dest3 = user_query
                    return "Which city are you leaving from?"

                elif(self.source3 == None):
                    self.source3 = user_query
                    return "What is the travel date?"

                elif(self.date3 == None):
                    self.date3 = user_query
                    return "What is the travel duration?"

                elif(self.duration3 == None):
                    self.duration3 = user_query
                    return "Thanks. Your Cab details will be shared soon!"
                pass
