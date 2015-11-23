//
//  PrettyPrint.cpp
//
//  Print concentric rectangular pattern in a 2d matrix.
//  The outermost rectangle is formed by A, then the next outermost is formed by A-1 and so on.
//  You will be given A as an argument to the function you need to implement, and you need to return a 2D array.
//  Example Output: A = 3
//  33333
//  32223
//  32123
//  32223
//  33333

vector<vector<int> > makeBox (int A)
{
    int size = 2*A - 1;
    vector<vector<int> > box (size, vector<int>(size));
    int leftBound = 0;
    int rightBound = size;
    int topBound = 0;
    int bottomBound = size;
    while (leftBound < rightBound && topBound < bottomBound)
    {
        for (int i = topBOund; i <bottomBound; i++)
        {
            for (int j = leftBound; j < rightBound; j++)
            {
                box[j][i] = A;
            }
        }
        A = A- 1;
        topBound++;
        bottomBound--;
        leftBound++;
        rightBound--;
    }
    return box;
}
