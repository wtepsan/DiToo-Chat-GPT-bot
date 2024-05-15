const chapters = [
    {
        title: "FINAL EXAM",
        subsections: [
            // {name: "Mocking Final Exam", link: "./quiz/?chapter=Finalexam&section=Prep&topic=Mocking Final Exam"}, 
            {name: "Final Exam", link: "./quiz/?chapter=Final&section=Exam&topic=Final Exam"}, 
        ]
    },
    {
        title: "Chapter 1: Introduction to Digital Tools",
        subsections: [
            // {name: "0) Six Step Problem Solving", link: "./quiz/?chapter=0&section=0&topic=TEST"},
            // {name: "1) Six Step Problem Solving", link: "./quiz/?chapter=1&section=1&topic=Six Step Problem Solving"},
            // {name: "2) Digital Tools in Data Driven Society", link: "./quiz/?chapter=1&section=2&topic=Digital Tools in Data Driven Society"},
            // {name: "3) Machine Learning and AI as tools for Entrepreneurs", link: "./quiz/?chapter=1&section=3&topic=Machine Learning and AI as tools for Entrepreneurs"},
        ] 
    },
    {
        title: "Chapter 2: Digital tools for financial problems and tasks ",
        subsections: [
            // {name: "3) Digital Tools for Financial Analysis",  link: "./quiz/?chapter=2&section=3&topic=Digital Tools for Financial Analysis"},
        ]
    },
    {
        title: "Chapter 3: Digital tools for time management",
        subsections: [
        ]
    },
    {
        title: "Chapter 4: Digital tools for teamwork management",
        subsections: [ 
        ]
    },
    {
        title: "Chapter 5: Digital tools for managing customers relationship management",
        subsections: [
        ]
    },
    {
        title: "Chapter 6: Digital tools for marketing",
        subsections: [
        ]
    },
    {
        title: "Chapter 7: Designing digital tools for a business painpoint",
        subsections: [
            // {name: "1) Design a Digital Tool", link: "./quiz/?chapter=7&section=1&topic=Design a Digital Tool"}, 
        ]
    },
    // Add other chapters following the same structure
];

document.addEventListener('DOMContentLoaded', function() { 
    const courseContent = document.getElementById('courseContent');

    chapters.forEach((chapter, index) => {
        const chapterDiv = document.createElement('div');

        const h3 = document.createElement('h3');
        h3.className = 'chapter'
        h3.style.cursor = 'pointer'; // Change cursor on hover

        // Arrow initialization with rightward arrow for collapsed state
        const arrow = document.createElement('span');
        arrow.innerHTML = '&#9658;';
        arrow.style.marginLeft = '10px';
        arrow.style.marginRight = '5px';

        // Insert the arrow before the chapter title text
        h3.appendChild(arrow);
        h3.appendChild(document.createTextNode(chapter.title));

        const subsectionsDiv = document.createElement('div');
        subsectionsDiv.className = 'subsections';
        subsectionsDiv.style.display = 'block';

        chapter.subsections.forEach(sub => {
            const a = document.createElement('a');
            // a.href = sub.link;
            a.href = `${sub.link}&studentID=${studentID}&studentName=${studentName}`;
            a.id = sub.name;
            a.textContent = sub.name;
            subsectionsDiv.appendChild(a);
            subsectionsDiv.appendChild(document.createElement('br'));
        });

        h3.onclick = function() {
            const isVisible = subsectionsDiv.style.display === 'block';
            subsectionsDiv.style.display = isVisible ? 'none' : 'block';
            // Update arrow direction based on visibility
            arrow.innerHTML = isVisible ? '&#9660;':'&#9658;'; // Change to upward arrow when expanded
        };

        chapterDiv.appendChild(h3);
        chapterDiv.appendChild(subsectionsDiv);
        courseContent.appendChild(chapterDiv);
    });
});