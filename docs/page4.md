# Advanced User Guide

This guide is intended for administrators who want to perform CRUD operations on MongoDB without using the API, but instead by directly accessing the MongoDB instance running inside a Docker container via SSH.

## Accessing Docker Container's Operating System

To access the operating system of a Docker container through the command-line interface, please follow these steps:

1. Make sure Docker is installed and running on your machine. If not, you'll need to install Docker first.

2. Open your preferred terminal or command prompt application.

3. Use the following command to list the running Docker containers:

    ```bash
    docker ps
    ```

   This command will display a list of running containers along with their IDs, names, and other details.

4. Identify the container you want to access and note down its container ID or name from the list.

5. To enter the operating system of the desired container, use the following command:

    ```bash
    docker exec -it <container_id_or_name> bash
    ```

   Replace `<container_id_or_name>` with the actual container ID or name you noted down in the previous step.

   For example, if the container ID is `abcd1234`, you would run:

    ```bash
    docker exec -it abcd1234 bash
    ```

   If the container is running a different shell, such as `sh` or `zsh`, replace `bash` with the appropriate shell name.

6. Press Enter to execute the command. This will start a new shell session within the container, effectively providing access to the container's operating system.

7. Congratulations! You are now inside the container's operating system. From here, you can run commands and perform tasks just as you would on a regular operating system.

   Remember that any changes made within the container's operating system will be isolated and specific to that container. Exiting the container's shell session will not stop the container itself unless you explicitly stop it.

## Note

It's important to note that accessing the Docker container's operating system directly should be done with caution, as it bypasses the usual API-based interaction and requires a good understanding of the container's configuration and setup.

## Accessing MongoDB Shell

Once you are inside the Docker container's operating system, you can execute the following command to enter the MongoDB shell:

```bash
mongosh
```
This will start the MongoDB shell, allowing you to interact with the database.

To access the test database, simply type db and press Enter.
To list all the databases available, execute the following command:
```bash
show dbs
```
Note that if you encounter an error saying `MongoServerError: command listDatabases requires authentication`, it means
you are not authenticated. You will need to authenticate by providing a username and password.

Switch to the admin database by executing:
```bash
use admin
```

Authenticate with the username and password specified in your docker-compose.yml
file using the `db.auth()` method:
```bash
db.auth('username', 'password')
```
When you change the username or password in the docker-compose.yml file for MongoDB,
the changes won't automatically take effect in the running container. This is 
because the container retains the older username and password configuration.
To update the authentication credentials in the MongoDB container, follow as:
```bash
db.changeUserPassword("username", "newPassword")
```
Changing the username for a MongoDB user involves creating a new user with the desired username and privileges,
and then removing the old user.

To switch to a specific database:
```bash
use <database_name>
```

To display a list of collections within the current database:
```bash
show collections
```

These are just a few examples of commonly used commands in the MongoDB shell. 
The MongoDB [documentation](https://www.mongodb.com/docs/) provides more detailed information and examples for each command.

[__Home Page__](README.md) |  [__Previous Page__](page3.md)
