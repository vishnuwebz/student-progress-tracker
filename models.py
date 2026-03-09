# models.py
# Student class and GraduateStudent inheritance

class Student:
    def __init__(self, name, age, course, subjects, marks):
        """
        Constructor (__init__) runs when we create a new Student object.
        It initializes all the attributes for that object.
        :param name:
        :param age:
        :param course:
        :param subjects:
        :param marks:
        """
        self.name = name
        self.age = age
        self.course = course
        self.subjects = subjects # list of subject names
        self.marks = marks # list of marks

    def get_total(self):
        return sum(self.marks)

    def get_average(self):
        if not self.marks:
            return 0.0
        return self.get_total() / len(self.marks)

    def get_percentage(self):
        if not self.marks:
            return 0.0
        max_total = len(self.marks) * 100
        return (self.get_total() / max_total) * 100

    def get_grade(self):
        avg = self.get_average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def get_type_label(self):
        """Return a label for display (van be overridden in subclasses)."""
        return "Student"

    def to_dict(self):
        """Convert this Student object to a dict (for storage / printing)."""
        return {
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "subjects": self.subjects,
            "marks": self.marks,
            "total": self.get_total(),
            "average": self.get_average(),
            "percentage": self.get_percentage(),
            "grade": self.get_grade(),
            "type": self.get_type_label(),
            "extra": None, # placeholder for subclasses
        }

    @staticmethod
    def from_dict(data: dict):
        """Create a Student object from a dict."""
        type_value = data.get("type", "Student")
        if type_value == "Graduate":
            return GraduateStudent(
                name=data["name"],
                age=data["age"],
                course=data["courses"],
                subjects=data["subjects"],
                marks=data["marks"],
                thesis_title=data.get("extra", "") or "",
            )
        else:
            return Student(
                name=data["name"],
                age=data["age"],
                course=data["course"],
                subjects=data["subjects"],
                marks=data["marks"],
            )

class GraduateStudent(Student):
    """
    GraduateStudent inherits from Student and adds a thesis_title.
    """

    def __init__(self, name, age, course, subjects, marks, thesis_title):
        super().__init__(name, age, course, subjects, marks)
        self.thesis_title = thesis_title

    def get_type_label(self):
        #override to show different type
        return "Graduate"

    def to_dict(self):
        base = super().to_dict()
        base["extra"] = self.thesis_title
        return base