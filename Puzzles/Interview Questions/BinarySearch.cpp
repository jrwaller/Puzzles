#include <iostream>

using namespace std;
//
//  main.cpp
//  BinarySearch
//
//  Created by James Waller on 5/4/15.
//  Copyright (c) 2015 JamesWaller. All rights reserved.
//

#include <iostream>

bool binSearch(int start, int last, int nums[10], int x)
{
    if (start <= last)
    {
        int mid = (start + last) / 2;
        if (nums[mid] == x)
        {
            return true;
        }
        else if (x < nums[mid])
        {
            return binSearch(start, mid - 1, nums, x);
        }
        else{
            return binSearch(mid+1, last, nums, x);
        }
    }
    return false;
}
