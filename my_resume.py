resume = {
    "name": "Anatolii Mikhov",
    "role": "Junior Frontend Developer",
    "summary": "Junior Frontend Developer with a half a year of commercial experience in a couple of freelance projects. Overall experience in programming - 5 years. Has completed a couple of Web Development courses. It started as a hobby and now I want to become a professional Frontend Developer. I’d like to find a friendly team where I can improve my skills. Interested in working with React library.",
    "experience": [
        {
            "employer": "Freelance",
            "period": "2021 – 2022",
            "details": "Developed a landing page for Yoga Tours from scratch. Technologies used: HTML, CSS, Javascript, JQuery, Bootstrap. Implemented a feature of placing orders in the existing web site for a building company. Technologies used: HTML, CSS, Javascript, Jquery.",
        }
    ],
    "education": [
        {"year": 2022, "details": "Udemy Web Developer 2022"},
        {"year": 2021, "details": "Udemy JavaScript + React full course"},
        {"year": 2018, "details": "GeeksForLess Inc. Linux and MySQL"},
        {
            "year": 2017,
            "details": "Web laboratory online IT school. Eight-week course of HTML, CSS and JavaScript",
        },
        {
            "year": 2016,
            "details": 'Center business technologies & computer training, Mykolaiv. "Web-master" (HTML, CSS, Graphics for the Web, Design of Web-sites, Elements and forms of the user interface)',
        },
    ],
    "contact": {
        "address_1": {
            "address": "Pulyuya St 15a, 80, Ivano-Frankivsk",
            "phone": "+380 97 512 0586",
            "email": "anatoli.mihov@gmail.com",
        },
        "address_2": {
            "address": "Dennmark, Aarhus",
            "phone": "+45 50 24 09 69",
            "email": "anatoli.mihov@gmail.com",
        },
    },
    "skills": {
        "main": ["HTML", "CSS", "SCSS", "Javascript", "React"],
        "os": ["Windows", "Linux", "MacOS"],
        "vcs": ["Git"],
        "devTools": ["VS Code", "Figma"],
        "additional": ["PHP", "Python", "MySQL", "Bash"],
    },
    "languages": {
        "english": "Beginner – Pre-Intermediate (A1-A2)",
        "ukrainian": "Native",
        "russian": "Native",
    },
}

# --------------------------------------------------------------------------- #
# print(resume)

print("\n...\n")
# --------------------------------------------------------------------------- #
for key, value in resume.items():
    print(f"\n{key.title()}:\n{value}")
