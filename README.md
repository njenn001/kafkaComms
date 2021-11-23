# kafkaComms

Communicate with cluster running Apache Kafka daemons 

## Background 
We have developed a small cluster of raspberry pi computers that are running the Apache Kafka daemons.  These include the zookeeper dameon on the master node and kafka broker daemons on all nodes. Once deployed, a suite of software packages can be used to send and recieve information stored on the cluster. 

## Software Requirements
    - python 3.8
    - kafka-python 
    - Tkinter 

## Usage
    Users can either run the GUI as an executable or through the command line. 

### Command Line 
Run python program. 

```
python app/app.py 
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