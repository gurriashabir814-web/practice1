# Given marks
marks = [88, 45, 92, 67, 30, 75]
passed_count = len([m for m in marks if m >= 50])
print(f"Passed: {passed_count}")
avg = sum(marks) / len(marks)
print(f"Average: {avg:.1f}")
print(f"Highest: {max(marks)} Lowest: {min(marks)}")