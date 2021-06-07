import java.util.*;

class sudo2 {
    public static void main(String[] args) {
        double first = 0.44960042304882464;
        double val = 1;
        int step = 0;
        long s1=0, s2=0, s3=0;
        for (long i = 100; i < 1000; i++) {
            for (long j = 100; j < 1000; j++) {
                for (long k = 100; k < 1000; k++) {
                    step += 1;
                    four tmp = WHrand(i, j, k);
                    if (Math.abs(tmp.value-first) < Math.abs(val-first)) {
                        val = tmp.value;
                        s1=i;s2=j;s3=k;
                        System.out.printf("changing to %s %s %s (val=%s)\n", i, j, k, val);
                    }
                }
            }
        }
        System.out.println(step);
        for (int i=0; i<100; i++) {
            four tmp = WHrand(s1, s2, s3);
            System.out.println(tmp.value);
            s1=tmp.s1; s2=tmp.s2; s3=tmp.s3;
        }
    }

    public static four WHrand(long s1, long s2, long s3) {
        s1 = ( ( 171 * s1 ) % 30269 );
        s2 = ( ( 172 * s2 ) % 30307 );
        s3 = ( ( 170 * s3 ) % 30323 );
        double value = ((double) s1 ) / 30269.0
            + ((double) s2 ) / 30307.0
            + ((double) s3 ) / 30323.0;
        value = (value % 1.0);
        // System.out.println(value);
        return new four(value, s1, s2, s3);
        // return value;
    }

    static class four {
        double value;
        long s1, s2, s3;
        public four(double val, long _s1, long _s2, long _s3) {
            value = val; s1 = _s1; s2 = _s2; s3 = _s3;
        }
    }
}