#include<iostream>
#include<vector>
using namespace std;

int main()
{
    string s;
    getline(cin, s);

    int n = s.size();
    vector<pair<int, int>> a (n, std::make_pair(0, 0));
    int qcount = 0;
    for(int i = 0; i < n; i++)
    {
        if(s[i] == 'Q')
        {    qcount += 1; }
        a[i].first = qcount;
    }
    qcount = 0;
    for(int i = n-1; i >= 0; i--)
    {
        if(s[i] == 'Q')
        {    qcount += 1; }
        a[i].second = qcount;
    }
    int count = 0;
    for(int i = 0; i < n; i ++)
    {
        if(s[i] == 'A')
        {
            count += (a[i].first * a[i].second);
        }
    }
    cout << (count+1);
}