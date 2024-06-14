def absent(present: int, total:int) -> list[str]:
    total += 1
    percentage = (present / total) * 100
    result = [str(present) + '\n', str(total) + '\n', str(percentage) + '\n']
    return result

def not_absent(present: int, total: int) -> list[str]:
    present += 1
    total += 1
    percentage = (present / total) * 100
    result = [str(present) + '\n', str(total) + '\n', str(percentage) + '\n']
    return result

def write_result(result: list[str]) -> None:
    File = open('attendance.txt', 'w')
    File.writelines(result)
    File.close()

def update_result() -> None:
    file = open('attendance.txt', 'r')
    data = file.readlines()
    present, total = int(data[0].strip()), int(data[1].strip())
    today = input("Were you present today? (yes/no): ").strip().lower()
    if today == 'yes':
        result_set = not_absent(present, total)
    elif today == 'no':
        result_set = absent(present, total)
    file.close()

    write_result(result_set)
    print("Attendance Updated")

def check_attendance() -> None:
    file = open('attendance.txt', 'r')
    data = file.readlines()
    present, total, percentage = int(data[0].strip()), int(data[1].strip()), float(data[2].strip())
    print(f'Present:        {present} days')
    print(f'Total:          {total} days')
    print(f'Percentage:     {percentage}%')

def main() -> None:
    while True:
        print("1. Update attendance ")
        print("2. Check attendance")
        print("3. Exit")
        choice: str = input("Enter a choice: ")
        if choice == '1':
            update_result()
            check_attendance()
        elif choice == '2':
            check_attendance()
        elif choice == '3':
            print("Closing program...")
            break
        else:
            print("Invalid input, try again...")
if __name__ == '__main__':
    main()