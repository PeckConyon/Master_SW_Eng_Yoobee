from database import create_user_table, create_course_table,create_user_course_table
from user_manager import add_user, view_users, search_user, delete_user, advanced_search,assign_course_to_user, search_user_courses
from course_manager import add_course

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Advanced Search")
    print("6. Add Course")
    print("7. Assign Course For User")
    print("8. Search courses of a User")
    print("9. Exit")

def main():
    create_user_table()
    create_course_table()
    create_user_course_table()
    
    while True:
        menu()
        choice = input("Select an option (1-9): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            user_id = int(input("Enter user ID to search: "))
            name = input("Enter name to search: ")
            result = advanced_search(user_id, name)
            print(result)
        elif choice == '6':
            course_name = input("Enter course name: ")
            units = int(input("Enter no of units: "))
            add_course(course_name, units)
        elif choice == '7':
            course_id = int(input("Enter course id: "))
            user_id = int(input("Enter user id: "))
            assign_course_to_user(user_id,course_id)
        elif choice == '8':
            course_id = int(input("Enter course id: "))
            user_name = input("Enter user name:")
            result = search_user_courses(course_id, user_name)
            print(result)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
