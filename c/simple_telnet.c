
#define DEFAULTIP "127.0.0.1"
#define DEFAULTPORT "23"
#define DEFAULTBACK "10"
#define DEFAULTDIR "/tmp"
#define DEFAULTLOG "/tmp/telnet-server.log"

void pemsg(char * msg);
#define pemsg(msg) {perror(msg);abort();}
void wemsg(char * msg);
#define wemsg(msg) {fputs(msg,logfp);fputs(strerror(errno),logfp);fflush(logfp);abort();}

void  pmsg(char * msg);
#define pmsg(msg) {fputs(msg,stdout);}
void wmsg(char * msg);
#define wmsg(msg) {fputs(msg,logfp);fflush(logfp);}

#define MAXBUF 2048

char buffer[MAXBUF + 1];
char * host = 0;
char * port = 0;
char * back = 0;
char * dirroot = 0;
char * logdir = 0;
unsigned char daemon_y_n = 0;
FILE *logfp;

#define MAXPATH 150


void allocateMem(char **s,int len,char *d) {
    *s = malloc(len+1);
    bzero(*s,l+1);
    memcpy(*s,d,len);
}

void getopt(int argc,char ** argv) {
    int c,len;
    char * p = 0;
    opterr = 0;
    while(1) {
	int opt_index = 0;
	static struct option long_options[]={
	    {"host",1,0,0},
	    {"port",1,0,0},
	    {"back",1,0,0},
	    {"dir",1,0,0},
	    {"log",1,0,0},
	    {"daemon",1,0,0},
	    {0,0,0,0}
	};
	c = getopt_long(argc,argv,"H:P:D:L",long_options,&opt_index);
	if (c == -1 || c=='?')
	    break;
	if(optarg)
	    len= strlen(optarg);
	else
	    len = 0;

	if((!c && !(strcasecmp(long_options[opt_index].name,"host")))||c=='H')
	    p = host=malloc(len+1);
	else if()
    }

}

