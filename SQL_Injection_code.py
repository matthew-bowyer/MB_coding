"""
This script simulates a passwordless login system.
It reads the student's email address and student ID from a text file
and verifies these credentials against a database. If a matching record is
found, the script logs the student into the system by displaying a welcome
message.

- Functionality has been implemented to
login without requiring the Student ID.
- The details of the student with the email address
  wimbeldon@strange.com are retreived.
"""


from create_database_file import get_sql_cursor

usage_message = '''--------------------------------------------------
Welcome to our logging in system.
We use the state-of-the-art passwordless login.

To log into your profile, simply enter into input2.txt the following details:
"email_address
student_id"

If you know your student ID, you will be logged into the system.
For an example, please look at input2_example.txt.
--------------------------------------------------
'''

print(usage_message)

# Create database and get cursor
cursor = get_sql_cursor()

with open("input2.txt", encoding='utf-8') as in_file:
    # Read input from input2.txt
    email_addr, stu_id = in_file.read().split("\n")
    print(f"Logging on for account {email_addr} . . .")

    # Format a string for the SQL SELECT statement
    execute_str = f"SELECT * FROM Student WHERE email = '{email_addr}'\
        AND student_id = '{stu_id}';"
    print(execute_str)

    # Run statement and print results
    results = cursor.execute(execute_str)
    result_data = cursor.fetchall()

    print(f"Found {len(result_data)} entries.")

    if len(result_data) == 1:
        _, firstname, lastname, _, _ = result_data[0]
        print(f"Welcome {firstname} {lastname}.")
    else:
        print("Login Unsuccessful.")
