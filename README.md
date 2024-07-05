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

### B-Tree:

Theoretical Part:

Definition of B-tree: A B-tree is a self-balancing tree data structure that maintains an ordered distribution of data. Unlike binary trees, each node in a
B-tree can have multiple child nodes.

Properties of B-trees:

Nodes contain keys and pointers to child nodes.

Each node contains between t and 2t-1 keys.

All leaf nodes are at the same level.

The keys in a node are arranged in ascending order.

Basic Operations:

Insertion: When the number of keys in a node exceeds 2t-1, the node splits, and the middle key moves up to the parent node.

Deletion: The deletion operation require the tree to be rebalanced to maintain the properties of the B-tree.

Search: The search operation recursively searches for an element in the node and its child nodes by comparing keys.

Practical Part:

Description of Classes and Methods:

BTreeNode class: Defines the structure and basic operations of a B-tree node.

BTree class: Provides methods for operations such as insertion, search, and deletion.

Insertion Operation: The insert method recursively finds the appropriate insertion position in the node and its child nodes, and performs node splitting when necessary to maintain the balance of the B-tree.

Search Operation: The search_tree method searches for a specific element in the node and its child nodes by comparing keys.

Search by Title: The search_by_title method provides a convenient way to search for books by a keyword in the book title.

Deletion Operation: The remove method is used to delete a specific key from the B-tree and require the tree to be rebalanced.

## 4. Implementation of Project

### The location of the source code：

https://github.com/dongzhebin/Library-Management-System.git

### Environment Setup

Visual Studio Code and Python extension 

Pyqt5

System: Windows 11

We are using Visual Studio Code as our development environment and have installed the necessary libraries, including csv for file handling and unittest for testing.

### Data Structure Implementation

1.Implement the Book class with attributes such as book ID, title, author, genre, publication year, availability, and borrow count, and methods for printing, comparison, and equality.

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/92966ad3-3cdf-4c72-b037-6cfdae45ce0b)

2.Implement the BTreeNode class with attributes such as keys (books), child nodes, and a flag for leaf nodes, and methods for splitting, adding keys, adding children, and determining size.

3.Implement the BTree class with attributes such as minimum degree, root node, and methods for inserting, searching, traversing, and removing nodes.

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/fb3549cd-db42-4cb9-bd88-513a4decfc9e)

### Library Class Implementation

1.Initialize the Library class with a filename to read and write book data.

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/4e1e4374-416d-4e81-95aa-d2234552d4bc)

2.Implement methods for reading the book dataset from a CSV file and writing the updated dataset 

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/0d09d2d9-0aca-462d-a014-45055abf35fe)

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/c64a3449-629c-48ee-af82-c8d95c1da61d)

3.back to the file.

4.Implement methods for reading and writing user data from and to a CSV file.

5.Implement methods for creating a new user, logging in, and updating user data.

6.Implement methods for adding a new book, displaying books, searching books, recommending books, and returning books.

7.Implement methods for updating borrowing statistics and displaying recently borrowed books.

### User Interface Implementation

1.Create a main function that initializes a Library object and provides a loop for user interaction.

2.Implement a menu-driven interface that prompts users for their choice of operation.

3.Implement methods for handling user input and executing the chosen operation.

### Testing

Write unit tests for each method in the Book, BTreeNode, BTree, and Library classes.

### The implementation for recommendations.

Find the most borrowed book: 

First, define an internal function named update_most_borrowed that is used to update the book with the most borrowings. This function traverses all books using the traverse method and uses the nonlocal keyword to modify the variable most_borrowed_book. If the current book being traversed has been borrowed more times than the recorded maximum, then most_borrowed_book will be updated to the current book.

Get books of the same genre: 

Once the book with the most borrowings is found, the method retrieves the genre of that book. Next, another internal function named add_if_same_genre is defined to add books of the same genre to the recommendation list recommended_books. When adding books, it checks to ensure that the book is not the same as most_borrowed_book to avoid recommending duplicates.

Return recommendation results: 

If books of the same genre are found, they will be returned as the recommendation results. If no books of the same genre are found, a message indicating that no other books in the same genre were found will be returned. If no books are found during the traversal, a message indicating that no books were found will be returned.

Exception handling:

 If any exceptions occur while performing the above operations, the exception will be caught, the stack trace will be printed, and a message containing the exception information will be returned.

## 5.Running and Debugging of Project

 Interface:

 ![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/3e10a990-9947-4b7a-ab51-500ee9a8803d)

 Register:

 ![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/a46c1af4-5b1d-49b1-a40d-be9b9b6c4ad1)

When registering, you need to enter the username, nickname, and password.

Registration successful:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/e322047e-5315-4216-83f4-692995ac0bf9)

Log in:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/5350d5c9-5736-416f-82dc-1b2b9c95be6d)

When logging in, you need to enter your username and password

 Log in successful:

 ![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/b821e8bc-07bd-4fe0-807d-ea1ac048aedf)

Search Book:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/5c513516-2470-47bd-b3b4-a68716ae45da)

I searched for the word “war” and the books above are the results

Add book:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/01f3b985-a142-4bf0-94ef-2640f62520d7)

Here, I added a book with an ID of 100, with the title, author, and category of the book being zzz, zz, and z, respectively

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/cc4db7bd-a89b-4365-90fc-40634f0a983f)

Modify book:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/68e52e65-f1ee-452f-a1f4-60149a9d770b)

I have changed the name of the book with ID 100 to hhh.

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/f59a5c4e-458e-49f6-9344-0127fb775b04)

Borrow book:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/b2215576-42e0-4b45-800a-2ae5ae0e60c0)

Recommened book:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/a394f17a-96a4-4e58-9746-c7242f5b8dfb)

I borrowed two books here, “1984” and “War and Peace”, and the books recommended above are based on this.

Delete book:


![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/bad52d89-e774-4265-843b-c4c8d6306530)


![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/612489ac-a562-4e9f-9763-2030431500eb)

Return book:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/f9b2e833-5aba-458b-bda5-87b2cef28924)


![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/3f7dfc75-9eea-4f84-9339-fceb4d7dec52)


![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/bdd104bc-e96e-462f-80e4-49313563ce4e)

### Test:

![image](https://github.com/dongzhebin/Library-Management-System/assets/173773038/ef01dc6e-53aa-4b14-8a39-eea49f537341)




## 6.Summary

### Tips:

Rui Guo:

Learning Reflection:

Recently, my group and I completed a task of developing a library system using the BTree data structure. This task not only deepened my understanding of BTree but also allowed me to apply this knowledge in real-world programming, from which I greatly benefited.

Firstly, through this task, I gained a deeper understanding of BTree's node structure, balancing mechanisms, and operations such as searching and insertion. BTree is a self-balancing tree data structure that maintains data order and remains efficient during insert, delete, and search operations. This makes it very useful in large database systems where frequent read and write operations are required. In the project, we used BTree for indexing books, making the operations of searching and inserting books fast and efficient.

Secondly, by collaborating with my group members, I learned how to better conduct teamwork and code division. During this process, we adopted agile development methods, regularly allocating tasks and checking progress to ensure the project was completed on time. We also ensured code quality and maintainability through code reviews and discussions. This collaborative approach not only improved work efficiency but also taught me a lot of soft skills beyond programming.

Finally, through this task, I gained a deeper understanding and application of the Python programming language. We utilized Python's powerful libraries and tools such as unittest for unit testing, pandas for data processing, and matplotlib for data visualization, which greatly simplified our development process.

In conclusion, this task not only significantly improved my technical skills but also provided me with valuable experience in teamwork and project management. This will lay a solid foundation for my future learning and work.
