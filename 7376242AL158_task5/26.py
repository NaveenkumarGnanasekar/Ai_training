class File:
    def __init__(self, name, size):
        self.name = name       
        self.size = size     
class StoragePlan:
    def __init__(self, name, max_storage):
        self.name = name
        self.max_storage = max_storage  
class User:
    def __init__(self, username, plan):
        self.username = username
        self.plan = plan
        self.files = []  

    def get_used_storage(self):
        total = 0
        for file in self.files:
            total += file.size
        return total


    def upload_file(self, file):
        if self.get_used_storage() + file.size <= self.plan.max_storage:
            self.files.append(file)
            print(f"{file.name} uploaded successfully!")
        else:
            print("Storage limit exceeded! Cannot upload file.")

    def show_files(self):
        print(f"\nFiles of {self.username}:")
        for file in self.files:
            print(f"- {file.name} ({file.size} MB)")
        print(f"Used: {self.get_used_storage()} / {self.plan.max_storage} MB\n")
basic_plan = StoragePlan("Basic", 100)  
premium_plan = StoragePlan("Premium", 500) 
user1 = User("Alice", basic_plan)
user2 = User("Bob", premium_plan)
file1 = File("photo.jpg", 40)
file2 = File("video.mp4", 80)
file3 = File("movie.mp4", 300)
user1.upload_file(file1)
user1.upload_file(file2)  
user2.upload_file(file3)
user1.show_files()
user2.show_files()
