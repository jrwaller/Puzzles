//
//  Kattis-ProblemID:lineup.cpp
//  
//  Problem description at: https://open.kattis.com/contests/biy245/problems/lineup

string lineThemUp(int num, string names[])
{
    bool increasing == false;
    bool decreasing == false;
    for (int i = 0; i < num - 1; i++)
    {
        string first = names[i];
        string second = names[i + 1];
        int index = 0;
        if (first[index] == second[index])
        {
            while (first[index] == second[index])
            {
                index++;
            }
        }
        
        if (first[index] < second[index] && decreasing)
        {
            return "NEITHER";
        }
        else if (first[index] > second[index] && increasing)
        {
            return "NEITHER";
        }
        else if (first[index] < second[index])
        {
            increasing = true;
        }
        else if (first[index] > second[index])
        {
            decreasing = true;
        }
        index = 0;
    }
    if (increasing)
    {
        return "INCREASING";
    }
    else
    {
        return "DECREASING";
    }
}
