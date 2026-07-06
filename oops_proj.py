class chatbook():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
    
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
        
obj = chatbook()
