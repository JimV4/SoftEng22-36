import subprocess
import json
import csv
import io
import pandas as pd


check_mark = "\u2713".encode("utf-8")

def load_variable_from_file():
    with open("token.txt", "r") as file:
        return str(file.read())

def run_login(username, password, form, output = True):
    result = subprocess.run(['python', 'cli.py', 'login', '--username', username, '--passw', password, '--format', form], capture_output=True)
    # response = json.loads(result.stdout)
    # print(result.stdout.decode('utf-8')+"\n====================")
    # print(">>> HERE <<<")
    # print(result.stdout.decode())
    if form == "json":
        res = json.loads(result.stdout.decode('utf-8'))
    else:
        res = csv.reader(io.StringIO(result.stdout.decode()))
    if result.returncode != 0:
        raise Exception('Login failed with return code {}'.format(result.returncode))
    # print("TYPE =", type(res))
    # if str(type(res)) == "<class '_csv.reader'>":
    #     print("GOOD")
    if isinstance(res, dict) and len(res) == 1:
        if next(iter(res)) == "token":
            if (output):
                print("PASSED", check_mark.decode("utf-8"))
        else:
            if (output):
                print("FAILED, wrong response data")
    elif str(type(res)) == "<class '_csv.reader'>":
        if next(res)[0] == "token":
            if (output):
                print("PASSED", check_mark.decode("utf-8"))
        else:
            if (output):
                print("FAILED, wrong response data")
    else:
        if (output):
            print("FAILED, wrong response type (expected 'dict', got '" + type(res)[8:-2] + "')")

    return

def run_logout(form): # (username, password, form):
    # run_login(username, password, form, False)
    result = subprocess.run(['python', 'cli.py', 'logout', '--format', form], capture_output=True)
    # print(">>> HERE <<<")
    # print(result.stdout.decode())
    # response = json.loads(result.stdout)
    # print(result.stdout.decode('utf-8')+"\n====================")
    if form == "json":
        res = json.loads(result.stdout.decode('utf-8'))
    else:
        res = csv.reader(io.StringIO(result.stdout.decode())) # TEMPORARY UNTIL CSV BUG FIXED        
        # csv_reader = csv.reader(result.stdout.decode('utf-8').splitlines())
        # for row in csv_reader:
        #     print(row)
        
    if result.returncode != 0:
        raise Exception('Logout failed with return code {}'.format(result.returncode))
    if isinstance(res, dict) and len(res) == 2:
        if list(res.keys()) == ["status", "message"]:
            if (res["status"] == "OK" and res["message"] == "You are successfully logged out."):    # !! Already logged out
                print("PASSED", check_mark.decode("utf-8"))
        else:
            print("FAILED, wrong response data")
    elif str(type(res)) == "<class '_csv.reader'>":
        firstRow = next(res)
        if firstRow[0] == "status" and firstRow[1] == "message":
            print("PASSED", check_mark.decode("utf-8"))
        else:
            print("FAILED, wrong response data")
    else:
        print("FAILED, wrong response type (expected 'dict', got '" + type(res)[8:-2] + "')")

    return

def run_healthcheck(username, form): # (username, password, form):
    # run_login(username, password, form, False)
    result = subprocess.run(['python', 'cli.py', 'healthcheck', '--format', form], capture_output=True)
    # response = json.loads(result.stdout)
    # print("=====")
    # print(list(result.stdout.decode()))
    # print("=====")

    if result.returncode != 0:
        raise Exception('Healthcheck failed with return code {}'.format(result.returncode))

    if form == "json":
        res = json.loads(result.stdout.decode('utf-8'))
    else:
        # res = csv.reader(result.stdout.decode()) # TEMPORARY UNTIL CSV BUG FIXED
        # res = pd.read_csv(result.stdout.decode('utf-8'), sep=",", header=None)
        # print(res)

        # csv_reader = csv.reader(result.stdout.decode('utf-8').splitlines())
        # for row in csv_reader:
        #     print(row)
        csv_string = result.stdout.decode('utf-8')
        lines = csv_string.splitlines(False)
        reader = csv.reader(lines)
        res = list(reader)
        res = [x for x in res if x]
        # print("RES:\n", res)
        # print("CSV CONVERTED")

    # print("RES:", res)

    if isinstance(res, dict) and len(res) == 2:
        if list(res.keys()) == ["status", "dbconnection"]:
            # print(">>> HERE <<<")
            # print(res)
            if res["status"] == "OK" and res["dbconnection"] == "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority" and username == "TheUltraSuperAdmin":
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        elif list(res.keys()) == ["status", "message"]:
            if res["status"] == "failed" and res["message"] == "User unauthorized to continue!" and (username == "adminTestJson" or username == "adminTestCsv" or username == "userTestJson" or username == "userTestCsv"):
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")
    elif isinstance(res, list) or len(res) == 4:
        if res[0][0] == "status" and res[0][1] == "dbconnection":
            if res[1][0] == "OK" and res[1][1] == "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority":
                if username == "TheUltraSuperAdmin":
                    print("PASSED", check_mark.decode("utf-8"))
                else:
                    print("FAILED, wrong response data")
        elif res[0][0] == "status" and res[0][1] == "message":
            if res[1][0] == "failed" and res[1][1] == "User unauthorized to continue!":
                if username == "adminTestJson" or username == "adminTestCsv" or username == "userTestJson" or username == "userTestCsv":
                    print("PASSED", check_mark.decode("utf-8"))
                else:
                    print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")
    else:
        print("FAILED, wrong response type (expected 'dict', got '" + type(res)[8:-2] + "')")

    return

# NOT DONE!!!
def run_resetall():
    # result = subprocess.run(['python', 'cli.py', 'resetall', '--format', 'json'], capture_output=True)
    # # response = json.loads(result.stdout)
    # print("=====")
    # print(result.stdout.decode())
    # print("=====")

    if result.returncode != 0:
        raise Exception('Healthcheck failed with return code {}'.format(result.returncode))

    # check for the expected status code
    status_code = response.get('status_code')
    if status_code != 200:
        raise Exception('Healthcheck failed with status code {}'.format(status_code))

    # check for the expected response format
    content_type = response.get('Content-Type')
    if content_type != 'application/json':
        raise Exception('Healthcheck failed with content type {}'.format(content_type))

    # check for the expected JSON response
    json_response = response.get('json_response')
    if not json_response:
        raise Exception('Healthcheck failed with missing JSON response')

    # Add additional checks for the JSON response if needed
    # ...
    return

def run_questionnaire_upd(username, source, form): #(username, password, source, form):
    # run_login(username, password, form, False)
    result = subprocess.run(['python', 'cli.py', 'questionnaire_upd', '--source', source, '--format', form], capture_output=True)

    if result.returncode != 0:
        raise Exception('Questionnaire_upd failed with return code {}'.format(result.returncode))

    if form == "json":
        res = json.loads(result.stdout.decode('utf-8'))
    else:
        # res = json.loads(result.stdout.decode('utf-8')) # TEMPORARY UNTIL CSV BUG FIXED        
        # csv_reader = csv.reader(result.stdout.decode('utf-8').splitlines())
        # for row in csv_reader:
        #     print(row)
        csv_string = result.stdout.decode('utf-8')
        lines = csv_string.splitlines(False)
        reader = csv.reader(lines)
        res = list(reader)
        res = [x for x in res if x]

    if isinstance(res, dict) and len(res) == 2:
        if list(res.keys()) == ["status", "dbconnection"]:
            if res["status"] == "OK" and (username == "adminTestJson" or username == "adminTestCsv"):
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        elif list(res.keys()) == ["status", "message"]:
            if res["status"] == "failed" and res["message"] == "User unauthorized to continue!" and (username == "TheUltraSuperAdmin" or username == "userTestJson" or username == "userTestCsv"):
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")
    elif isinstance(res, list) or len(res) == 4:
        if res[0][0] == "status" and res[0][1] == "dbconnection":
            if res[1][0] == "OK" and res[1][1] == "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority":
                if username == "adminTestJson" or username == "adminTestCsv":
                    print("PASSED", check_mark.decode("utf-8"))
                else:
                    print("FAILED, wrong response data")
        elif res[0][0] == "status" and res[0][1] == "message":
            if res[1][0] == "failed" and res[1][1] == "User unauthorized to continue!":
                if username == "TheUltraSuperAdmin" or username == "userTestJson" or username == "userTestCsv":
                    print("PASSED", check_mark.decode("utf-8"))
                else:
                    print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")
    else:
        print("FAILED, wrong response type (expected 'dict', got '" + type(res)[8:-2] + "')")

    return

def run_doanswer(questionnaire_id, question_id, session_id, option_id, username, password, form):
    run_login(username, password, form, False)
    result = subprocess.run(['python', 'cli.py', 'doanswer', '--questionnaire_id', questionnaire_id, '--question_id', question_id,
                             '--session_id', session_id, '--option_id', option_id, '--format', form], capture_output=True)
    # response = json.loads(result.stdout)
    # print("=====")
    # print(list(result.stdout.decode()))
    # print("=====")

    if result.returncode != 0:
        raise Exception('Healthcheck failed with return code {}'.format(result.returncode))

    if form == "json":
        res = json.loads(result.stdout.decode('utf-8'))
    else:
        # res = csv.reader(result.stdout.decode()) # TEMPORARY UNTIL CSV BUG FIXED
        # res = pd.read_csv(result.stdout.decode('utf-8'), sep=",", header=None)
        # print(res)

        # csv_reader = csv.reader(result.stdout.decode('utf-8').splitlines()) 
        # for row in csv_reader:
        #     print(row)
        csv_string = result.stdout.decode('utf-8')
        lines = csv_string.splitlines(False)
        reader = csv.reader(lines)
        res = list(reader)
        res = [x for x in res if x]
        # print("RES:\n", res)
        # print("CSV CONVERTED")

    # NOT READY YET
    if isinstance(res, dict) and len(res) == 2:
        if list(res.keys()) == ["status", "dbconnection"]:
            if res["status"] == "OK" and res["dbconnection"] == "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority" and username == "TheUltraSuperAdmin":
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        elif list(res.keys()) == ["status", "message"]:
            if res["status"] == "failed" and res["message"] == "User unauthorized to continue!" and username == "jimv":
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")
    elif isinstance(res, list) or len(res) == 4:
        if res[0][0] == "status" and res[0][1] == "dbconnection":
            if res[1][0] == "OK" and res[1][1] == "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority":
                if username == "TheUltraSuperAdmin":
                    print("PASSED", check_mark.decode("utf-8"))
                else:
                    print("FAILED, wrong response data")
        elif res[0][0] == "status" and res[0][1] == "message":
            if res[1][0] == "failed" and res[1][1] == "User unauthorized to continue!":
                if username == "jimv":
                    print("PASSED", check_mark.decode("utf-8"))
                else:
                    print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")
    else:
        print("FAILED, wrong response type (expected 'dict', got '" + type(res)[8:-2] + "')")

    return

def run_usermod(role, username, password, form):
    result = subprocess.run(['python', 'cli.py', 'admin', '--usermod', role, '--username', username, '--passw', password, '--format', form], capture_output=True)
    # response = json.loads(result.stdout)
    # print(result.stdout.decode('utf-8')+"\n====================")
    # print(">>> HERE <<<")
    # print(result.stdout.decode())
    if result.returncode != 0:
        raise Exception('usermod failed with return code {}'.format(result.returncode))

    if form == "json":
        # print(result.stdout.decode('utf-8'))
        res = json.loads(result.stdout.decode('utf-8'))

        keys = list(res.keys())
        if keys == ["status"]:
            if res["status"] == "OK" and (username == "adminTestJson" or username == "userTestJson"):
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        elif keys == ["status", "message"]:
            if res["status"] == "failed" and res["message"] == "Username taken! Please provide a new username." and (username == "existingAdminTest" or username == "existingUserTest"):
                print("PASSED", check_mark.decode("utf-8"))
            elif res["status"] == "failed" and res["message"] == "Invalid input data. A password must have at least 8 characters" and len(password):
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")

    elif form == "csv":
        csv_string = result.stdout.decode('utf-8')
        lines = csv_string.splitlines(False)
        reader = csv.reader(lines)
        res = list(reader)
        res = [x for x in res if x]

        if len(res) == 2:
            if res[0][0] == "status" and res[1][0] == "OK" and (username == "adminTestCsv" or username == "userTestCsv"):
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        elif len(res) == 4:
            if res[0][0] == "status" and res[1][0] == "failed" and res[1][0] == "message" and res[1][1] == "Username taken! Please provide a new username." and (username == "existingAdminTest" or username == "existingUserTest"):
                print("PASSED", check_mark.decode("utf-8"))
            else:
                print("FAILED, wrong response data")
        else:
            print("FAILED, wrong response data")
    else:
        print("FAILED, wrong input data")
    
    # print("TYPE =", type(res))
    # if str(type(res)) == "<class '_csv.reader'>":
    #     print("GOOD")

    # if isinstance(res, dict) and len(res) == 2:
    #     if list(res.keys()) == ["status", "dbconnection"]:
    #         if res["status"] == "OK" and username == "jimv":
    #             print("PASSED", check_mark.decode("utf-8"))
    #         else:
    #             print("FAILED, wrong response data")
    #     elif list(res.keys()) == ["status", "message"]:
    #         if res["status"] == "failed" and res["message"] == "User unauthorized to continue!" and username == "TheUltraSuperAdmin":
    #             print("PASSED", check_mark.decode("utf-8"))
    #         else:
    #             print("FAILED, wrong response data")
    #     else:
    #         print("FAILED, wrong response data")
    # elif isinstance(res, list) or len(res) == 4:
    #     if res[0][0] == "status" and res[0][1] == "dbconnection":
    #         if res[1][0] == "OK" and res[1][1] == "mongodb+srv://jimv:<password>@cluster0.oav8j31.mongodb.net/?retryWrites=true&w=majority":
    #             if username == "TheUltraSuperAdmin":
    #                 print("PASSED", check_mark.decode("utf-8"))
    #             else:
    #                 print("FAILED, wrong response data")
    #     elif res[0][0] == "status" and res[0][1] == "message":
    #         if res[1][0] == "failed" and res[1][1] == "User unauthorized to continue!":
    #             if username == "jimv":
    #                 print("PASSED", check_mark.decode("utf-8"))
    #             else:
    #                 print("FAILED, wrong response data")
    #     else:
    #         print("FAILED, wrong response data")
    # else:
    #     print("FAILED, wrong response type (expected 'dict', got '" + type(res)[8:-2] + "')")

    return

if __name__ == '__main__':
    usernamess = ['TheUltraSuperAdmin', 'jimv']
    usernames = {"adminJson" : ["adminTestJson", "adminTestJson123"],
                 "adminCsv"  : ["adminTestCsv", "adminTestCsv123"],
                 "userJson"  : ["userTestJson", "userTestJson123"],
                 "userCsv"   : ["userTestCsv", "userTestCsv123"]}
    passwords = ['the-password-is-secret', '123456789']
    sources = ['jtest.json']
    forms = ['json', 'csv']
    i = 1
    
    # ====================================================================================
    # ================================== START TESTING ===================================
    # ====================================================================================

    # First login with superadmin to create the test users
    print("Test", str(i).ljust(2, ' ').rjust(2, ' '), end = " - ")
    print("Login with super admin test (format = " + forms[0] + ")", end = ":\t\t\t\t\t")
    run_login(usernames["adminJson"][0], usernames["adminJson"][1], forms[0], True)
    i += 1

    print("Test", str(i).ljust(2, ' ').rjust(2, ' '), end = " - ")
    print("Logout with super admin test (format = " + forms[0] + ")", end = ":\t\t\t\t\t")
    run_logout(forms[0])
    i += 1

    print("Test", str(i).ljust(2, ' ').rjust(2, ' '), end = " - ")
    print("Login with super admin test (format = " + forms[1] + ")", end = ":\t\t\t\t\t")
    run_login(usernames["adminJson"][0], usernames["adminJson"][1], forms[1], True)
    i += 1

    print("Test", str(i).ljust(2, ' ').rjust(2, ' '), end = " - ")
    print("Logout with super admin test (format = " + forms[1] + ")", end = ":\t\t\t\t\t")
    run_logout(forms[0])
    i += 1

    run_login("TheUltraSuperAdmin", "the-password-is-secret", forms[0], False)

    # Healthcheck test
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Healthcheck test with super admin (should be authorized) (format = " + forms[0] + ")", end = ":\t")
    run_healthcheck("TheUltraSuperAdmin", forms[0])
    i += 1

    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Healthcheck test with super admin (should be authorized) (format = " + forms[1] + ")", end = ":\t")
    run_healthcheck("TheUltraSuperAdmin", forms[1])
    i += 1

    print('================================ Super admin Testing completed! ================================')


    # Create admin with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Create admin test (format = " + forms[0] + ")", end = ":\t\t\t\t\t\t")
    run_usermod("admin", usernames["adminJson"][0], usernames["adminJson"][1], forms[0])
    i += 1
    
    # Create admin with csv format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Create admin test (format = " + forms[1] + ")", end = ":\t\t\t\t\t\t")
    run_usermod("admin", usernames["adminCsv"][0], usernames["adminCsv"][1], forms[1])
    i += 1

    # Create user with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Create user test (format = " + forms[0] + ")", end = ":\t\t\t\t\t\t")
    run_usermod("user", usernames["userJson"][0], usernames["userJson"][1], forms[0])
    i += 1

    # Create user with csv format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Create user test (format = " + forms[1] + ")", end = ":\t\t\t\t\t\t")
    run_usermod("user", usernames["userCsv"][0], usernames["userCsv"][1], forms[1])
    i += 1
    print('============================ Creating Admin/User Testing completed! ============================')

    # ====================================================================================
    # At this point 2 admins and 2 users are created. We will use them for further testing
    # ====================================================================================

    # ======================= Admin Testing with json format only ========================

    # Login admin with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Login test with admin (format = " + forms[0] + ")", end = ":\t\t\t\t\t")
    run_login(usernames["adminJson"][0], usernames["adminJson"][1], forms[0], True)
    i += 1

    # Logout admin with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Logout test with admin (format = " + forms[0] + ")", end = ":\t\t\t\t\t")
    run_logout(forms[1])
    i += 1

    run_login(usernames["adminJson"][0], usernames["adminJson"][1], forms[0], False)

    # Healthcheck admin with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Healthcheck test with admin (should not be authorized) (format = " + forms[0] + ")", end = ":\t")
    run_healthcheck(usernames["adminJson"][0], forms[0])
    i += 1

    # Questionnaire_upd admin with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Questionnaire_upd test with admin (should be authorized) (format = " + forms[0] + ")", end = ":\t")
    run_questionnaire_upd(usernames["adminJson"][0], "jtest.txt", forms[0])
    i += 1

    print("=========================== Admin Testing with json format Completed  ==========================")

    # =====================================================================================
    # ======================== Admin Testing with csv format only  ========================

    # Login admin with csv format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Login test with admin (format = " + forms[1] + ")", end = ":\t\t\t\t\t\t")
    run_login(usernames["adminCsv"][0], usernames["adminCsv"][1], forms[1], True)
    i += 1

    # Logout admin with csv format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Logout test with admin (format = " + forms[1] + ")", end = ":\t\t\t\t\t")
    run_logout(forms[1])
    i += 1

    run_login(usernames["adminCsv"][0], usernames["adminCsv"][1], forms[1], False)

    # Healthcheck admin with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Healthcheck test with admin (should not be authorized) (format = " + forms[1] + ")", end = ":\t")
    run_healthcheck(usernames["adminCsv"][0], forms[1])
    i += 1

    # Questionnaire_upd admin with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Questionnaire_upd test with admin (should be authorized) (format = " + forms[1] + ")", end = ":\t")
    run_questionnaire_upd(usernames["adminCsv"][0], "jtest.txt", forms[1])
    i += 1

    print("=========================== Admin Testing with csv format Completed  ===========================")

    # =====================================================================================
    # ======================== User Testing with json format only =========================

    # Login user with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Login test with user (format = " + forms[0] + ")", end = ":\t\t\t\t\t\t")
    run_login(usernames["userJson"][0], usernames["userJson"][1], forms[0], True)
    i += 1

    # Logout user with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Logout test with user (format = " + forms[0] + ")", end = ":\t\t\t\t\t")
    run_logout(forms[1])
    i += 1

    run_login(usernames["userJson"][0], usernames["userJson"][1], forms[0], False)

    # Healthcheck user with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Healthcheck test with user (should not be authorized) (format = " + forms[0] + ")", end = ":\t")
    run_healthcheck(usernames["userJson"][0], forms[0])
    i += 1

    # Questionnaire_upd user with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Questionnaire_upd test with user (should not be authorized) (format = " + forms[0] + ")", end = ":\t")
    run_questionnaire_upd(usernames["userJson"][0], "jtest.txt", forms[0])
    i += 1

    print("=========================== user Testing with json format Completed  ===========================")

    # =====================================================================================
    # ========================= User Testing with csv format only  ========================

    # Login user with csv format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Login test with user (format = " + forms[1] + ")", end = ":\t\t\t\t\t\t")
    run_login(usernames["userCsv"][0], usernames["userCsv"][1], forms[1], True)
    i += 1

    # Logout user with csv format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Logout test with user (format = " + forms[1] + ")", end = ":\t\t\t\t\t\t")
    run_logout(forms[1])
    i += 1

    run_login(usernames["userCsv"][0], usernames["userCsv"][1], forms[1], False)

    # Healthcheck user with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Healthcheck test with user (should not be authorized) (format = " + forms[1] + ")", end = ":\t\t")
    run_healthcheck(usernames["userCsv"][0], forms[1])
    i += 1

    # Questionnaire_upd user with json format
    print("Test", str(i).ljust(2, ' '), end = " - ")
    print("Questionnaire_upd test with user (should not be authorized) (format = " + forms[1] + ")", end = ":\t")
    run_questionnaire_upd(usernames["userCsv"][0], "jtest.txt", forms[1])
    i += 1

    print("============================ user Testing with csv format Completed  ===========================")

    # =====================================================================================

    # for i in range(len(usernames)):
    #     for form in forms:
    #         print('Login test ' + str(i + 1) + " (format = " + form + ")", end = ":\t\t\t")
    #         run_login(usernames[i], passwords[i], form, True)
    # print('=============== Login Testing completed! ===============')

    # for i in range(len(usernames)):
    #     for form in forms:
    #         print('Logout test ' + str(i + 1) + " (format = " + form + ")", end = ":\t\t\t")
    #         run_logout(usernames[i], passwords[i], form)
    # print('=============== Logout Testing completed! ==============')

    # for i in range(len(usernames)):
    #     for form in forms:
    #         print('Healthcheck test ' + str(i + 1) + " (format = " + form + ")", end = ":\t\t")
    #         run_healthcheck(usernames[i], passwords[i], form)
    # print('============ Healthcheck Testing completed! ============')
    
    # for i in range(len(usernames)):
    #     for j in range(len(sources)):
    #         for form in forms:
    #             print('Questionnaire_upd test ' + str(i*len(sources) + j + 1) + " (format = " + form + ")", end = ":\t")
    #             run_questionnaire_upd(usernames[i], passwords[i], sources[j], form)
    # print('======== Questionnaire_upd Testing completed! ========')

    

    try:
        print("e")

    except Exception as e:
        print('Healthcheck failed: {}'.format(e))