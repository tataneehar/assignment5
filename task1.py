students={"neehar":100,
          "suvarsha":90,
          "saharsh":80,
          "sahasra":79}
name=input("Enter the Student name: ")
try:
    print(f"{name}'s Marks : {students[name]}")
except KeyError:
    print("Student not found")