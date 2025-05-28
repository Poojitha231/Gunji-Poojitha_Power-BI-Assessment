university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#Q1: Print all student names and their majors
for student in university_data.values():
    print(f"{student['name']} - {student['major']}")

#Q2: Average score per course per student
for sid,info in university_data.items():
    print(f"{info['name']} {sid}")
    for course,scores in info['courses'].items():
               avg_score = sum(scores.values()) / len(scores)
               print(f"  {course}: {avg_score:.2f}")

#Q3: Find students who scored >90 in final of Python101
for sid,info in university_data.items():
      courses = info["courses"]
      if "Python101" in courses and courses["Python101"]["final"] > 90:
            print(f"Student [{info['name']}] {sid} Scored {courses["Python101"]["final"]} in final of Python101")

#Add new course AI101 for student S101 
university_data["S101"]["courses"].update({"AI101":{"midterm": 75, "final": 82, "project": 78}})
print(university_data['S101'])
#university_data["S101"]["courses"]["AI101"] = {"midterm": 90, "final": 92, "project": 95}

# Print average for each course
for std_id,std_info in university_data.items():
    print(std_id,std_info)
    print("name of the student is ",std_info["name"])
    for course,course_data in std_info["courses"].items():
        average = sum(course_data.values()) / len(course_data)
        print("Average:",course, average)
    print()

