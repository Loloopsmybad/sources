

    #include <iostream>
    #include <stdio.h>
    using namespace std;
    //Position
    int posc(char suit[], char fc, int sz)
        {
            int i = 0;
            do
            {
                if (toupper(fc) == suit[i]) return i;
                else
                i = i + 1;
            } 
            while (i < sz);
            cout << "\n Character " << fc << " not available in list";
            return 99;
        }
    int main()
    {
        char suit[] = { 'S', 'D', 'C', 'H' };
        char fc;
        int res;
        int sz = size(suit);
        cout << "\n Enter a character: ";
        cin >> fc;
        res = posc(suit, fc, sz);
        cout << "\n Sequence no: " << res;
        return 0;
    }
