from enum import IntEnum

class ExerciseType(IntEnum):
    Running = 1
    swimming = 2
    cycling = 3
def calculate_calories(exr_type: ExerciseType,  duration: int )->int:
    if exr_type == ExerciseType.Running:
        return duration*10
    elif exr_type == ExerciseType.swimming:
        return duration*6
    elif exr_type ==ExerciseType.cycling:
        return  duration*8
    return 0

def display_results(exr_type: ExerciseType, calories: int, duration: int):
    name = exr_type.name
    print(f"\n Exercise:{name}")
    print (f"Duration:{duration}minutes")
    print(f"calories burned:{calories} cal\n")
def main():
    while True:
        print("select exercise type:")
        print("1. Running")
        print("2. swimming")
        print("3. cycling")
        print("0. quit")
        try:
            choice = int(input("Your choice:"))
        except ValueError:
            print("Invalid input. please enter a number")
            continue
        if choice ==0:
            print("Invalid choice . Good bye!")
            break
        if choice not in [1,2,3]:
            print("choose between 0-3")
            continue
        try:
            duration = int(input("Enter duration in minutes: "))
            if duration <= 0:
                raise ValueError()
        except ValueError:
            print("Invalid duration. Please enter a positive number.")
            continue

        ex_type = ExerciseType(choice)
        calories = calculate_calories(ex_type, duration)
        display_results(ex_type, calories, duration)

if __name__ == "__main__":
    main()







