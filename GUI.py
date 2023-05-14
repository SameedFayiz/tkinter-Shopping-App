from abc import abstractmethod, ABC
from time import time, ctime
from os import getcwd
from tkinter import *
from tkinter.font import Font

path = getcwd() + '/accounts/'
admin_approves = False
user_approves = False


class User(ABC):
    '''An abstract Class designed for user info'''
    login_details = {}

    def __init__(self, file_name):
        self.file_name = file_name
        # opening the file with all the login credentials
        with open(file_name) as f:
            self.login_info = f.read().split(',')
        # updating the dictionary with the credentials of the user(username and password)
        for i in range(2, len(self.login_info), 2):
            User.login_details.update({self.login_info[i]: self.login_info[i + 1]})

    @staticmethod
    def SignUp(self, file_name1, file_name2, user_name):
        '''a static method for signing up'''
        User.__init__(self, file_name1)
        # invoked when the username is not found in the dictionary created above
        if user_name not in User.login_details:
            # setting a gui design for collecting password
            password = Entry(user_frame1, width=50, font=font1, bd=5)
            password.insert(0, 'Enter your password')
            password.grid(row=1, column=1)
            # setting a gui design for collecting email
            email = Entry(user_frame1, width=50, font=font1, bd=5)
            email.insert(0, 'Enter your Email address')
            email.grid(row=2, column=1)
            # setting a gui design for collecting credit card info
            credit_card_info = Entry(user_frame1, width=50, font=font1, bd=5)
            credit_card_info.insert(0, 'Enter your credit card info')
            credit_card_info.grid(row=3, column=1)
            # setting a gui design for collecting the user's shipping address
            shipping_address = Entry(user_frame1, width=50, font=font1, bd=5)
            shipping_address.insert(0, 'Enter your Shipping address')
            shipping_address.grid(row=4, column=1)

            def button2():
                '''button concerned with registering the signup data'''
                proceed.destroy()
                with open(self.file_name, 'a') as f:
                    f.write((',' + user_name + ',' + password.get()))
                    # registering user's password in a file
                with open(file_name2, 'a') as f:
                    f.write(
                        ',' + user_name + ',' + email.get() + ',' + credit_card_info.get() +
                        ',' + shipping_address.get())
                    # registering all of the user's info barring the password in a file
                msg2 = Tk()
                # creating a gui object
                msg2.title('Message!')
                Label(msg2, text='Your account has been created please proceed to the login step.', font=font1,
                      width=50, bd=10, bg='white', relief=RIDGE).pack(pady=2)
                # message after the signup info has been registered
                Button(msg2, text='OK', font=font1, bd=10, command=msg2.destroy).pack()
                # the button which destroys the label
                user_frame1.destroy()
                main_screen()
                msg2.mainloop()

            proceed = Button(user_frame1, text='Proceed', font=font1, width=50, height=2, command=button2)
            # the button which executes the button2 function
            proceed.grid(row=5, column=1)

        else:
            msg1 = Label(user_frame1, text='This Username is already taken, Please try another one.', font=font1)
            # handling a redundancy
            msg1.grid(row=8, column=1)

    @abstractmethod
    def Login(self, var):
        # creating an abstract login method for use later
        pass


class Admin(User):
    '''Class for the Admin panel, inherits from the User class'''

    def __init__(self, file_name, product):
        User.__init__(self, file_name)
        self.id = None
        _ = getcwd() + '/products/'
        # getting the current working directory and creating a products extension
        self.inst_product = product(_ + 'fruits.csv', _ + 'vegetable.csv', _ + 'fish.csv',
                                    _ + 'beverages.csv', _ + 'meat.csv')
        # composition being applied here

    def Login(self, var):
        ''' overriding the login function of the abstract class'''
        self.id = var
        if self.id in self.login_details:
            id_check.destroy()
            password = Entry(admin_frame1, width=50, font=font1, bd=5)
            password.insert(0, 'Enter Admin Password')
            password.grid(row=2, column=1, columnspan=3)

            # collecting password for admin when the file exists in login details

            def button4():
                '''button for proceeding to the admins section'''
                pswd = password.get()
                # the code to be executed if the id exists
                if pswd == User.login_details.get(self.id):
                    global admin_approves
                    admin_approves = True
                    ad_approved()
                # the code to be executed otherwise
                else:
                    # message being displayed if the password isn't found in the pre-existing records
                    msg2 = Label(admin_frame1, text='Password is incorrect.', font=font1)
                    msg2.grid(row=5, column=1)

            # gui code for proceeding to the next step
            proceed = Button(admin_frame1, text='Proceed', font=font1, width=50, height=2, pady=2, command=button4)
            proceed.grid(row=3, column=1)
        # code to be executed if the id entered is incorrect
        else:
            msg1 = Label(admin_frame1, text='Please enter correct Administrator ID.', font=font1)
            msg1.grid(row=4, column=1)

    def ManageProducts(self):
        '''method for instantiating multiple buttons to deal with the products'''
        self.inst_product.CategoryChooser()
        global manager

        def manager():
            '''method for the admin'''
            admin_frame3 = Frame(root, bg='light pink', padx=150, pady=150, relief=RAISED)
            admin_frame3.pack()
            # code for displaying products
            b1 = Button(admin_frame3, text='Display Products', font=font1, width=50, height=2,
                        pady=2, command=lambda: [admin_frame3.destroy(), self.inst_product.DisplayProductDetails()])
            b1.grid(row=0, column=0)
            # code for adding products
            b2 = Button(admin_frame3, text='Add Products', font=font1, width=50, height=2,
                        pady=2, command=lambda: [admin_frame3.destroy(), self.inst_product.AddProducts()])
            b2.grid(row=1, column=0)
            # code for deleting products
            b3 = Button(admin_frame3, text='Remove Products', font=font1, width=50, height=2,
                        pady=2, command=lambda: [admin_frame3.destroy(), self.inst_product.RemoveProduct()])
            b3.grid(row=2, column=0)
            # code for going back
            b4 = Button(admin_frame3, text='Back', font=font1, width=50,
                        height=2, pady=2, command=lambda: [admin_frame3.destroy(), admin_panel(obj_1)])
            b4.grid(row=3, column=0)

    def ChangeAccountPass(self):
        '''Method which contains the code which allows you to change your password'''
        admin_frame2.destroy()
        admin_frame4 = Frame(root, bg='bisque2', padx=150, pady=150, relief=RAISED)
        admin_frame4.pack()
        # for entering old password
        old_password = Entry(admin_frame4, width=50, font=font1, bd=5)
        old_password.insert(0, 'Enter Old Password')
        old_password.grid(row=0, column=0, columnspan=3)
        # for entering new password
        new_password = Entry(admin_frame4, width=50, font=font1, bd=5)
        new_password.insert(0, 'Enter New Password')
        new_password.grid(row=1, column=0, columnspan=3)

        def button5():
            '''method which lets the password info to get restored'''
            # code for checking if the user entered a correct old password
            if old_password.get() == User.login_details.get(self.id):
                # code which checks the password
                User.login_details[self.id] = new_password.get()
                with open(self.file_name, 'w') as f:
                    f.write('base,base')
                    for i in User.login_details:
                        f.write(',' + i + ',' + User.login_details.get(i))
                admin_frame4.destroy()
                admin_panel(obj_1)
            # code to be executed otherwise
            else:
                Label(admin_frame4, text='Old Password is incorrect.', font=font1).grid(row=4, column=1)

        # gui button which executes the button5 method
        proceed = Button(admin_frame4, text='Proceed', font=font1, width=50, height=2, pady=2, command=button5)
        proceed.grid(row=2, column=1)
        back = Button(admin_frame4, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [admin_frame4.destroy(), admin_panel(obj_1)])
        back.grid(row=3, column=1)


class Products:
    '''class which contains most of the code linked to the products panel'''

    def __init__(self, *args):
        self.category = None
        self.file_data = {}
        self.file = getcwd() + '/products/'
        self.base = None
        for i in args:
            with open(i) as f:
                prd_info = f.read().split(',')
            self.prd_stock = {}
            self.prd_prices = {}
            if len(prd_info) > 4:
                for j in range(4, len(prd_info), 4):
                    self.prd_stock.update({prd_info[j]: int(prd_info[j + 1])})
                for j in range(4, len(prd_info), 4):
                    self.prd_prices.update({prd_info[j]: [int(prd_info[j + 2]), prd_info[j + 3]]})
            self.file_data.update({prd_info[0]: [self.prd_stock, self.prd_prices]})

    def CategoryChooser(self, local_='admin'):
        ''' code for choosing a products category'''
        if local_ == 'admin':
            admin_frame2.destroy()
        product_frame = Frame(root, bg='navajo white', padx=150, pady=150, relief=RAISED)
        Label(product_frame, text='Select one Category', font=font1, width=50,
              bd=5, bg='white', relief=RIDGE).grid(row=0, column=0, columnspan=2)
        self.file = getcwd() + '/products/'

        def fruits():
            # creating a file for fruits info
            self.base = 'Fruits'
            self.category = self.file_data.get(self.base)
            self.file += 'fruits.csv'
            func()

        def veg():
            # creating a file for vegetables info
            self.base = 'Vegetable'
            self.category = self.file_data.get(self.base)
            self.file += 'vegetable.csv'
            func()

        def fish():
            # creating a file for fish info
            self.base = 'Fish'
            self.category = self.file_data.get(self.base)
            self.file += 'fish.csv'
            func()

        def meat():
            # creating a file for meats info
            self.base = 'Beef/Mutton/Chicken'
            self.category = self.file_data.get(self.base)
            self.file += 'meat.csv'
            func()

        def drink():
            # creating a file for beverages info
            self.base = 'Beverages'
            self.category = self.file_data.get(self.base)
            self.file += 'beverages.csv'
            func()

        def back():
            # method with actions to be executed when the user has to go back
            product_frame.destroy()
            # the product frame will be destroyed
            if local_ == 'admin':
                admin_panel(obj_1)
            elif local_ == 'cart':
                user_panel()

        def func():
            self.prd_stock = self.category[0]
            self.prd_prices = self.category[1]
            product_frame.destroy()
            if local_ == 'admin':
                manager()
            elif local_ == 'cart':
                market()

        # instantiating buttons which lead to all these product info sections
        b1 = Button(product_frame, text='Fruits', font=font1, width=25, height=2, pady=2, command=fruits)
        b1.grid(row=1, column=0)
        b2 = Button(product_frame, text='Vegetables', font=font1, width=25, height=2, pady=2, command=veg)
        b2.grid(row=1, column=1)
        b3 = Button(product_frame, text='Fish', font=font1, width=25, height=2, pady=2, command=fish)
        b3.grid(row=2, column=0)
        b4 = Button(product_frame, text='Meat', font=font1, width=25, height=2, pady=2, command=meat)
        b4.grid(row=2, column=1)
        b5 = Button(product_frame, text='Beverages', font=font1, width=25, height=2, pady=2, command=drink)
        b5.grid(row=3, column=0, columnspan=2)
        b6 = Button(product_frame, text='Back', font=font1, width=50, height=2, pady=2, command=back)
        b6.grid(row=4, column=0, columnspan=2)
        product_frame.pack()

    def DisplayProductDetails(self, local_='admin'):
        '''method for displaying the product infos'''
        prod_list = list(self.prd_stock.keys())
        # if the accessor is an admin
        if local_ == 'admin':
            prod_frame1 = Frame(root, bg='cornsilk1', relief=RAISED)
            # setting the appropriate labels
            Label(prod_frame1, text='Products:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=0, column=0, padx=10, pady=10)
            Label(prod_frame1, text='Items in stock:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=0, column=1, padx=10, pady=10)
            Label(prod_frame1, text='Price:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=0, column=2, padx=10, pady=10)
            # looping through all the products
            for i in range(0, len(prod_list)):
                # setting all the relevant labels, like name, price etc
                Label(prod_frame1, text=prod_list[i], font=font1, width=25, bd=5,
                      bg='white', relief=RIDGE).grid(row=i + 1, column=0)
                Label(prod_frame1,
                      text=str(self.prd_stock.get(prod_list[i])) + self.prd_prices.get(prod_list[i])[1][3:],
                      font=font1, width=25, bd=5, bg='white', relief=RIDGE).grid(row=i + 1, column=1)
                Label(prod_frame1,
                      text=str(self.prd_prices.get(prod_list[i])[0]) + self.prd_prices.get(prod_list[i])[1],
                      font=font1, width=25, bd=5, bg='white', relief=RIDGE).grid(row=i + 1, column=2)
            # creating a button for going back
            back = Button(prod_frame1, text='Back', font=font1, width=50, height=2,
                          pady=2, command=lambda: [prod_frame1.destroy(), manager()])
            back.grid(column=0, columnspan=3, padx=10, pady=10)
            prod_frame1.pack()
        # if the accessor is cart
        elif local_ == 'cart':
            # setting all the appropriate labels
            Label(cart_frame, text='Products:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=0, column=0, padx=10, pady=10)
            Label(cart_frame, text='Items in stock:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=0, column=1, padx=10, pady=10)
            Label(cart_frame, text='Price:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=0, column=2, padx=10, pady=10)
            # looping through the products
            for i in range(0, len(prod_list)):
                # setting the labels for all items in the cart
                Label(cart_frame, text=prod_list[i], font=font1, width=25, bd=5,
                      bg='white', relief=RIDGE).grid(row=i + 1, column=0)
                Label(cart_frame,
                      text=str(self.prd_stock.get(prod_list[i])) + self.prd_prices.get(prod_list[i])[1][3:],
                      font=font1, width=25, bd=5, bg='white', relief=RIDGE).grid(row=i + 1, column=1)
                Label(cart_frame,
                      text=str(self.prd_prices.get(prod_list[i])[0]) + self.prd_prices.get(prod_list[i])[1],
                      font=font1, width=25, bd=5, bg='white', relief=RIDGE).grid(row=i + 1, column=2)

            def add_to_cart(j):
                '''button which will add the product to cart'''
                buttons[j]['state'] = DISABLED
                adder(prod_list[j])

            buttons = []
            for i in range(0, len(prod_list)):
                # looping through the products
                z = Button(cart_frame, text='Add to Cart', font=font1, width=10, height=1,
                           command=lambda j=i: add_to_cart(j))
                z.grid(row=i + 1, column=3, pady=2)
                buttons.append(z)
            global cart
            # button for destroying cart and loads cart view
            cart = Button(cart_frame, text='View Cart', font=font1, width=10, height=1,
                          command=lambda: [cart_frame.destroy(), cart_view()])
            cart.grid(row=0, column=3)
            # button which destroys cart frame and executes BrowseMarket
            back = Button(cart_frame, text='Back', font=font1, width=50, height=2,
                          pady=2, command=lambda: [cart_frame.destroy(), obj_3.BrowseMarket()])
            back.grid(column=0, columnspan=3, padx=10, pady=10)

    def AddProducts(self):
        '''Method for adding products by admin'''
        prod_frame2 = Frame(root, bg='cornsilk1', padx=150, pady=150, relief=RAISED)
        prod_frame2.pack()
        product = Entry(prod_frame2, width=50, font=font1, bd=5)
        product.insert(0, 'Enter product name')
        product.grid(row=0, column=0, columnspan=3)
        stock = Entry(prod_frame2, width=50, font=font1, bd=5)
        stock.insert(0, 'Enter items in stock(only digits)')
        stock.grid(row=1, column=1)
        price = Entry(prod_frame2, width=50, font=font1, bd=5)
        price.insert(0, 'Enter Price(only digits)')
        price.grid(row=2, column=1)
        rate_convention = Entry(prod_frame2, width=50, font=font1, bd=5)
        rate_convention.insert(0, 'Enter Rate convention(E.g: per kg or per any amount of item)')
        rate_convention.grid(row=3, column=1)

        def button6():
            '''function to be executed when button6 is pressed'''
            # exception handler for non integer values
            try:
                if stock.get().isdigit() and price.get().isdigit():
                    pass
                else:
                    raise ValueError('ValueError...\nINVALID INPUT FOR INTEGER')
            except ValueError as ve:
                print(ve)
                new = Tk()
                new.title('Message!')
                Label(new, text='INVALID INPUT FOR STOCK OR PRICE. Value cannot be other than integer', font=font1,
                      width=60, bd=5, bg='white', relief=RIDGE).pack(pady=2)
                prod_frame2.destroy()
                manager()
                new.mainloop()
            # code for handling product placement
            self.prd_stock.update({product.get(): stock.get()})
            self.prd_prices.update({product.get(): [price.get(), rate_convention.get()]})
            with open(self.file, 'w') as f:
                prd_str = self.base + ',base,base,base'
                for i in self.prd_stock:
                    _1 = str(self.prd_stock.get(i))
                    _2 = str(self.prd_prices.get(i)[0])
                    _3 = self.prd_prices.get(i)[1]
                    prd_str += (',' + i + ',' + _1 + ',' + _2 + ',' + _3)
                f.write(prd_str)
            Label(prod_frame2, text='The product ' + product.get() + ' has been added',
                  font=font1).grid(row=6, column=1)
            proceed['state'] = DISABLED

        # gui code for executing button6
        proceed = Button(prod_frame2, text='Proceed', font=font1, width=50, height=2, pady=2, command=button6)
        proceed.grid(row=4, column=1)
        back = Button(prod_frame2, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [prod_frame2.destroy(), manager()])
        back.grid(row=5, column=1)

    def RemoveProduct(self):
        '''method for removing products'''
        prod_frame3 = Frame(root, bg='cornsilk1', padx=150, pady=150, relief=RAISED)
        prod_frame3.pack()
        product = Entry(prod_frame3, width=50, font=font1, bd=5)
        product.insert(0, 'Enter the product name you want to remove')
        product.grid(row=0, column=0, columnspan=3)

        def button7():
            '''code for product placement after removal'''
            if product.get() in self.prd_stock:
                self.prd_stock.pop(product.get())
                self.prd_prices.pop(product.get())
                with open(self.file, 'w') as f:
                    product_str = self.base + ',base,base,base'
                    for i in self.prd_stock:
                        _1 = str(self.prd_stock.get(i))
                        _2 = str(self.prd_prices.get(i)[0])
                        _3 = self.prd_prices.get(i)[1]
                        product_str += (',' + i + ',' + _1 + ',' + _2 + ',' + _3)
                    f.write(product_str)
                t = 'The product ' + product.get() + ' has been removed from the list.'
                Label(prod_frame3, text=t, font=font1).grid(row=3, column=1)
                proceed['state'] = DISABLED
            else:
                # when product isn't present in previous records
                Label(prod_frame3, text='The product name you have entered is not the list.',
                      font=font1).grid(row=3, column=1)

        # gui button which executes button7
        proceed = Button(prod_frame3, text='Proceed', font=font1, width=50, height=2, pady=2, command=button7)
        proceed.grid(row=1, column=1)
        back = Button(prod_frame3, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [prod_frame3.destroy(), manager()])
        back.grid(row=2, column=1)


class Customer(User):
    '''Customer class which inherits from the abstract class User'''
    User_name = None

    def __init__(self, file_name1, file_name2):
        User.__init__(self, file_name1)
        self.user_name = None
        self.password = None
        with open(file_name2) as f:
            self.acc_info = f.read().split(',')
            self.acc_details = {}
        for i in range(4, len(self.acc_info), 4):
            self.acc_details.update(
                {self.acc_info[i]: [self.acc_info[i + 1], self.acc_info[i + 2], self.acc_info[i + 3]]})

    def __str__(self):
        return 'Welcome ' + self.user_name
        # Label(root, text='Welcome '+self.user_name, font=font1, relief=GROOVE).pack()

    def Login(self, var):
        '''The overrided login method'''
        self.user_name = var
        # username validation
        if self.user_name in User.login_details:
            id_check.destroy()
            password = Entry(signin_frame, width=50, font=font1, bd=5)
            password.insert(0, 'Enter your Password')
            password.grid(row=1, column=1)
            Customer.User_name = self.user_name

            def button9():
                '''code to be executed if button9 is pressed'''
                # password validation
                self.password = password.get()
                if self.password == User.login_details.get(self.user_name):
                    global user_approves
                    user_approves = True
                    approved()
                else:
                    Label(signin_frame, text='Password is incorrect.', width=30,
                          font=font1).grid(row=3, column=1)

            # code for executing button9
            proceed = Button(signin_frame, text='Proceed', font=font1, width=50, height=2, pady=2, command=button9)
            proceed.grid(row=2, column=1)
        else:
            Label(signin_frame, text='There is no account with this username.', width=30,
                  font=font1).grid(row=3, column=1)

    def AccountInfo(self):
        '''method for displaying account info'''
        cust_frame.destroy()
        cust_frame1 = Frame(root, bg='peach puff', padx=150, pady=150, relief=RAISED)
        cust_frame1.pack()
        _1 = self.acc_details.get(self.user_name)[0]
        _2 = self.acc_details.get(self.user_name)[1]
        _3 = self.acc_details.get(self.user_name)[2]
        a_ = Label(cust_frame1, text='ACCOUNT INFORMATION', font=font1, width=50, bd=20, relief=SUNKEN,
                   bg='white')
        a_.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        b_ = Label(cust_frame1, text='Username: ' + self.user_name, font=font1, width=40, bd=10, relief=GROOVE,
                   bg='white')
        b_.grid(row=1, column=2, padx=10, pady=10)
        c_ = Label(cust_frame1, text='Password: ' + len(self.password) * '*', font=font1, width=40, bd=10,
                   relief=GROOVE, bg='white')
        c_.grid(row=2, column=2, padx=10, pady=10)
        d_ = Label(cust_frame1, text='Email Address: ' + _1, font=font1, width=40, bd=10, relief=GROOVE,
                   bg='white')
        d_.grid(row=3, column=2, padx=10, pady=10)
        e_ = Label(cust_frame1, text='Credit Card info: ' + _2, font=font1, width=40, bd=10, relief=GROOVE,
                   bg='white')
        e_.grid(row=4, column=2, padx=10, pady=10)
        f_ = Label(cust_frame1, text='Shipping Address: ' + _3, font=font1, width=40, bd=10, relief=GROOVE,
                   bg='white')
        f_.grid(row=5, column=2, padx=10, pady=10)
        back = Button(cust_frame1, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [cust_frame1.destroy(), user_panel()])
        back.grid(row=6, column=0, columnspan=5, pady=5)

        def reset():
            # method for resetting the frame
            cust_frame1.destroy()
            obj_2.AccountInfo()

        def saver():
            '''method for saving login details'''
            with open(getcwd() + '/accounts/login_details.csv', 'w') as f:
                whole_string = 'base,base'
                for i in User.login_details.keys():
                    whole_string += ',' + i + ',' + User.login_details.get(i)
                f.write(whole_string)
            with open(getcwd() + '/accounts/account_details.csv', 'w') as f:
                whole_string = 'base,base,base,base'
                for i in self.acc_details.keys():
                    whole_string += ',' + i
                    for j in self.acc_details.get(i):
                        whole_string += ',' + j
                f.write(whole_string)

        def name_change():
            '''method for changing name'''
            b_.destroy()
            new_username = Entry(cust_frame1, width=40, font=font1, bd=5)
            new_username.insert(0, 'Enter new username')
            new_username.grid(row=1, column=2)

            def button10():
                '''method to be executed once button10 is pressed'''
                if new_username.get() not in User.login_details.keys():
                    User.login_details[new_username.get()] = User.login_details[self.user_name]
                    self.acc_details[new_username.get()] = self.acc_details[self.user_name]
                    User.login_details.pop(self.user_name)
                    self.acc_details.pop(self.user_name)
                    self.user_name = new_username.get()
                    reset()
                    saver()
                else:
                    Label(cust_frame1, text='This Username is already taken, Please try another one.', font=font1,
                          width=50, bd=20, relief=SUNKEN, bg='white').grid(row=7, column=0, columnspan=5)

            # gui button display which executes button10
            done = Button(cust_frame1, text='Done', font=font1, width=5, height=1,
                          pady=2, command=button10)
            done.grid(row=1, column=3)
            nope = Button(cust_frame1, text='Cancel', font=font1, width=5, height=1,
                          pady=2, command=reset)
            nope.grid(row=1, column=5)

        def pass_change():
            '''method for password change'''
            new = Tk()
            new.minsize(width=500, height=250)
            new.maxsize(width=500, height=250)
            new.title('PASSWORD CHANGER')
            old_password = Entry(new, width=40, font=font1, bd=5)
            old_password.insert(0, 'Enter old password')
            old_password.grid(row=0, column=0, padx=5, pady=5)
            new_password = Entry(new, width=40, font=font1, bd=5)
            new_password.insert(0, 'Enter new password')
            new_password.grid(row=2, column=0, padx=5, pady=5)

            def button11():
                '''method to be executed once button11 is pressed'''
                if old_password.get() == User.login_details.get(self.user_name):
                    User.login_details[self.user_name] = new_password.get()
                    saver()
                    new.destroy()
                else:
                    Label(new, text='Old Password is incorrect', font=font1,
                          width=30, bd=5, relief=GROOVE, bg='white').grid(row=5, column=0, padx=5, pady=5)

            # button11 gui code
            proceed = Button(new, text='Done', font=font1, width=10, height=1,
                             pady=2, command=button11)
            proceed.grid(row=3, column=0, padx=5, pady=5)
            nope = Button(new, text='Cancel', font=font1, width=10, height=1,
                          pady=2, command=lambda: [reset(), new.destroy()])
            nope.grid(row=4, column=0, padx=5, pady=5)
            new.mainloop()

        def change_1():
            '''method for changing email address'''
            d_.destroy()
            new_email = Entry(cust_frame1, width=40, font=font1, bd=5)
            new_email.insert(0, 'Enter new email address')
            new_email.grid(row=3, column=2)

            def button12():
                self.acc_details[self.user_name][0] = new_email.get()
                saver()
                reset()

            done = Button(cust_frame1, text='Done', font=font1, width=5, height=1,
                          pady=2, command=button12)
            done.grid(row=3, column=3)
            nope = Button(cust_frame1, text='Cancel', font=font1, width=5, height=1,
                          pady=2, command=reset)
            nope.grid(row=3, column=5)

        def change_2():
            '''method for changing credit card info'''
            e_.destroy()
            credit_card = Entry(cust_frame1, width=40, font=font1, bd=5)
            credit_card.insert(0, 'Enter new credit card information')
            credit_card.grid(row=4, column=2)

            def button13():
                self.acc_details[self.user_name][1] = credit_card.get()
                saver()
                reset()

            done = Button(cust_frame1, text='Done', font=font1, width=5, height=1,
                          pady=2, command=button13)
            done.grid(row=4, column=3)
            nope = Button(cust_frame1, text='Cancel', font=font1, width=5, height=1,
                          pady=2, command=reset)
            nope.grid(row=4, column=5)

        def change_3():
            '''method for changing shipping address'''
            f_.destroy()
            shipping_address = Entry(cust_frame1, width=40, font=font1, bd=5)
            shipping_address.insert(0, 'Enter new shipping_address')
            shipping_address.grid(row=5, column=2)

            def button14():
                self.acc_details[self.user_name][2] = shipping_address.get()
                saver()
                reset()

            done = Button(cust_frame1, text='Done', font=font1, width=5, height=1,
                          pady=2, command=button14)
            done.grid(row=5, column=3)
            nope = Button(cust_frame1, text='Cancel', font=font1, width=5, height=1,
                          pady=2, command=reset)
            nope.grid(row=5, column=5)

        edit_1 = Button(cust_frame1, text='Edit', font=font1, width=3, height=1,
                        pady=2, command=lambda: [name_change(), edit_1.destroy()])
        edit_2 = Button(cust_frame1, text='Edit', font=font1, width=3, height=1,
                        pady=2, command=lambda: [pass_change(), edit_2.destroy()])
        edit_3 = Button(cust_frame1, text='Edit', font=font1, width=3, height=1,
                        pady=2, command=lambda: [change_1(), edit_3.destroy()])
        edit_4 = Button(cust_frame1, text='Edit', font=font1, width=3, height=1,
                        pady=2, command=lambda: [change_2(), edit_4.destroy()])
        edit_5 = Button(cust_frame1, text='Edit', font=font1, width=3, height=1,
                        pady=2, command=lambda: [change_3(), edit_5.destroy()])
        edit_1.grid(row=1, column=3)
        edit_2.grid(row=2, column=3)
        edit_3.grid(row=3, column=3)
        edit_4.grid(row=4, column=3)
        edit_5.grid(row=5, column=3)

    def ViewOrderHistory(self):
        '''Method which displays a user's order history'''
        x = self.user_name
        y = getcwd() + '/history/'
        # opening the history file to store info
        with open(y + x + 'history.txt', 'a+') as f:
            cust_frame2 = Frame(root, bg='peach puff', padx=150, pady=150, relief=RAISED)
            cust_frame2.pack()
            Label(cust_frame2, text='ORDER HISTORY', font=font1, width=47, bd=20, relief=GROOVE,
                  bg='white').grid(row=0, column=0)
            f.seek(0)
            words = f.read()
            if words != '':
                f.seek(0)
                Label(cust_frame2, text=words, font=font1, width=50, bd=3, relief=GROOVE, pady=5,
                      bg='white').grid(row=1, column=0)
            else:
                Label(cust_frame2, text='There is no order history of your account', font=font1, width=50, bd=5,
                      relief=GROOVE, bg='white').grid(row=2, column=0)
        # button which destroys cust_frame2 and opens the user panel
        back = Button(cust_frame2, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [cust_frame2.destroy(), user_panel()])
        back.grid(row=3, column=0)


class Cart:
    '''The class for cart'''

    def __init__(self, product):
        _ = getcwd() + '/products/'
        self.inst_product = product(_ + 'fruits.csv', _ + 'vegetable.csv', _ + 'fish.csv', _ + 'beverages.csv',
                                    _ + 'meat.csv')
        self.cart = []
        self.quantity = []
        self.bill = []
        self.base_list = ['Fruits', 'Vegetable', 'Fish', 'Beverages', 'Beef/Mutton/Chicken']

    def BrowseMarket(self):
        '''method for browsing the store'''
        self.inst_product.CategoryChooser(local_='cart')
        global market

        def market():
            # market implementation
            global cart_frame
            cart_frame = Frame(root, bg='light salmon', padx=150, pady=150, relief=RAISED)
            cart_frame.pack()
            self.inst_product.DisplayProductDetails(local_='cart')

        global adder

        def adder(k):
            '''method which handles the products getting added to carts'''
            new = Tk()
            new.title('Add to cart')
            quantity = Entry(new, width=25, font=font1, bd=2)
            quantity.insert(0, 'Enter Quantity of product')
            quantity.grid(row=0, column=0, columnspan=3)

            def plus_():
                # exception handler for non integer values
                try:
                    if quantity.get().isdigit():
                        pass
                    else:
                        raise ValueError('ValueError...\nINVALID INPUT FOR INTEGER')
                except ValueError as ve:
                    print(ve)
                    new1 = Tk()
                    new1.title('Message!')
                    Label(new1, text='INVALID INPUT FOR QUANTITY. Value cannot be other than integer', font=font1,
                          width=60, bd=5, bg='white', relief=RIDGE).pack(pady=2)
                    new.destroy()
                    cart_frame.destroy()
                    market()
                    new1.mainloop()
                # when no product is to be added
                if int(quantity.get()) == 0:
                    new.destroy()
                    cart_frame.destroy()
                    market()
                # when quantity of the product being added is less than the pre-existing stock
                if int(quantity.get()) <= self.inst_product.prd_stock.get(k):
                    self.cart.append(k)
                    self.inst_product.prd_stock[k] -= int(quantity.get())
                    self.quantity.append(int(quantity.get()))
                    self.bill.append(self.inst_product.prd_prices.get(k)[0] * int(quantity.get()))
                    new.destroy()
                    cart_frame.destroy()
                    market()
                # when the inverse is true
                else:
                    if self.inst_product.prd_stock.get(k) == 0:
                        adds['state'] = DISABLED
                        Label(new, text='Product out of stock', width=20,
                              font=font1).grid(row=3, column=0, columnspan=3)
                    else:
                        adds['state'] = DISABLED
                        Label(new, text='Purchase limit exceeds items in stock', width=30,
                              font=font1).grid(row=3, column=0, columnspan=3)

            # gui button for adding products to cart and going back
            adds = Button(new, text='Add', font=font1, width=5, height=1,
                          command=plus_)
            adds.grid(row=1, column=0)
            back = Button(new, text='Back', font=font1, width=5, height=1,
                          command=lambda: [new.destroy(), cart_frame.destroy(), market()])
            back.grid(row=1, column=2)
            new.mainloop()

    def ViewCart(self):
        '''method for viewing contents of the cart'''
        if self.cart:
            Label(cart_frame2, text='Products:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=1, column=0, padx=10, pady=10)
            Label(cart_frame2, text='Quantity', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=1, column=1, padx=10, pady=10)
            Label(cart_frame2, text='Price:', font=font1, width=25, bd=10, relief=GROOVE,
                  bg='white').grid(row=1, column=2, padx=10, pady=10)
            Label(cart_frame2, text='Remove', font=font1, width=10, bd=10, relief=GROOVE,
                  bg='white').grid(row=1, column=3, padx=25, pady=10)
            for i in range(0, len(self.cart)):
                Label(cart_frame2, text=self.cart[i], font=font1, width=25, bd=5,
                      bg='white', relief=RIDGE).grid(row=i + 2, column=0)
                Label(cart_frame2, text=self.quantity[i], font=font1, width=25, bd=5, bg='white',
                      relief=RIDGE).grid(row=i + 2, column=1)
                Label(cart_frame2, text=self.bill[i], font=font1, width=25, bd=5, bg='white',
                      relief=RIDGE).grid(row=i + 2, column=2)
        else:
            Label(cart_frame2, text='Your Cart is empty please add items first :(', width=40,
                  font=font1).grid(row=99, column=0, columnspan=3)
            order.destroy()
        back = Button(cart_frame2, text='Back', font=font1, width=15, height=1,
                      pady=2, command=lambda: [cart_frame2.destroy(), market()])
        back.grid(row=100, column=1, pady=10)

    def RemoveFromCart(self):
        '''method for removing contents of the cart'''
        buttons = []
        for i in range(0, len(self.cart)):
            z = Button(cart_frame2, text='X', font=font1, width=1, height=1,
                       command=lambda j=i: remove(j))
            z.grid(row=i + 2, column=3, pady=2)
            buttons.append(z)

        def remove(index):
            put_back = self.cart.pop(index)
            return_ = self.quantity.pop(index)
            for o in self.base_list:
                if put_back in self.inst_product.file_data.get(o)[0]:
                    self.inst_product.file_data.get(o)[0][put_back] += return_
            self.bill.pop(index)
            cart_frame2.destroy()
            cart_view()


class Order:
    '''An order class which handles the products that have already been ordered'''

    def __init__(self, cart_):
        self.inst_cart = cart_

    def PlaceOrder(self):
        '''method which deals with placing the orders'''
        cart_frame2.destroy()
        order_frame = Frame(root, bg='light sea green', padx=150, pady=150, relief=RAISED)
        order_frame.pack()
        bill = sum(self.inst_cart.bill)
        Label(order_frame, text='YOUR ORDER', font=font1, width=50, bd=10, bg='white',
              relief=RIDGE).grid(row=0, column=0, columnspan=2, pady=2)
        Label(order_frame, text='Shipping fee: Rs. 100', font=font1, width=50, bd=5, bg='white',
              relief=RIDGE).grid(row=1, column=0, columnspan=2)
        Label(order_frame, text='Subtotal: Rs.' + str(bill), font=font1, width=50, bd=5, bg='white',
              relief=RIDGE).grid(row=2, column=0, columnspan=2)
        Label(order_frame, text='Total: Rs.' + str(bill + 100), font=font1, width=50, bd=5, bg='white',
              relief=RIDGE).grid(row=3, column=0, columnspan=2)

        def button():
            # the button which deals with the actual implementation of place order
            x = Customer.User_name
            y = getcwd() + '/history/'
            with open(y + x + 'history.txt', 'a') as f:
                string = ''
                for i in range(0, len(self.inst_cart.cart)):
                    string += ('Product name:' + self.inst_cart.cart[i] + ', ' + 'Quantity:' +
                               str(self.inst_cart.quantity[i]) + '\n')
                string += 'Total Price:' + str(bill + 100) + ', ' + 'Order Time:' + ctime(time()) + '\n'
                f.write(string)
            for j in range(0, len(self.inst_cart.cart)):
                self.inst_cart.cart.pop(-1)
                self.inst_cart.quantity.pop(-1)
                self.inst_cart.bill.pop(-1)
            new = Tk()
            new.title('Message!')
            Label(new, text='Your order has been placed.', font=font1, width=50, bd=10, bg='white',
                  relief=RIDGE).pack(pady=2)
            Button(new, text='OK', font=font1, bd=10, command=new.destroy).pack()
            order_frame.destroy()
            user_panel()
            new.mainloop()

        # button for finalizing the order
        finalize = Button(order_frame, text='Proceed', font=font1, width=24, height=1, pady=2, command=button)
        finalize.grid(row=4, column=1)
        back = Button(order_frame, text='Cancel', font=font1, width=24, height=1,
                      pady=2, command=lambda: [order_frame.destroy(), cart_view()])
        back.grid(row=4, column=0)


def admin_enter(my_id):
    global obj_1
    obj_1 = Admin(path + 'admin_details.csv', Products)
    obj_1.Login(my_id)


def user_entry(my_id):
    global obj_2
    obj_2 = Customer(path + 'login_details.csv', path + 'account_details.csv')
    obj_2.Login(my_id)


def your_cart():
    global obj_3
    obj_3 = Cart(Products)


root = Tk()
font1 = Font(family='Times New Roman', size=13)


def main_screen():
    ''' Code which deals with all the contents on the main screen of the gui'''
    root.title('shopping Cart')
    root.maxsize(width=1100, height=750)
    root.minsize(width=900, height=550)
    main_frame = LabelFrame(root, text='WELCOME', bd=20,
                            bg='light coral', relief=SUNKEN, width=1000, height=700)
    label_2 = Label(main_frame, text='SHOPPING CART', width=38, font='bold', bg='MistyRose',
                    relief=RIDGE, height=3, bd=10)
    main_frame.pack(anchor='center')
    main_frame.pack_propagate(False)
    label_2.grid(row=0, column=0, padx=100, pady=10)

    def sign_up():
        # driver code for signing up
        main_frame.destroy()
        global user_frame1
        user_frame1 = Frame(root, bg='yellow', padx=150, pady=150, relief=RAISED)
        user_frame1.pack()
        user_name = Entry(user_frame1, width=50, font=font1, bd=5)
        user_name.insert(0, 'Enter your Username')
        user_name.grid(row=0, column=0, columnspan=3)

        def button1():
            a = user_name.get()
            proceed.destroy()
            user = Label(user_frame1, text='Username:' + a, font=font1, width=50, bd=5, bg='white', relief=RIDGE)
            user.grid(row=0, column=0, columnspan=3)
            user_name.destroy()
            User.SignUp(User, path + 'login_details.csv', path + 'account_details.csv', a)

        proceed = Button(user_frame1, text='Proceed', font=font1, width=50, height=2, pady=2, command=button1)
        proceed.grid(row=6, column=1)
        back = Button(user_frame1, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [user_frame1.destroy(), main_screen()])
        back.grid(row=7, column=1)

    def admin_login():
        # driver code for the log in of an admin
        main_frame.destroy()
        global admin_frame1
        admin_frame1 = Frame(root, bg='lightblue', padx=150, pady=150, relief=RAISED)
        admin_frame1.pack()
        admin_id = Entry(admin_frame1, width=50, font=font1, bd=5)
        admin_id.insert(0, 'Enter Administrator ID')
        admin_id.grid(row=0, column=0, columnspan=3)

        def button3():
            my_id = admin_id.get()
            admin_enter(my_id)
            global ad_approved

            def ad_approved():
                if admin_approves:
                    admin_frame1.destroy()
                    admin_panel(obj_1)

        global id_check
        id_check = Button(admin_frame1, text='Proceed', font=font1, width=50, height=2, pady=2, command=button3)
        id_check.grid(row=1, column=1)
        back = Button(admin_frame1, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [admin_frame1.destroy(), main_screen()])
        back.grid(row=6, column=1)

    global admin_panel

    def admin_panel(obj):
        # driver code for an admin panel
        global admin_frame2
        admin_frame2 = Frame(root, bg='LightCyan4', padx=150, pady=150, relief=RAISED)
        change_pass = Button(admin_frame2, text='Change password', font=font1, width=50, height=2, pady=2,
                             bg='lightyellow', command=obj.ChangeAccountPass)
        change_pass.grid(row=0, column=0)
        manage_prd = Button(admin_frame2, text='Manage Product Details', font=font1, width=50, height=2, pady=2,
                            bg='lightyellow', command=obj.ManageProducts)
        manage_prd.grid(row=1, column=0)
        back = Button(admin_frame2, text='Back', font=font1, width=50, height=2, pady=2,
                      bg='lightyellow', command=lambda: [admin_frame2.destroy(), main_screen()])
        back.grid(row=2, column=0)
        admin_frame2.pack()

    global user_signin

    def user_signin():
        # driver code for user sign in
        main_frame.destroy()
        global signin_frame
        signin_frame = Frame(root, bg='lightblue', padx=150, pady=150, relief=RAISED)
        signin_frame.pack()
        user_name = Entry(signin_frame, width=50, font=font1, bd=5)
        user_name.insert(0, 'Enter your Username')
        user_name.grid(row=0, column=0, columnspan=3)

        def button8():
            my_id = user_name.get()
            user_entry(my_id)
            global approved

            def approved():
                if user_approves:
                    signin_frame.destroy()
                    user_panel()
                    your_cart()

        global id_check
        id_check = Button(signin_frame, text='Proceed', font=font1, width=50, height=2, pady=2, command=button8)
        id_check.grid(row=1, column=1)
        back = Button(signin_frame, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [signin_frame.destroy(), main_screen()])
        back.grid(row=6, column=1)

    global user_panel

    def user_panel():
        # driver code for user panel
        global cust_frame
        cust_frame = Frame(root, bg='light sea green', padx=150, pady=150, relief=RAISED)
        Label(cust_frame, text=obj_2, font=font1, relief=GROOVE, width=47, height=2,
              pady=2, bd=20).grid(row=0, column=0)
        acc_info = Button(cust_frame, text='Account Information', font=font1, width=50, height=2,
                          pady=2, command=obj_2.AccountInfo)
        acc_info.grid(row=1, column=0)
        order_ = Button(cust_frame, text='View Order History', font=font1, width=50, height=2,
                        pady=2, command=lambda: [cust_frame.destroy(), obj_2.ViewOrderHistory(), cust_frame.destroy()])
        order_.grid(row=2, column=0)
        view_store = Button(cust_frame, text='Visit Store', font=font1, width=50, height=2,
                            pady=2, command=shopping)
        view_store.grid(row=3, column=0)
        back = Button(cust_frame, text='Back', font=font1, width=50, height=2,
                      pady=2, command=lambda: [cust_frame.destroy(), main_screen()])
        back.grid(row=4, column=0)
        cust_frame.pack()

    def shopping():
        cust_frame.destroy()
        obj_3.BrowseMarket()
        global cart_view

        def cart_view():
            global cart_frame2
            cart_frame2 = Frame(root, bg='light slate gray', padx=150, pady=150, relief=RAISED)
            Label(cart_frame2, text='YOUR CART', font=font1, width=25, height=3, bd=5, bg='white',
                  relief=RIDGE).grid(row=0, column=0, columnspan=3)
            cart_frame2.pack()
            global order
            order = Button(cart_frame2, text='PLACE ORDER', font=font1, width=15, height=1,
                           pady=2, command=lambda: [take_order(), cart_frame2.destroy()])
            order.grid(row=101, column=1, pady=10)
            obj_3.ViewCart()
            obj_3.RemoveFromCart()

        def take_order():
            obj_4 = Order(obj_3)
            obj_4.PlaceOrder()

    signup = Button(main_frame, text='Sign Up', font=font1, width=50, height=2, pady=2, bg='LavenderBlush2',
                    command=sign_up, relief=SUNKEN, bd=15)
    signin = Button(main_frame, text='Sign In', font=font1, width=50, height=2, pady=2, bg='LavenderBlush2',
                    relief=SUNKEN, bd=15, command=user_signin)
    admin = Button(main_frame, text='Administrator Login', font=font1, width=50, height=2, pady=2, bg='LavenderBlush2',
                   command=admin_login, relief=SUNKEN, bd=15)
    exit_ = Button(main_frame, text='Exit', font=font1, width=50, height=2, pady=2, bg='red',
                   command=exit, relief=SUNKEN, bd=15)
    signup.grid(row=1, column=0, padx=100, pady=5)
    signin.grid(row=2, column=0, padx=100, pady=5)
    admin.grid(row=3, column=0, padx=100, pady=5)
    exit_.grid(row=4, column=0, padx=100, pady=5)
    root.mainloop()


main_screen()
