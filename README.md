# kafkaComms

Communicate with cluster running Apache Kafka daemons.

## Background
We have developed a small cluster of raspberry pi computers that are running the Apache Kafka daemons.  These include the zookeeper dameon on the master node and kafka broker daemons on all nodes. Once deployed, a suite of software packages can be used to send and recieve information stored on the cluster.

## Software Requirements
    - python 3.8.2
    - pipreqs 
    - pytest
    - kafka-python 
    - Tkinter 

## Usage

Users can start the communication center through the file system on Windows machines or the command line on both Linux and Windows machines.


### Linux

Linux users have a number or options when trying to start the communication center.

```
After installing Python 3.8, users can simply start the communication center. 

- python3.8 app/app.py
```

```
Using Make provides users a shortcut when installing dependencies, running tests, or starting the communication center. Below is a list applicable rules: 

- make   
- make test_native   
- make test_virtual 
- make native 
- make virtual 
```


### Windows 
Windows users have a number or options when trying to start the communication center.

```
After installing Python 3.8.2, users must satisfy project dependencies within a virtual environment before using the communication center.  

- virtualenv venv
- .\venv\Scripts\activate 
- .\venv\Scripts\pip.exe install -r requirements.txt
- .\venv\Scripts\python.exe app/app.py -s
```

## Acknowledgments


### Code Contributors 

    - Noah Jennings 
        - njenn001@odu.edu

### Authors

    - Noah Jennings
        - njenn001@odu.edu

## Sources 

- https://projects.apache.org/projects.html 
- https://kafka.apache.org/
- https://kafka-python.readthedocs.io/ 
- https://docs.python.org/