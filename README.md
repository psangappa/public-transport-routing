# Public Transport Routing Application

Search for the quickest route between two given stations.

### Dependencies

* Python >= 3.8
* Make

### Building

To create a virtual environment (`/env`) that contains the Python dependencies run:
```shell script
make
```

### Testing

To run the tests of the project run:
::

    make test

### Start the application

To start the service, run:
```shell script
env/bin/start_app
```

### Usage

Once you start, the application is ready to read the user inputs.

There are 3 types of input that the user need to provide.

1. Number of edges.
    ```prompt
    Enter the number of edges in the graph:
    ```
2. The edges.
    ```prompt
    Enter the edges in the form <source> -> <destination>: <travel time>
    ```
3. A routing query
    ```prompt
    Type route <source> -> <destination> to find out the shortest route between two stations.
    Type nearby <source>, <maximum travel time> to find out all the stations that can be reached from a given station within a given time.
    Type exit to terminate the program.
    ```

#### Errors

* Note that you may encounter `Wrong form.` or `Entered query is wrong.` error if you do not follow the above pattern.
  For example, If you enter an edge `A->B:10` instead of `A -> B: 10`
  In case of these errors, you will be asked to enter the edges or the query again, or you may end the program by typing `exit`.

* If no route exists an error message is printed `Error: No route from <source> to <destination>`

* If no station exists that can be reached from a given station within a given time, an error message is printed `Error: No nearby stations from <source> with the travel time of <maximum travel time>`