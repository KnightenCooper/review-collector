import sqlite3 # import sqlite to use as a database to store reviews
import sys # used to allow the user to close the program

# class that is responsible for dealing with the database.
class Database:
    def __init__(self):
         """store connection and cursor in self so all functions in class can use them"""
         self.connection
         self.cur

    def establishDatabaseConnection(self):
        """is called to establish a connection to the database"""
        # open a SQLite connection, a database file called data.db will be created, if it does not exist
        self.connection = sqlite3.connect('data.db')

    def createDatabaseCursor(self):
        """is called to create the database cursor"""
        self.cur = self.connection.cursor() # create a database cursor

    def createDatabaseTable(self):
        """is called to create the reviews database table if it doesn't exist"""
        table_schema = """
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            rating INTEGER 
        );
        """ # the schema outlines all the columns of the table
        self.cur.execute(table_schema) # create the database table if it doesn't exist

    def closeDatabaseConnection(self):
        """is called to close the database connection and cursor"""
        self.cur.close() # close the cursor
        self.connection.close() # close the connection

    def insertReview(self):
        """inserts a new review to database"""
        title = input('Review Title: ') # get title from user
        desc = input('Review Description: ') # get description from user
        number = True # create number variable so we can use a while loop to force the user to input a int for the rating
        while number:
            try:
                rating = input('Numeric Rating: ') # get rating
                val = int(rating) # test to see if rating is a int
            except ValueError: # if rating is not a int
                print("Please type a integar number without a decimal") # tell user rating should be a int
                number = True
            else: # rating is a int
                number = False # stop while loop
        insert_query = """
        INSERT INTO reviews (title, description, rating)
        VALUES (?, ?, ?);
        """ # query that is used to insert into database
        self.cur.execute(insert_query, (title, desc, rating)) # execute the query
        self.connection.commit() # save it in the database file

    def retrieveReviews(self):
        """ get all the reviews from the database to display them"""
        self.cur.execute('SELECT * FROM reviews;') # query the database for ALL data in the reviews table
        print('\nReviews:')# print the result
        for row in self.cur.fetchall(): # get each value from each review and print them all
            display_title = row[1]
            display_desc = row[2]
            display_rating = row[3]
            print(f'Review title: {display_title}\nReview description: {display_desc}\nRating: {display_rating}\n')

    def retrieveReviewsWithPrimaryKey(self):
        """get all the reviews with their primary keys and display, we need primary keys so user can use primary key for delete or modify a review"""
        self.cur.execute('SELECT * FROM reviews;') # query the database for ALL data in the reviews table
        print('\nReviews:') # print all the results of the query
        for row in self.cur.fetchall():
            display_primary_key = row[0]
            display_title = row[1]
            display_desc = row[2]
            display_rating = row[3]
            print(f'Review Primary Key: {display_primary_key}\nReview title: {display_title}\nReview description: {display_desc}\nRating: {display_rating}\n')

    def modifyReview(self):
        """get primary id of a review from user and data necessary to modify a review and modify that review"""
        id = input('Primary key of review you want to modify: ') # need a way to know which review to change
        title = input('New Review Title: ') # new title after modify
        desc = input('New Review Description: ') # new review description
        number = True # create number variable so we can use a while loop to force the user to input a int for the rating
        while number:
            try:
                rating = input('New Numeric Rating: ') # get new rating
                val = int(rating) # test to see if rating is a int
            except ValueError: # if rating is not a int
                print("Please type a integar number without a decimal") # tell user rating should be a int
                number = True
            else: # rating is a int
                number = False # stop while loop
        update_query = """
        UPDATE reviews 
        SET title = '""" + title + """',
        description = '""" + desc + """',
        rating = """+ str(rating) + """
        WHERE id = """+ str(id) + """;
        """ # query that will update review
        self.cur.execute(update_query) # execute update to database
        self.connection.commit()# save it in the database file

    def deleteReview(self):
        """delete review"""
        id = input('Primary key of review you want to delete: ') #get id of review user wants deleted
        delete_query = """
        DELETE FROM reviews 
        WHERE id = """+ str(id) + """;
        """ # query that will delete review
        self.cur.execute(delete_query) # execute query
        self.connection.commit() # save it in the database file

    def retrieveAverageRating(self):
        """query the database to get average rating and display it"""
        self.cur.execute('SELECT AVG(rating) FROM reviews;') # query database to get average of ratings
        for row in self.cur.fetchall():         # print the result
            display_primary_key = row[0]
            print(f'Average Rating: {display_primary_key}')

    def retrieveMinRating(self):
        """query the database to get smallest rating and display it"""
        # query the database for ALL data in the reviews table
        self.cur.execute('SELECT MIN(rating) FROM reviews;') # query database to get smallest rating
        for row in self.cur.fetchall(): # print the result
            display_primary_key = row[0]
            print(f'Smallest Rating: {display_primary_key}')

    def retrieveMaxRating(self):
        """query the database to get smallest rating and display it"""
        self.cur.execute('SELECT MAX(rating) FROM reviews;') # query database to get smallest rating
        for row in self.cur.fetchall(): # print the result
            display_primary_key = row[0]
            print(f'Largest Rating: {display_primary_key}')

# class that is used to display the menu and give options to user to manipulate reviews
class Menu:
    def menu(self):
        """ The main display and commandline interface for the user """
        print("Review Collector by Knighten Cooper")
        # loop through the menu forever
        while True:
            # Tell the user the options for commands and ask for input. If the user input matches a command call those functions
            print("Enter command ( \'i\' insert review, \'m\' modify review, \'d\' delete review, \'r\' retrieve all reviews, \'s\' statistics, and \'end\' ends program")
            val = input("Enter your value: ") # get user input
            if val == 'i': # if the user inputs 'i' then insert a new review
                database = Database # call database class
                database.establishDatabaseConnection(self) # connect to database
                database.createDatabaseCursor(self) # create database cursor
                database.createDatabaseTable(self) # create database table if it doesn't exist
                database.insertReview(self) # inserts a new review into the database
                database.closeDatabaseConnection(self) # close the database connection cleanly

            if val == 'm': # if the user inputs 'm' then modify a review
                database = Database # call database class
                database.establishDatabaseConnection(self) # connect to database
                database.createDatabaseCursor(self) # create database cursor
                database.createDatabaseTable(self) # create database table if it doesn't exist
                database.retrieveReviewsWithPrimaryKey(self) # displays all current reviews with their primary keys
                database.modifyReview(self) # modifies review that user selects using inputted primary key
                database.closeDatabaseConnection(self) # close the database connection cleanly

            if val == 'd': # if the user inputs 'd' then delete a review
                database = Database # call database class
                database.establishDatabaseConnection(self) # connect to database
                database.createDatabaseCursor(self) # create database cursor
                database.createDatabaseTable(self) # create database table if it doesn't exist
                database.retrieveReviewsWithPrimaryKey(self) # displays all current reviews with their primary keys
                database.deleteReview(self) # deletes review that user selects by inputting primary key
                database.closeDatabaseConnection(self) # close the database connection cleanly

            if val == 'r': # if the user inputs 'r' then retrieve all reviews
                database = Database # call database class
                database.establishDatabaseConnection(self) # connect to database
                database.createDatabaseCursor(self) # create database cursor
                database.createDatabaseTable(self) # create database table if it doesn't exist
                database.retrieveReviews(self) # gets all reviews and displays them
                database.closeDatabaseConnection(self) # close the database connection cleanly

            if val == 's': # if the user inputs 's' then display the stats based on the user's reviews
                # the stats are the average rating, minimum rating, and max rating
                database = Database # call database class
                database.establishDatabaseConnection(self) # connect to database
                database.createDatabaseCursor(self) # create database cursor
                database.createDatabaseTable(self) # create database table if it doesn't exist
                database.retrieveAverageRating(self) # gets all review ratings and averages them
                database.retrieveMinRating(self) # gets all review ratings and displays the smallest one
                database.retrieveMaxRating(self)# gets all review ratings and displays the largest one
                database.closeDatabaseConnection(self) # close the database connection cleanly

            if val == 'end': # if the user types 'end' then end the program
                sys.exit() # exit program

            # If the user inputs a incorrect command, display a error message
            if val != 'i' and val != 'm' and val != 'd' and val != 'r' and val != 's' and val != 'end':
                print('\nError Command Not Recognized, Please Type \'i\', \'m\', \'d\', \'r\', \'s\', or \'end\'\n')

# class called Main class that calls menu() from Menu class
class Main:
    def main1(self):
        """call the menu function"""
        menu = Menu()
        menu.menu()

# call main1 function using Main class
main = Main()
main.main1()


# # Sources Used:
# # https://newbedev.com/python-while-loop-until-user-input-code-example
# # https://dev.to/karmekk/creating-a-simple-sqlite-based-app-with-python-2p2c
# # https://pynative.com/python-check-user-input-is-number-or-string/
# # https://www.sqlitetutorial.net/sqlite-update/
# # https://www.sqlitetutorial.net/sqlite-delete/
# # https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# # Additional Sources Used:
# # https://stackoverflow.com/questions/147741/character-reading-from-file-in-python
# # https://www.keepinspiring.me/famous-quotes/
# # https://stackoverflow.com/questions/43137141/show-command-line-results-in-tkinter-text-widget
# # https://stackoverflow.com/questions/5136611/capture-stdout-from-a-script/5136686#5136686
# # https://docs.python.org/3.5/library/contextlib.html
# # https://stackoverflow.com/questions/42828416/print-output-in-gui-interface-tkinter-python
# # https://k3no.medium.com/command-line-uis-in-python-80af755aa27d
# # https://codeburst.io/building-beautiful-command-line-interfaces-with-python-26c7e1bb54df
# # https://en.wikipedia.org/wiki/Array_data_structure#:~:text=In%20computer%20science%2C%20an%20array,one%20array%20index%20or%20key.&text=Arrays%20are%20among%20the%20oldest,used%20by%20almost%20every%20program.
# # https://www.geeksforgeeks.org/random-numbers-in-python/
# # https://www.w3schools.com/python/gloss_python_array_length.asp
# # https://www.geeksforgeeks.org/reading-writing-text-files-python/
# # https://docs.python.org/3/library/sys.html#sys.exit
# # https://stackoverflow.com/questions/905189/why-does-sys-exit-not-exit-when-called-inside-a-thread-in-python
# # https://docs.python.org/2/library/thread.html#thread.interrupt_main
# # https://stackoverflow.com/questions/1489669/how-to-exit-the-entire-application-from-a-python-thread
# # https://docs.python.org/3/library/os.html#os._exit
# # https://stackoverflow.com/questions/18406165/creating-a-timer-in-python/18406263
# # https://www.tutorialspoint.com/python/python_basic_operators.htm
# # https://unitconverter.fyi/en/86340-s-h/86340-seconds-to-hours
# # https://24hourtime.net/86340-seconds-to-hours
# # https://www.codegrepper.com/code-examples/whatever/vs+code+unident+multiple+lines
# # https://www.geeksforgeeks.org/python-convert-string-to-datetime-and-vice-versa/#:~:text=Program%20to%20convert%20string%20to%20DateTime%20using%20strptime()%20function.&text=strptime()%20is%20available%20in,datetime%20into%20the%20desired%20format.&text=The%20arguments%20date_string%20and%20format%20should%20be%20of%20string%20type.
# # https://docs.python.org/3/library/datetime.html#datetime.timedelta.total_seconds
# # https://stackoverflow.com/questions/3096953/how-to-calculate-the-time-interval-between-two-time-strings
# # https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# # https://www.geeksforgeeks.org/timeit-python-examples/
# # https://docs.python.org/3/library/timeit.html
# # https://stackoverflow.com/questions/23698871/cannot-install-timeit-with-pip-how-can-i-fix-this#:~:text=timeit%20is%20part%20of%20the,to%20install%20it%20via%20pip.&text=That%27s%20because%20timeit%20is%20a,to%20use%20pip%20for%20that.
# # https://stackoverflow.com/questions/24210700/nameerror-name-timer-is-not-defined
# # https://github.com/colyseus/timer/issues/20
# # https://docs.python.org/2/library/threading.html#timer-objects
# # https://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day
# # https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjDrsbi8p_zAhWkk2oFHT2lCkkQFnoECAsQAQ&url=https%3A%2F%2Fcodingshiksha.com%2Fpython%2Fpython-tkinter-script-to-make-a-alarm-clock-and-set-alarm-time-full-project-for-beginners%2F&usg=AOvVaw23E9sLSRyWuaWIjbif9CWx
# # https://stackoverflow.com/questions/16325039/python-alarm-clock
# # https://stackoverflow.com/questions/16325039/python-alarm-clock
# # https://discuss.codecademy.com/t/how-to-convert-to-12-hour-clock/3920/2
# # https://stackoverflow.com/questions/13855111/how-can-i-convert-24-hour-time-to-12-hour-time
# # https://www.geeksforgeeks.org/how-to-create-a-new-thread-in-python/
# # https://stackoverflow.com/questions/66074642/variable-not-accessed
# # https://careerkarma.com/blog/python-uppercase/
# # https://www.kite.com/python/answers/how-to-check-if-a-string-contains-only-numbers-in-python#:~:text=Use%20str.,are%20numeric%20digits%20or%20not.
# # https://stackabuse.com/python-check-if-variable-is-a-number/
# # https://www.geeksforgeeks.org/python-string-length-len/
# # https://www.edureka.co/community/21051/how-to-exit-a-python-script-in-an-if-statement
# # https://realpython.com/python-or-operator/#if-statements
# # https://www.openbookproject.net/books/bpp4awd/ch04.html
# # https://www.geeksforgeeks.org/taking-input-in-python/
# # https://pypi.org/project/pynput/
# # https://www.hackerearth.com/practice/python/working-with-data/expressions/tutorial/#:~:text=Python%20Expressions%3A,expressions%20are%20representation%20of%20value.&text=Python%20has%20some%20advanced%20constructs,constructs%20are%20also%20called%20expressions.
# # https://pythonbasics.org/python-play-sound/
# # https://www.geeksforgeeks.org/play-sound-in-python/
# # https://bigsoundbank.com/detail-1616-answering-machine-beep.html
# # https://pypi.org/project/playsound/1.2.2/
# # https://docs.python.org/3/tutorial/introduction.html
# # https://dev.to/mindninjax/alarm-clock-python-project-4jn4
# # https://www.w3schools.com/python/ref_string_lower.asp
# # https://www.geeksforgeeks.org/creat-an-alarm-clock-using-tkinter/
# # https://github.com/microsoft/pylance-release/issues/31
# # https://stackoverflow.com/questions/7712389/copy-paste-into-python-interactive-interpreter-and-indentation
# # https://stackoverflow.com/questions/1016814/what-to-do-with-unexpected-indent-in-python
# # https://stackoverflow.com/questions/31340/how-do-threads-work-in-python-and-what-are-common-python-threading-specific-pit
# # https://www.activestate.com/resources/quick-reads/how-to-use-pack-in-tkinter/
# # https://www.educba.com/tkinter-window-size/?source=leftnav
# # https://www.geeksforgeeks.org/how-to-create-full-screen-window-in-tkinter/
# # https://www.geeksforgeeks.org/python-create-a-digital-clock-using-tkinter/
# # https://www.tutorialspoint.com/python/tk_colors.htm
# # https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
# # https://www.tutorialspoint.com/python/tk_grid.htm
# # https://www.tutorialspoint.com/how-to-add-padding-to-a-tkinter-widget-only-on-one-side
# # https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi855iGtp_zAhVInp4KHdB1AlEQFnoECAUQAQ&url=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F4174575%2Fadding-padding-to-a-tkinter-widget-only-on-one-side&usg=AOvVaw3O9WZnEA72nFR2UwPvo30A
# # https://www.w3schools.com/python/python_variables.asp
# # https://stackoverflow.com/questions/16043797/python-passing-variables-between-functions
# # https://github.com/microsoft/pylance-release/issues/757
# # https://github.com/microsoft/pylance-release/blob/main/TROUBLESHOOTING.md#unresolved-import-warnings
# # https://data-flair.training/blogs/alarm-clock-python/
# # https://gist.github.com/charleyXuTO/edf153da4980e7ea68356a6f1edd3c44
# # https://www.codeitbro.com/how-to-make-digital-clock-in-python/
# # https://www.youtube.com/watch?v=ruohUTTo8Kw
# # https://www.reddit.com/r/learnpython/comments/d2slyc/alarm_clock_tkinter/
# # https://riptutorial.com/tkinter/example/22870/-after--
# # https://www.tutorialspoint.com/python/python_multithreading.htm
# # https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwimw6e00Z_zAhXQkmoFHTynAUgQFnoECDUQAw&url=https%3A%2F%2Fwww.geeksforgeeks.org%2Fmultithreading-python-set-1%2F&usg=AOvVaw1zEwsK-nmVWADtD9kVyhRf
# # https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwimw6e00Z_zAhXQkmoFHTynAUgQFnoECCkQAw&url=https%3A%2F%2Fen.wikibooks.org%2Fwiki%2FPython_Programming%2FThreading&usg=AOvVaw3iJ8cgmE5gsyEaVq66OaVE
# # https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwimw6e00Z_zAhXQkmoFHTynAUgQFnoECAIQAQ&url=https%3A%2F%2Frealpython.com%2Fintro-to-python-threading%2F&usg=AOvVaw3oiOZpTGDtJmj9x7FWIoVx
# # https://stackoverflow.com/questions/14824163/how-to-get-the-input-from-the-tkinter-text-widget
# # https://docs.python.org/3/tutorial/classes.html
# # https://newbedev.com/python-list-takes-0-positional-arguments-but-1-was-given-code-example
# # https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds