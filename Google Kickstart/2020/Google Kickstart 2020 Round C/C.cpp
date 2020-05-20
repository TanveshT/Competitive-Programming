//Only passed the first test set

#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define ld long double

bool perfectSquare(ll x)
{
    ld sqroot = sqrt(x);
    return ((sqroot - floor(sqroot) == 0)); 
}

int main(){

    int t, n, v, count;
    cin >> t;

    vector<ll> a, prefix;

    for(int k = 1; k<=n; k++)
    {

        count = 0;

        cin >> n;
        for(int i = 0; i < n; i++){
            cin >> v;
            a.push_back(v);
        }

        prefix.resize(n+1, 0);

        for(int i = 0; i < n; i++)
            prefix[i+1] = prefix[i] + a[i];
        
        for (int i = 1; i <= n; i++) 
            for(int j = i; j <= n; j++) 
                if(perfectSquare(prefix[j] - prefix[i-1]))
                    count++;

        cout << count;

        cout << "Case #"<<k<<": "<<count << "\n";
        a.clear();
    }

}