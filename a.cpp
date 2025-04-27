#include<bits/stdc++.h>

using namespace std;


int main(){

    int t;
     cin>>t;
      while(t--){

            int x,y,a;
            cin>>x>>y>>a;

            int aa= y+y;
            int b=x+x;
            if(aa==b){
                  cout<<"NO"<<endl;
            }else if(aa>=a){
                   cout<<"YES"<<endl;

            }else{
                  cout<<"NO"<<endl;

            }
      }





    return 0;

}