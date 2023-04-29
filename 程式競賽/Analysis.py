n, m = map(int, input().split())

most_progress = -1
most_progress_student = 1

most_concern = -1
most_concern_student = 1

for i in range(1, n + 1):
    scores = list(map(int, input().split()))
    progress = 0
    concern = 0
    for j in range(1, m):
        if scores[j] > scores[j - 1]:
            progress += scores[j] - scores[j - 1]
        else:
            concern += scores[j - 1] - scores[j]
    if progress > most_progress:
        most_progress = progress
        most_progress_student = i
    if concern > most_concern:
        most_concern = concern
        most_concern_student = i

print(most_progress_student)
print(most_concern_student)
