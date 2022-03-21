# kafkaComms

Communicate with cluster running Apache Kafka daemons.

## Background
We have developed a small cluster of raspberry pi computers that are running the Apache Kafka daemons.  These include the zookeeper dameon on the master node and kafka broker daemons on all nodes. Once deployed, a suite of software packages can be used to send and recieve information stored on the cluster.

## Software Requirements
    - python 3.8.2
    - virtualenv
    - matplotlib
    - kafka-python 

## Usage

After confirming correct Python 3.8.2 installation, os dependent instructions are provided below.

### Windows users
First install dependencies and create virtual environment by running setup scripts:

```
python setup.py 
python app\app.py -s 
```

Activate the virtual environment before using. A help script is provided with the application.

```
.\venv\Scripts\activate     
python app\app.py -h
```

Run in GUI mode or strict mode, consuming and producing messages under specified servers and topics.

```
python app\app.py -r
python app\app.py -c --bss 000.000.000.000 --topic example 
python app\app.py -p --bss 000.000.000.000 --topic example_topic --msg example_message 
```

Deactivate the virtual environment as such:

```
deactivate 
```

### Linux users
First create virtual environment and install dependencies by running setup scripts:

```
python setup.py 
python app/app.py -s 
```

Activate the virtual environment before using. A help script is provided with the application.

```
source ./venv/bin/activate      
./venv/bin/python app/app.py -h
```

Run in GUI mode or strict mode, consuming and producing messages under specified servers and topics.

```
./venv/bin/python app/app.py -r
./venv/bin/python app/app.py -c --bss 000.000.000.000 --topic example 
./venv/bin/python app/app.py -p --bss 000.000.000.000 --topic example_topic --msg example_message 
```

Deactivate the virtual environment as such:

```
deactivate 
```


## Acknowledgments


### Code Contributors

    - Noah Jennings 
        - njenn001@odu.edu
    - Vincent Houston 
        - vincent.e.houston@nasa.gov

### Authors

    - Noah Jennings
        - njenn001@odu.edu

## Sources

- https://projects.apache.org/projects.html 
- https://kafka.apache.org/
- https://kafka-python.readthedocs.io/ 
- https://docs.python.org/