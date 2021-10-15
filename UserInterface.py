from MPMS import MPMS # import MPMS class to use the methods here
import sys

# This is boundary class for interacting with the user and contains all relevant displays methods
class UserInterface:
    # display login method takes the input from the user and decides the type of account from the options entered by
    # user.
    def display_login(self):
        print(
            "\t" * 2 + "*" * 32 + "\n" + "\t" * 2 + "Monash Patient Management System" + "\n" + "\t" * 2 + "*" * 32 + "\n")
        print("--Please enter your login credentials: " + "\n" + "_" * 38 + "\n")
        user_option_flag = True
        while (user_option_flag == True):
            user_input_email = input("--Email: ")
            user_input_passwd = input("--Password: ")
            print("\n")
            user_type = MPMS.verify_user(user_input_email, user_input_passwd)
            if user_type == "admin":
                MPMS.read_GP_data()
                MPMS.read_appointment_data()
                self.display_admin_main_menu()
                user_option_flag = False
            elif user_type == "patient":
                MPMS.read_reason_data()
                MPMS.read_question_data()
                MPMS.read_clinic_from_db()
                MPMS.read_GP_data()
                MPMS.read_appointment_data()
                self.display_patient_main_menu()
                user_option_flag = False
            else:
                print("!Error: username or password incorrect. please try login again or contact the admin." + "\n")

    # display patient main menu method with manage my appointment feature working
    def display_patient_main_menu(self):
        print(
            "\t" * 2 + "*" * 32 + "\n" + "\t" * 2 + "Monash Patient Management System" + "\n" + "\t" * 2 + "*" * 32 + "\n")
        print("Account Type: Patient" + "\n")
        print("*" * 6 + "Welcome Patient to MPMS" + "*" * 6 + "\n")
        print("--Please choose option from below:" + "\n" + "_" * 34 + "\n")
        print(
            "1. Nearest Monash Clinic Branch." + "\n" + "2. Manage My Appointment." + "\n" + "3. My Favourite Branch & GP."
            + "\n" + "4. Clinic Branch Details." + "\n")
        patient_option_flag = True
        while (patient_option_flag == True):
            patient_option = input("--Enter the option 1-4 or 'q' to log out: ")
            print("\n")
            if patient_option == "1" or patient_option == "3" or patient_option == "4":
                print("###Sorry, this feature under construction, please try later###" + "\n")
            elif patient_option == "2":
                self.display_manage_my_appointment()
                patient_option_flag = False
            elif patient_option == "q":
                print("\n" + "###Thank you to use Monash Patient Managment System###")
                sys.exit()
                patient_option_flag = False
            else:
                print("!Error: the option is incorrect. The option should be from 1 to 4." + "\n")

    # manage my appointment method can take input from user and do the required actions
    # display make new appointment and check in are working the rest under the construction
    def display_manage_my_appointment(self):
        print(
            "\t" * 2 + "*" * 32 + "\n" + "\t" * 2 + "Monash Patient Management System" + "\n" + "\t" * 2 + "*" * 32 + "\n")
        print("Account Type: Patient" + "\n")
        print("*" * 6 + "Manage My Appointment" + "*" * 6 + "\n")
        print("--Please choose option from below:" + "\n" + "_" * 34 + "\n")
        print("1. New Appointment." + "\n" + "2. Cancel Appointment." + "\n" +
              "3. Check in." + "\n" + "4. Back to main menu." + "\n")
        patient_option_flag = True
        while (patient_option_flag == True):
            patient_option = input("--Enter the option 1-4: ")
            print("\n")
            if patient_option == "1":
                self.display_new_appointment()
                patient_option_flag = False
            elif patient_option == "2":
                print("###Sorry, this feature under construction, please try later###" + "\n")
            elif patient_option == "3":
                self.display_patient_checkin()
                patient_option_flag = False
            elif patient_option == "4":
                self.display_patient_main_menu()
                patient_option_flag = False
            else:
                print("!Error: the option is incorrect. The option should be from 1 to 4." + "\n")

    #  patient status method displays if the patient is a new patient or a existing
    def display_patient_status(self):
        print("--Please choose your status from below:" + "\n" + "_" * 40 + "\n")
        print("1. New Patient." + "\n" + "2. Existing Patient." + "\n")
        patient_option_flag = True
        while (patient_option_flag == True):
            patient_status_option = input("--Enter the option 1 or 2: ")
            print("\n")
            patient_status = MPMS.verify_patient_status(patient_status_option)
            if patient_status:
                patient_option_flag = False
            else:
                print("!Error: the option is incorrect. The option should be 1 or 2." + "\n")

    # display patient reason method displays the reasons patient can choose to book an appointment
    def display_patient_reason(self):
        print("--Please choose reason for seeing GP from below:" + "\n" + "_" * 47 + "\n")
        MPMS.get_list_of_reasons()
        print("\n")
        patient_option_flag = True
        while (patient_option_flag == True):
            patient_reason_option = input("--Enter the option 1-3: ")
            print("\n")
            reason_for_seeing_gp = MPMS.verify_reason(patient_reason_option)
            if reason_for_seeing_gp != False:
                patient_option_flag = False
            else:
                print("!Error: the option is incorrect. The option should be from 1 to 3." + "\n")

    # display covid questionnaire
    def display_question(self):
        print("--Please enter answer for Covid questionnaire:" + "\n" + "_" * 47 + "\n")
        index = 0
        while index < len(MPMS.list_of_question) :
            print(MPMS.list_of_question[index].get_question())
            pateint_answer = input("--Enter 'Yes' or 'No': ")
            print("\n")
            if pateint_answer == "Yes" or pateint_answer == "yes":
                print("###Please search on health.gov.au and attend a free COVID-19 respiratory clinic###" + "\n")
                patient_option_flag = True
                while patient_option_flag == True:
                    patient_option = input("--Enter q to back to home:")
                    if patient_option == "q":
                        self.display_patient_main_menu()
                        patient_option_flag = False
                    else:
                        print("!Error: the input is incorrect. Please enter q.")
            elif pateint_answer == "No" or pateint_answer == "no":
                index += 1
            else:
                print("!Error: the option is incorrect. The option should be yes or no." + "\n")



    # display new appointment method to let the user book new appointment.
    def display_new_appointment(self):
        print(
            "\t" * 2 + "*" * 32 + "\n" + "\t" * 2 + "Monash Patient Management System" + "\n" + "\t" * 2 + "*" * 32 + "\n")
        print("Account Type: Patient" + "\n")
        print("*" * 6 + "Create new appointment" + "*" * 6 + "\n")
        self.display_patient_status()
        self.display_patient_reason()
        self.display_question()
        print("--Please choose the clinic branch from below:" + "\n" + "_" * 44 + "\n")
        appointment_clinic = MPMS.get_list_clinic_branches()
        patient_option_flag = True
        patient_clinic_option = ""
        while patient_option_flag:
            patient_clinic_option = input("\n" + "--Enter the option 1-4: ")
            print("\n")
            if MPMS.verify_clinic_option(patient_clinic_option):
                appointment_clinic = str(MPMS.get_clinic_branch(patient_clinic_option))
                print(MPMS.get_clinic_details(patient_clinic_option))
                patient_option_flag = False
        continue_flag = True
        print("--Would you like to continue to book appointment?" + "\n" + "1. Yes" + "\n" + "2. No" + "\n")
        while continue_flag:
            continue_confirmation = input("--Enter the option 1 or 2: ")
            print("\n")
            if continue_confirmation == "1":
                continue_flag = False
            elif continue_confirmation == "2":
                self.display_patient_main_menu()
                continue_flag = False
            else:
                print("!Error: the option is incorrect. The option should be 1 or 2." + "\n")
        print("--Please choose the GP from below: " + "\n" + "_" * 34 + "\n")
        appointment_GP = MPMS.get_GP_names(patient_clinic_option)
        patient_GP_option_flag = True
        while patient_GP_option_flag:
            patient_GP_option = input("\n" + "--Enter the option 1-3: ")
            print('\n')
            if MPMS.verify_GP_option(patient_GP_option) == True:
                appointment_GP = str(MPMS.search_GP_appointment(patient_GP_option))
                patient_GP_option_flag = False
        print("--Please choose the appointment date from below:" + "\n" + "_" * 47 + "\n")
        appointment_date = MPMS.search_appointment_date()
        patient_date_option_flag = True
        while patient_date_option_flag:
            patient_date_option = input("\n" + "--Enter the option 1-5: ")
            print("\n")
            if MPMS.verify_date_option(patient_date_option) == True:
                appointment_date = MPMS.selectd_appointment_date(patient_date_option)
                patient_date_option_flag = False
        print("--Please choose the appointment time from below:" + "\n" + "_" * 47 + "\n")
        appointment_time = MPMS.search_appointment_time()
        patient_time_option_flag = True
        while patient_time_option_flag:
            patient_time_option = input("\n" + "--Enter the option 1-5: ")
            print("\n")
            if MPMS.verify_time_option(patient_time_option) == True:
                appointment_time = MPMS.selectd_appointment_time(patient_time_option)
                patient_time_option_flag = False
        print("Appiontment Details: " + "\n" + "_" * 19 + "\n")
        print("Date:" + appointment_date + "\n" + "Time: " + appointment_time
              + "\n" + "Clinic Branch: " + appointment_clinic + "\n" +
              "GP: " + appointment_GP + "\n" * 2 + "--Are you sure to book this appointment?"
              + "\n" + "1. Yes" + "\n" + "2. No" + "\n")
        appointment_confirmation_flag = True
        while appointment_confirmation_flag:
            appointment_confirmation = input("--Enter the option 1 or 2: ")
            print("\n")
            if appointment_confirmation == "1":
                print("###The appointment has been booked###" + "\n")
                MPMS.write_appointment_data(appointment_clinic, appointment_date, appointment_time, appointment_GP)
                appointment_confirmation_flag = False

                quit_option_flag = True
                while quit_option_flag:
                    quit_option = input("--Enter 'q' to back to home: ")
                    print("\n")
                    if quit_option == "q":
                        self.display_patient_main_menu()
                        quit_option_flag = False
                    else:
                        print("!Error: the option is incorrect, please enter q." + "\n")
            elif appointment_confirmation == "2":
                self.display_patient_main_menu()
                appointment_confirmation_flag = False
            else:
                print("!Error: the option is incorrect, please enter 1 or 2." + "\n")

    # display admin main menu method, generate report is working the rest are under the construction.
    def display_admin_main_menu(self):
        print(
            "\t" * 2 + "*" * 32 + "\n" + "\t" * 2 + "Monash Patient Management System" + "\n" + "\t" * 2 + "*" * 32 + "\n")
        print("Account Type: Admin" + "\n")
        print("*" * 6 + "Welcome Admin to MPMS" + "*" * 6 + "\n")
        print("--Please choose option from below:" + "\n" + "_" * 34 + "\n")
        print("1. Manage clinic." + "\n" + "2. Modify reason for seeing GP." + "\n" + "3. Modify COVID questionnaire." +
              "\n" + "4. Manage GP." + "\n" + "5. Modify assigned GP appointment." + "\n" + "6. Generate report." + "\n" +
              "7. Log out." + "\n")
        admin_option_flag = True
        while admin_option_flag:

            admin_option = input("--Enter the option from 1-7: ")
            print("\n")
            if admin_option == "6":
                self.display_generate_report()
                admin_option_flag = False
            elif admin_option == "7":
                print("\n" + "###Thank you to use Monash Patient Managment System###")
                admin_option_flag = False
            elif admin_option in ("1","2","3","4","5"):
                print("###Sorry, this feature under construction, please try later###" + "\n")
            else:
                print("!Error: the option is incorrect. The option should be from 1 to 7." + "\n")


    #display generate report method, the amount of patient a GP handles is working, the rest are under construction
    def display_generate_report(self):
        print(
            "\t" * 2 + "*" * 32 + "\n" + "\t" * 2 + "Monash Patient Management System" + "\n" + "\t" * 2 + "*" * 32 + "\n")
        print("Account Type: Admin" + "\n")
        print("*" * 6 + "Generate Report" + "*" * 6 + "\n")
        print("--Please choose the report type:" + "\n" + "_" * 34 + "\n")
        print("1. The amount of patients  a GP handles during the period." + "\n" +
              "2. The amount of patients a clinic handled during a period." + "\n" +
              "3. The percentage of reasons for pateint appointment duirng a period." + "\n" +
              "4. Back to main menu." + "\n")
        admin_option_flag = True
        while admin_option_flag:
            admin_option = input("--Enter the option from 1-4: ")
            print("\n")
            if admin_option == "1":
                print("--Please choose the GP name from below:" + "\n" + "_" * 38 + "\n")
                MPMS.get_list_GP_names()
                print("\n")
                GP_option_flag = True
                while admin_option_flag:
                    GP_option = input("--Enter the option from 1 to {}: ".format(len(MPMS.list_of_GP)))
                    if MPMS.verify_GP_name(GP_option) == True:
                        MPMS.generate_report(GP_option)
                        admin_option_flag = False
            elif admin_option == "4":
                self.display_admin_main_menu()
                admin_option_flag = False
            elif admin_option in ("2","3"):
                print("###Sorry, this feature under construction, please try later###" + "\n")
            else:
                print("!Error: the option is incorrect. The option should be from 1 to 4." + "\n")

    # method displays all appointments for patient and checks-in the patient 10 minutes before the appointment
    def display_patient_checkin(self):
        print(
            "\t" * 2 + "*" * 32 + "\n" + "\t" * 2 + "Monash Patient Management System" + "\n" + "\t" * 2 + "*" * 32 + "\n")
        print("Account Type: Patient" + "\n")
        print("*" * 6 + "Check in Appointment" + "*" * 6 + "\n")
        print("--Please choose the appointment dates from below to check in:" + "\n" + "_" * 55 + "\n")
        MPMS.get_appointments_for_patient()
        MPMS.print_appointments_for_patient()
        print("\n")
        check_in_option_flag = True
        while check_in_option_flag:
            check_in_option = input("--Enter the option from 1 to {} OR b to go back to previous screen: ".format(len(MPMS.lst_new_object)))
            print("\n")
            if check_in_option == 'b':
                self.display_manage_my_appointment()
                return
            if MPMS.verify_date_checkin(check_in_option):
                if MPMS.is_checkin_valid(check_in_option):
                    MPMS.do_check_in(check_in_option)
                    print("\n")
                    print("#" * 3 + "The appointment has been checked in" + "#" * 3)
                    MPMS.remove_checkin()
                    print("\n")
                    print("#" * 3 + "The appointment has been removed" + "#" * 3)
                    quit_option_flag = True
                    while quit_option_flag:
                        quit_option = input("--Enter 'q' to back to home: ")
                        print("\n")
                        if quit_option == "q":
                            self.display_patient_main_menu()
                            quit_option_flag = False
                        else:
                            print("!Error: the option is incorrect, please enter q." + "\n")
                    check_in_option_flag = False
                else:
                    print("#" * 3 + "Check in is invalid, Checkin should be in the same day and 10 mins before the appointment" + "#" * 3 + "\n")




# initialise the UserInterface object, then call the display loin method to start the system.
u = UserInterface()
u.display_login()


