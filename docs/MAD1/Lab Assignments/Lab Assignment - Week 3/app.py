import sys
import csv
from jinja2 import Template
import matplotlib.pyplot as plt

if sys.argv[1] == "-c":
    id = sys.argv[2]
    arg_type = "course"
elif sys.argv[1] == "-s":
    id = sys.argv[2]
    arg_type = "student"


def get_student_data(student_id):
    student_data = []
    with open("./data.csv") as file:
        csvreader = csv.reader(file)
        next(csvreader)  # ignore header
        for row in csvreader:
            if row[0].strip() == student_id:
                student_data.append(row)
        return student_data


def get_course_data(course_id):
    course_data = []
    with open("./data.csv") as file:
        csvreader = csv.reader(file)
        next(csvreader)  # ignore header
        for row in csvreader:
            if row[1].strip() == course_id:
                course_data.append(int(row[2]))
        return course_data


def exists(id_type, id):
    with open("./data.csv") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            if id_type == "student":
                if row[0].strip() == id:
                    return "student"
            elif id_type == "course":
                if row[1].strip() == id:
                    return "course"
        return False


if exists(arg_type, id) == "student":
    student_data = get_student_data(id)
    total_marks = sum([int(row[2]) for row in student_data])
    template = Template(
        """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
  </head>
  <body>
  <h1>Student Details</h1>
      <table>
          <tr>
              <th>Student ID</th>
              <th>Course ID<th>
              <th<Marks</th>
          </tr>
          {% for row in student_data %}
          <tr>
              <td>{{ row[0] }}</td>
              <td>{{ row[1] }}</td>
              <td>{{ row[2] }}</td>
          </tr>
          {% endfor %}
          <tr>
              <td colspan="2">Total Marks</td>
              <td>{{ total_marks }}</td>
          </tr>
      </table>
  </body>
</html>
"""
    )
    output = template.render(student_data=student_data, total_marks=total_marks)


elif exists(arg_type, id) == "course":
    course_data = get_course_data(id)
    max_marks = max(course_data)
    mean_marks = sum(course_data) / len(course_data)

    histogram = plt.hist(course_data)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("histogram.png")

    template = Template(
        """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
  </head>
  <body>
  <h1>Course Details</h1>
      <table>
          <tr>
              <th>Average Marks</th>
              <th>Maximum Marks</th>
          </tr>
          <tr>
              <td>{{ mean_marks }}</td>
              <td>{{ max_marks }}</td>
          </tr>
      </table>
      <img src="./histogram.png"/>
  </body>
</html>
"""
    )
    output = template.render(mean_marks=mean_marks, max_marks=max_marks)

else:
    output = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
  </head>
  <body>
      <h1>Wrong Inputs</h1>
      <p>Something Went Wrong</p>
  </body>
</html>
"""

with open("output.html", "w") as outputfile:
    outputfile.write(output)
