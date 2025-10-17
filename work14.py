d = {'Matt': 'D', 'John': 'B', 'Sarah': 'C', 'Emily': 'A', 'David': 'B', 'İsmet':'AA'}

def find_grades(grades, students):
    ans_list = []
    for student, grade in grades.items():
        if student in students:
            ans_list.append(grade)
    return ans_list



def find_grades2(grades, students):
    ans_list = []
    for student in students:
        if student in grades:
            grade = grades[student]
            ans_list.append(grade)
    return ans_list

def find_grades3(grades, students):
    students_set = set(students)
    return [grade for student, grade in grades.items() if student in students_set]


print(find_grades2(d, ['İsmet']))

'''
Great question, Mike 👌
Let’s break it down carefully — these two functions look similar but differ **in iteration order and efficiency**, especially as data grows.

---

### 🧩 The Code

```python
d = {'Matt': 'D', 'John': 'B', 'Sarah': 'C', 'Emily': 'A', 'David': 'B', 'İsmet':'AA'}

def find_grades(grades, students):
    ans_list = []
    for student, grade in grades.items():
        if student in students:
            ans_list.append(grade)
    return ans_list

def find_grades2(grades, students):
    ans_list = []
    for student in students:
        if student in grades:
            grade = grades[student]
            ans_list.append(grade)
    return ans_list
```

---

### ⚙️ What Each Function Does

| Function       | Iteration direction                          | Checks membership in                                     |
| -------------- | -------------------------------------------- | -------------------------------------------------------- |
| `find_grades`  | Iterates over all **grades dictionary keys** | Checks if each key (student) is in the **students list** |
| `find_grades2` | Iterates over **students list**              | Checks if each student is in the **grades dictionary**   |

---

### 📈 Time Complexity (Big O)

#### 1️⃣ `find_grades`

```python
for student, grade in grades.items():  # O(n)
    if student in students:            # O(m) for list membership
```

If `students` is a **list**, then `student in students` is **O(m)**.
So total:

> 🕒 **O(n × m)**
> (where `n` = number of students in `grades`, `m` = number of students in `students`)

If `students` were a **set**, then membership would be **O(1)** → total becomes **O(n)**.

---

#### 2️⃣ `find_grades2`

```python
for student in students:   # O(m)
    if student in grades:  # O(1) because dict lookup
```

Total:

> 🕒 **O(m)**

This is **faster**, especially when `students` is smaller than `grades`.

---

### 💡 Example

Imagine:

* 10,000 students in `grades`
* 10 students in `students`

| Function       | Operations                   | Expected Speed |
| -------------- | ---------------------------- | -------------- |
| `find_grades`  | 10,000 × 10 = 100,000 checks | 🚫 slower      |
| `find_grades2` | 10 + small lookups           | ⚡ much faster  |

---

### 💬 Space Complexity

Both use an additional list (`ans_list`) proportional to the result count:

> **O(k)**, where `k` = number of matches.

No significant difference here.

---

### 🧠 Usage Recommendation

✅ **Use `find_grades2`** most of the time:

* Efficient (O(m))
* Clean logic: “for each student we care about, get their grade”
* Works best when `students` is a subset or small list

---

### 🧪 Tip for Maximum Efficiency

If `students` is a list and you expect many lookups, convert it to a set first:

```python
def find_grades3(grades, students):
    students_set = set(students)
    return [grade for student, grade in grades.items() if student in students_set]
```

This version:

> 🕒 **O(n)** time, very efficient for large data.

---

### 🧾 Summary Table

| Function       | Time Complexity                           | When Fastest              | Notes                       |
| -------------- | ----------------------------------------- | ------------------------- | --------------------------- |
| `find_grades`  | O(n × m) (or O(n) if `students` is a set) | Small lists               | Iterates through all grades |
| `find_grades2` | O(m)                                      | When few students queried | Best overall                |
| `find_grades3` | O(n)                                      | When `students` large     | Use set for speed           |

---

**Conclusion:**
➡️ `find_grades2` is generally **more efficient** and **scales better**.
➡️ `find_grades3` (using a set) is the **best universal pattern** for large data.

'''