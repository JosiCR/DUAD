const student = {
    name: "John Doe",
    grades: [
        { name: "math", grade: 80 },
        { name: "science", grade: 100 },
        { name: "history", grade: 60 },
        { name: "PE", grade: 90 },
        { name: "music", grade: 98 }
    ]
};

let sum = 0;

let highest = 0;
let highestSubject = "";

let lowest = student.grades[0].grade;
let lowestSubject = student.grades[0].name;

for (let i = 0; i < student.grades.length; i++) {
    const subject = student.grades[i];

    sum += subject.grade;

    if (subject.grade > highest) {
    highest = subject.grade;
    highestSubject = subject.name;
    }

    if (subject.grade < lowest) {
    lowest = subject.grade;
    lowestSubject = subject.name;
    }
}

const result = {
    name: student.name,
    gradeAvg: sum / student.grades.length,
    highestGrade: highestSubject,
    lowestGrade: lowestSubject
};

console.log(result);
