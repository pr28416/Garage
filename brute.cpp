#include <iostream>
#include <tuple>


using namespace std;

tuple<double, int, int, int> rand(int s1, int s2, int s3) {
    s1 = ( ( 171 * s1 ) % 30269 );
    s2 = ( ( 172 * s2 ) % 30307 );
    s3 = ( ( 170 * s3 ) % 30323 );

    double value = float ( s1 ) / 30269.0 + float ( s2 ) / 30307.0 + float ( s3 ) / 30323.0;

    // value = ( value % 1);

    return tuple<double, int, int, int>{value, s1, s2, s3};
}

int main() {

}