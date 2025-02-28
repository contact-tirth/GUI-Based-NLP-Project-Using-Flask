import json

class Database:
    def insert(self,name,email,password):
        with open('users.json','r') as f:
            emails = json.load(f)

            if email in emails:
                return 0
            else:
                emails[email]=[name,password]

        with open('users.json','w') as fw:
            json.dump(emails,fw,indent=4)
            return 1

    def search(self,email,password):
        with open('users.json','r') as fr:
            emails_1=json.load(fr)

        if email in emails_1:
            if emails_1[email][1]==password:
                return 1
            else: return 0