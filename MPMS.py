# This is the control class which does validation and work as moderator between the boundary and entities classes
from Questions import Question
from Patient import Patient
from Administrator import Admin
from Reason import Reason
from Clinic import Clinic
from GP import GP
from datetime import datetime
from datetime import date
from Appointment import Appointment
import time


class MPMS:
    list_of_question = []  # a list of question objects
    list_of_reason = []  # a list of reason
    list_of_clinics = []  # a list for storing clinic objects
    list_of_GP = []  # list of GP objects
    list_of_appointment = []  # list of appointment

    @classmethod
    # control method interacting with patient and admin class
    def verify_user(self, email, pwd):
        object_patient = Patient()  # initialise the patient object
        object_admin = Admin()  # initialise the admin object
        if email == object_patient.get_email() and pwd == object_patient.get_password():
            return "patient"
        elif email == object_admin.get_email() and pwd == object_admin.get_password():
            return "admin"
        else:
            return False

    @classmethod
    # read reason data method
    def read_reason_data(self):
        with open("Reason_data.txt", "r") as data:  # open the txt file
            for line in data:  # loop over each line
                try:
                    type_of_reason, duration = line.strip().split(",")  # each line would have the these data
                    temp = Reason(type_of_reason, duration)  # These data are used for construction of a clinic object
                    self.list_of_reason.append(temp)  # Once the clinic object is ready, it will be append into the DB

                except:
                    print("!Error: missing value detected.")

    @classmethod
    # get list of reasons method
    def get_list_of_reasons(self):
        for each in self.list_of_reason:
            print(each)

    # verify reason method to return reason for seeing GP or return false when the patient enter thee option that not exist
    @classmethod
    def verify_reason(self, patient_reason):
        if patient_reason == "1":
            return self.list_of_reason[0]
        elif patient_reason == "2":
            return self.list_of_reason[1]
        elif patient_reason == "3":
            return self.list_of_reason[2]
        else:
            return False

    @classmethod
    # read the question data method
    def read_question_data(self):
        with open("Question_data.txt", "r") as data:
            for line in data:
                try:
                    question_content = line.strip()
                    temp_question = Question(question_content)  # Construct a question object
                    self.list_of_question.append(temp_question)
                except:
                    print("!Error: missing value detected.")

    @classmethod
    # get list of reasons method
    def get_list_of_question(self):
        for each in self.list_of_question:
            print(each.get_question())

    # verify patient status method to validate the option that enter selected from the patient
    @classmethod
    def verify_patient_status(self, patient_status):
        if patient_status == "1":
            return "New Patient"
        elif patient_status == "2":
            return "Existing Patient"
        else:
            return False

    # read clinic from db method to read the clinic data from clinic txt file and append it to the clinic list
    # after constuct the clinic object
    @classmethod
    def read_clinic_from_db(self):
        with open("Clinic_data.txt", "r") as data:  # open the txt file
            for line in data:  # loop over each line
                try:
                    branch, address, phone, time = line.split(",")  # each line would have the these data
                    temp = Clinic(branch, address, phone,
                                  time)  # These data are used for construction of a clinic object
                    self.list_of_clinics.append(temp)  # Once the clinic object is ready, it will be append into the DB
                except:
                    print("!Error: missing value detected.")

    list_sorted_clinic_names = []  # decleare list sorted clinic names as list

    # get list clinic branches method to return the nmaes of clinic branches after sort it
    @classmethod
    def get_list_clinic_branches(self):
        index = 0
        if len(self.list_sorted_clinic_names) > 0:
            while index < len(self.list_sorted_clinic_names):
                print(str(index + 1) + ". " + self.list_sorted_clinic_names[index])
                index += 1
        else:
            for each in self.list_of_clinics:
                self.list_sorted_clinic_names.append(each.get_clinic_branch())
                self.list_sorted_clinic_names.sort()
            while index < len(self.list_sorted_clinic_names):
                print(str(index + 1) + ". " + self.list_sorted_clinic_names[index])
                index += 1

    # verify clinic option method to validate the option that slected from the patient
    @classmethod
    def verify_clinic_option(self, clinic_branch_number):
        try:
            clinic_branch_number = int(clinic_branch_number)
            if clinic_branch_number <= len(self.list_of_clinics) and type(
                    clinic_branch_number) == int and clinic_branch_number > 0:
                return True
            else:
                print("!Error: the option is incorrect.")
        except ValueError:
            print("!Error: the option is incorrect. Please only use number.")

    # get clinic branch to return the clinic branch name the has been slected from the patient
    @classmethod
    def get_clinic_branch(self, clinic_branch_number):
        clinic_branch_number = int(clinic_branch_number)
        clinic_branch_number -= 1
        return self.list_sorted_clinic_names[clinic_branch_number]

    # get clinic details method to return clinic details
    @classmethod
    def get_clinic_details(self, clinic_branch_number):
        clinic_branch_number = int(clinic_branch_number)
        clinic_branch_number -= 1
        selected_clinic_names = self.list_sorted_clinic_names[clinic_branch_number]
        for each in self.list_of_clinics:
            if selected_clinic_names == each.get_clinic_branch():
                return each

    # read GP data method to read the GP data from the GP txt and append it to the GP list after construct GP object
    @classmethod
    def read_GP_data(self):
        with open("GP.txt", "r") as data:  # open the file in "read" mode
            for line in data:  # iterate through each line in the file
                try:
                    GP_first_name, GP_last_name, GP_phone, GP_area_intrest, GP_assigned, GP_appointments = line.strip().split(
                        ",")
                    temp = GP(GP_first_name, GP_last_name, GP_phone, GP_area_intrest, GP_assigned,
                              GP_appointments)  # Construct a GP object
                    self.list_of_GP.append(temp)
                except:
                    print("!Error: missing value detected.")

    list_GP_selected_clinic = []  # decleare the list GP slected clinic as lsit

    # get GP names method to return all GP names
    @classmethod
    def get_GP_names(self, clinic_branch_number):
        if self.verify_clinic_option(clinic_branch_number) == True:
            clinic_branch_number = int(clinic_branch_number)
            clinic_branch_number -= 1
            clinic_name = self.list_sorted_clinic_names[clinic_branch_number]
            count = 1
            for each in self.list_of_GP:
                if each.get_GP_clinic_assigned() == clinic_name:
                    self.list_GP_selected_clinic.append(each)
                    print(str(count) + ". " + each.get_GP_first_name() + " " + each.get_GP_last_name())
                    count += 1
            print(str(count) + ". Any GP")

    # verify GP option method to validate the input from the patient for slecting GP
    @classmethod
    def verify_GP_option(self, GP_option):
        try:
            GP_option_number = int(GP_option)
            if GP_option_number <= len(self.list_GP_selected_clinic) + 1 and type(
                    GP_option_number) == int and GP_option_number > 0:
                return True
            else:
                print("!Error: the option is incorrect.")
        except ValueError:
            print("!Error: the option is incorrect. Please only use number")

    # search GP appointment method to return the GP names that has been selected from the patient
    # or assign a GP that has least appointment when the patient select any.
    @classmethod
    def search_GP_appointment(self, GP_option_number):
        if self.verify_GP_option(GP_option_number) == True:
            GP_option_number = int(GP_option_number)
            if GP_option_number == len(self.list_GP_selected_clinic) + 1:
                list_number_appointment = []
                for each in self.list_GP_selected_clinic:
                    list_number_appointment.append(each.get_GP_number_of_appointment())

                list_number_appointment.sort()
                for each in self.list_GP_selected_clinic:
                    if list_number_appointment[0] == each.get_GP_number_of_appointment():
                        return each.get_GP_first_name() + " " + each.get_GP_last_name()
            else:
                return self.list_GP_selected_clinic[GP_option_number - 1]

    date_availability = ["10/11/2021", "11/11/2021", "12/11/2021", "13/11/2021", "14/11/2021"]

    # search appointment date method to return all the available date for book new appointment
    @classmethod
    def search_appointment_date(self):
        count = 1
        for each in self.date_availability:
            print(str(count) + ". " + each)
            count += 1

    # verify date option method to validate the input that has been entered from the patient
    @classmethod
    def verify_date_option(self, date_option_number):
        try:
            date_option_number = int(date_option_number)
            if date_option_number <= len(self.date_availability) and type(
                    date_option_number) == int and date_option_number > 0:
                return True
            else:
                print("!Error: the option is incorrect.")
        except ValueError:
            print("!Error: the option is incorrect. Please only use number")

    # selected appontment date method to return the appointment date that has been selected from the patient
    @classmethod
    def selectd_appointment_date(self, date_option_number):
        date_option_number = int(date_option_number)
        date_option_number -= 1
        return self.date_availability[date_option_number]

    time_availability = ["8:30", "09:00", "10:15", "11:00", "11:45"]

    # search appointment time method to return all the available time for make new appointment
    @classmethod
    def search_appointment_time(self):
        count = 1
        for each in self.time_availability:
            print(str(count) + ". " + each)
            count += 1

    # verify time option method to validate the input that has been entered from the patient
    @classmethod
    def verify_time_option(self, time_option_number):
        try:
            time_option_number = int(time_option_number)
            if time_option_number <= len(self.time_availability) and type(
                    time_option_number) == int and time_option_number > 0:
                return True
            else:
                print("!Error: the option is incorrect.")
        except ValueError:
            print("!Error: the option is incorrect. Please only use number")

    # selected appontment time method to return the appointment time that has been selected from the patient
    @classmethod
    def selectd_appointment_time(self, time_option_number):
        time_option_number = int(time_option_number)
        time_option_number -= 1
        return self.time_availability[time_option_number]

    # write appointment data method to write the new appointment data to appointments txt file, after construct appointment object
    @classmethod
    def write_appointment_data(self, app_branch, app_date, app_time, app_gp):
        temp_appointment = str(Patient()) + "," + app_branch + "," + app_date + "," + app_time + "," + app_gp
        with open("Appointments.txt", "a+") as data:  # open the file in "append" mode
            try:
                data.write("\n")
                data.write(temp_appointment)
            except:
                print("!Error: missing value detected.")

    # read appointment data method to read the data from appointment txt file and append it to the list of appointment
    # after the construct appointment objects
    @classmethod
    def read_appointment_data(self):
        with open("Appointments.txt", "r") as data:  # open the file in "read" mode
            for line in data:  # iterate through each line in the file
                try:
                    patient_name, app_branch, app_date, app_time, app_gp = line.strip().split(",")
                    temp = Appointment(patient_name, app_branch, app_date, app_time,
                                       app_gp)  # Construct an appointment object
                    self.list_of_appointment.append(temp)
                except:
                    print("!Error: missing value detected.")

    # get list GP names to return all the GP names from the list
    @classmethod
    def get_list_GP_names(self):
        count = 1
        for each in self.list_of_GP:
            print(str(count) + ". " + each.get_GP_first_name() + " " + each.get_GP_last_name())
            count += 1

    @classmethod
    def verify_GP_name(self, GP_option):
        try:
            GP_option_number = int(GP_option)
            if GP_option_number <= len(self.list_of_GP) and type(GP_option_number) == int and GP_option_number > 0:
                return True
            else:
                print("!Error: the option is incorrect.")
        except ValueError:
            print("!Error: the option is incorrect. Please only use number")

    # This method prompt the user to enter both starting date and ending date
    # It's meant to collaborate with the generate_report()
    # It includes full validations regarding date input from user (e.g Date format and logical check)
    @classmethod
    def prompt_date(self):
        start_date = ""
        end_date = ""
        flag1 = False  # if user's input satisfied with all conditions, it reaches to the line where assign it to True
        flag2 = False  # Same as above, but validate the end date

        while not flag1:  # While the user inputs does not meet the conditions
            try:
                start_date_temp = input("\n--Please enter the start date e.g.(dd/mm/yyyy): ")
                dd, mm, yyyy = start_date_temp.split("/")  # split into 3 variables to validate individually
                if int(dd) in range(1, 32) and int(mm) in range(1, 13) and int(yyyy) in range(2000, 2022):
                    start_date = start_date_temp  # e.g. day should not exceed 31, month not exceed 12
                    flag1 = True  # if all satisfied, it turns true to break the loop
                else:
                    print("!Error: Invalid Date Input ***")
            except:
                print("!Error: Invalid Date Format ***")  # Limiting the user input format

        while not flag2:
            try:
                end_date_temp = input("\n--Please enter the End date e.g.(dd/mm/yyyy): ")
                dd, mm, yyyy = end_date_temp.split("/")  # Same as previous
                # Calculate to ensure end date > start date
                if int(dd) in range(1, 32) and int(mm) in range(1, 13) and int(yyyy) in range(2000, 2022):
                    dd2, mm2, yyyy2 = start_date.split("/")
                    temp_start = int(dd2) + int(mm2) * 100 + int(yyyy2) * 10000
                    temp_end = int(dd) + int(mm) * 100 + int(yyyy) * 10000

                    if temp_end - temp_start >= 0:  # Validation: End date must be later than Start date
                        end_date = end_date_temp
                        flag2 = True  # 1.Format Check and 2.Logic Check, Completed
                    else:
                        print("!Error: End date must not earlier than Start date.")
                else:
                    print("!Error: Invalid Date Input.")
            except:
                print("!Error: Invalid Date Format.")  # Limiting the user input format

        return start_date, end_date

    # (1)GP option would pass to here, while prompt_date() is called in this method to capture date range of the report
    # It matches the chosen GP with the Database to see how many appointment one has in a given time range
    @classmethod
    def generate_report(self, GP_option):
        GP_option = int(GP_option)
        GP_name = self.list_of_GP[GP_option - 1].get_GP_first_name() + " " + self.list_of_GP[
            GP_option - 1].get_GP_last_name()
        start_date, end_date = self.prompt_date()  # Prompt date inputs from user
        return_list = []
        for item in self.list_of_appointment:
            # Calculation Algorithm for comparing date
            dd, mm, yyyy = item.get_appointment_date().split("/")  # Split them into 3 individual variables dd mm yyyy
            read_total = int(dd) + int(mm) * 100 + int(yyyy) * 10000
            # Convert into integer for calculation  (e.g. 01/01/2021 -> 20210101)
            dd, mm, yyyy = start_date.split("/")  # 20200101 is actually 2020 01 01 without comma :D
            self_start_total = int(dd) + int(mm) * 100 + int(yyyy) * 10000
            dd, mm, yyyy = end_date.split("/")  # Now you have got (1)start, (2)end ,and (3)each appointment in int
            self_end_total = int(dd) + int(mm) * 100 + int(yyyy) * 10000

            if (read_total >= self_start_total and read_total <= self_end_total) and item.appointment_GP == GP_name:
                return_list.append(item)  # Append and count the qualified appointment object

        print("\nGP Name: {}\nNumber of Appointment: {}\nDate Range: {} - {}".format(GP_name, len(return_list),
                                                                                     start_date, end_date))
        return return_list

    count_number_queue = 0
    list_checkin_count = []
    lst_new_object = []

    # displays all the appointment dates patient has booked
    @classmethod
    def get_appointments_for_patient(self):
        if len(self.lst_new_object) > 0:
            return
        for each in self.list_of_appointment:
            patient_name = Patient().get_first_name() + " " + Patient().get_last_name()
            if patient_name == each.get_patient_name():
                self.lst_new_object.append(each)

    @classmethod
    def print_appointments_for_patient(self):
        count = 1
        for each in self.lst_new_object:
            print(str(count) + ". " + each.get_appointment_date())
            count += 1

    # verfies the input inserted by the user
    @classmethod
    def verify_date_checkin(self, option):
        try:
            option = int(option)
            if option <= len(self.lst_new_object) and type(option) == int and option > 0:
                return True
            else:
                print("!Error: the option is incorrect.")
        except ValueError:
            print("!Error: the option is incorrect. Please only use number")

    # returning the appointment object from the list
    @classmethod
    def get_appointment_object(self, option):
        if self.verify_date_checkin(option) == True:
            option = int(option)
            option -= 1
            return self.lst_new_object[option]

    # appointment object returned from get_appointment_object is used in this method to retreive date time of that
    # particular appointment object and compares it with present time and checks in user if the duration of
    # appointment is less than 10 minutes
    @classmethod
    def is_checkin_valid(self, option):
        appointment_obj = self.get_appointment_object(option)
        appointment_date = appointment_obj.get_appointment_date()
        appointment_time = appointment_obj.get_appointment_time()
        datetimeObj = datetime.strptime(appointment_date + appointment_time, "%d/%m/%Y%H:%M")
        time_now = datetime.now()
        time_diff = datetimeObj - time_now
        duration_in_seconds = time_diff.total_seconds()
        duration_in_minutes = divmod(duration_in_seconds, 60)[0]
        today = date.today()
        today_new_format = today.strftime("%d/%m/%Y")
        if 0 < duration_in_minutes < 10 and appointment_date == today_new_format:
            return True
        else:
            return False

    @classmethod
    # takes the response from user and completes the check-in
    def do_check_in(self, option):
        appointment_obj = self.get_appointment_object(option)
        self.list_checkin_count.append(appointment_obj)
        count_number_queue = self.list_checkin_count.index(appointment_obj)
        print(appointment_obj, end='')
        print("Number in the queue : " + str(self.count_number_queue + 1))

    # removes the appointment from the list after 45 minutes
    @classmethod
    def remove_checkin(self):
        time.sleep(2700)  # 60 seconds need to be changed to 45 mins i.e. 45*60
        del self.list_checkin_count[-1]
