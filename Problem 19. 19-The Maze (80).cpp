#include <bits/stdc++.h>

using namespace std;

void check(vector<pair<int,int> > &v, pair<int,int> p, vector<vector<int> > &a){
    int c=0;
    if(p.second+1<a.size()){
        if(a[p.first][p.second+1]==0){
            v.push_back(p);
            a[p.first][p.second+1]=1;
            v.push_back({p.first,p.second+1});
            check(v, {p.first,p.second+1}, a);
            c=1;
        }
    }
    if(p.first+1<a[0].size()){
        if (a[p.first+1][p.second]==0){
            v.push_back(p);
            a[p.first+1][p.second]=1;
            v.push_back({p.first+1,p.second});
            check(v, {p.first+1,p.second}, a);
            c=1;
        }
    }
    if(p.first-1>=0){
        if(a[p.first-1][p.second]==0){
            v.push_back(p);
            a[p.first-1][p.second]=1;
            v.push_back({p.first-1,p.second});
            check(v, {p.first-1,p.second}, a);
            c=1;
        }
    }
    if(p.second-1>=0){
        if(a[p.first][p.second-1]==0){
            v.push_back(p);
            a[p.first][p.second-1]=1;
            v.push_back({p.first,p.second-1});
            check(v, {p.first,p.second-1}, a);
            c=1;
        }
    }
    if(c==0){
        v.push_back({-1,-1});
        return;
    }
}

int main(){
    int x, y;
    cin>>x>>y;
    vector<vector<int> > a;
    vector<int> b;
    int c;
    for(int i=0;i<y;i++){
        b.clear();
        for(int k=0;k<x;k++){
            cin>>c;
            b.push_back(c);
        }
        a.push_back(b);
    }

    vector<pair<int,int> > v;
    a[0][0]=1;
    v.push_back({0,0});
    check(v, {0,0}, a);

    v.erase(find_if(v.begin(),v.end(),[=](pair<int,int> b){return (b.first)==y-1&&(b.second)==x-1;})+1,v.end());

    while(find_if(v.begin(),v.end(),[=](pair<int,int> b){return b.first==-1&&b.second==-1;})!=v.end()){
        vector<pair<int,int> >::iterator it=find_if(v.begin(),v.end(),[=](pair<int,int> b){return b.first==-1&&b.second==-1;})+1;
        v.erase(1+find_if(v.begin(),v.end(),[=](pair<int,int> b){return b.first==it->first&&b.second==it->second;}), it+1);
    }

    int i=0;
    while(i<v.size()-1){
        if(v[i].first==v[i+1].first&&v[i].second==v[i+1].second) v.erase(v.begin()+i);
        else i++;
    }

    cout << endl;
    for(auto i:v) cout << i.first << ' ' << i.second << endl;
    return 0;
}
