#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
const int N=201;
int n;
vector<int> g[N];
int minnum[N];
bool cmp(const int &a,const int &b)
{
	return minnum[a]>minnum[b];
}
void dfs(int pos)
{
	
	if(g[pos].empty())
		minnum[pos]=1;
	else
	{
		for (int i=0;i<g[pos].size();i++)
			dfs(g[pos][i]);
		sort(g[pos].begin(),g[pos].end(),cmp);
		int max=-1;
		for(int i=0;i<g[pos].size();i++)
		{
			if(i+minnum[g[pos][i]]>max)
				max=i+minnum[g[pos][i]];
			minnum[pos]=max;
		}
		
	}
	return ;
}
int main()
{
	int testcase;
	scanf("%d",&testcase);
	while(testcase--)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++)
		{
			int num,pos;
			scanf("%d %d",&pos,&num);
			g[pos].clear();
			while(num--)
			{
				int t;
				scanf("%d",&t);
				g[pos].push_back(t);
			}
		}

		dfs(1);
		printf("%d\n",minnum[1]);
	}
	return 0;
}
