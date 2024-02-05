module BlackCell(PIK, PKJ, GIK, GKJ, GIJ, PIJ);
    input PIK, PKJ, GIK, GKJ;
    output GIJ, PIJ;
    wire w0;
    and AND0(PIJ, PIK, PKJ);
    and AND1(w0, GKJ, PIK);
    or  OR0(GIJ, GIK, w0);

endmodule