import json


class Scores():

    def most_tests(self):
        most = 0
        name = ""
        with open('data.json',encoding='UTF-8') as json_file:
            data = json.load(json_file)
            for school in data['data']:
                if school[10].isnumeric():
                    if(int(school[10])>most):
                        most = int(school[10])
                        name = school[9]
        return name,most
    def best_score(self):
        max = 0
        name = ""
        with open('data.json',encoding='UTF-8') as json_file:
            data = json.load(json_file)
            for school in data['data']:
                if(school[11].isnumeric() and school[12].isnumeric() and school[13].isnumeric()):
                    score = int(school[11]) + int(school[12]) + int(school[13])
                    if(score>max):
                        max = score
                        name = school[9]
        return name,max

    def best_score_small(self):
        max = 0
        name = ""
        with open('data.json',encoding='UTF-8') as json_file:
            data = json.load(json_file)
            for school in data['data']:
                if(school[11].isnumeric() and school[12].isnumeric() and school[13].isnumeric() and school[10].isnumeric()):
                    score = int(school[11]) + int(school[12]) + int(school[13])
                    if(score>max and int(school[10])<=50):
                        max = score
                        name = school[9]
        return name,max

    def x_most_tests(self, x):
        arr = []
        with open('data.json',encoding='UTF-8') as json_file:
            data = json.load(json_file)
            for a in range(x):
                high = 0
                name = ""
                for school in data['data']:
                    if(school[10].isnumeric()):
                        if( not((school[9],int(school[10])) in arr) and int(school[10])>high):
                            high = int(school[10])
                            name = school[9]
                arr.append((name,high))
        return arr


    def x_highest_scores(self, x):
        arr = []
        with open('data.json',encoding='UTF-8') as json_file:
            data = json.load(json_file)
            for a in range(x):
                high = 0
                name = ""
                for school in data['data']:
                    if(school[11].isnumeric() and school[12].isnumeric() and school[13].isnumeric()):
                        score = int(school[11]) + int(school[12]) + int(school[13])
                        if( not((school[9],score) in arr) and score>high):
                            high = score
                            name = school[9]
                arr.append((name,high))
        return arr
