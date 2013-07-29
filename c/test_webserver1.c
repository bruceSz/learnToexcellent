#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<sys/un.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<fcntl.h>

#define MAX 1024
int socket_listen(char *ip,unsigned short int port){
    int res_socket,res,on;
    struct sockaddr_in address;
    struct in_addr in_ip;
    res = res_socket=socket(AF_INET,SOCK_STREAM,0);
    setsockopt(res_socket,SOL_SOCKET,SO_REUSEADDR,&on,sizeof(on));
    memset(&address,0,sizeof(address));
    address.sin_family=AF_INET;
    address.sin_port=htons(port);
    address.sin_addr.s_addr=htonl(INADDR_ANY);
    res = bind(res_socket,(struct sockaddr*)&address,sizeof(address));
    if (res){
	printf("port is used,not to repeat bind\n");
	exit(101);
    }
    res = listen(res_socket,5);
    if(res){
	printf("listen port is error\n");
	exit(102);
    }
    return res_socket;
}
int main(int argc,char * argv[]){
    int res_socket,conn_socket;
    int tmp;
    struct sockaddr_in client_addr;
    char buf[MAX];
    int len = sizeof(client_addr);
    res_socket=socket_listen("127.0.0.1",1024);
    while(1){
	conn_socket = accept(res_socket,(struct sockaddr *)&client_addr,&len);
	printf("web brower information\n\n");
	while(0==(tmp=read(conn_socket,buf,MAX-1))||tmp!=EOF){
	    buf[MAX-1]=0;
	    printf("%s\n",buf);
	    break;
	}
	close(conn_socket);
    }
}
