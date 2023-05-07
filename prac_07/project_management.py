"""
Project Management Program
Estimate: 15 hours
Exact: 20 hours
"""
import datetime
from project import Project

MENU = """- (L)oad Projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit"""
FILENAME = "projects"

def main():
    with open(f"{FILENAME}.txt", "r", newline='') as in_file:
        project_data = in_file.readlines()[1:]
        projects = put_data_in_list(project_data)
    print("Welcome to the Project Management Program")
    print(MENU)

    choice = input(">>> ").lower()
    while choice != "Q":
        if choice == "L":
            projects = load_project()
        elif choice == "S":
            save_project(projects)
        elif choice == "D":
            display_project(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            projects = add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        print(MENU)
        choice = input(">>> ").lower()
    save_data(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def put_data_in_list(project_data):
    projects = []
    for data in project_data:
        data = data.strip().split("\t")
        projects.append(Project(data[0], data[1], int(data[2]), float(data[3]), int(data[4])))
    return projects


def load_project():
    try:
        get_filename = input("Filename: ")
        with open(f"{get_filename}.txt", "r", newline='') as in_file:
            new_data = in_file.readlines()[1:]
            projects = put_data_in_list(new_data)
        print("Load complete")
    except FileNotFoundError:
        print("File is not found")


def save_project(projects):
    filename = input("Filename: ")
    with open(f"{filename}.txt", "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}"
                  f"\t{project.completion_percentage}", file=out_file)


def display_project(projects):
    incomplete_project = []
    completed_project = []
    for project in projects:
        if project.is_completed():
            incomplete_project.append(project)
        else:
            completed_project.append(project)
    print("Incomplete projects:")
    for project in incomplete_project:
        print(" ", project)
    print("Completed projects:")
    for project in completed_project:
        print(" ", project)



def get_date_elem(elem):
    return elem.start_date


def filter_projects_by_date(projects):
    input_date = input("Show projects that start after date (dd/mm/yy):")
    try:
        date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date. Please enter mm/dd/yyyy.")
        return

    filtered_projects = []
    for project in projects:
        if project.is_after_certain_time(date):
            filtered_projects.append(project)

    filtered_projects.sort(key=get_date_elem)
    print("Filtered projects:")
    for project in filtered_projects:
        print(" ", project)


def get_valid_completion_percentage(minimum, maximum):
    completion_percentage = int(input("New Percentage: "))
    while completion_percentage < minimum or completion_percentage > maximum:
        print("Invalid completion percentage")
        completion_percentage = int(input("Completion percentage: "))
    return completion_percentage


def add_new_project(projects):
    def valid_integer(prompt):
        is_valid_integer = False
        while not is_valid_integer:
            try:
                number = int(input(prompt))
                is_valid = True
                return number
            except ValueError:
                print("Invalid input, integer only")

    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))

    cost_estimate = float(input("Cost estimate: "))
    while cost_estimate < 0:
        print("Invalid input, must be more than $0")
        cost_estimate = float(valid_integer("Cost estimate: $"))

    completion_percentage = get_valid_completion_percentage(0, 100)
    projects.append(Project(name, datetime.datetime.strptime(start_date, "%d/%m/%Y").
                            date(), priority, cost_estimate, completion_percentage))
    return projects


def valid_project_index(projects):
    project_index = int(input("Project choice: "))
    while project_index < 0 or project_index >= len(projects):
        print("Invalid project number")
        project_index = int(input("Project choice: "))
    return project_index


def update_project(projects):
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_index = valid_project_index(projects)
    print(projects[project_index])

    completion_percentage = get_valid_completion_percentage(0, 100)
    projects[project_index].completion_percentage = completion_percentage
    try:
        new_priority = int(input("New Priority: "))
    except ValueError:
        return projects
    projects[project_index].priority = new_priority
    return projects


def save_data(filename, projects):
    with open(f"{filename}.txt", "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}"
                  f"\t{project.completion_percentage}", file=out_file)

main()