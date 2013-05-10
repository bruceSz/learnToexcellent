#include <stdio.h>
#include <stdlib.h>
#include <math.h>
typedef struct
{
	int x;
	int y;
}type;
type p[10001];
int cmpx(const void * a,const void * b)
{
	return ((type *)a)->x-((type * )b)->x;
}
int cmpy(const void * a,const void * b)
{
	return ((type * )a)->y-((type *)b)->y;

}

int main()
{
	int i,n;
	while(scanf("%d",&n)!=EOF)
	{
		for(i=0;i<n;i++)
		{
			scanf("%d %d",&p[i].x,&p[i].y);
		}
		if(n==1)
		{
			printf("0\n");
			continue;
		}
		int mid;
		int ans=0;
		qsort(p,n,sizeof(type),cmpy);
		if(!n&1)
		{
			mid=(p[n/2].y+p[n/2-1].y)/2;
		}
		else
		{
			mid=p[n/2].y;
		}
		for(i=0;i<n;i++)
		{
			ans+=abs(p[i].y-mid);
		}
		qsort(p,n,sizeof(type),cmpx);
		for(i=0;i<n;i++)
		{
			p[i].x-=i;
		}
		qsort(p,n,sizeof(type),cmpx);
		if(!n&1)
		{
			mid=(p[n/2].x+p[n/2-1].x)/2;

		}
		else
		{
			mid=p[n/2].x;
		}
		for(i=0;i<n;i++)
		{
			ans+=abs(p[i].x-mid);
		}
		printf("%d\n",ans);
		fflush(stdout);

	}
	return 0;
}
