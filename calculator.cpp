#include<iostream>
#include<cmath>

using namespace std;

int main()
{
long long num1,num2;
int ch;
do
{

cout<<"Scientific Calculator:";
cout<<"\n1: Square Root \n2: Factorial \n3: Natural Logarithm \n4: Power function";
cout<<"\nEnter your choice:";
cin>>ch;
switch(ch)
   {
	case 1:
		cout<<"\nEnter the number:";
		cin>>num1;
		cout<<sqrt(num1);
	break;
	case 2: 
		cout<<"\nEnter the number:";
		cin>>num1;
		num2 = 1;
		if( num1 < 0 )
			cout<<"\nInvalid Value";
		else if(num1==0)
			cout<<num2;
		else
		{
			for(int i = 1; i<=num1; i++)
				num2 *= i;
			cout<<num2;
		}

	break;
	case 3:
		cout<<"\nEnter the number:";
		cin>>num1;
		cout<<log(num1);
	break;
	case 4:
		cout<<"\nEnter the Base and Exponent value:";
		cin>>num1>>num2;
		cout<<pow(num1,num2);

	break;
	default: "Invalid Option!\nTry again";

   }
cout<<"\nDo you want to go again? (1 for yes):";
cin>>ch;
}while(ch==1);

return 0;

}
