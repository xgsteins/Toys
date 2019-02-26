#include <bits/stdc++.h>
#include <unistd.h>
using namespace std;
const int maxn = 50;
bool cell[2][maxn][maxn];
int ind;

int itX[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int itY[] = {-1, 0, 1, -1, 1, -1, 0, 1};

inline bool OutOfBounds(int x, int y) { return !(x >= 0 && x < maxn && y >= 0 && y < maxn); }

bool judge(int x, int y, int ind)
{
    bool nowState = cell[ind][x][y];
    int survivingCellNum = 0;
    for (int i = 0; i < 8; i++)
    {
        if (OutOfBounds(x + itX[i], y + itY[i]))                    continue;
        survivingCellNum += (cell[ind][x + itX[i]][y + itY[i]] ? 1:0);
    }
    if (nowState)
    {
        if (survivingCellNum > 3 || survivingCellNum < 2)           return false;
        else                                                        return true;
    }
    else
    {
        if (survivingCellNum == 3 /*|| rand()%1000 > 998*/)         return true;        // 瞎吉尔改规则
        else                                                        return false;
    }
}

int main()
{
    for (int i = 0; i < maxn; i++)
    {
        for (int j = 0; j < maxn; j++)
        {
            int p = rand() % 100;
            if (p < 63)                 //  活的细胞产生概率
                cell[ind][i][j] = true;
        }
    }
    while (1)
    {
        for (int i = 0; i < maxn; i++)
        {
            for (int j = 0; j < maxn; j++)
            {
                cout << (cell[ind][i][j] ? "[]" : "  ");
            }
            cout << endl;
        }
        cout << endl;
        for (int i = 0; i < maxn; i++)
        {
            for (int j = 0; j < maxn; j++)
            {
                cell[ind^1][i][j] = judge(i, j, ind);
            }
        }
        usleep(50000);
        system("clear");
        ind ^= 1;
    }
}