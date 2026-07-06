class chatbook():
    
    __user_id = 0
    
    def __init__(self):
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.__name = 'Default User'
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
    
    #static methods 
        
    @staticmethod
    def get_id(self):
        return chatbook.__user_id
    
    @staticmethod
    def set_id(self,value):
        chatbook.__user_id = value
        
    def get_name(self):
        return self.__name
    
    def set_name(self, value):
        self.__name = value
    
    def menu(self):
        user_input = input(""" Welcome to Chatbook!!! How would you like to proceed?
              1. press 1 to signup
              2. press 2 to signin
              3. pres 3 to write a post
              4. press 4 to message a friend
              5. press any other key to exit
              """)
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.write_post()
        elif user_input == '4':
            self.message_friend()
        else:
            print("Exiting...")
            exit()
            
    def signup(self):
        email = input("Enter you email ->")
        pwd   = input("Set up your password ->")
        self.username = email
        self.password = pwd
        print(f"Account created successfully for {self.username}")
        print("\n")
        self.menu()
    
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please signup first to create an account, by pressing 1 in the menu...")
        else:
            email = input("Enter your email ->")
            pwd =  input("Enter your password ->")
            if email == self.username and pwd == self.password:
                print(f"Welcome back {self.username}, you are logged in successfully")
                self.loggedin = True
            else:
                print("Invalid credentials, please try again")
        print("\n")
        self.menu() 
        
    def write_post(self):
        if self.loggedin ==True:
            txt = input("Write your post here ->")
            print(f"Your post is published successfully: {txt}")
        else:
            print("Please login first to write a post...")
        
        print("\n")
        self.menu()     
        
    def message_friend(self):
        if self.loggedin == True:
            txt = input("Write your message here ->")
            frnd = input("Enter your friend's name ->")
            print(f"Your message is sent successfully to {frnd}: {txt}")
        else:
            print("Please login first to message a friend...")
        print("\n")
        self.menu()
    
obj = chatbook()
