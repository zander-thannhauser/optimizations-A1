PROGRAM bubble;

 VAR a:ARRAY[1..15] OF INTEGER;
     i,j,t,least:INTEGER;

BEGIN
	a[1] := 32;
	a[2] := 11;
	a[3] := 111;
	a[4] := 88;
	a[5] := 11;
	a[6] := 44;
	a[7] := 33;
	a[8] := 33;
	a[9] := 22;
	a[10] := 77;
	a[11] := 45;
	a[12] := 65;
	a[13] := 76;
	a[14] := 87;
	a[15] := 34;
	
	i := 1;
	
	WHILE i<=14 DO BEGIN
          least := i;
	  j := i + 1;
	  WHILE j<=15 DO BEGIN
            IF a[j] < a[least] THEN 
              least := j;
	    j := j + 1 
	  END;
          t := a[i];
          a[i] := a[least];
          a[least] := t;
          i:= i + 1
	END;

	i := 1;
	WHILE i<=15 DO BEGIN
          WRITE(a[i]);
	  i := i + 1
        END
      
END
