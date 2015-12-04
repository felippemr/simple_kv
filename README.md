# simple_kv
A simple key-value store based on https://www.jeffknupp.com/blog/2014/09/01/what-is-a-nosql-database-learn-by-writing-one-in-python/



## Installing
 * ```git clone https://github.com/felippemr/simple_kv.git```
 * ```make pip; make pip_test```
 * ```make test```

## Usage
There is not a command-line client for simple_kv but, users are able to interact with it by telnet. Run the project with ```make run``` and connect with ```telnet localhost 50505```.

Available commands are:
 * ```GET;<KEY>;<VALUE>;```     -> Return a key if it exists
 * ```PUT;<KEY>;<VALUE>;INT``` -> Insert a new key(Currently simple_kv only supports INT)
 * ```GETLIST;<KEY>;;```        -> Return a key if it exists
 * ```PUTLIST;<KEY>;<LIST_VALUE>;LIST``` -> Insert a new key, it must be a list
 * ```INCREMENT;<KEY>;;```      -> Increment a key if it exists
 * ```APPEND;<KEY>;<ELEMENT>;``` -> Append a new element to a key which if it is a list
 * ```DELETE;<KEY>;;``` -> Delete a key if it exists
 * ```STATS;;;``` -> Return the database stats
