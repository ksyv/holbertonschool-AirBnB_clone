#**Readme for AirBnB Clone - The Console**

This project is a command-line interface (CLI) implementation of an AirBnB clone.
The project aims to replicate some of the functionality of the popular AirBnB website.

![alt text](https://github.com/ksyv/holbertonschool-AirBnB_clone/blob/ff7c5e5f4d3eeb28306d064a98646ae55c80f48c/location-airbnb.jpg)

**Table of Contents**
Introduction
Installation
Usage
Available Commands
Contributing
License

**Introduction**
This console application provides a command-line interface to interact with the AirBnB clone. It allows users to create, update, delete, and display various objects such as BaseModel, User, State, City, Amenity, Place, Review, and Place.

The application follows the Model-View-Controller (MVC) design pattern, where the console serves as the controller. It utilizes JSON serialization to store and retrieve object data persistently.

**Installation**
To install and run the AirBnB clone console, follow these steps:

Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your_username_here/AirBnB_clone.git
Navigate to the project directory:

bash
Copy code
cd AirBnB_clone
Run the console:

bash
Copy code
./console.py

**Usage**
Once the console is running, you can start entering commands. Use the help command to display a list of available commands or help <command> to get help for a specific command.

bash
Copy code
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
To exit the console, type quit or EOF.

**Available Commands**
Here's a list of commands available in the AirBnB clone console:

EOF: Exits the console.
all [class_name]: Displays all objects or all objects of a specific class.
create <class_name>: Creates a new instance of a class.
destroy <class_name> <id>: Deletes an object by its ID.
help [command]: Displays help for the specified command or lists all available commands.
quit: Exits the console.
show <class_name> <id>: Displays an object based on its class name and ID.
update <class_name> <id> <attribute_name> "<attribute_value>": Updates an attribute of an object.

**Contributing**
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

**License**
This project is licensed under the MIT License - see the LICENSE file for details.
