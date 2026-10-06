import json

class manner:
    def __init__(self):  #初始信息
        self.user = []
        self.id = 1


    def add(self,name,age):
        user = {"id":self.id,
                "name":name,        #添加名字年龄即可添加个人，id顺延
                "age":age
                }
        self.user.append(user)
        self.id += 1
        return user

    
    def match(self,id):
        for user in self.user:        #查询
            if user["id"] == id:
                return user
            else:
                pass
        return None    #没有返回

    
    def update_age(self, id, age):
        user = self.match(id)

        if user is None:
            return False
        else:
            user["age"] = age     #修改
        return True

    
    def remove(self, user_id):
        user = self.match(user_id)       

        if user is None:
            return False
        else:
            self.user.remove(user)     #删除
        return True
    def list_users(self):           #列出
        return self.user.copy()

    
    def save_to_json(self, filepath):
            with open(filepath, "w", encoding="utf-8") as file:         #打开并保存为json文件
                    json.dump(self.user, file, ensure_ascii = False)

                    
    def load_from_json(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:   
            self.user = json.load(file)            #读取并覆盖

 