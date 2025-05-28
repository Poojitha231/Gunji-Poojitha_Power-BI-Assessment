#-------------------------Assignment----------------------------------
# 1. create a class in the name of department which has dept name, id, hod, and location. through the constructor initialize the attributes, crerate a method to disp the dept info.
# disp the total depts in the organization.
# 2. get the input from the user, the number of depts, create a list or dictionary to store the number of depts. use for loop to get the dept information. Add dept info to the list or dictionary
# Modify the existing code display all dept info to the list
# 3. Search dept by dept id, user will input the dept id- show details of that dept. 
# add a function to search dept by name.
class Department:
    department_count = 0  # class variable to count departments

    def __init__(self, dept_name, dept_id, hod, location):
        self.dept_name = dept_name
        self.dept_id = dept_id
        self.hod = hod
        self.location = location
        Department.department_count += 1

    def get_department_info(self):
        # Return department details as a dictionary
        return {
            "Department Name": self.dept_name,
            "ID": self.dept_id,
            "HOD": self.hod,
            "Location": self.location
        }

    def display_location(self):
        print(f"{self.dept_name} department is located at {self.location}")

    @classmethod
    def get_total_departments(cls):
        return cls.department_count


# List to store department info
department_info_list = []

# Get number of departments from user
num_depts = int(input("Enter the number of departments: "))

# Loop to get department info
for i in range(num_depts):
    print(f"\nEnter details for Department {i + 1}:")
    name = input("Enter Department Name: ")
    dept_id = input("Enter Department ID: ")
    hod = input("Enter HOD Name: ")
    location = input("Enter Department Location: ")

    # Create object and store info as dictionary
    dept = Department(name, dept_id, hod, location)
    department_info_list.append(dept.get_department_info())

# Display all department info from the list, nicely formatted
for dept_info in department_info_list:
    print(f"Department Name : {dept_info['Department Name']}")
    print(f"ID              : {dept_info['ID']}")
    print(f"HOD             : {dept_info['HOD']}")
    print(f"Location        : {dept_info['Location']}\n")

# Show total number of departments
print(f"Total Departments in the Organization: {Department.get_total_departments()}")


#Search by Department ID
def search_by_id(dept_list, search_id):
    for dept in dept_list:
        if dept['ID'].lower() == search_id.lower():
            print("\nDepartment Found:")
            print(f"Department Name : {dept['Department Name']}")
            print(f"ID              : {dept['ID']}")
            print(f"HOD             : {dept['HOD']}")
            print(f"Location        : {dept['Location']}")
            return
    print("Department not found.")


#Search by Department Name
def search_by_name(dept_list, search_name):
    for dept in dept_list:
        if dept['Department Name'].lower() == search_name.lower():
            print("\nDepartment Found:")
            print(f"Department Name : {dept['Department Name']}")
            print(f"ID              : {dept['ID']}")
            print(f"HOD             : {dept['HOD']}")
            print(f"Location        : {dept['Location']}")
            return
    print("Department not found.")


# Search operations
search_id_input = input("\nEnter Department ID to search: ")
search_by_id(department_info_list, search_id_input)

search_name_input = input("\nEnter Department Name to search: ")
search_by_name(department_info_list, search_name_input)

