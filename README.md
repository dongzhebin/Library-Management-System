# Library Management System

## Abstract

### Project Abstract: Library Management System

The Library Management System is a software application designed to streamline the processes involved in managing a library’s inventory of books. This system is implemented using a B-Tree data structure to efficiently store and organize the books, enabling fast search, insertion, and deletion operations. The system also includes features for user management, book borrowing, and statistical analysis of borrowing patterns.

The system’s user interface is designed to be intuitive and user-friendly, allowing librarians and users to interact with the system easily. It provides options for adding new books, searching for books, borrowing books, returning books, and updating borrowing statistics. The system also includes a recommendation feature that suggests books based on user borrowing history and preferences.

The system is designed to be scalable and can handle a large volume of books and users. It is also secure, ensuring the privacy and security of user data and preventing unauthorized access. The system is compatible with common operating systems and has minimal hardware requirements, allowing it to run on a standard computer setup.

The system has been thoroughly tested using unit tests and user acceptance tests to ensure its correctness and reliability. The project also includes a detailed report documenting the design decisions, algorithms used, and challenges faced during the development process.

In summary, the Library Management System is a robust and efficient system that can effectively manage a library’s inventory of books and provide a user-friendly interface for librarians and users. It is designed to be scalable, secure, and compatible with common operating systems, making it a suitable choice for libraries of various sizes.

## Catalogue

I Description Of Project

II Requirement Analysis of Projec

III Design of Project 

IV Implementation of Project

V Running and Debugging of Project

VI Summary

## 1.Description Of Project

### Project Objective:

1.Develop an efficient library management system to optimize the organization, retrieval, and lending of books.

2.Utilize the B-Tree data structure for efficient management of book information.

### Project Content:

Part 1: Building the Software Toolbox:

1.Define a Python class to represent books in the library, including attributes such as title, author, genre, etc.

2.Implement a B-Tree data structure for storing and managing book information.

3.Develop book management utilities, including functions for adding, searching, and updating books.

4.Load a dataset to initialize the B-Tree and test all methods using unittest.

### Part 2: Analysis and Optimization:

1.Implement lending management functions, including handling book lending, returns, and displaying available books.

2.Develop a recommendation system to suggest books based on user borrowing history and preferences.

3.Create a graphical interface that allows users to search, lend, and return books.

### Part 3: Extra Features:

1.Enhance the graphical interface with interactive elements, such as displaying book details on hover and lending/returning books on click.

2.Analyze lending patterns and the most popular books to gain insights into user preferences and library usage.

3.Integrate with external systems to enhance functionality, such as searching for book details in online catalogs.

Project Data:

library_books_dataset.csv

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/67ce840b-b2c3-4bc8-9b87-a115cac559a6)

## 2.Requirement Analysis of Project

### Functional Requirements:

1.The system must be able to efficiently manage and organize a large collection of books in a library.

2.The system should support quick search, insertion, and deletion of books using the B-Tree data structure.

3.The system should allow users to borrow and return books, updating the availability status of the books.

4.The system should provide a recommendation feature based on user borrowing history and preferences.

5.The system should have a graphical interface for easy interaction with users.

6.The system should be able to load and initialize the B-Tree with a dataset of book information.

### Non-functional Requirements:

1.The system should be efficient in terms of time complexity for search, insertion, and deletion operations.

2.The system should be user-friendly and intuitive, with a clear and visually appealing graphical interface.

3.The system should be reliable and maintain data integrity, ensuring that no data is lost or corrupted.

4.The system should be scalable, able to handle an increasing number of books and users.

5.The system should be secure, protecting user data and preventing unauthorized access.

### Technical Requirements:

1.The system should be developed using Python, leveraging its libraries and frameworks for efficient implementation.

2.The B-Tree data structure should be implemented from scratch, without using any external libraries.

2.The B-Tree data structure should be implemented from scratch, without using any external libraries.

3.The graphical interface should be developed using a suitable library or framework, such as Tkinter or PyQt.

4.The system should be tested thoroughly using unit tests to ensure the correctness and efficiency of the implemented functionalities.

## 3.Design of Project 

### Project Overview:

Develop a library management system for efficient management of book information, user information, and borrowing records.

Utilize a B-Tree data structure to implement fast search, insertion, and deletion operations for books.

### Data Structure Design:

Book Class (Book): Contains attributes such as book ID, title, author, genre, publication year, availability, and borrow count.

B-Tree Node Class (BTreeNode): Contains attributes such as keys (books), child nodes, and a flag for leaf nodes.

B-Tree Class (BTree): Contains attributes such as minimum degree, root node, and methods for insertion, search, and deletion.

### System Function Design:

User Management: User registration, login, creating users, and updating user information.

Book Management: Adding books, displaying book lists, searching for books, recommending books, and deleting books.

Borrowing Management: Borrowing books, returning books, and displaying recently borrowed books.

Statistical Analysis: Updating borrowing statistics, displaying borrowing statistics information.

### Interface Design:

Main Interface: Displays system operation options, including adding books, displaying book lists, searching for books, etc.

Book Information Interface: Displays detailed book information, including book ID, title, author, etc.

Borrowing Information Interface: Displays borrowing records and borrowing statistics information.

### Data Storage Design:

Use CSV files to store book information and user information.

The system loads CSV files to initialize the B-Tree.

### Testing and Quality Assurance:

Conduct unit tests to ensure the correctness and efficiency of each functional module.

### Project Deliverables:

Well-documented and organized source code, regularly versioned and uploaded to GitHub.

Project report, documenting design decisions, algorithms used, challenges faced, and solutions.

Presentation, showcasing system functionality and analysis results.

## 4. Implementation of Project

Environment Setup

Visual Studio Code and Python extension 

System: Windows 11

We are using Visual Studio Code as our development environment and have installed the necessary libraries, including csv for file handling and unittest for testing.
