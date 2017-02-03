ATTN: Docker swarm is probably a better/cleaner/more automated fit for most load balancing tasks utilizing docker. If you are not positive that docker swarm doesn't fit your use case, please check it out before attempting the following in a production environment.

This repository contains a demo of running a load balanced web application on a single host utilizing docker containers.

What you'll need for this demo

- docker
- docker-compose
- 1 terminal window
- 2 browser windows
- The IP address of your docker machine
    - On linux this is (probably) localhost/127.0.01
    - On Windows/Mac this is the IP address of your docker machine
        - [See here](https://docs.docker.com/machine/get-started/)


In the terminal (in this repos dir):
```
docker-compose up -d
```

Open one browser window @ http://$DOCKERIP:8989/stats

Note that our front end is listening, and one of our back end servers is online.

Open another brower window @ http://$DOCKERIP:8080

Refresh (probably without cache) a few times. Notice the same host responds each time.

In the terminal:
```
docker-compose scale web_app=4
```

Refresh the browser window @ http://$DOCKERIP:8989/stats a few times. 
Notice the other hosts coming up.

Refresh the browser window (without cache) @ http://127.0.01:8080 a few times.
Notice that we are now receiving responses from all the hosts (in a round-robin fashion)

In the terminal:
```
docker-compose scale web_app=0
```

Refresh the browser window @ http://$DOCKERIP:8989/stats a few times. 
Notice all the hosts going down.

Refresh the browser window (without cache) @ http://127.0.01:8080 a few times.
Now we get a 503

In the terminal:
```
docker-compose scale web_app=2
```

Refresh the browser window @ http://$DOCKERIP:8989/stats a few times. 
Two hosts should come online

Refresh the browser window (without cache) @ http://127.0.01:8080 a few times.
We now go back and forth between those two hosts

In the terminal:
```
docker-compose scale loadbalancer=0
```

Refresh the browser window @ http://$DOCKERIP:8989/stats a few times. 
Notice nothing is there

Refresh the browser window (without cache) @ http://127.0.01:8080 a few times.
Nothing here either

If you'd like navigate to to the port the application binds to, 8910.
Nothing is accessible (through the host) here either.

In the terminal:
```
docker ps -a
```

Notice that two of our web application hosts are still alive and well, just inaccessible

In the terminal:
```
docker-compose scale loadbalancer=1
```

Refresh the browser window @ http://$DOCKERIP:8989/stats a few times. 
A new load balancer is back online, and has picked up where the other left off.

Refresh the browser window (without cache) @ http://127.0.01:8080 a few times.
Two of our hosts are once again accessible.

In the terminal:
```
docker-compose scale loadbalancer=2
```

Notice that docker fails at running a second load balancer (because it is bound to a port on the host), but our application is still accessible via refreshing the other pages

In the terminal:
```
docker-compose down
```

Our whole web application stack is cleanly shutdown and removed.
