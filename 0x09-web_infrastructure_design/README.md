# 0x09. Web infrastructure design

Design of a web stack diagram and sysadmin/devops. 
**Acronyms:** LAMP, SPOF, QPS

### What is a server?
A server is a device, a virtual device or computer program or providing functionality for other programs or devices, called “clients”

### What is a web server?  
A web server is a software that serves web pages to clients upon their request, it does this over the protocol HTTP.

### What is a codebase?
Is the collection of source code that is used to build a software system.

### What is a database?
Is a collection of information that is stored and organized so that it can be easily accessed, updated and managed.

### What is a DNS?
A system to translate domain names into IP addresses.

### What is HTTPS?
A version of HTTP that secure the traffic between your browser and the website by encrypting it.

### What is TCP/IP?
Transmission Control Protocol/Internet Protocol, is a suite of communications protocols used to interconnect network devices on the Internet or any private network.

## SPOF
A  **single point of failure**  (**SPOF**) is a part of a system that, if it fails, will stop the entire system from working. SPOFs are undesirable in any system with a goal of high availability or reliability, be it a business practice, software application, or other industrial system.

## LAMP
**LAMP** (**L**inux, **A**pache, **M**ySQL, **P**HP/**P**erl/**P**ython) is a very common example of a [web service](https://en.wikipedia.org/wiki/Web_service "Web service")  [stack](https://en.wikipedia.org/wiki/Solution_stack "Solution stack"), named as an [acronym](https://en.wikipedia.org/wiki/Acronym "Acronym") of the names of its original four [open-source](https://en.wikipedia.org/wiki/Open-source_software "Open-source software") components: the [Linux](https://en.wikipedia.org/wiki/Linux "Linux")  [operating system](https://en.wikipedia.org/wiki/Operating_system "Operating system"), the [Apache HTTP Server](https://en.wikipedia.org/wiki/Apache_HTTP_Server "Apache HTTP Server"), the [MySQL](https://en.wikipedia.org/wiki/MySQL "MySQL")  [relational database management system](https://en.wikipedia.org/wiki/Relational_database_management_system "Relational database management system") (RDBMS), and the [PHP](https://en.wikipedia.org/wiki/PHP "PHP")  [programming language](https://en.wikipedia.org/wiki/Programming_language "Programming language"). The LAMP components are largely interchangeable and not limited to the original selection. As a solution stack, LAMP is suitable for building [dynamic web sites](https://en.wikipedia.org/wiki/Dynamic_web_site "Dynamic web site") and [web applications](https://en.wikipedia.org/wiki/Web_application "Web application").

## QPS
"Query rate" redirects here. It is not to be confused with  [Query throughput](https://en.wikipedia.org/wiki/Query_throughput "Query throughput").

**Queries per second**  (QPS) is a common measure of the amount of search traffic an  [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval "Information retrieval")  system, such as a  [search engine](https://en.wikipedia.org/wiki/Search_engine "Search engine")  or a  [database](https://en.wikipedia.org/wiki/Database "Database"), receives during one second.[[1]](https://en.wikipedia.org/wiki/Queries_per_second#cite_note-1)  The term is used more broadly for any  [request–response](https://en.wikipedia.org/wiki/Request%E2%80%93response)  system, more correctly called  [requests per second](https://en.wikipedia.org/wiki/Requests_per_second "Requests per second")  (RPS).

High-traffic systems must watch their QPS in order to know when to scale the system to handle more load.

#### Authors:
> Kelly Villa <900@holbertonschool.com>
