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
        self.users.append(user)
        self.next_id += 1
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

        self.users.remove(user)
        return True
    def list_users(self):
        return self.users.copy()
    def save_to_json(self, filepath):
                with open(filepath, "w", encoding="utf-8") as file:
                    json.dump(self.users, file, ensure_ascii = False)
    def load_from_json(self, filepath):
        with open(filepath, "r", encoding="utf-8") as file:
            self.users = json.load(file)

        self.next_id = 1
        for user in self.users:
            if user["id"] >= self.next_id:
                self.next_id = user["id"] + 1