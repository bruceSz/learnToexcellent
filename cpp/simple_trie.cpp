#include<iostream>
#include<cstring>
#include<fstream>
#include<time.h>

using namespace std;
const int n = 26;

typedef struct Trie_node
{
    int count;
    struct Trie_node * next[n];
    bool exist;
}TrieNode,*Trie;

TrieNode * createTrieNode()
{
    TrieNode * node = (TrieNode *)malloc(sizeof(TrieNode));
    node->count = 0;
    node->exist = false;
    memset(node->next,0,sizeof(node->next));
    return node;
}

void Trie_insert(Trie root,char * word){
    Trie node = root;
    char *p = word;
    int id;
    while(*p){
	id = *p - 'a';
	if(node->next[id] == NULL) {
	    node->next[id] = createTrieNode();
	}
	node = node->next[id];
	++p;
    }
    node->exist = true;
    node->count++;
}

int Trie_search(Trie root,char * word) {
    Trie node = root;
    char *p = word;
    int id;
    while(*p) {
	id = *p - 'a';
	node = node->next[id];
	++p;
	if(node == NULL) {
	    cout<<endl<<word<<"not exist";
	    return 0;
	}

    }

    if (node->exist == true) {
	cout<<endl<<word<<"exist"<<node->count<<"times";
    }
    return node->count;
}

const int num=5000;

void createStrTXT(){

    srand((int)time(0));
    char temp[12];
    for(int i=0;i<num;i++){

	for(int j=0;j<11;j++){
	    temp[j] = rand()%26 + 'a';
	}
	temp[11]='\0';

	char * str = temp;
	ofstream ofs("str.txt",ios::app);
	ofs<<str<<endl;
    }
}
void establishTrieTree(Trie root){
    ifstream ifs("str.txt");
    char str[12];
    int i = 0;

    while(ifs>>str){
	cout<<str<<endl;
	Trie_insert(root,str);
	cout<<"insert word: "<<str<<endl;
	i++;
    }
    cout<<"totally insert :"<<i<<"words";
}
int main(void){
    Trie root = createTrieNode();
//    createStrTXT();
    establishTrieTree(root);
    Trie_search(root,"zxuglsdsm");
    return 0;
}
