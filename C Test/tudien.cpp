#include<stdio.h>
#include<string.h>
int main(void)
{
	char tudien[][8] =
	{
		"ability", "absence", "actions", "amazing", "believe", "browser", "caption", "captive", "ceiling", "degrees", "denizen", "develop", "examine", "example", "exploit", "fifteen", "focused", "fortune", "forward", "garbage", "gasping", "graphic", "handgun", "hastily", "helpful", "iceberg", "impeach", "inspect", "jawbone", "justify", "keyword", "kickoff", "kneepad", "lactose", "latency", "legible", "madness", "magical", "manhunt", "mission", "nametag", "nitrate", "nowhere", "officer", "optical", "outlook", "oxidize", "paradox", "pathway", "patient", "payment", "qualify", "quality", "quarrel", "radical", "railing", "reduced", "resolve", "savings", "sayings", "scissor", "shadows", "tactics", "teacher", "terrify", "tractor", "unarmed", "unmasks", "updates", "vaccine", "valleys", "walnuts", "wealthy", "whacked", "willing", "wizards", "xysters", "yielded", "yoghurt", "younger", "zippers", "zombies"
	},chuoi[3][8],chuoinhap[30];
	int i=0,j=0,k=0,kq[2],mangkq[81];
	fflush(stdin);
	scanf("%[^\n]",chuoinhap);
	while(i<=strlen(chuoinhap)){
		if(chuoinhap[i]==','){
			chuoi[j][k]='\0';
			j++;
			k=0;
			i+=2;
		}
		chuoi[j][k]=chuoinhap[i];
		k++;
		i++;
	}
	for(i=0;i<3;i++)
	{	
		kq[i]=0;
		for(k=0;k<strlen(chuoi[i]);k++)
		{
			kq[i]=kq[i]+chuoi[i][k]*chuoi[i][k];
		}
	}
		for(i=0;i<82;i++)
		{	
			mangkq[i]=0;
			for(j=0;j<strlen(tudien[i]);j++)
			{	
				mangkq[i]=mangkq[i]+tudien[i][j]*tudien[i][j];
			}
		}
	for(j=0;j<3;j++)
	{
		for(i=0;i<82;i++)
		{
			if(kq[j]==mangkq[i]){
				if(j==2)
				printf("%s\n",tudien[i]);
				else
				printf("%s, ",tudien[i]);	
			}
		}	
		
	}
}