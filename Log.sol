pragma solidity ^0.4.17;

contract Log
{
    function log(
        uint a, 
        uint b
    )
        public
        pure
        returns (uint c)
    {
        assert(a > 1);
        assert(b > 1);
        assert(a >= b);

        for (c = 0; c <= 256; c++)
        {
            if (a == 1) break;
            if (a % b > 0) break;
            a /= b;
        }
    }
}   
