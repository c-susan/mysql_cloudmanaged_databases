# mysql_cloudmanaged_databases
HHA504 / Cloud Computing / Assignment 4a / MySQL Cloud DB

This repo focuses on MySQL along with implementation on cloud services, Google Cloud Platform and Microsft Azure. MySQL instances were set up on GCP and Azure and connected to MySQL workbench. SQL script was written to create sample tables. 

## This repo contains the following: 
+ An **azure** folder containing SQL script for table creation and screenshpts of thet action output, entity relationship diagram (ERD), and tables in the database. The folder also contains a ```.gitignore``` and ```populate.py``` file to insert sample values into the tables on MySQL workbench.
+ A folder named **gcp** also containing SQL script for table creation and screenshpts of thet action output, entity relationship diagram (ERD), and tables in the database.
+ A **README.md** file containing an overview of the repo.

### Azure Setup
+ Azure Database for MySQL
+ Deployment option: Flexible,
+ Tier: Burstable
+ Compute: B1S [$6.21 p/month]

### Google Cloud Platform (GCP) Setup
+ Cloud SQL edition: Enterprise
+ Machine Configuration: Shared core; 1vCPU, 0.614 GB

### Python Script for Database Interaction
**1.** The **azure** file contains a python file for database interaction with MySQL workbench. The the .env and .gitignore files were configured correctly according to the database host, name, username, and password. However, the following error message was shown: 
```
Python-dotenv could not parse statement starting at line 1
Python-dotenv could not parse statement starting at line 2
Python-dotenv could not parse statement starting at line 3
Python-dotenv could not parse statement starting at line 4
Python-dotenv could not parse statement starting at line 5
Python-dotenv could not parse statement starting at line 6
Traceback (most recent call last):
  File "/home/susan_chen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 644, in connect
    sock = socket.create_connection(
  File "/usr/lib/python3.9/socket.py", line 822, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
  File "/usr/lib/python3.9/socket.py", line 953, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -2] Name or service not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 145, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3288, in raw_connection
    return self.pool.connect()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 452, in connect
    return _ConnectionFairy._checkout(self)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 1267, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 716, in checkout
    rec = pool._do_get()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 170, in _do_get
    self._dec_overflow()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 147, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 167, in _do_get
    return self._create_connection()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 393, in _create_connection
    return _ConnectionRecord(self)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 678, in __init__
    self.__connect()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 903, in __connect
    pool.logger.debug("Error on connect(): %s", e)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 147, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 898, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 637, in connect
    return dialect.connect(*cargs, **cparams)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 615, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 358, in __init__
    self.connect()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 711, in connect
    raise exc
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on 'None' ([Errno -2] Name or service not known)")

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/susan_chen/mysql_cloudmanaged_databases/populate.py", line 86, in <module>
    insert_fake_data(db_engine)
  File "/home/susan_chen/mysql_cloudmanaged_databases/populate.py", line 33, in insert_fake_data
    with engine.connect() as connection:
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3264, in connect
    return self._connection_cls(self)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 147, in __init__
    Connection._handle_dbapi_exception_noconnection(
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 2426, in _handle_dbapi_exception_noconnection
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 145, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 3288, in raw_connection
    return self.pool.connect()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 452, in connect
    return _ConnectionFairy._checkout(self)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 1267, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 716, in checkout
    rec = pool._do_get()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 170, in _do_get
    self._dec_overflow()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 147, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/impl.py", line 167, in _do_get
    return self._create_connection()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 393, in _create_connection
    return _ConnectionRecord(self)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 678, in __init__
    self.__connect()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 903, in __connect
    pool.logger.debug("Error on connect(): %s", e)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/util/langhelpers.py", line 147, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/pool/base.py", line 898, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/create.py", line 637, in connect
    return dialect.connect(*cargs, **cparams)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/default.py", line 615, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)
  File "/home/susan_chen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 358, in __init__
    self.connect()
  File "/home/susan_chen/.local/lib/python3.9/site-packages/pymysql/connections.py", line 711, in connect
    raise exc
sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'None' ([Errno -2] Name or service not known)")
(Background on this error at: https://sqlalche.me/e/20/e3q8)
```
<br>

**2.** To address this error, the ```.env``` file containing the database credentials was edited. In addition, the connection string was also changed to:
```
connect_args={'ssl':{'fake_flag_to_enable_tls': True}}
connection_string = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}'
engine = create_engine(
        connection_string,
        connect_args=connect_args)
```

+ The python script was able to make a connection the the MySQL instance however returned the following error: 
```
Traceback (most recent call last):
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1408, in execute
    meth = statement._execute_on_connection
AttributeError: 'str' object has no attribute '_execute_on_connection'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/susan_chen/mysql_cloudmanaged_databases/script.py", line 88, in <module>
    insert_fake_data(engine)
  File "/home/susan_chen/mysql_cloudmanaged_databases/script.py", line 44, in insert_fake_data
    connection.execute(f"""
  File "/home/susan_chen/.local/lib/python3.9/site-packages/sqlalchemy/engine/base.py", line 1410, in execute
    raise exc.ObjectNotExecutableError(statement) from err
sqlalchemy.exc.ObjectNotExecutableError: Not an executable object: "\n                INSERT INTO patients (first_name, last_name,\n                                date_of_birth, gender, address, phone_number)\n                VALUES ('Jennifer', 'Wright', '1957-11-13', 'F',\n                '5606 Lopez Island Apt. 376, North James, TN 19628', '248.386.9259x108') \n            "
```

To address this error, several changes were made. 
+ The ```text``` function was imported from sqlalchemy.
+ Defined SQL queries for each of the tables as a **'text'** object and executed using connection.execute(sql_query). 

**The python file was successfully ran with ```Fake data insertion complete!``` being printed in the terminal. However, the tables in MySQL shows NULL values/data was not inserted.**
