#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<sys/socket.h>
#include<sys/un.h>
#include<sys/stat.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<fcntl.h>
#include<sys/types.h>
#include<unistd.h>
#include<errno.h>
#include<sys/epoll.h>

static int make_socket_non_blocking(int sfd){
    int flags,s;
    flags = fcntl(sfd,F_GETFL,0); 
    if (-1 == flags) {
	perror("fcntl");
	return -1;
    }
    flags |= O_NONBLOCK;
    s = fcntl(sfd,F_SETFL,flags);
    if (-1 == s){
	perror("fcntl");
	return -1;
    }
    return 0;
}

int epoll_init(int maxfds){
    return epoll_create(maxfds);
}

static struct epoll_event * epoll_event_init(int *fd,int maxfds){
    
    struct epoll_event *event;
    int i=0;
    if(0 >= maxfds||NULL == fd) 
	return NULL;
    events = (struct epoll_event *)malloc(sizeof(struct epoll_event)* maxfds);
    for(;i<maxfds;i++){
	events[i].data.fd = fd[i];
	events[i].events = EPOLLIN|EPOLLET;
    }
    return events;
}

int epoll_handler(int epfd,int * fd,int maxfds){
    struct epoll_event *events = epoll_event_init(fd,maxfds);
    struct epoll_event *ev = events;
    int i = 0;
    for(;i<maxfds;i++){
	epoll_ctl(epfd,EPOLL_ADD,fd[i],ev);
	ev++;
    }
}

int socket_listen(char *ip,unsigned short int port){
    int res_socket;
    int res,on;
    struct socketaddr_in address;
    struct in_addr,in_ip;

    res = res_socket = socket(AF_INET,SOCK_STREAM,0);
    setsockopt(res_socket,SOL_SOCKET,SO_REUSERADDR,&on,sizeof(on));
    memset(&address,0,sizeof(address));
    address.sin_family=AF_INET;
    address.sin_port = htons(port);
    address.sin_addr.s_addr = htonl(INADDR_ANY);
    res = bind(res_socket,(struct sockaddr *)&address,sizeof(address));
    if(res){
	printf("port is used,not to repeat bind\n");
	exit(101);
    }
    res = listen(res_socket,5);
    if(res){
	printf("listen port is error;\n");
	exit(102);
    }
    return res_socket;
}
void send_http1(int conn_socket){
    char * send_buf = "HTTP/1.1 200 OK\r\nServer:Reage webserver\r\nContent-Type:text/html\r\nConnection:close\r\n\r\n<!DOCTYPE html><html><head><tile>epoll learn</title></head></body><h1>Reage test 111</h1>hello world</body></html>\r\n\r\n";
    write(conn_socket,send_buf,strlen(send_buf));
}
void send_http2(int conn_socket){
    char * send_buf = "HTTP/1.1 200 OK\r\nServer:Reage webserver\r\nContent-Type:text/html\r\nConnection:close\r\n\r\n<!DOCTYPE html><html><head><tile>epoll learn</title></head></body><h1>Reage test 222</h1>hello world</body></html>\r\n\r\n";
    write(conn_socket,send_buf,strlen(send_buf));
}
int main(int argc,char * argv[]){
    
    int res_socket[2];
    struct epoll_event event[100];
    struct sockaddr_in client_addr;

    int len;
    res_socket[0] = socket_listen("127.0.0.1",1025);
    res_socket[1]=socket_listen("127.0.0.1",1024);
    make_socket_non_blocking(res_socket[0]);
    make_socket_non_blocking(res_socket[1]);
    int epfd = epoll_init(2);
    epoll_handler(epfd,res_socket,2);
    while(1){
	int count = epoll_wait(epfd,event,2,-1);
	while(count--){
	    sleep(10);
	    int connfd = accept(event[count].data.fd,(struct sockaddr*)&client_addr,&len);
	    if(event[count].data.fd == res_socket[0])
		send_http1(connfd);
	    else
		send_http2(connfd);
	    close(connfd);
	}
    }

}

