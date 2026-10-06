import json

class manner:
    def __init__(self):
        self.user = []
        self.id = 1


    def add(self,name,age):
        user = {"id":self.id,
                "name":name,
                "age":age
                }
        self.user.append(user)
        self.id += 1
        return user

    
    def match(self,id):
        for user in self.user:
            if user["id"] == id:
                return user
            else:
                pass
        return None

    
    def update_age(self, id, age):
        user = self.match(id)

        if user is None:
            return False

        user["age"] = age
        return True

    
    def remove(self, user_id):
        user = self.match(user_id)

        if user is None:
            return False

        self.user.remove(user)
        return True
    def list_users(self):
        return self.user.copy()

    
    def save_to_json(self, filepath):
            with open(filepath, "w", encoding="utf-8") as file:
                    json.dump(self.user, file, ensure_ascii = False)

                    
    def load_from_json(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            self.user = json.load(file)

 