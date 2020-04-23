#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<string> result(n);
    bool flag = false;
    for(int i = 0; i< n; i++){
        string s;
        cin>>s;
        for(int j = 1; j < 5; j++){

            if(s[i-1] == 'O' && s[i] =='O' && flag == false){
                s[i-1] = '+';
                s[i] = '+';
                flag = true;
            }  
        }
        cout<<s;
    }
    for(int i = 0; i< n; i++){
        cout<<result[i];
    }

    return 0;
}